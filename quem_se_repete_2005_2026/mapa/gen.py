# -*- coding: utf-8 -*-
"""Gera matriz_repeticoes.svg e rede_cadeias.svg (+ .html + .png).
Versão 2 (06/09/2026): células corrigidas conforme ../materialidade_2026-09-06.md e
terceiro campo por célula, o PESO DA PROVA, desenhado na borda:
  P = prova formal (decisão, documento oficial, operação, admissão)  -> borda cheia grossa
  R = relato documentado (reportagem com documento)                  -> borda cheia fina
  A = alegação (delação rejeitada, fonte anônima, coluna)             -> borda tracejada
  O = inocência formal (absolvido, arquivado, anulado, prescrito)     -> borda verde
PNG gerado com PyMuPDF (fitz) a partir do SVG."""
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
PESO = {
 "P": (INK, 2.6, "", "prova formal: decisão, documento oficial, operação, admissão"),
 "R": (INK2, 1.3, "", "relato documentado: reportagem com documento"),
 "A": (INK2, 1.3, "6 4", "alegação: delação rejeitada, fonte anônima, coluna"),
 "O": (GRN, 1.6, "", "inocência formal: absolvido, arquivado, anulado ou prescrito"),
}
# (status, texto, peso)
ROWS = [
 ("POLÍTICOS", None),
 ("Lula", {"M": ("cit", "testemunha, não réu; relato de Valério (2012) sem denúncia", "P"),
           "L": ("anul", "condenado em 3 instâncias (triplex; Atibaia); anulado em 2021 por competência e suspeição, sem mérito", "O"),
           "I": ("cit", "irmão (Sindnapi) e filho (3 inquéritos); ele não é investigado", "P"),
           "B": ("cit", "reunião fora da agenda com Vorcaro (04/12/2024); encontro reservado com Toffoli sobre o caso (dez/2025)", "R")}),
 ("José Dirceu", {"M": ("cond", "7a11m, corrupção ativa; absolvido de quadrilha em 2014", "P"), "L": ("anul", "23a (2016) e 11a3m (2017); anuladas por Gilmar em out/2024", "O")}),
 ("Delúbio Soares", {"M": ("cond", "8a11m, reduzida a 6a8m em 2014 (quadrilha)", "P"), "L": ("anul", "5a (Moro, 2017); STJ anulou; prescrita", "O")}),
 ("José Genoino", {"M": ("cond", "6a11m, reduzida a 4a8m em 2014 (quadrilha)", "P")}),
 ("Roberto Jefferson", {"M": ("cond", "delator informal do mensalão; 7 anos e 14 dias", "P")}),
 ("Valdemar Costa Neto", {"M": ("cond", "7a10m, corrupção passiva e lavagem; indulto em 2016", "P"), "E": ("inv", "PF: 21 emendas, R$ 119 mi, sem mandato; bens bloqueados por Dino; nega", "P")}),
 ("José Janene (PP)", {"M": ("reu", "denunciado; R$ 4,1 mi de Valério; morreu em 2010", "P"), "L": ("cit", "apontado como mentor do esquema do PP; Youssef era seu doleiro", "R")}),
 ("Eduardo Cunha", {"L": ("anul", "Curitiba 2017 (15a4m), anulada pela 2ª Turma em 2023; Brasília/Sépsis 2018 (24a10m)", "O"), "E": ("inv", "PF: 29 emendas indicadas sem mandato, 21 pagas; R$ 6,15 mi bloqueados por Dino (10/07/2026); nega", "P")}),
 ("Michel Temer", {"L": ("abs", "2 denúncias barradas (2017); preso 10 dias (2019); absolvido em Angra 3 (2022)", "O"), "B": ("cit", "contratado (set/2025) para destravar a venda ao BRB; intermediário com árabes (imprensa)", "R")}),
 ("Guido Mantega", {"L": ("abs", "fases anuladas (Gilmar); absolvido BNDES (2023); Zelotes prescrita (fev/2025)", "O"), "B": ("cit", "R$ 1 mi/mês (jul–nov/2025) a pedido de Wagner; levou Vorcaro a Lula (imprensa, jan/2026)", "R")}),
 ("Ciro Nogueira", {"L": ("abs", "denúncia por R$ 7,3 mi da Odebrecht; a PGR pediu a rejeição (2023); STF rejeitou", "O"), "B": ("inv", "busca 07/05/2026; R$ 300 mil/mês; emenda do FGC; malotes apreendidos", "P")}),
 ("Jaques Wagner", {"L": ("abs", "inquérito Arena Fonte Nova (2018) arquivado em fev/2025", "O"), "B": ("inv", "busca 18/06/2026; admite ter indicado Lewandowski ao Master; PF: apto R$ 2,45 mi, 'Emenda Master'", "P")}),
 ("Gilberto Kassab", {"L": ("abs", "réu (2021) por R$ 16,5 mi da JBS; absolvido, trânsito em julgado em 29/11/2023", "O"), "B": ("cit", "delação rejeitada: propina via Credcesta; nega", "A")}),
 ("Davi Alcolumbre", {"L": ("abs", "citado em denúncia de 2019; 2 inquéritos eleitorais (2014) arquivados em 2019", "O"), "B": ("cit", "US$ 30 mi em delação rejeitada; nega; guardou os dados de Vorcaro (dez/2025–fev/2026); não pauta impeachment", "A")}),
 ("Jair Bolsonaro", {"I": ("cit", "IN de 25/03/2022, no seu governo, liberou a Credcesta 16 dias após ofício do Master", "R"), "B": ("cit", "delação rejeitada: doação de 2022 como propina; nega", "A")}),
 ("Flávio Bolsonaro", {"B": ("inv", "inquérito autorizado em 23/07/2026: US$ 12,3 mi do Dark Horse", "P")}),
 ("Tarcísio de Freitas", {"B": ("cit", "delação rejeitada: R$ 2 mi como propina; nega", "A")}),
 ("Carlos Lupi", {"I": ("cit", "delatado por 2 ex-diretores do INSS (fev/2026); saiu em abr/2025", "A")}),
 ("Fábio Luís (Lulinha)", {"I": ("inv", "3 inquéritos (jul–ago/2026); o relatório da CPMI que pedia seu indiciamento foi rejeitado (19 a 12)", "P")}),
 ("Frei Chico", {"I": ("cit", "vice do Sindnapi (R$ 599,5 mi descontados); não investigado; CPMI não o convocou", "P")}),
 ("Marco Aurélio Ribeiro", {"I": ("inv", "ex-chefe de gabinete de Lula; inquérito (Dino, 04/08/2026); PF: R$ 217 mil em despesas pagas por Luchsinger; pediu quadro de 100 mil euros", "P"), "B": ("cit", "recebeu Mantega 4 vezes no Planalto enquanto o Master o pagava (R$ 1 mi/mês)", "R")}),
 ("Fernando Bittar", {"L": ("cit", "dono formal do sítio de Atibaia, objeto de condenação de Lula anulada em 2021", "P"), "I": ("inv", "PF investiga 'sociedade oculta' com Lulinha e Luchsinger (grupo 'Musaranhos'); filho Kalil recebeu R$ 750 mil de Lulinha", "R")}),
 ("OPERADORES E EMPRESÁRIOS", None),
 ("Marcos Valério", {"M": ("cond", "40 anos, corrigida para 37a5m; mensalão tucano: 16a9m (2018)", "P")}),
 ("Alberto Youssef", {"M": ("cond", "lavou R$ 1,16 mi de Janene (condenado em 2015)", "P"), "L": ("del", "doleiro pivô; delator; condenado", "P")}),
 ("Paulo Roberto Costa", {"L": ("del", "ex-diretor da Petrobras (PP); delator", "P")}),
 ("Marcelo Odebrecht", {"L": ("del", "19a (2016); delator; provas da leniência anuladas por Toffoli (2023)", "P")}),
 ("Lúcio Funaro", {"L": ("del", "operador ligado a Cunha e ao MDB; delator (2017)", "P")}),
 ("Alessandro Stefanutto", {"I": ("reu", "ex-presidente do INSS; R$ 250 mil/mês; preso em 13/11/2025", "P")}),
 ("'Careca do INSS'", {"I": ("reu", "preso 12/09/2025; R$ 24,5 mi em 5 meses; PF: 'epicentro' do esquema, 48 indiciados", "P")}),
 ("Maurício Camisotti", {"I": ("del", "preso 12/09/2025; delação refeita com PF e PGR (2026); cerca de R$ 400 mi", "P")}),
 ("Roberta Luchsinger", {"I": ("inv", "tráfico de influência; admitiu à PF ter apresentado Lulinha ao Careca", "P")}),
 ("Daniel Vorcaro", {"I": ("cit", "consignado 74% irregular; o relatório da CPMI (rejeitado) pedia seu indiciamento", "R"), "B": ("reu", "preso em 17/11/2025 e 04/03/2026; réu; 2 delações rejeitadas", "P")}),
 ("Augusto Lima", {"B": ("inv", "preso 11 dias (nov/2025); 9ª fase; 'Emenda Master' com Wagner; Banco Pleno liquidado", "P")}),
 ("JUDICIÁRIO, MINISTÉRIO PÚBLICO E POLÍCIA FEDERAL", None),
 ("Dias Toffoli", {"M": ("inst", "votou pela absolvição de Dirceu, seu ex-chefe, sem se declarar impedido", "P"), "L": ("inst", "set/2023: anulou todas as provas da leniência da Odebrecht", "P"), "B": ("cit", "R$ 35 mi a empresa da família via fundo ligado ao Master; sorteado relator em 28/11/2025, saiu em 12/02/2026", "R")}),
 ("Ricardo Lewandowski", {"M": ("inst", "revisor; absolveu Dirceu de corrupção ativa e 13 réus de quadrilha", "P"), "L": ("inst", "2ª Turma: votou a suspeição de Moro", "P"), "B": ("cit", "R$ 6,5 mi ao escritório da família (2023–2025), R$ 5,25 mi já ministro da Justiça; indicado por Wagner (admitido)", "R")}),
 ("Gilmar Mendes", {"M": ("inst", "julgador", "P"), "L": ("inst", "anulou fases (Mantega) e condenações (Dirceu); relator da suspeição de Moro", "P"), "B": ("cit", "relator de recurso do Master; presente em fórum de Londres pago pelo Master (abr/2024); fundou o IDP com Gonet", "R")}),
 ("Edson Fachin", {"L": ("inst", "relator no STF; anulou as condenações de Lula (2021)", "P"), "B": ("inst", "presidente; procedimento de 03/09; sem registro de vínculo com Vorcaro", "P")}),
 ("Alexandre de Moraes", {"L": ("inst", "a favor da prisão em 2ª instância (2019); pela anulação (2021)", "P"), "B": ("cit", "218 páginas da PF; escritório da mulher (R$ 131 mi brutos, ~R$ 80 mi pagos); jato, cartões; negou 5 vezes", "R")}),
 ("Cristiano Zanin", {"L": ("inst", "advogado de Lula (2013–2022); obteve a suspeição de Moro", "P"), "B": ("inst", "ministro (2023–); 1ª Turma; sem registro de vínculo com Vorcaro", "P")}),
 ("Flávio Dino", {"I": ("inst", "autorizou o 3º inquérito de Lulinha (04/08)", "P"), "B": ("inst", "dados do Dark Horse à PF; sem registro de vínculo com Vorcaro", "P"), "E": ("inst", "relator; 'emendas de líder' nulas (23/08); bloqueou bens de Valdemar e Cunha", "P")}),
 ("André Mendonça", {"I": ("inst", "relator da Sem Desconto", "P"), "B": ("inst", "relator; levantou o sigilo; recebeu Vorcaro em 14/03/2025 (admitido)", "P")}),
 ("Sergio Moro", {"L": ("inst", "juiz (2014–18); suspeito (2021); ministro de Bolsonaro; senador", "P")}),
 ("Paulo Gonet", {"I": ("inst", "PGR pediu refazer a delação de Camisotti", "P"), "B": ("cit", "Londres 2024 (pago por Vorcaro); mensagens atribuídas via intermediário; arquivou apuração sobre Moraes (dez/2025); pediu nulidade", "R")}),
 ("Andrei Rodrigues", {"I": ("inst", "PF conduz a Sem Desconto (48 indiciados, 14/07/2026)", "P"), "B": ("cit", "Londres 2024 (pago por Vorcaro); 'reforçar com Andrei'; relatório de inteligência sobre o relator; acusado por Vorcaro (alegação)", "R")}),
]

