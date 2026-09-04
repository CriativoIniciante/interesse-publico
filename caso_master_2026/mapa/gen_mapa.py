# -*- coding: utf-8 -*-
"""Gera mapa_relacoes.svg e mapa_relacoes.html (caso Master, 04/09/2026).
Nós = pessoas/órgãos. Linhas = relações, coloridas pelo status e com espessura pelo peso da prova.
PNG: Chrome headless (ver render.sh)."""
import html, pathlib

W, H = 2100, 1600
SURF, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
RED, AMB, GRN, GRY = "#d03b3b", "#fab219", "#0ca30c", "#9a9990"
TAG = {"I": "[I] ", "S": "[S] ", "L": "[L] ", "V": ""}
COL = {"I": RED, "S": AMB, "L": GRN, "V": GRY}

# id: (x, y, nome, sub, largura)
N = {
 "vorcaro":  (1000, 760, "Daniel Vorcaro", "ex-dono do Master · preso 2× · réu", 210),
 "barci":    (330, 330, "Escritório Barci de Moraes", "Viviane Barci, mulher do ministro", 230),
 "moraes":   (330, 520, "Alexandre de Moraes", "negou contato 5× (mar–jun/2026)", 230),
 "toffoli":  (330, 700, "Dias Toffoli", "saiu da relatoria em 12/02", 190),
 "mendonca": (330, 900, "André Mendonça", "relator: Master, INSS e Dark Horse", 230),
 "fachin":   (180, 1070, "Edson Fachin", "presidente do STF", 170),
 "dino":     (480, 1070, "Flávio Dino", "emendas · GoUp · 3º inquérito de Lulinha", 240),
 "faria":    (740, 430, "Fábio Faria", "ex-ministro (Bolsonaro)", 180),
 "ciro":     (740, 250, "Ciro Soares", "advogado, ex-defensor do Master", 200),
 "cezinha":  (660, 990, "Cezinha de Madureira", "deputado (PL-SP)", 190),
 "gonet":    (980, 200, "Paulo Gonet", "PGR · pediu nulidade em 12 h", 200),
 "andrei":   (1300, 200, "Andrei Rodrigues", "diretor-geral da PF", 190),
 "perito":   (1640, 200, "Perito da PF", "'Moraes.pdf' em 04/12/2025 · afastado", 220),
 "relint":   (1300, 370, "Relatório de inteligência da PF", "50 pp · sem timbre nem assinatura", 250),
 "vaza":     (1640, 370, "Vazamentos à imprensa", "Vaza Flávio (mai) · áudios (set)", 210),
 "lima":     (1290, 600, "Augusto Lima", "ex-sócio · Banco Pleno liquidado", 200),
 "galipolo": (1560, 640, "Gabriel Galípolo", "Banco Central ('G')", 180),
 "alcol":    (1900, 560, "Davi Alcolumbre", "presidente do Senado", 190),
 "wagner":   (1900, 720, "Jaques Wagner", "senador PT-BA · busca 18/06", 200),
 "nogueira": (1900, 880, "Ciro Nogueira", "senador PP-PI · busca 07/05", 200),
 "brb":      (1560, 900, "BRB · P. H. Costa", "ex-presidente · preso 16/04", 200),
 "lula":     (1800, 1000, "Lula", "presidente · candidato", 160),
 "flavio":   (860, 1270, "Flávio Bolsonaro", "candidato PL · inquérito 23/07", 210),
 "eduardo":  (520, 1340, "Eduardo Bolsonaro · Havengate", "fundo do advogado Paulo Calixto (TX)", 240),
 "goup":     (680, 1480, "GoUp · emendas de Mario Frias", "produtora do filme · R$ 2 mi", 240),
 "jair":     (1030, 1480, "Jair Bolsonaro · Tarcísio · Kassab", "doações de 2022 · negam", 260),
 "careca":   (1380, 1280, "'Careca do INSS'", "A. C. Camilo Antunes · preso 12/09/2025", 230),
 "luchs":    (1640, 1180, "Roberta Luchsinger", "empresária · investigada", 190),
 "lulinha":  (1800, 1280, "Fábio Luís (Lulinha)", "3 inquéritos (jul–ago/2026)", 200),
 "marcola":  (1640, 1440, "Marco Aurélio Ribeiro", "ex-chefe de gabinete de Lula", 210),
 "freichico":(1930, 1130, "Frei Chico · Sindnapi", "R$ 599,5 mi descontados · ele não é investigado", 250),
}

