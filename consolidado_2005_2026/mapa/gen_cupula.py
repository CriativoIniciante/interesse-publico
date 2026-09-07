# -*- coding: utf-8 -*-
"""Mapa da cúpula: quem está ligado a quem, com o peso da prova de cada ligação.
Gera mapa_cupula.svg/.html/.png (PNG via PyMuPDF). Fonte: ../README.md e
../../quem_se_repete_2005_2026/materialidade_2026-09-06.md (seção 2.2).
Faixas: em cima o STF; no meio PF, PGR, o banqueiro e o Senado; embaixo o Executivo e os operadores."""
import html, pathlib

SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e0dfd9"
KIND = {  # natureza do vínculo -> cor
 "dinheiro": ("#d03b3b", "dinheiro ou bem a parente, empresa ou escritório"),
 "evento":   ("#ec835a", "evento, viagem ou hospitalidade paga pelo investigado"),
 "contato":  ("#8e5bd6", "encontro ou reunião documentada"),
 "ato":      ("#2a78d6", "ato institucional que afetou o caso"),
 "cargo":    ("#6d6c68", "nomeação, hierarquia, sociedade ou indicação"),
 "alegacao": ("#e0a400", "alegação: delação rejeitada, fonte anônima ou coluna"),
}
PESO = {"P": (5.0, ""), "R": (3.0, ""), "A": (2.2, "8 6")}  # largura e tracejado
def esc(s): return html.escape(s, quote=True)