def wrap(txt, n, maxl=4):
    words = txt.split(); lines = []; line = ""
    for w in words:
        if len(line + " " + w) > n and line: lines.append(line); line = w
        else: line = (line + " " + w).strip()
    if line: lines.append(line)
    return lines[:maxl]

def matriz():
    NAME_W, COL_W, ROW_H, SEC_H = 250, 310, 60, 34
    W = 60 + NAME_W + 5*COL_W + 60
    top = 150
    rows_h = sum(SEC_H if r[1] is None else ROW_H for r in ROWS)
    H = top + rows_h + 200
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Inter, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="{SURF}"/>']
    o.append(f'<text x="40" y="48" font-size="30" font-weight="700" fill="{INK}">Quem aparece onde: mensalão, petrolão e Lava Jato, INSS, Master e emendas</text>')
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">Símbolo = condição jurídica · borda = peso da prova · estado em 06/09/2026 · nos casos de 2025 e 2026 ninguém foi condenado · fontes em github.com/CriativoIniciante/interesse-publico</text>')
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
                st, txt, peso = cells[k]
                col, sym, _ = SYM[st]
                pcol, pw, pdash, _ = PESO[peso]
                dash = f' stroke-dasharray="{pdash}"' if pdash else ''
                o.append(f'<rect x="{cx}" y="{y+3}" width="{COL_W-6}" height="{ROW_H-6}" rx="6" fill="{CASE[k][0]}" opacity="0.07"/>')
                o.append(f'<rect x="{cx+0.5}" y="{y+3.5}" width="{COL_W-7}" height="{ROW_H-7}" rx="6" fill="none" stroke="{pcol}" stroke-width="{pw}"{dash}/>')
                o.append(f'<text x="{cx+16}" y="{y+ROW_H/2+7}" font-size="20" fill="{col}">{sym}</text>')
                o.append(f'<text x="{cx+COL_W-14}" y="{y+14}" font-size="9.5" font-weight="700" text-anchor="end" fill="{pcol}">{peso}</text>')
                lines = wrap(txt, 44)
                yy = y + ROW_H/2 - (len(lines)-1)*6 + 4
                for j, ln in enumerate(lines):
                    o.append(f'<text x="{cx+44}" y="{yy+j*12:.0f}" font-size="10.2" fill="{INK}">{esc(ln)}</text>')
        y += ROW_H
    ly = y + 30
    o.append(f'<text x="60" y="{ly}" font-size="14" font-weight="700" fill="{INK}">Como ler o símbolo</text>')
    lx = 60
    for k, (col, sym, lab) in SYM.items():
        o.append(f'<text x="{lx}" y="{ly+30}" font-size="18" fill="{col}">{sym}</text>')
        o.append(f'<text x="{lx+26}" y="{ly+28}" font-size="12" fill="{INK}">{esc(lab)}</text>')
        lx += 26 + len(lab)*6.6 + 26
    o.append(f'<text x="60" y="{ly+62}" font-size="14" font-weight="700" fill="{INK}">Como ler a borda (peso da prova)</text>')
    lx = 60
    for k, (pcol, pw, pdash, lab) in PESO.items():
        dash = f' stroke-dasharray="{pdash}"' if pdash else ''
        o.append(f'<rect x="{lx}" y="{ly+78}" width="34" height="18" rx="4" fill="none" stroke="{pcol}" stroke-width="{pw}"{dash}/>')
        o.append(f'<text x="{lx+42}" y="{ly+92}" font-size="12" fill="{INK}">{k} = {esc(lab)}</text>')
        lx += 42 + len(lab)*6.6 + 40
    o.append(f'<text x="60" y="{ly+126}" font-size="12" fill="{INK2}">Célula vazia = sem registro público nessa coluna, o que não diz nada sobre a pessoa. Condenação anulada não é absolvição de mérito. Delação rejeitada entra como alegação. Detalhes, fontes e a conferência célula a célula em materialidade_2026-09-06.md. CC BY 4.0, Rafael B. Brotto.</text>')
    o.append('</svg>')
    return "\n".join(o), W, H

