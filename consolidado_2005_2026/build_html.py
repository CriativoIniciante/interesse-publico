# -*- coding: utf-8 -*-
"""Monta dossie_visual.html a partir do template, do README.md (tabelas das seções 1, 3 e 6)
e dos quatro mapas SVG embutidos. Uso: python build_html.py [saida_artifact.html]
O README é a fonte canônica do texto; este arquivo só o apresenta."""
import re, sys, html, pathlib, subprocess

here = pathlib.Path(__file__).parent
repo = here.parent
README = (here / "README.md").read_text(encoding="utf-8")
TPL = (here / "dossie_visual_template.html").read_text(encoding="utf-8")
REPO_URL = "https://github.com/CriativoIniciante/interesse-publico"
try:
    BRANCH = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip() or "main"
except Exception:
    BRANCH = "main"
DATA = re.search(r"\*\*Estado em (\d{2}/\d{2}/\d{4})", README).group(1)

GRADE = re.compile(r"\[([PRANO])((?:[ /][^\]]*)?)\]")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD = re.compile(r"\*\*(.+?)\*\*")

def inline(md):
    """markdown de célula -> html (escape, links, negrito, letras de prova)."""
    s = html.escape(md, quote=False)
    def link(m):
        href = m.group(2)
        if href.startswith("../"): href = f"{REPO_URL}/blob/{BRANCH}/" + href[3:]
        elif not href.startswith("http"): href = f"{REPO_URL}/blob/{BRANCH}/consolidado_2005_2026/" + href
        return f'<a href="{href}">{m.group(1)}</a>'
    s = LINK.sub(link, s)
    s = BOLD.sub(r"<strong>\1</strong>", s)
    s = GRADE.sub(lambda m: f'<span class="g g-{m.group(1)}">[{m.group(1)}{m.group(2)}]</span>', s)
    return s

def tables(md):
    """Todas as tabelas markdown: lista de (posição, cabeçalho, linhas)."""
    out = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i+1]):
            head = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            rows = []; j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            out.append((i, head, rows)); i = j
        else:
            i += 1
    return out

def section(md, title_start):
    """Texto de uma seção '## N. título' até a próxima '## '."""
    m = re.search(r"^## " + re.escape(title_start) + r".*?$", md, flags=re.M)
    if not m: raise SystemExit("seção não encontrada: " + title_start)
    rest = md[m.end():]
    n = re.search(r"^## ", rest, flags=re.M)
    return rest[:n.start()] if n else rest