# (a, b, status, peso 1-3, rótulo, (dx,dy) do ponto de controle, t, (ox,oy) deslocamento do rótulo, anchor)
E = [
 ("vorcaro","barci","I",3,"R$ 131 mi · 'pague sem nota' · aeronaves", (0,-170), 0.72, (0,16), "middle"),
 ("vorcaro","moraes","I",3,"52 notas · 'conseguiu bloquear?' · 'já tenho que estar fora?'", (0,0), 0.25, (0,12), "middle"),
 ("moraes","barci","V",1,"marido da sócia", (0,0), 0.5, (15,4), "start"),
 ("faria","vorcaro","S",2,"apresentou a Moraes · 'o careca não pode atrasar'", (0,0), 0.5, (15,-4), "start"),
 ("vorcaro","toffoli","S",2,"R$ 35 mi a empresa da família · nega", (0,-30), 0.5, (0,18), "middle"),
 ("ciro","gonet","S",2,"'charuto e Macallan' · filho em Londres", (0,0), 0.5, (10,-22), "end"),
 ("vorcaro","ciro","V",1,"advogado do banco", (0,0), 0.5, (15,-35), "start"),
 ("vorcaro","andrei","S",2,"Londres 2024, evento pago · 'reforçar com Andrei'", (100,0), 0.55, (16,0), "start"),
 ("vorcaro","mendonca","S",2,"reunião 14/03/2025 · votou contra o banco", (0,70), 0.5, (0,18), "middle"),
 ("mendonca","vorcaro","L",3,"levantou o sigilo · mandou identificar", (0,-70), 0.5, (0,18), "middle"),
 ("cezinha","mendonca","V",1,"intermediou", (0,0), 0.5, (0,-10), "middle"),
 ("moraes","mendonca","S",2,"petição no INQ 4781", (-230,0), 0.3, (-84,-6), "middle"),
 ("gonet","mendonca","S",2,"pede nulidade em 12 h", (-330,-120), 0.12, (17,3), "start"),
 ("andrei","relint","S",2,"monitorou o juiz", (0,0), 0.5, (15,4), "start"),
 ("relint","moraes","S",2,"entregue a Moraes 01/09 · usado 03/09", (0,80), 0.75, (-103,28), "start"),
 ("perito","vaza","I",2,"sugeriu vazar", (0,0), 0.5, (15,4), "start"),
 ("andrei","vorcaro","L",3,"prendeu 2× · 218 páginas", (-200,0), 0.6, (11,4), "start"),
 ("fachin","mendonca","L",2,"5 dias úteis (03/09)", (0,0), 0.5, (-90,125), "start"),
 ("vorcaro","alcol","S",1,"US$ 30 mi (delação rejeitada) · nega", (0,-90), 0.85, (25,31), "end"),
 ("alcol","moraes","S",2,"reunião 03/09 · não pauta impeachment", (0,-90), 0.2, (0,26), "middle"),
 ("vorcaro","wagner","I",3,"apto R$ 2,45 mi · R$ 3,5 mi · busca", (0,0), 0.6, (0,-14), "middle"),
 ("lima","wagner","S",2,"'Emenda Master'", (0,0), 0.7, (0,-14), "middle"),
 ("vorcaro","lima","V",1,"ex-sócio", (0,0), 0.5, (5,-12), "middle"),
 ("vorcaro","nogueira","I",3,"R$ 300 mil/mês · busca", (0,-40), 0.7, (0,-12), "middle"),
 ("vorcaro","galipolo","S",2,"'amigos no BC' · 'G'", (0,0), 0.5, (0,-10), "middle"),
 ("vorcaro","brb","I",3,"6 imóveis, R$ 146 mi", (0,0), 0.55, (0,18), "middle"),
 ("vorcaro","lula","S",2,"reunião fora da agenda (dez/2024)", (0,120), 0.5, (0,18), "middle"),
 ("vorcaro","flavio","I",3,"US$ 12,3 mi pagos · inquérito 23/07", (60,0), 0.5, (20,0), "start"),
 ("flavio","eduardo","S",2,"Havengate · malas (delação Freixo)", (0,0), 0.5, (10,35), "start"),
 ("vorcaro","jair","S",1,"doações de 2022 = propina? (delação rejeitada)", (60,0), 0.6, (13,0), "start"),
 ("mendonca","flavio","L",2,"abriu o inquérito (23/07)", (0,0), 0.55, (19,7), "start"),
 ("dino","goup","L",2,"liberou dados à PF (21/08)", (0,0), 0.35, (-15,-3), "end"),
 ("careca","luchs","S",2,"apresentou Lulinha", (0,0), 0.5, (0,-12), "middle"),
 ("luchs","lulinha","I",2,"R$ 300 mil 'para o filho do cara'", (0,0), 0.5, (-30,-10), "middle"),
 ("luchs","marcola","I",2,"pagamentos · joias · quadro € 100 mil", (0,0), 0.5, (15,30), "start"),
 ("lula","lulinha","V",1,"pai e filho", (0,0), 0.75, (15,4), "start"),
 ("lula","freichico","V",1,"irmãos", (0,0), 0.5, (5,-10), "start"),
]