# ---------- REDE (inalterada, salvo datas e rótulos corrigidos) ----------
NW, NH = 2000, 1500
N = {
 "valerio":  (230, 300, "Marcos Valério", "publicitário · operador do mensalão"),
 "janene":   (230, 560, "José Janene (PP)", "morto em 2010"),
 "dirceu":   (230, 820, "José Dirceu", "M: condenado · L: anulado 2024"),
 "valdemar": (230, 1080, "Valdemar Costa Neto (PL)", "M: condenado · E: 21 emendas, bens bloqueados"),
 "youssef":  (600, 560, "Alberto Youssef", "doleiro de Janene · pivô da Lava Jato"),
 "costa":    (600, 760, "Paulo Roberto Costa", "diretor da Petrobras (PP) · delator"),
 "odebrecht":(760, 1000, "Odebrecht", "hub da Lava Jato · delações e leniência"),
 "cunha":    (600, 1250, "Eduardo Cunha (MDB)", "L: anulada 2023 · E: 29 emendas"),
 "temer":    (1060, 640, "Michel Temer", "L: absolvido · B: contratado set/2025"),
 "mantega":  (1060, 760, "Guido Mantega", "L: absolvido/prescrito · B: R$ 1 mi/mês"),
 "wagner":   (1060, 880, "Jaques Wagner", "L: arquivado 2025 · B: busca 2026"),
 "nogueira": (1060, 1000, "Ciro Nogueira (PP)", "L: rejeitado · B: R$ 300 mil/mês"),
 "alcol":    (1060, 1120, "Davi Alcolumbre", "L: citado 2019 · B: alegação, nega"),
 "vorcaro":  (1380, 880, "Daniel Vorcaro", "hub do Master · preso · réu"),
 "moraes":   (1820, 460, "Alexandre de Moraes", "escritório da mulher: R$ 131 mi brutos"),
 "toffoli":  (1820, 600, "Dias Toffoli", "M: absolveu Dirceu · L: anulou Odebrecht · B: R$ 35 mi"),
 "lewand":   (1820, 720, "Ricardo Lewandowski", "M: revisor · L: suspeição · B: R$ 6,5 mi"),
 "gilmar":   (1820, 840, "Gilmar Mendes", "M: julgou · L: anulou Dirceu, Mantega · B: Londres 2024"),
 "flavio":   (1820, 960, "Flávio e Eduardo Bolsonaro", "B: US$ 12,3 mi, Dark Horse"),
 "gonet":    (1820, 1080, "Gonet e Andrei", "PGR e PF · Londres 2024"),
 "lula":     (1450, 300, "Lula", "M: testemunha · L: anulado · I: filho e irmão · B: reunião"),
 "zanin":    (1060, 300, "Zanin · Fachin · Moro", "L: advogado, relator, juiz suspeito"),
 "inss":     (1380, 1180, "INSS · consignado Credcesta", "IN 25/03/2022 · 74% irregular · CPMI"),
 "careca":   (1380, 1360, "'Careca do INSS'", "hub do INSS · preso"),
 "stefan":   (1820, 1300, "Stefanutto · Lupi", "R$ 250 mil/mês · preso; delatado"),
 "luchs":    (1060, 1360, "Luchsinger → Lulinha", "R$ 300 mil 'para o filho do cara'"),
 "camisotti":(1820, 1420, "Camisotti", "delator do INSS"),
}
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
 ("vorcaro","temer","B",False,"contratado set/2025 (imprensa)",(0,0),0.5,(14,-6),"start"),
 ("vorcaro","mantega","B",False,"R$ 1 mi/mês (imprensa)",(0,0),0.5,(0,-10),"middle"),
 ("vorcaro","wagner","B",True,"busca 18/06/2026",(0,0),0.5,(0,-40),"middle"),
 ("vorcaro","alcol","B",False,"US$ 30 mi (delação rejeitada)",(0,40),0.5,(0,18),"middle"),
 ("vorcaro","moraes","B",True,"notas e contrato",(40,0),0.25,(10,-4),"start"),
 ("vorcaro","toffoli","B",True,"R$ 35 mi",(0,0),0.25,(10,-4),"start"),
 ("vorcaro","lewand","B",True,"R$ 250 mil/mês",(0,0),0.25,(10,-4),"start"),
 ("vorcaro","gilmar","B",True,"Londres 2024 pago pelo Master",(0,0),0.3,(10,-4),"start"),
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
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">Cor da linha = caso · linha cheia = fato documentado (condenação, documento, operação) · tracejada = alegação ou citação · estado em 06/09/2026</text>')
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
        # fundo branco + texto (paint-order não é suportado pelo renderizador do PyMuPDF)
        tw = len(txt) * 6.4 + 10
        bx = lx - 5 if anchor == "start" else (lx - tw + 5 if anchor == "end" else lx - tw/2)
        o.append(f'<rect x="{bx:.0f}" y="{ly-12:.0f}" width="{tw:.0f}" height="17" rx="4" fill="{SURF}" opacity="0.92"/>')
        o.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="12.5" text-anchor="{anchor}" fill="{INK}">{esc(txt)}</text>')
    for nid, (x, y, name, sub) in N.items():
        w = max(len(name)*9.5, len(sub)*6.3) + 30; w = min(max(w, 170), 320)
        o.append(f'<rect x="{x-w/2}" y="{y-28}" width="{w}" height="56" rx="10" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>')
        o.append(f'<text x="{x}" y="{y-4}" font-size="15" font-weight="700" text-anchor="middle" fill="{INK}">{esc(name)}</text>')
        o.append(f'<text x="{x}" y="{y+15}" font-size="11" text-anchor="middle" fill="{INK2}">{esc(sub)}</text>')
    lx = 80; ly = NH - 32
    for k, (col, lab) in CASE.items():
        o.append(f'<line x1="{lx}" y1="{ly-4}" x2="{lx+34}" y2="{ly-4}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
        o.append(f'<text x="{lx+42}" y="{ly}" font-size="12.5" fill="{INK}">{k} · {lab}</text>')
        lx += 190
    o.append(f'<text x="{lx+20}" y="{ly}" font-size="12" fill="{INK2}">Ninguém foi condenado nos casos de 2025 e 2026. Fontes no README. CC BY 4.0, Rafael B. Brotto.</text>')
    o.append('</svg>')
    return "\n".join(o)

def to_png(svg_path, png_path, dpi=110):
    import fitz
    doc = fitz.open(str(svg_path)); pix = doc[0].get_pixmap(dpi=dpi); pix.save(str(png_path)); return pix.width, pix.height

here = pathlib.Path(__file__).parent
svg, W, H = matriz()
(here/"matriz_repeticoes.svg").write_text(svg, encoding="utf-8")
(here/"matriz_repeticoes.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{svg}', encoding="utf-8")
svg2 = rede()
(here/"rede_cadeias.svg").write_text(svg2, encoding="utf-8")
(here/"rede_cadeias.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{svg2}', encoding="utf-8")
print("matriz", W, H, "| rede", NW, NH)
print("png", to_png(here/"matriz_repeticoes.svg", here/"matriz_repeticoes.png"), to_png(here/"rede_cadeias.svg", here/"rede_cadeias.png"))
