# -*- coding: utf-8 -*-
"""Gera matriz_repeticoes.svg e rede_cadeias.svg (+ .html). PNG via Chrome headless."""
import html, pathlib

SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e0dfd9"
RED, ORG, AMB, BLU, GRN, GRY = "#d03b3b", "#ec835a", "#fab219", "#2a78d6", "#0ca30c", "#9a9990"
CASE = {"M": ("#2a78d6", "Mensalão"), "L": ("#eb6834", "Lava Jato"), "I": ("#1baf7a", "INSS"), "B": ("#e87ba4", "Master"), "E": ("#eda100", "Emendas")}
def esc(s): return html.escape(s, quote=True)

# ---------- MATRIZ ----------
COLS = [("M", "MENSALÃO", "2005–2012"), ("L", "PETROLÃO · LAVA JATO", "2014–2021"), ("I", "INSS", "2025–2026"), ("B", "MASTER", "2025–2026"), ("E", "EMENDAS", "2025–2026")]
SYM = {
 "cond": (RED, "●", "condenado"),
 "anul": (RED, "◐", "condenação anulada"),
 "reu":  (ORG, "▲", "réu, denunciado ou preso preventivo"),
 "inv":  (AMB, "■", "investigado ou alvo de busca"),
 "del":  (BLU, "◆", "delator"),
 "cit":  (GRY, "○", "citado, sem processo"),
 "abs":  (GRN, "✓", "absolvido, arquivado ou prescrito"),
 "inst": (INK, "▣", "atuação institucional (julgou, relatou, decidiu)"),
}
ROWS = [
 ("POLÍTICOS", None),
 ("Lula", {"M": ("cit", "testemunha, não réu; relato de Valério (2012) sem denúncia"), "L": ("anul", "condenado em 3 instâncias (triplex); anulado em 2021"), "I": ("cit", "irmão e filho; ele não é investigado"), "B": ("cit", "reunião fora da agenda (dez/2024)")}),
 ("José Dirceu", {"M": ("cond", "7a11m, corrupção ativa"), "L": ("anul", "23a (2016) e 11a3m (2017); anuladas por Gilmar em out/2024")}),
 ("Delúbio Soares", {"M": ("cond", "8a11m"), "L": ("anul", "5a (Moro, 2017); STJ anulou; prescrita")}),
 ("José Genoino", {"M": ("cond", "6a11m")}),
 ("Roberto Jefferson", {"M": ("cond", "delator informal do mensalão; condenado")}),
 ("Valdemar Costa Neto", {"M": ("cond", "7a10m; indulto em 2016"), "E": ("cit", "PF: 21 emendas, R$ 119 mi, sem mandato; nega")}),
 ("José Janene (PP)", {"M": ("reu", "denunciado; R$ 4,1 mi de Valério; morreu em 2010"), "L": ("cit", "apontado como mentor do esquema do PP; Youssef era seu doleiro")}),
 ("Eduardo Cunha", {"L": ("anul", "condenado 2017 e 2020; 2ª Turma anulou a de 2020 (2023)"), "E": ("cit", "PF: ao menos 29 emendas sem mandato; nega")}),
 ("Michel Temer", {"L": ("abs", "3 denúncias barradas (2017); preso 5 dias (2019); absolvido (Angra 3)"), "B": ("cit", "pagamentos do Master (imprensa, abr/2026)")}),
 ("Guido Mantega", {"L": ("abs", "fases anuladas (Gilmar); absolvido BNDES (2023); Zelotes prescrita (2025)"), "B": ("cit", "R$ 1 mi/mês (imprensa, abr/2026)")}),
 ("Ciro Nogueira", {"L": ("abs", "denunciado 2016 e 2020 (R$ 7,3 mi Odebrecht); arquivado e rejeitado"), "B": ("inv", "busca 07/05/2026; R$ 300 mil/mês; emenda do FGC")}),
 ("Jaques Wagner", {"L": ("abs", "inquérito Arena Fonte Nova (2018) arquivado em fev/2025"), "B": ("inv", "busca 18/06/2026; apto R$ 2,45 mi; R$ 3,5 mi; voos")}),
 ("Gilberto Kassab", {"L": ("reu", "réu na Justiça Eleitoral de SP (JBS, desde 2021)"), "B": ("cit", "delação rejeitada: propina via Credcesta; nega")}),
 ("Davi Alcolumbre", {"L": ("cit", "citado em denúncia de 2019; 2 inquéritos arquivados no STF"), "B": ("cit", "US$ 30 mi em delação rejeitada; nega; não pauta impeachment")}),
 ("Jair Bolsonaro", {"I": ("cit", "IN de 25/03/2022, no seu governo, liberou a Credcesta 16 dias após ofício do Master"), "B": ("cit", "delação rejeitada: doação 2022 como propina; nega")}),
 ("Flávio Bolsonaro", {"B": ("inv", "inquérito 23/07/2026: US$ 12,3 mi do Dark Horse")}),
 ("Tarcísio de Freitas", {"B": ("cit", "delação rejeitada: R$ 2 mi como propina; nega")}),
 ("Carlos Lupi", {"I": ("cit", "citado em delações de ex-diretores do INSS (fev/2026); saiu em abr/2025")}),
 ("Fábio Luís (Lulinha)", {"I": ("inv", "3 inquéritos (jul–ago/2026); CPMI pediu indiciamento")}),
 ("Frei Chico", {"I": ("cit", "vice do Sindnapi (R$ 599,5 mi descontados); não investigado")}),
 ("OPERADORES E EMPRESÁRIOS", None),
 ("Marcos Valério", {"M": ("cond", "40 anos (reduzida); mensalão tucano: 16a9m (2018)")}),
 ("Alberto Youssef", {"M": ("cond", "lavou R$ 1,16 mi de Janene (condenado 2015)"), "L": ("del", "doleiro pivô; delator; condenado")}),
 ("Paulo Roberto Costa", {"L": ("del", "ex-diretor da Petrobras (PP); delator")}),
 ("Marcelo Odebrecht", {"L": ("del", "19a (2016); delator; provas da leniência anuladas (2023)")}),
 ("Lúcio Funaro", {"L": ("del", "operador ligado a Cunha e ao MDB; delator (2017)")}),
 ("Alessandro Stefanutto", {"I": ("reu", "ex-presidente do INSS; R$ 250 mil/mês; preso nov/2025")}),
 ("'Careca do INSS'", {"I": ("reu", "preso 12/09/2025; R$ 24,5 mi em 5 meses")}),
 ("Maurício Camisotti", {"I": ("del", "preso 12/09/2025; delação com PF e PGR")}),
 ("Roberta Luchsinger", {"I": ("inv", "tráfico de influência; apresentou Lulinha ao Careca")}),
 ("Daniel Vorcaro", {"I": ("cit", "consignado 74% irregular; CPMI pediu indiciamento"), "B": ("reu", "preso 2×; réu; 2 delações rejeitadas")}),
 ("Augusto Lima", {"B": ("inv", "9ª fase; 'Emenda Master' com Wagner; Banco Pleno liquidado")}),
 ("JUDICIÁRIO, MINISTÉRIO PÚBLICO E POLÍCIA FEDERAL", None),
 ("Dias Toffoli", {"M": ("inst", "votou pela absolvição de Dirceu, seu ex-chefe, sem se declarar impedido"), "L": ("inst", "set/2023: anulou todas as provas da leniência da Odebrecht"), "B": ("cit", "R$ 35 mi a empresa da família; deixou a relatoria")}),
 ("Ricardo Lewandowski", {"M": ("inst", "revisor; absolveu Dirceu de corrupção ativa e 13 réus de quadrilha"), "L": ("inst", "2ª Turma: votou a suspeição de Moro"), "B": ("cit", "R$ 250 mil/mês ao escritório da família (2023–2025), sendo ministro da Justiça")}),
 ("Gilmar Mendes", {"M": ("inst", "julgador"), "L": ("inst", "anulou fases (Mantega) e condenações (Dirceu); relator da suspeição de Moro"), "B": ("inst", "alinhado a Moraes contra Mendonça")}),
 ("Edson Fachin", {"L": ("inst", "relator no STF; anulou as condenações de Lula (2021)"), "B": ("inst", "presidente; procedimento de 03/09")}),
 ("Alexandre de Moraes", {"L": ("inst", "contra a soltura (2019); pela anulação (2021)"), "B": ("cit", "218 páginas da PF; escritório da mulher, R$ 80 mi; pede investigação de Mendonça")}),
 ("Cristiano Zanin", {"L": ("inst", "advogado de Lula (2013–2022); obteve a suspeição de Moro"), "B": ("inst", "ministro (2023–); 1ª Turma; alinhado a Moraes")}),
 ("Flávio Dino", {"I": ("inst", "autorizou o 3º inquérito de Lulinha (04/08)"), "B": ("inst", "dados do Dark Horse à PF; alinhado a Moraes"), "E": ("inst", "relator; 'emendas de líder' nulas (23/08)")}),
 ("André Mendonça", {"I": ("inst", "relator da Sem Desconto"), "B": ("inst", "relator; levantou o sigilo; recebeu Vorcaro em 2025")}),
 ("Sergio Moro", {"L": ("inst", "juiz (2014–18); suspeito (2021); ministro de Bolsonaro; senador")}),
 ("Paulo Gonet", {"I": ("inst", "PGR pediu refazer a delação de Camisotti"), "B": ("cit", "mensagens atribuídas; pediu nulidade")}),
 ("Andrei Rodrigues", {"I": ("inst", "PF conduz a Sem Desconto (48 indiciados, 14/07/2026)"), "B": ("cit", "Londres 2024; relatório de inteligência; acusado por Vorcaro")}),
]

