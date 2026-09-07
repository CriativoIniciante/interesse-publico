# -*- coding: utf-8 -*-
"""O circuito: como as cúpulas dos três Poderes se protegem, com os números de ../README.md.
Gera circuito.svg/.html/.png (PNG via PyMuPDF)."""
import html, pathlib

SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e0dfd9"
KIND = {
 "nomeia": ("#6d6c68", "nomeação e escolha"),
 "regra":  ("#2a78d6", "regra escrita pela própria Corte"),
 "dinheiro": ("#c48a14", "dinheiro e acesso"),
 "bloqueio": ("#d03b3b", "bloqueio da responsabilização"),
}
def esc(s): return html.escape(s, quote=True)

W, H = 2100, 1560
N = {
 "pres":  (1050, 190, "PRESIDENTE DA REPÚBLICA", "escolhe quem investiga, quem acusa e quem julga", "#fbeeee"),
 "pgr":   (1620, 400, "PGR", "Aras e Gonet fora da lista tríplice (2019, 2021, 2023, 2025)", "#f3eefb"),
 "pf":    (1760, 700, "POLÍCIA FEDERAL", "cargo de confiança: 4 diretores sob Bolsonaro; chefe da segurança de Lula", "#eef8f2"),
 "stf":   (1050, 760, "STF", "5 de 10 ministros com vínculo direto com quem os indicou; nenhum rejeitado em 38 anos", "#eef3fb"),
 "cong":  (330, 700, "SENADO E CÂMARA", "109 pedidos de impeachment sem despacho; CPI do Master não lida; PEC da Blindagem: 353 votos", "#fbf5e8"),
 "tcu":   (480, 400, "TCU E CNJ", "6 de 9 do TCU escolhidos pelo Congresso; CNJ presidido pelo STF e sem alcance sobre ele", "#f1f1ee"),
 "emp":   (1050, 1090, "BANCOS E EMPRESAS COM CAUSAS NA CORTE", "Fórum de Lisboa: 64 grupos; Master: 5 eventos, 4 famílias de ministros pagas; 1.860 processos com parentes", "#fff8e6"),
}
E = [
 ("pres","pgr","nomeia","indica fora da lista tríplice",(0,-40),0.5,(0,-12),"middle"),
 ("pres","pf","nomeia","nomeia o diretor-geral",(120,-160),0.5,(10,-8),"start"),
 ("pres","stf","nomeia","indica; o Senado aprova (até 2026)",(-120,0),0.5,(-12,0),"end"),
 ("pres","cong","dinheiro","R$ 47 bi em emendas (2025); ministérios ao Centrão",(-120,-160),0.3,(-10,-14),"end"),
 ("cong","tcu","nomeia","elege 6 de 9 ministros; Pacheco 63 a 4 (2026)",(-80,0),0.5,(-12,0),"end"),
 ("cong","stf","bloqueio","não pauta impeachment nem CPI; aprova a Blindagem",(0,120),0.5,(0,18),"middle"),
 ("stf","stf","regra","",(0,0),0.5,(0,0),"middle"),
 ("stf","cong","regra","reescreve a lei do impeachment (dez/2025); freia as emendas (Dino)",(0,-120),0.5,(0,-44),"middle"),
 ("stf","pgr","regra","valida o inquérito de ofício (10 a 1) e arquiva o que a PGR pede",(120,0),0.5,(12,0),"start"),
 ("pgr","stf","bloqueio","não se opõe às anulações (Aras); arquiva apuração sobre Moraes (Gonet)",(-60,120),0.5,(-12,14),"end"),
 ("pf","stf","bloqueio","relatórios sob demanda do relator; delegado do caso vira assessor",(60,120),0.5,(12,14),"start"),
 ("emp","stf","dinheiro","eventos, institutos, escritórios de cônjuges e filhos",(-200,0),0.5,(-12,0),"end"),
 ("emp","cong","dinheiro","doações e patrocínios; lobby de emendas (FGC)",(-200,60),0.5,(-10,14),"end"),
 ("emp","pgr","dinheiro","Londres 2024: Vorcaro pagou evento com PGR e DG da PF",(200,60),0.5,(10,14),"start"),
 ("tcu","stf","bloqueio","sigilo dos voos da FAB (2024); CNJ sem competência sobre ministros",(0,80),0.5,(0,18),"middle"),
]
RULES = [
 "impedimento por escritório do cônjuge derrubado (7 a 4, 2023)",
 "inquérito das fake news aberto de ofício e mantido por 7 anos",
 "foro ampliado para depois do cargo (7 a 4, 2025)",
 "provas da Odebrecht anuladas erga omnes (monocrática, 2023)",
 "lei do impeachment de ministros suspensa (monocrática, 2025)",
 "80,5% das decisões monocráticas; 3,6% derrubadas pelo plenário",
]