W, H = 2260, 1760
Y1, Y2, Y3, Y4 = 240, 760, 1280, 1500
N = {  # id: (x, y, nome, subtítulo, grupo)
 "lewand":   (200,  Y1, "Ricardo Lewandowski", "ex-STF, ex-ministro da Justiça · R$ 6,5 mi", "stf"),
 "gilmar":   (520,  Y1, "Gilmar Mendes", "STF · relator de recurso do Master", "stf"),
 "moraes":   (820,  Y1, "Alexandre de Moraes", "STF · 218 páginas da PF", "stf"),
 "toffoli":  (1130, Y1, "Dias Toffoli", "STF · R$ 35 mi via fundo ligado ao Master", "stf"),
 "kassio":   (1440, Y1, "Kassio Nunes Marques", "STF · filho: R$ 281,6 mil", "stf"),
 "fux":      (1750, Y1, "Luiz Fux", "STF · filho em eventos de Vorcaro", "stf"),
 "mendonca": (2060, Y1, "André Mendonça", "STF · relator · 1 encontro admitido", "stf"),
 "andrei":   (400,  Y2, "Andrei Rodrigues", "diretor-geral da PF · Londres 2024", "pf"),
 "gonet":    (760,  Y2, "Paulo Gonet", "PGR · Londres 2024", "mp"),
 "vorcaro":  (1180, Y2, "Daniel Vorcaro", "ex-dono do Master · preso · réu", "op"),
 "alcol":    (1660, Y2, "Davi Alcolumbre", "presidente do Senado", "leg"),
 "outros":   (2060, Y2, "Fachin · Zanin · Dino · Cármen", "STF · sem registro de vínculo com Vorcaro", "none"),
 "lima":     (200,  Y3, "Augusto Lima", "ex-sócio de Vorcaro · Emenda Master", "op"),
 "wagner":   (560,  Y3, "Jaques Wagner", "líder do governo · busca 18/06/2026", "exe"),
 "lula":     (920,  Y3, "Lula", "presidente", "exe"),
 "mantega":  (1280, Y3, "Guido Mantega", "ex-ministro · R$ 1 mi/mês do Master", "exe"),
 "marcola":  (1640, Y3, "Marco Aurélio Ribeiro", "ex-chefe de gabinete de Lula · inquérito", "exe"),
 "luchs":    (1640, Y4, "Luchsinger · Bittar · Careca", "sociedade oculta com Lulinha (PF)", "op"),
}
GROUP_FILL = {"stf": "#eef3fb", "mp": "#f3eefb", "pf": "#eef8f2", "leg": "#fbf5e8", "exe": "#fbeeee", "op": "#ffffff", "none": "#f1f1ee"}
# (a, b, peso, kind, rótulo, ctrl(dx,dy), t, off(dx,dy), anchor)
E = [
 # o banqueiro e o STF
 ("vorcaro","lewand","R","dinheiro","R$ 6,5 mi ao escritório da família",(0,0),0.62,(0,-12),"middle"),
 ("vorcaro","gilmar","R","evento","Londres 2024: Master pagou a palestra de Blair",(0,0),0.3,(-10,-10),"end"),
 ("vorcaro","moraes","R","dinheiro","R$ 131 mi (esposa) · jato · cartões",(0,0),0.6,(-10,0),"end"),
 ("vorcaro","toffoli","R","dinheiro","R$ 35 mi (Arleen → Maridt) · jato",(0,0),0.55,(10,0),"start"),
 ("vorcaro","kassio","R","dinheiro","filho: consultoria paga pelo Master",(0,0),0.8,(10,-6),"start"),
 ("vorcaro","fux","R","evento","filho: NY 2024 · Sapucaí 2025",(0,0),0.5,(10,-6),"start"),
 ("vorcaro","mendonca","P","contato","encontro 14/03/2025 (admitido)",(0,0),0.7,(10,-6),"start"),
 # o banqueiro, a PGR, a PF e o Senado
 ("vorcaro","gonet","R","evento","Londres 2024 · filho · mensagens",(0,0),0.5,(0,-40),"middle"),
 ("vorcaro","andrei","R","evento","Londres 2024 · 'reforçar com Andrei'",(0,-170),0.5,(0,-12),"middle"),
 ("vorcaro","alcol","A","alegacao","US$ 30 mi (delação rejeitada) · nega",(0,0),0.5,(0,-40),"middle"),
 # o banqueiro e o Executivo
 ("vorcaro","lula","R","contato","reunião 04/12/2024, fora da agenda",(0,0),0.3,(10,0),"start"),
 ("vorcaro","mantega","R","dinheiro","R$ 1 mi/mês, jul–nov/2025",(0,0),0.5,(10,0),"start"),
 ("vorcaro","lima","P","cargo","sócio · preso 11 dias · Banco Pleno",(0,0),0.35,(0,-12),"middle"),
 # ligações entre os demais
 ("lima","wagner","R","dinheiro","Emenda Master · apto R$ 2,45 mi (PF)",(0,0),0.5,(0,-42),"middle"),
 ("wagner","lewand","P","cargo","indicou ao Master (admitido)",(-260,0),0.3,(0,-12),"middle"),
 ("wagner","mantega","A","alegacao","indicação ao Master (Wagner nega)",(0,150),0.5,(0,18),"middle"),
 ("mantega","lula","R","contato","levou Vorcaro ao Planalto",(0,0),0.5,(0,48),"middle"),
 ("mantega","marcola","R","contato","4 visitas ao Planalto",(0,0),0.5,(0,48),"middle"),
 ("lula","marcola","P","cargo","chefe de gabinete até 21/07/2026",(0,190),0.5,(0,18),"middle"),
 ("marcola","luchs","R","dinheiro","R$ 217 mil em despesas · quadro de 100 mil euros (PF)",(0,0),0.5,(14,4),"start"),
 ("lula","andrei","P","cargo","segurança 2022 · nomeado DG da PF",(0,0),0.5,(-10,0),"end"),
 ("lula","gonet","P","cargo","indicou (2023) · reconduziu (2025)",(0,0),0.5,(10,0),"start"),
 ("lula","toffoli","R","contato","encontro reservado dez/2025 (coluna)",(-120,-200),0.75,(-10,0),"end"),
 ("gonet","andrei","R","evento","'Andrei e Paulo' · Londres",(0,0),0.5,(0,-40),"middle"),
 ("gonet","gilmar","P","cargo","sócios fundadores do IDP (1998–2017)",(0,0),0.5,(-10,0),"end"),
 ("gonet","moraes","P","ato","arquivou apuração (dez/2025) · pediu nulidade",(0,0),0.5,(10,0),"start"),
 ("andrei","moraes","P","cargo","secretário sob Moraes (2016) · relatórios (2026)",(-60,-120),0.7,(-10,0),"end"),
 ("toffoli","alcol","P","ato","guarda dos dados de Vorcaro (dez/2025–fev/2026)",(0,0),0.3,(10,0),"start"),
 ("moraes","alcol","R","contato","reunião 03/09/2026 · impeachment não pautado",(80,-60),0.7,(10,-8),"start"),
]

def label(o, lx, ly, anchor, txt, size=12.5):
    tw = len(txt) * (size*0.52) + 10
    bx = lx - 5 if anchor == "start" else (lx - tw + 5 if anchor == "end" else lx - tw/2)
    o.append(f'<rect x="{bx:.0f}" y="{ly-size:.0f}" width="{tw:.0f}" height="{size+5:.0f}" rx="4" fill="{SURF}" opacity="0.93"/>')
    o.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="{size}" text-anchor="{anchor}" fill="{INK}">{esc(txt)}</text>')