# ---- seção 1: tabela dos casos ----
sec1 = section(README, "1. ")
_, head, rows = tables(sec1)[0]
CASE_COLOR = {"Mensalão": "M", "Petrolão": "L", "INSS": "I", "Master": "B", "Emendas": "E"}
t = ["<table><thead><tr>" + "".join(f"<th>{html.escape(h)}</th>" for h in head) + "</tr></thead><tbody>"]
for r in rows:
    key = next((v for k, v in CASE_COLOR.items() if k in r[0]), "")
    style = f' style="--c:var(--{key})"' if key else ""
    t.append(f"<tr{style}>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
t.append("</tbody></table>")
CASOS_TABLE = "\n".join(t)

# ---- seção 3: fichas ----
sec3 = section(README, "3. ")
groups = re.split(r"^### ", sec3, flags=re.M)[1:]
GRADE_ORDER = {"P": 0, "R": 1, "A": 2, "N": 3, "O": 4}
fichas_html = []
n_people = 0
for g in groups:
    gtitle, gbody = g.split("\n", 1)
    gtitle = re.sub(r"^\d\.\d\s*", "", gtitle).strip()
    tb = tables(gbody)
    if not tb:  # 3.7: texto corrido
        paras = [p.strip() for p in gbody.strip().split("\n\n") if p.strip()]
        fichas_html.append(f'<div class="group"><h3>{html.escape(gtitle)}</h3><div class="prose">' + "".join(f"<p>{inline(p)}</p>" for p in paras) + "</div></div>")
        continue
    _, head, rows = tb[0]
    cards = []
    for r in rows:
        n_people += 1
        raw_name = r[0]
        m = re.match(r"\*\*(.+?)\*\*\s*(.*)", raw_name)
        name = m.group(1) if m else BOLD.sub(r"\1", raw_name)
        role = (m.group(2) if m else "").strip().strip("()")
        cells = dict(zip(head, r))
        grade_txt = cells.get("Grau", "").strip()
        gm = re.match(r"\[([PRANO])", grade_txt)
        grade = gm.group(1) if gm else ""
        if "Condição" in cells:  # 3.6 históricos
            cond = cells["Condição"]
            gm2 = GRADE.search(cond); grade = gm2.group(1) if gm2 else ""
            role = GRADE.sub("", BOLD.sub(r"\1", cond)).strip(" ;")
        badge = f'<span class="grade {grade}">[{grade}]</span>' if grade else '<span class="grade none">sem registro</span>'
        fields = []
        for h in head[1:]:
            if h in ("Grau", "Condição"): continue
            v = cells.get(h, "").strip()
            if not v: continue
            cls = ' class="clean"' if v.startswith("**Sem registro") else ""
            fields.append(f"<div><dt>{html.escape(h)}</dt><dd{cls}>{inline(v)}</dd></div>")
        if not fields:
            fields.append('<div><dd class="clean">Sem registro de vínculo com Vorcaro.</dd></div>')
        cards.append(f'<article class="ficha"><div class="top"><div><div class="name">{html.escape(name)}</div>' + (f'<div class="role">{inline(role)}</div>' if role else "") + f'</div>{badge}</div><dl>' + "".join(fields) + "</dl></article>")
    fichas_html.append(f'<div class="group"><h3>{html.escape(gtitle)} <small>{len(rows)} nomes</small></h3><div class="fichas">' + "".join(cards) + "</div></div>")
FICHAS = "\n".join(fichas_html)

# ---- seção 6: correções ----
sec6 = section(README, "6. ")
_, head6, rows6 = tables(sec6)[0]
fx = [f'<div class="fix" style="border-top:1px solid var(--line2)"><div class="w">{html.escape(head6[0])}</div><div class="w">{html.escape(head6[1])}</div><div class="w">{html.escape(head6[2])}</div></div>']
for r in rows6:
    fx.append(f'<div class="fix"><div class="w">{inline(r[0])}</div><div class="was">{inline(r[1])}</div><div class="now">{inline(r[2])}</div></div>')
CORRECOES = "\n".join(fx)

# ---- SVGs embutidos ----
def svg_inline(path, label):
    s = pathlib.Path(path).read_text(encoding="utf-8")
    s = re.sub(r'<svg([^>]*?)\swidth="\d+"\sheight="\d+"', r'<svg\1', s, count=1)
    s = s.replace("<svg ", f'<svg role="img" aria-label="{label}" ', 1)
    return s
SVG_MATRIZ = svg_inline(repo / "quem_se_repete_2005_2026/mapa/matriz_repeticoes.svg", "Matriz pessoa por caso")
SVG_CUPULA = svg_inline(here / "mapa/mapa_cupula.svg", "Mapa da cúpula e do banqueiro")
SVG_CADEIAS = svg_inline(repo / "quem_se_repete_2005_2026/mapa/rede_cadeias.svg", "Cadeias de operadores")
SVG_MASTER = svg_inline(repo / "caso_master_2026/mapa/mapa_relacoes.svg", "Mapa das relações do caso Master")
n_rows = len(re.findall(r'^ \("[^"]+", \{', (repo / "quem_se_repete_2005_2026/mapa/gen.py").read_text(encoding="utf-8"), flags=re.M))

head_html = TPL.split("<!--HEAD-->")[1].split("<!--/HEAD-->")[0]
body_html = TPL.split("<!--BODY-->")[1].split("<!--/BODY-->")[0]
fill = {"{{CASOS_TABLE}}": CASOS_TABLE, "{{FICHAS}}": FICHAS, "{{CORRECOES}}": CORRECOES,
        "{{SVG_MATRIZ}}": SVG_MATRIZ, "{{SVG_CUPULA}}": SVG_CUPULA, "{{SVG_CADEIAS}}": SVG_CADEIAS, "{{SVG_MASTER}}": SVG_MASTER,
        "{{REPO}}": REPO_URL, "{{BRANCH}}": BRANCH, "{{DATA}}": DATA, "{{N_ROWS}}": str(n_rows)}
for k, v in fill.items():
    head_html = head_html.replace(k, v); body_html = body_html.replace(k, v)

full = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + head_html + '</head>\n<body>\n' + body_html + '</body>\n</html>\n')
(here / "dossie_visual.html").write_text(full, encoding="utf-8")
if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(head_html + body_html, encoding="utf-8")
print("dossie_visual.html", len(full), "bytes ·", n_people, "fichas ·", n_rows, "linhas na matriz · branch", BRANCH)