def label(o, lx, ly, anchor, txt, size=12.5):
    tw = len(txt)*(size*0.52)+10
    bx = lx-5 if anchor=="start" else (lx-tw+5 if anchor=="end" else lx-tw/2)
    o.append(f'<rect x="{bx:.0f}" y="{ly-size:.0f}" width="{tw:.0f}" height="{size+5:.0f}" rx="4" fill="{SURF}" opacity="0.94"/>')
    o.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="{size}" text-anchor="{anchor}" fill="{INK}">{esc(txt)}</text>')

def wrap(txt, n):
    words = txt.split(); lines = []; line = ""
    for w in words:
        if len(line+" "+w) > n and line: lines.append(line); line = w
        else: line = (line+" "+w).strip()
    if line: lines.append(line)
    return lines

def svg():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Inter, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="{SURF}"/>']
    o.append(f'<text x="40" y="48" font-size="30" font-weight="700" fill="{INK}">O circuito: como as cúpulas dos três Poderes se protegem umas às outras</text>')
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">Cor = natureza da ligação · números em 07/09/2026 · nenhum item é de um só governo: os mesmos mecanismos foram usados por Bolsonaro e por Lula · fontes em republica_2026/README.md</text>')
    labels = []
    for a, b, kind, txt, ctrl, t, off, anchor in E:
        if a == b: continue
        ax, ay = N[a][0], N[a][1]; bx, by = N[b][0], N[b][1]
        mx, my = (ax+bx)/2+ctrl[0], (ay+by)/2+ctrl[1]
        col = KIND[kind][0]
        o.append(f'<path d="M{ax},{ay} Q{mx},{my} {bx},{by}" fill="none" stroke="{col}" stroke-width="3.4" stroke-linecap="round" opacity="0.85"/>')
        lx = (1-t)**2*ax + 2*(1-t)*t*mx + t**2*bx; ly = (1-t)**2*ay + 2*(1-t)*t*my + t**2*by
        if txt: labels.append((lx+off[0], ly+off[1], anchor, txt))
    for nid, (x, y, name, sub, fill) in N.items():
        big = nid in ("stf", "pres")
        w = 380 if big else 330
        if nid == "emp": w = 470
        lines = wrap(sub, 46 if big else (56 if nid == "emp" else 40))
        h = 44 + 13*len(lines)
        o.append(f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{INK}" stroke-width="{3 if nid=="stf" else 1.6}"/>')
        o.append(f'<text x="{x}" y="{y-h/2+24}" font-size="{16 if big else 14.5}" font-weight="700" text-anchor="middle" fill="{INK}">{esc(name)}</text>')
        for j, ln in enumerate(lines):
            o.append(f'<text x="{x}" y="{y-h/2+42+j*13}" font-size="10.5" text-anchor="middle" fill="{INK2}">{esc(ln)}</text>')
    # caixa das regras, abaixo do STF, à direita
    rx, ry, rw = 1290, 840, 480
    o.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{34+len(RULES)*20}" rx="8" fill="#eef3fb" stroke="{KIND["regra"][0]}" stroke-width="1.6"/>')
    o.append(f'<text x="{rx+14}" y="{ry+22}" font-size="12" font-weight="700" letter-spacing="1" fill="{KIND["regra"][0]}">AS REGRAS QUE A CORTE ESCREVEU PARA SI</text>')
    for j, r in enumerate(RULES):
        o.append(f'<text x="{rx+14}" y="{ry+44+j*20}" font-size="11.5" fill="{INK}">• {esc(r)}</text>')
    # caixas de resultado
    for (x, title, lines, col) in [
        (330, "PARA A CÚPULA: FORMA SEM MÉRITO", ["25 condenações anuladas ou reiniciadas (2019–2026)", "nenhum mérito rejulgado; R$ 14 bi em multas suspensos", "mensalão: 20 anos depois, nenhum condenado preso"], "#0ca30c"),
        (330, "PARA A BASE: MÉRITO SEM FORMA", ["8 de janeiro: 1.734 ações, 1.399 condenados em 3 anos", "254 pessoas com 12 a 14 anos; 119 com 16 a 18 anos", "179 presos; lei da dosimetria suspensa por monocrática"], "#d03b3b")]:
        pass
    bx, by = 330, 1020
    for i, (title, lines, col) in enumerate([
        ("PARA A CÚPULA: FORMA SEM MÉRITO", ["25 condenações anuladas ou reiniciadas (2019 a 2026)", "nenhum mérito rejulgado; R$ 14 bi em multas suspensos", "mensalão: 20 anos depois, nenhum condenado preso"], "#0ca30c"),
        ("PARA A BASE: MÉRITO SEM FORMA", ["8 de janeiro: 1.734 ações, 1.399 condenados em 3 anos", "254 pessoas com 12 a 14 anos; 119 com 16 a 18 anos", "179 presos; lei da dosimetria suspensa por monocrática"], "#d03b3b")]):
        y0 = by + i*150
        o.append(f'<rect x="{bx-230}" y="{y0}" width="460" height="118" rx="8" fill="#ffffff" stroke="{col}" stroke-width="2.4"/>')
        o.append(f'<rect x="{bx-230}" y="{y0}" width="8" height="118" rx="3" fill="{col}"/>')
        o.append(f'<text x="{bx-208}" y="{y0+26}" font-size="12.5" font-weight="700" letter-spacing="1" fill="{col}">{esc(title)}</text>')
        for j, ln in enumerate(lines):
            o.append(f'<text x="{bx-208}" y="{y0+50+j*20}" font-size="12" fill="{INK}">{esc(ln)}</text>')
    o.append(f'<text x="{bx}" y="{by-22}" font-size="13" font-weight="700" text-anchor="middle" fill="{INK}">O RESULTADO, EM DOIS NÚMEROS</text>')
    for lx, ly, anchor, txt in labels: label(o, lx, ly, anchor, txt)
    lx, ly = 60, H-30
    o.append(f'<text x="{lx}" y="{ly-24}" font-size="13" font-weight="700" fill="{INK}">Natureza da ligação</text>')
    for k, (col, lab) in KIND.items():
        o.append(f'<line x1="{lx}" y1="{ly-4}" x2="{lx+34}" y2="{ly-4}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
        o.append(f'<text x="{lx+42}" y="{ly}" font-size="12.5" fill="{INK}">{esc(lab)}</text>')
        lx += 42 + len(lab)*6.6 + 40
    o.append(f'<text x="{W-40}" y="{H-8}" font-size="11" text-anchor="end" fill="{INK2}">Nada aqui é crime provado; é regra, número e decisão pública. CC BY 4.0, Rafael B. Brotto</text>')
    o.append('</svg>')
    return "\n".join(o)

here = pathlib.Path(__file__).parent
s = svg()
(here/"circuito.svg").write_text(s, encoding="utf-8")
(here/"circuito.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{s}', encoding="utf-8")
import fitz
d = fitz.open(str(here/"circuito.svg")); pix = d[0].get_pixmap(dpi=100); pix.save(str(here/"circuito.png"))
print("circuito", W, H, pix.width, pix.height)