def svg():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Inter, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="{SURF}"/>']
    o.append(f'<text x="40" y="48" font-size="30" font-weight="700" fill="{INK}">A cúpula e o banqueiro: quem está ligado a quem, e com que prova</text>')
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">Cor = natureza do vínculo · espessura = peso da prova ([P] grossa: prova formal · [R] média: relato documentado · [A] tracejada: alegação) · estado em 06/09/2026 · ninguém aqui foi condenado por nada ligado ao Master</text>')
    # faixas
    for y, lab in [(Y1, "SUPREMO TRIBUNAL FEDERAL"), (Y2, "POLÍCIA FEDERAL · PGR · O BANQUEIRO · SENADO"), (Y3, "EXECUTIVO E OPERADORES")]:
        o.append(f'<rect x="40" y="{y-70}" width="{W-80}" height="140" rx="16" fill="#f3f3f0"/>')
        o.append(f'<text x="56" y="{y-52}" font-size="12" font-weight="700" letter-spacing="1" fill="{INK2}">{lab}</text>')
    labels = []
    for a, b, peso, kind, txt, ctrl, t, off, anchor in E:
        ax, ay = N[a][0], N[a][1]; bx, by = N[b][0], N[b][1]
        mx, my = (ax+bx)/2+ctrl[0], (ay+by)/2+ctrl[1]
        col = KIND[kind][0]; w, dash = PESO[peso]
        d = f' stroke-dasharray="{dash}"' if dash else ''
        o.append(f'<path d="M{ax},{ay} Q{mx},{my} {bx},{by}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" opacity="0.88"{d}/>')
        lx = (1-t)**2*ax + 2*(1-t)*t*mx + t**2*bx; ly = (1-t)**2*ay + 2*(1-t)*t*my + t**2*by
        labels.append((lx+off[0], ly+off[1], anchor, f"[{peso}] {txt}"))
    for nid, (x, y, name, sub, grp) in N.items():
        w = max(len(name)*9.8, len(sub)*6.4) + 34; w = min(max(w, 190), 300)
        big = nid == "vorcaro"
        o.append(f'<rect x="{x-w/2}" y="{y-30}" width="{w}" height="60" rx="12" fill="{GROUP_FILL[grp]}" stroke="{INK}" stroke-width="{3 if big else 1.6}"/>')
        o.append(f'<text x="{x}" y="{y-5}" font-size="{17 if big else 15}" font-weight="700" text-anchor="middle" fill="{INK}">{esc(name)}</text>')
        o.append(f'<text x="{x}" y="{y+15}" font-size="11" text-anchor="middle" fill="{INK2}">{esc(sub)}</text>')
    for lx, ly, anchor, txt in labels:
        label(o, lx, ly, anchor, txt)
    # legenda
    lx, ly = 60, H-72
    o.append(f'<text x="{lx}" y="{ly-24}" font-size="13" font-weight="700" fill="{INK}">Natureza do vínculo (cor)</text>')
    for k, (col, lab) in KIND.items():
        o.append(f'<line x1="{lx}" y1="{ly-4}" x2="{lx+34}" y2="{ly-4}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
        o.append(f'<text x="{lx+42}" y="{ly}" font-size="12" fill="{INK}">{esc(lab)}</text>')
        lx += 42 + len(lab)*6.3 + 30
    lx = 60; ly = H-26
    o.append(f'<text x="{lx}" y="{ly-24}" font-size="13" font-weight="700" fill="{INK}">Peso da prova (espessura)</text>')
    for k, lab in [("P", "prova formal: decisão, documento oficial, operação, admissão"), ("R", "relato documentado: reportagem com documento"), ("A", "alegação: delação rejeitada, fonte anônima, coluna")]:
        w, dash = PESO[k]; d = f' stroke-dasharray="{dash}"' if dash else ''
        o.append(f'<line x1="{lx}" y1="{ly-4}" x2="{lx+34}" y2="{ly-4}" stroke="{INK}" stroke-width="{w}" stroke-linecap="round"{d}/>')
        o.append(f'<text x="{lx+42}" y="{ly}" font-size="12" fill="{INK}">[{k}] {esc(lab)}</text>')
        lx += 42 + len(lab)*6.3 + 50
    o.append(f'<text x="{W-40}" y="{H-8}" font-size="11" text-anchor="end" fill="{INK2}">Fontes e detalhes em consolidado_2005_2026/README.md · CC BY 4.0, Rafael B. Brotto</text>')
    o.append('</svg>')
    return "\n".join(o)

here = pathlib.Path(__file__).parent
s = svg()
(here/"mapa_cupula.svg").write_text(s, encoding="utf-8")
(here/"mapa_cupula.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{s}', encoding="utf-8")
import fitz
doc = fitz.open(str(here/"mapa_cupula.svg")); pix = doc[0].get_pixmap(dpi=100); pix.save(str(here/"mapa_cupula.png"))
print("mapa_cupula", W, H, pix.width, pix.height)