def wrap(txt, n):
    words = txt.split(); lines = []; line = ""
    for w in words:
        if len(line + " " + w) > n and line: lines.append(line); line = w
        else: line = (line + " " + w).strip()
    if line: lines.append(line)
    return lines[:3]

def matriz():
    NAME_W, COL_W, ROW_H, SEC_H = 250, 300, 50, 34
    W = 60 + NAME_W + 5*COL_W + 60
    top = 150
    rows_h = sum(SEC_H if r[1] is None else ROW_H for r in ROWS)
    H = top + rows_h + 150
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Inter, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="{SURF}"/>']
    o.append(f'<text x="40" y="48" font-size="30" font-weight="700" fill="{INK}">Quem aparece onde: mensalão, petrolão e Lava Jato, INSS, Master e emendas</text>')
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">Condição jurídica de cada pessoa em cada caso · estado em 04/09/2026 · nos casos de 2025 e 2026 ninguém foi condenado · fontes em github.com/CriativoIniciante/interesse-publico</text>')
    # headers
    x0 = 60 + NAME_W
    for i, (k, title, yrs) in enumerate(COLS):
        cx = x0 + i*COL_W
        o.append(f'<rect x="{cx}" y="{top-52}" width="{COL_W-6}" height="46" rx="8" fill="{CASE[k][0]}" opacity="0.18"/>')
        o.append(f'<rect x="{cx}" y="{top-52}" width="8" height="46" rx="3" fill="{CASE[k][0]}"/>')
        o.append(f'<text x="{cx+18}" y="{top-32}" font-size="14" font-weight="700" fill="{INK}">{esc(title)}</text>')
        o.append(f'<text x="{cx+18}" y="{top-14}" font-size="12" fill="{INK2}">{yrs}</text>')
    y = top
    for name, cells in ROWS:
        if cells is None:
            o.append(f'<text x="60" y="{y+24}" font-size="13" font-weight="700" letter-spacing="1" fill="{INK2}">{esc(name)}</text>')
            o.append(f'<line x1="60" y1="{y+SEC_H-2}" x2="{W-60}" y2="{y+SEC_H-2}" stroke="{INK}" stroke-width="1"/>')
            y += SEC_H; continue
        o.append(f'<line x1="60" y1="{y+ROW_H}" x2="{W-60}" y2="{y+ROW_H}" stroke="{GRID}" stroke-width="1"/>')
        n = sum(1 for k in cells if k in CASE)
        o.append(f'<text x="60" y="{y+ROW_H/2+5}" font-size="14" font-weight="700" fill="{INK}">{esc(name)}</text>')
        if n >= 2:
            o.append(f'<text x="{60+NAME_W-14}" y="{y+ROW_H/2+5}" font-size="12" text-anchor="end" fill="{INK2}">{n} casos</text>')
        for i, (k, _, _) in enumerate(COLS):
            cx = x0 + i*COL_W
            if k in cells:
                st, txt = cells[k]
                col, sym, _ = SYM[st]
                o.append(f'<rect x="{cx}" y="{y+3}" width="{COL_W-6}" height="{ROW_H-6}" rx="6" fill="{CASE[k][0]}" opacity="0.07"/>')
                o.append(f'<text x="{cx+16}" y="{y+ROW_H/2+7}" font-size="20" fill="{col}">{sym}</text>')
                lines = wrap(txt, 40)
                yy = y + ROW_H/2 - (len(lines)-1)*6.5 + 4
                for j, ln in enumerate(lines):
                    o.append(f'<text x="{cx+44}" y="{yy+j*13:.0f}" font-size="10.8" fill="{INK}">{esc(ln)}</text>')
        y += ROW_H
    # legend
    ly = y + 30
    o.append(f'<text x="60" y="{ly}" font-size="14" font-weight="700" fill="{INK}">Como ler</text>')
    lx = 60
    for k, (col, sym, lab) in SYM.items():
        o.append(f'<text x="{lx}" y="{ly+30}" font-size="18" fill="{col}">{sym}</text>')
        o.append(f'<text x="{lx+26}" y="{ly+28}" font-size="12" fill="{INK}">{esc(lab)}</text>')
        lx += 26 + len(lab)*6.6 + 26
    o.append(f'<text x="60" y="{ly+62}" font-size="12" fill="{INK2}">Célula vazia = sem registro público nessa coluna, o que não diz nada sobre a pessoa. Condenação anulada não é absolvição de mérito. Delação rejeitada entra como alegação. Detalhes e fontes no README. CC BY 4.0, Rafael B. Brotto.</text>')
    o.append('</svg>')
    return "\n".join(o), W, H