GROUPS = [
 ("SUPREMO TRIBUNAL FEDERAL", 60, 250, 620, 1130),
 ("PGR E POLÍCIA FEDERAL", 860, 110, 1780, 440),
 ("CONGRESSO, EXECUTIVO E BANCO CENTRAL", 1440, 480, 2060, 1035),
 ("CAMPO BOLSONARO · DARK HORSE", 340, 1170, 1180, 1530),
 ("FRENTE DO INSS (mesmo relator)", 1240, 1070, 2080, 1530),
]

def esc(s): return html.escape(s, quote=True)

def bez(a, b, ctrl, t):
    ax, ay = N[a][0], N[a][1]; bx, by = N[b][0], N[b][1]
    mx, my = (ax+bx)/2 + ctrl[0], (ay+by)/2 + ctrl[1]
    x = (1-t)**2*ax + 2*(1-t)*t*mx + t**2*bx
    y = (1-t)**2*ay + 2*(1-t)*t*my + t**2*by
    return x, y, (ax, ay, mx, my, bx, by)

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Inter, Arial, sans-serif">')
out.append(f'<rect width="{W}" height="{H}" fill="{SURF}"/>')
out.append(f'<text x="40" y="52" font-size="32" font-weight="700" fill="{INK}">Caso Master: quem se liga a quem, e com que peso de prova</text>')
out.append(f'<text x="40" y="82" font-size="16" fill="{INK2}">Estado em 04/09/2026 · ninguém foi condenado · cada linha é checável em github.com/CriativoIniciante/interesse-publico (caso_master_2026)</text>')

