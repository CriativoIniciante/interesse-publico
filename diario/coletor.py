# -*- coding: utf-8 -*-
"""
Coletor da leitura do dia.

Lê as fontes de fontes.json (mainstream, independente, checagem, oficial, popular,
mundo), guarda o que saiu nas últimas horas em diario/raw/AAAA-MM-DD.json e monta
uma versão compacta para leitura em diario/raw/AAAA-MM-DD.md.

Só biblioteca padrão. Não publica nada; só lê. A leitura, a triangulação e o texto
do dia são feitos depois, com revisão humana (ver diario/README.md).

Uso:
    python coletor.py            # coleta de hoje
    python coletor.py --data 2026-09-09
    python coletor.py --status   # o que já existe em raw/
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAW = AQUI / "raw"
FONTES = AQUI / "fontes.json"
UA = "Mozilla/5.0 (compatible; interesse-publico-coletor/1.0; +https://github.com/CriativoIniciante/interesse-publico)"
FUSO = timezone(timedelta(hours=-3))  # Brasília

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "ht": "https://trends.google.com/trending/rss",
    "media": "http://search.yahoo.com/mrss/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "rss1": "http://purl.org/rss/1.0/",
}

ENTIDADES_HTML = {  # entidades HTML que aparecem em feeds mal formados e que o XML não conhece
    "nbsp": " ", "aacute": "á", "agrave": "à", "atilde": "ã", "acirc": "â", "eacute": "é", "ecirc": "ê",
    "iacute": "í", "oacute": "ó", "otilde": "õ", "ocirc": "ô", "uacute": "ú", "ccedil": "ç",
    "Aacute": "Á", "Atilde": "Ã", "Eacute": "É", "Ecirc": "Ê", "Iacute": "Í", "Oacute": "Ó", "Otilde": "Õ",
    "Uacute": "Ú", "Ccedil": "Ç", "ldquo": "“", "rdquo": "”", "lsquo": "‘", "rsquo": "’", "hellip": "…",
    "ndash": "–", "mdash": "—", "raquo": "»", "laquo": "«", "copy": "©", "reg": "®", "deg": "°", "ordf": "ª", "ordm": "º",
}


def limpa(texto, maximo=240):
    if not texto:
        return ""
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = html.unescape(texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    if len(texto) > maximo:
        texto = texto[: maximo - 1].rstrip() + "…"
    return texto


def baixa(url, timeout=25, tentativas=2):
    """Baixa com uma nova tentativa em timeout e espera maior em HTTP 429."""
    ultimo = None
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            ultimo = e
            if e.code == 429 and i + 1 < tentativas:
                time.sleep(20)
                continue
            raise
        except Exception as e:  # noqa: BLE001 (timeout, reset, DNS)
            ultimo = e
            if i + 1 < tentativas:
                time.sleep(3)
                timeout = timeout * 2
                continue
            raise
    raise ultimo


def parse_data(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = parsedate_to_datetime(s)
        if d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        return d
    except Exception:
        pass
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        return d
    except Exception:
        return None


def texto(el, *caminhos):
    for c in caminhos:
        x = el.find(c, NS)
        if x is not None and (x.text or "").strip():
            return x.text.strip()
    return ""


def _parse_xml(dados):
    try:
        return ET.fromstring(dados)
    except ET.ParseError:
        pass
    txt = dados.decode("utf-8", "ignore")
    txt = txt[txt.find("<"):]
    # entidades HTML que o XML não conhece (feed do Senado)
    txt = re.sub(r"&([A-Za-z]+);", lambda m: ENTIDADES_HTML.get(m.group(1), m.group(0)) if m.group(1) not in ("amp", "lt", "gt", "quot", "apos") else m.group(0), txt)
    try:
        return ET.fromstring(txt.encode("utf-8"))
    except ET.ParseError:
        return None


def _parse_regex(dados):
    """Último recurso para feeds com prefixo de namespace não declarado (Revista Oeste): extrai item a item."""
    txt = dados.decode("utf-8", "ignore")
    itens = []
    for bloco in re.findall(r"<item\b.*?</item>", txt, re.S):
        def campo(nome):
            m = re.search(rf"<{nome}\b[^>]*>(.*?)</{nome}>", bloco, re.S)
            if not m:
                return ""
            v = m.group(1).strip()
            v = re.sub(r"^<!\[CDATA\[(.*?)\]\]>$", r"\1", v, flags=re.S)
            return v.strip()
        itens.append({
            "titulo": limpa(campo("title"), 300),
            "link": limpa(campo("link"), 500),
            "data": limpa(campo("pubDate"), 80),
            "resumo": limpa(campo("description")),
        })
    return itens


def parse_feed(dados):
    """Devolve lista de dicts {titulo, link, data, resumo, extra}. Aceita RSS 2.0, RSS 1.0 e Atom."""
    raiz = _parse_xml(dados)
    if raiz is None:
        return _parse_regex(dados)
    itens = []
    if raiz.tag.lower().endswith("feed"):  # Atom
        for e in raiz.findall("atom:entry", NS):
            link = ""
            for l in e.findall("atom:link", NS):
                if l.get("rel", "alternate") == "alternate":
                    link = l.get("href", "")
                    break
            itens.append({
                "titulo": limpa(texto(e, "atom:title"), 300),
                "link": link,
                "data": texto(e, "atom:published", "atom:updated"),
                "resumo": limpa(texto(e, "atom:summary", "atom:content")),
            })
        return itens

    canal = raiz.find("channel")
    lista = canal.findall("item") if canal is not None else (raiz.findall("rss1:item", NS) or raiz.findall("item"))
    for it in lista:
        d = {
            "titulo": limpa(texto(it, "title", "rss1:title"), 300),
            "link": texto(it, "link", "rss1:link"),
            "data": texto(it, "pubDate", "dc:date", "rss1:date"),
            "resumo": limpa(texto(it, "description", "content:encoded", "rss1:description")),
        }
        traf = it.find("ht:approx_traffic", NS)  # Google Trends
        if traf is not None:
            d["extra"] = {"trafego": (traf.text or "").strip(), "noticias": []}
            for n in it.findall("ht:news_item", NS):
                d["extra"]["noticias"].append({
                    "titulo": limpa(texto(n, "ht:news_item_title"), 200),
                    "fonte": texto(n, "ht:news_item_source"),
                    "link": texto(n, "ht:news_item_url"),
                })
        itens.append(d)
    return itens


def parse_trends24(dados):
    """Extrai a lista mais recente de tendências do X no Brasil na página do trends24.in."""
    txt = dados.decode("utf-8", "ignore")
    m = re.search(r"trend-card__list.*?</ol>", txt, re.S)
    if not m:
        return []
    itens = []
    for a in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', m.group(0), re.S):
        nome = limpa(a.group(2), 120)
        link = html.unescape(a.group(1))
        if nome and "trends24.in" not in link:
            itens.append({"titulo": nome, "link": link, "data": "", "resumo": ""})
    return itens


def coleta(cfg, agora):
    janela = timedelta(hours=cfg.get("janela_horas", 36))
    maximo = cfg.get("max_por_fonte", 40)
    resultado = {"gerado_em": agora.isoformat(), "janela_horas": cfg.get("janela_horas", 36), "fontes": [], "falhas": []}
    for f in cfg["fontes"]:
        t0 = time.time()
        if "reddit.com" in f["url"]:
            time.sleep(10)  # o Reddit devolve 429 para pedidos seguidos sem autenticação
        try:
            dados = baixa(f["url"])
            itens = parse_trends24(dados) if f.get("tipo") == "html_trends24" else parse_feed(dados)
        except Exception as e:  # noqa: BLE001
            erro = f"{type(e).__name__}: {e}"[:200]
            resultado["falhas"].append({"id": f["id"], "nome": f["nome"], "erro": erro})
            print(f"  FALHA {f['id']}: {erro[:120]}")
            continue
        dentro = []
        for it in itens:
            d = parse_data(it.get("data"))
            if d is not None and agora - d > janela:
                continue
            it["data_iso"] = d.astimezone(FUSO).strftime("%Y-%m-%d %H:%M") if d else ""
            dentro.append(it)
        dentro = dentro[:maximo]
        resultado["fontes"].append({
            "id": f["id"], "nome": f["nome"], "lente": f["lente"], "perfil": f.get("perfil", ""),
            "url": f["url"], "total_no_feed": len(itens), "itens": dentro,
        })
        print(f"  ok    {f['id']:<18} {len(dentro):>3} itens ({len(itens)} no feed, {time.time() - t0:.1f}s)")
    return resultado


def radar(resultado, termos):
    """Conta quantas manchetes de cada lente citam cada termo do radar (palavra inteira, sem distinguir maiúsculas)."""
    padroes = [(t.strip(), re.compile(r"(?<!\w)" + re.escape(t.strip()) + r"(?!\w)", re.I)) for t in termos if t.strip()]
    contagem = {}
    for f in resultado["fontes"]:
        for it in f["itens"]:
            t = it.get("titulo", "") + " " + it.get("resumo", "")
            for termo, p in padroes:
                if p.search(t):
                    c = contagem.setdefault(termo, {})
                    c[f["lente"]] = c.get(f["lente"], 0) + 1
    linhas = [(sum(pl.values()), termo, pl) for termo, pl in contagem.items()]
    linhas.sort(reverse=True)
    return linhas


ORDEM_LENTES = ["mainstream", "independente", "checagem", "oficial", "popular", "mundo"]


def escreve_md(resultado, linhas_radar, caminho, data_str):
    out = [f"# Coleta bruta de {data_str}", ""]
    out.append(f"Gerado em {resultado['gerado_em']} (janela de {resultado['janela_horas']}h). Material de trabalho, não publicado: só título, link, hora e resumo do próprio feed. A leitura triangulada fica em `diario/{data_str[:4]}/{data_str}.md`.")
    out.append("")
    if resultado["falhas"]:
        out.append("## Fontes que falharam")
        for f in resultado["falhas"]:
            out.append(f"- {f['nome']} ({f['id']}): {f['erro']}")
        out.append("")
    out += ["## Radar de termos (quantas manchetes citam, por lente)", "", "| termo | total | por lente |", "|---|---|---|"]
    for total, termo, pl in linhas_radar[:40]:
        out.append(f"| {termo} | {total} | " + ", ".join(f"{k} {v}" for k, v in sorted(pl.items(), key=lambda kv: -kv[1])) + " |")
    out.append("")
    for lente in ORDEM_LENTES:
        fontes = [f for f in resultado["fontes"] if f["lente"] == lente]
        if not fontes:
            continue
        out += [f"## Lente: {lente}", ""]
        for f in fontes:
            out += [f"### {f['nome']}  ·  {f['perfil']}", ""]
            if not f["itens"]:
                out.append("- (nada na janela)")
            for it in f["itens"]:
                linha = f"- {it.get('data_iso', '')} **{it['titulo']}**"
                if it.get("link"):
                    linha += f" — {it['link']}"
                out.append(linha)
                if it.get("extra"):
                    ex = it["extra"]
                    if ex.get("trafego"):
                        out.append(f"  - tráfego aprox.: {ex['trafego']}")
                    for n in ex.get("noticias", [])[:3]:
                        out.append(f"  - {n['fonte']}: {n['titulo']} — {n['link']}")
                elif it.get("resumo"):
                    out.append(f"  - {it['resumo']}")
            out.append("")
    caminho.write_text("\n".join(out), encoding="utf-8")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", help="AAAA-MM-DD (padrão: hoje)")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    RAW.mkdir(exist_ok=True)
    if args.status:
        for p in sorted(RAW.glob("*.json")):
            d = json.loads(p.read_text(encoding="utf-8"))
            n = sum(len(f["itens"]) for f in d["fontes"])
            print(f"{p.stem}: {len(d['fontes'])} fontes ok, {len(d['falhas'])} falhas, {n} itens")
        return

    agora = datetime.now(FUSO)
    data_str = args.data or agora.strftime("%Y-%m-%d")
    cfg = json.loads(FONTES.read_text(encoding="utf-8"))
    print(f"Coleta de {data_str} ({len(cfg['fontes'])} fontes)")
    resultado = coleta(cfg, agora)
    linhas_radar = radar(resultado, cfg.get("radar_termos", []))
    (RAW / f"{data_str}.json").write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    escreve_md(resultado, linhas_radar, RAW / f"{data_str}.md", data_str)
    n = sum(len(f["itens"]) for f in resultado["fontes"])
    print(f"\n{len(resultado['fontes'])} fontes ok, {len(resultado['falhas'])} falhas, {n} itens na janela")
    print(f"-> {RAW / (data_str + '.md')}")
    print("\nRadar (top 15):")
    for total, termo, pl in linhas_radar[:15]:
        print(f"  {total:>3}  {termo:<16} " + ", ".join(f"{k} {v}" for k, v in sorted(pl.items(), key=lambda kv: -kv[1])))


if __name__ == "__main__":
    main()