# ---------- REDE ----------
NW, NH = 2000, 1500
N = {
 "valerio":  (230, 300, "Marcos Valério", "publicitário · operador do mensalão"),
 "janene":   (230, 560, "José Janene (PP)", "morto em 2010"),
 "dirceu":   (230, 820, "José Dirceu", "M: condenado · L: anulado 2024"),
 "valdemar": (230, 1080, "Valdemar Costa Neto (PL)", "M: condenado · E: 21 emendas"),
 "youssef":  (600, 560, "Alberto Youssef", "doleiro de Janene · pivô da Lava Jato"),
 "costa":    (600, 760, "Paulo Roberto Costa", "diretor da Petrobras (PP) · delator"),
 "odebrecht":(760, 1000, "Odebrecht", "hub da Lava Jato · delações e leniência"),
 "cunha":    (600, 1250, "Eduardo Cunha (MDB)", "L: condenado · E: 29 emendas"),
 "temer":    (1060, 640, "Michel Temer", "L: absolvido · B: pagamentos"),
 "mantega":  (1060, 760, "Guido Mantega", "L: absolvido/prescrito · B: R$ 1 mi/mês"),
 "wagner":   (1060, 880, "Jaques Wagner", "L: arquivado 2025 · B: busca 2026"),
 "nogueira": (1060, 1000, "Ciro Nogueira (PP)", "L: rejeitado · B: R$ 300 mil/mês"),
 "alcol":    (1060, 1120, "Davi Alcolumbre", "L: citado 2019 · B: alegação, nega"),
 "vorcaro":  (1380, 880, "Daniel Vorcaro", "hub do Master · preso · réu"),
 "moraes":   (1820, 460, "Alexandre de Moraes", "escritório da mulher: R$ 80 mi"),
 "toffoli":  (1820, 600, "Dias Toffoli", "M: absolveu Dirceu · L: anulou Odebrecht · B: R$ 35 mi"),
 "lewand":   (1820, 720, "Ricardo Lewandowski", "M: revisor · L: suspeição · B: R$ 6 mi"),
 "gilmar":   (1820, 840, "Gilmar Mendes", "M: julgou · L: anulou Dirceu, Mantega · B: bloco Moraes"),
 "flavio":   (1820, 960, "Flávio e Eduardo Bolsonaro", "B: US$ 12,3 mi, Dark Horse"),
 "gonet":    (1820, 1080, "Gonet e Andrei", "PGR e PF · Londres 2024"),
 "lula":     (1450, 300, "Lula", "M: testemunha · L: anulado · I: filho e irmão · B: reunião"),
 "zanin":    (1060, 300, "Zanin · Fachin · Moro", "L: advogado, relator, juiz suspeito"),
 "inss":     (1380, 1180, "INSS · consignado Credcesta", "IN 25/03/2022 · 74% irregular · CPMI"),
 "careca":   (1380, 1360, "'Careca do INSS'", "hub do INSS · preso"),
 "stefan":   (1820, 1300, "Stefanutto · Lupi", "R$ 250 mil/mês · preso; citado"),
 "luchs":    (1060, 1360, "Luchsinger → Lulinha", "R$ 300 mil 'para o filho do cara'"),
 "camisotti":(1820, 1420, "Camisotti", "delator do INSS"),
}
# (a, b, caso, solid?, label, ctrl, t, off, anchor)
E = [
 ("valerio","janene","M",True,"R$ 4,1 mi (mensalão)",(0,0),0.5,(14,0),"start"),
 ("janene","youssef","M",True,"lavou R$ 1,16 mi do mensalão",(0,-40),0.5,(0,-12),"middle"),
 ("janene","costa","L",False,"Janene, 'mentor' do esquema do PP",(0,60),0.5,(0,18),"middle"),
 ("youssef","costa","L",True,"pivôs e delatores da Lava Jato",(0,0),0.5,(14,0),"start"),
 ("costa","nogueira","L",True,"PP: cota na Petrobras",(0,60),0.5,(0,18),"middle"),
 ("nogueira","vorcaro","B",True,"R$ 300 mil/mês · busca 07/05/2026",(0,40),0.5,(-15,18),"start"),
 ("odebrecht","temer","L",True,"denúncias, prisão; absolvido",(-60,0),0.5,(-14,0),"end"),
 ("odebrecht","mantega","L",True,"fases anuladas",(-40,0),0.5,(-14,0),"end"),
 ("odebrecht","wagner","L",True,"Fonte Nova; arquivado 2025",(0,0),0.3,(-14,6),"end"),
 ("odebrecht","nogueira","L",True,"R$ 7,3 mi; rejeitado",(0,0),0.5,(0,36),"middle"),
 ("odebrecht","alcol","L",False,"denúncia de 2019; citado",(0,0),0.5,(0,16),"middle"),
 ("odebrecht","cunha","L",True,"condenado; anulado 2023",(0,0),0.5,(-14,0),"end"),
 ("odebrecht","dirceu","L",True,"condenado 2016/17; anulado 2024",(0,60),0.5,(0,18),"middle"),
 ("odebrecht","lula","L",True,"triplex, sítio; anulado 2021",(-380,-250),0.6,(0,-12),"middle"),
 ("vorcaro","temer","B",False,"pagamentos (imprensa)",(0,0),0.5,(14,-6),"start"),
 ("vorcaro","mantega","B",False,"R$ 1 mi/mês (imprensa)",(0,0),0.5,(0,-10),"middle"),
 ("vorcaro","wagner","B",True,"busca 18/06/2026",(0,0),0.5,(0,-40),"middle"),
 ("vorcaro","alcol","B",False,"US$ 30 mi (delação rejeitada)",(0,40),0.5,(0,18),"middle"),
 ("vorcaro","moraes","B",True,"notas e contrato",(40,0),0.25,(10,-4),"start"),
 ("vorcaro","toffoli","B",True,"R$ 35 mi",(0,0),0.25,(10,-4),"start"),
 ("vorcaro","lewand","B",True,"R$ 250 mil/mês",(0,0),0.25,(10,-4),"start"),
 ("vorcaro","flavio","B",True,"Dark Horse, US$ 12,3 mi",(0,0),0.35,(12,10),"start"),
 ("vorcaro","gonet","B",True,"Londres 2024",(0,0),0.35,(12,10),"start"),
 ("vorcaro","lula","B",False,"reunião, dez/2024",(100,0),0.5,(14,0),"start"),
 ("vorcaro","inss","I",True,"consignado 74% irregular · CPMI",(0,0),0.5,(14,0),"start"),
 ("inss","careca","I",False,"mesmo relator (Mendonça) · mesma CPMI",(0,0),0.5,(14,0),"start"),
 ("careca","stefan","I",True,"R$ 250 mil/mês",(0,0),0.4,(0,-10),"middle"),
 ("careca","camisotti","I",True,"sócio; delator",(0,0),0.5,(0,16),"middle"),
 ("careca","luchs","I",True,"apresentou Lulinha · R$ 300 mil",(0,0),0.5,(0,-34),"middle"),
 ("dirceu","toffoli","M",True,"ex-chefe de Toffoli na Casa Civil; absolvido por ele em 2012",(200,-600),0.5,(0,-12),"middle"),
 ("dirceu","gilmar","L",True,"Gilmar anulou tudo em 2024",(380,-280),0.5,(0,18),"middle"),
 ("lula","zanin","L",True,"defesa · suspeição de Moro · anulação (Fachin)",(0,0),0.5,(0,-40),"middle"),
 ("valdemar","cunha","E",False,"controle de emendas sem mandato (PF, 2026)",(0,60),0.5,(0,18),"middle"),
 ("valerio","dirceu","M",True,"AP 470",(-120,0),0.2,(-14,0),"end"),
 ("valerio","valdemar","M",True,"AP 470",(-180,0),0.8,(-14,0),"end"),
]