for title, x1, y1, x2, y2 in GROUPS:
    out.append(f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" rx="14" fill="#f1f1ee" stroke="#e0dfd9"/>')
    out.append(f'<text x="{x1+14}" y="{y1+24}" font-size="13" font-weight="700" letter-spacing="1" fill="{INK2}">{esc(title)}</text>')

labels = []
for a, b, st, wgt, label, ctrl, t, off, anchor in E:
    lx, ly, (ax, ay, mx, my, bx, by) = bez(a, b, ctrl, t)
    col = COL[st]
    width = {3: 6, 2: 4, 1: 2}[wgt]
    dash = ' stroke-dasharray="9 7"' if wgt == 1 else ''
    out.append(f'<path d="M{ax},{ay} Q{mx},{my} {bx},{by}" fill="none" stroke="{col}" stroke-width="{width}" stroke-linecap="round" opacity="0.92"{dash}/>')
    labels.append((lx+off[0], ly+off[1], anchor, TAG[st] + label))

# labels drawn after all lines, before nodes
for lx, ly, anchor, txt in labels:
    out.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="13" text-anchor="{anchor}" fill="{INK}" paint-order="stroke" stroke="{SURF}" stroke-width="6" stroke-linejoin="round">{esc(txt)}</text>')

for nid in N:
    x, y, name, sub, w = N[nid]
    out.append(f'<rect x="{x-w/2}" y="{y-30}" width="{w}" height="60" rx="10" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<text x="{x}" y="{y-4}" font-size="16" font-weight="700" text-anchor="middle" fill="{INK}">{esc(name)}</text>')
    out.append(f'<text x="{x}" y="{y+16}" font-size="11.5" text-anchor="middle" fill="{INK2}">{esc(sub)}</text>')

# legend
lx, ly = 70, 1190
out.append(f'<rect x="{lx-15}" y="{ly-28}" width="265" height="330" rx="12" fill="#ffffff" stroke="#e0dfd9"/>')
out.append(f'<text x="{lx}" y="{ly}" font-size="14" font-weight="700" fill="{INK}">Como ler</text>')
rows = [
 (RED, 6, "[I] vermelho: indício documentado de ilegalidade, ou inquérito formal com prova material"),
 (AMB, 4, "[S] amarelo: suspeito. Conflito de interesse, alegação sem corroboração, omissão sem explicação"),
 (GRN, 4, "[L] verde: ato lícito, dentro da função"),
 (GRY, 2, "cinza: vínculo (família, sociedade), sem status"),
]
yy = ly + 24
for c, wdt, txt in rows:
    out.append(f'<line x1="{lx}" y1="{yy-4}" x2="{lx+38}" y2="{yy-4}" stroke="{c}" stroke-width="{wdt}" stroke-linecap="round"/>')
    words = txt.split(); line = ""; lines = []
    for wd in words:
        if len(line + " " + wd) > 31: lines.append(line); line = wd
        else: line = (line + " " + wd).strip()
    lines.append(line)
    for i, ln in enumerate(lines):
        out.append(f'<text x="{lx+48}" y="{yy+i*15}" font-size="11.5" fill="{INK}">{esc(ln)}</text>')
    yy += 15*len(lines) + 12
out.append(f'<text x="{lx}" y="{yy+6}" font-size="12.5" font-weight="700" fill="{INK}">Espessura = peso da prova</text>')
for i, (wdt, d, txt) in enumerate([(6, "", "prova material: documento, transferência, mensagem"), (4, "", "relato documentado: PF, imprensa com fonte"), (2, ' stroke-dasharray="9 7"', "alegação de parte interessada")]):
    y0 = yy + 26 + i*22
    out.append(f'<line x1="{lx}" y1="{y0}" x2="{lx+38}" y2="{y0}" stroke="{INK2}" stroke-width="{wdt}" stroke-linecap="round"{d}/>')
    out.append(f'<text x="{lx+48}" y="{y0+4}" font-size="11.5" fill="{INK}">{esc(txt)}</text>')

out.append(f'<text x="40" y="{H-18}" font-size="12" fill="{INK2}">Fora do mapa por espaço: Kassio, Fux, Lewandowski, Mantega, Cláudio Castro, Mansur, Freixo, Zanin e Gilmar (ver personagens.md). Etiqueta [I]/[S]/[L] em cada linha para o significado não depender só da cor. CC BY 4.0, Rafael B. Brotto.</text>')
out.append('</svg>')

svg = "\n".join(out)
here = pathlib.Path(__file__).parent
(here / "mapa_relacoes.svg").write_text(svg, encoding="utf-8")
(here / "mapa_relacoes.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{svg}', encoding="utf-8")
print("ok")