def rede():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{NW}" height="{NH}" viewBox="0 0 {NW} {NH}" font-family="Segoe UI, Inter, Arial, sans-serif">', f'<rect width="{NW}" height="{NH}" fill="{SURF}"/>']
    o.append(f'<text x="40" y="48" font-size="30" font-weight="700" fill="{INK}">As cadeias que se repetem: dos operadores do mensalão ao Master e ao INSS</text>')
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">Cor da linha = caso · linha cheia = fato documentado (condenação, documento, operação) · tracejada = alegação ou citação · estado em 04/09/2026</text>')
    # eras
    for x1, x2, lab in [(80, 420, "MENSALÃO · 2005–2012"), (440, 900, "PETROLÃO · LAVA JATO · 2014–2021"), (920, 1220, "OS MESMOS NOMES"), (1240, 1990, "MASTER · INSS · EMENDAS · 2025–2026")]:
        o.append(f'<rect x="{x1}" y="200" width="{x2-x1}" height="1260" rx="14" fill="#f1f1ee" stroke="{GRID}"/>')
        o.append(f'<text x="{x1+14}" y="{224}" font-size="13" font-weight="700" letter-spacing="1" fill="{INK2}">{lab}</text>')
    labels = []
    for a, b, k, solid, label, ctrl, t, off, anchor in E:
        ax, ay = N[a][0], N[a][1]; bx, by = N[b][0], N[b][1]
        mx, my = (ax+bx)/2+ctrl[0], (ay+by)/2+ctrl[1]
        col = CASE[k][0]
        dash = '' if solid else ' stroke-dasharray="9 7"'
        o.append(f'<path d="M{ax},{ay} Q{mx},{my} {bx},{by}" fill="none" stroke="{col}" stroke-width="{4 if solid else 2.5}" stroke-linecap="round" opacity="0.9"{dash}/>')
        lx = (1-t)**2*ax + 2*(1-t)*t*mx + t**2*bx; ly = (1-t)**2*ay + 2*(1-t)*t*my + t**2*by
        labels.append((lx+off[0], ly+off[1], anchor, f"{k} · {label}"))
    for lx, ly, anchor, txt in labels:
        o.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="12.5" text-anchor="{anchor}" fill="{INK}" paint-order="stroke" stroke="{SURF}" stroke-width="6" stroke-linejoin="round">{esc(txt)}</text>')
    for nid, (x, y, name, sub) in N.items():
        w = max(len(name)*9.5, len(sub)*6.3) + 30; w = min(max(w, 170), 300)
        o.append(f'<rect x="{x-w/2}" y="{y-28}" width="{w}" height="56" rx="10" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>')
        o.append(f'<text x="{x}" y="{y-4}" font-size="15" font-weight="700" text-anchor="middle" fill="{INK}">{esc(name)}</text>')
        o.append(f'<text x="{x}" y="{y+15}" font-size="11" text-anchor="middle" fill="{INK2}">{esc(sub)}</text>')
    # legend
    lx = 80; ly = NH - 32
    for k, (col, lab) in CASE.items():
        o.append(f'<line x1="{lx}" y1="{ly-4}" x2="{lx+34}" y2="{ly-4}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
        o.append(f'<text x="{lx+42}" y="{ly}" font-size="12.5" fill="{INK}">{k} · {lab}</text>')
        lx += 190
    o.append(f'<text x="{lx+20}" y="{ly}" font-size="12" fill="{INK2}">Ninguém foi condenado nos casos de 2025 e 2026. Fontes no README. CC BY 4.0, Rafael B. Brotto.</text>')
    o.append('</svg>')
    return "\n".join(o)

here = pathlib.Path(__file__).parent
svg, W, H = matriz()
(here/"matriz_repeticoes.svg").write_text(svg, encoding="utf-8")
(here/"matriz_repeticoes.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{svg}', encoding="utf-8")
svg2 = rede()
(here/"rede_cadeias.svg").write_text(svg2, encoding="utf-8")
(here/"rede_cadeias.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{svg2}', encoding="utf-8")
print("matriz", W, H, "| rede", NW, NH)
