# -*- coding: utf-8 -*-
"""Quadro 'quem investiga, quem julga' da família Bolsonaro: uma linha por caso, quatro colunas
(o caso e sua origem; quem investiga; quem julga; estado em 07/09/2026), agrupadas por pessoa.
A cor da borda da última coluna é o estado. Gera mapa_investiga_julga.svg/.html/.png. Fonte: ../README.md."""
import html, pathlib

SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e0dfd9"
EST = {
 "cond": ("#d03b3b", "condenado"),
 "reu":  ("#ec835a", "réu, denunciado ou indiciado"),
 "inv":  ("#c48a14", "inquérito ou apuração em curso"),
 "pend": ("#2a78d6", "pendente de decisão"),
 "arq":  ("#0ca30c", "arquivado, anulado, trancado ou improcedente"),
}
COLS = [("caso", "O CASO E A ORIGEM DA ACUSAÇÃO"), ("inv", "QUEM INVESTIGA"), ("jul", "QUEM JULGA"), ("est", "ESTADO EM 07/09/2026")]
def esc(s): return html.escape(s, quote=True)

# (pessoa, subtítulo) ou (caso, investiga, julga, estado_txt, estado_key)
ROWS = [
 ("Jair Bolsonaro", "ex-presidente · uma condenação definitiva"),
 ("Trama golpista (AP 2.668). Origem: 8/1/2023, minuta na casa de Torres (12/01/2023), delação de Cid (set/2023), relatório da PF (nov/2024)", "PF (DG Andrei Rodrigues; delegado Fábio Shor); PGR (Gonet) denunciou 34 em 18/02/2025", "STF, 1ª Turma, relator Moraes; Dino, Cármen Lúcia, Zanin pela condenação; Fux pela absolvição", "condenado a 27 anos e 3 meses (4x1, 11/09/2025); trânsito em 25/11/2025; domiciliar humanitária desde 27/03/2026", "cond"),
 ("Revisão criminal (RVC 6.021) e lei da dosimetria (Lei 15.402/2026)", "PGR contrária à revisão (16/06/2026)", "STF, Plenário: relator Nunes Marques (revisão); Moraes suspendeu a lei em 09/05/2026", "pendente: sem julgamento até 07/09/2026", "pend"),
 ("Inelegibilidade. Origem: reunião com embaixadores (jul/2022) e 7 de Setembro de 2022", "PDT; Ministério Público Eleitoral", "TSE (5x2 em jun e out/2023; Kassio e Raul Araújo contra)", "inelegível até 2030", "cond"),
 ("Joias sauditas. Origem: retenção na Receita (out/2021); Estadão (03/03/2023)", "PF (indiciou em jul/2024); TCU; PGR pediu arquivar (mar/2026)", "STF, Moraes: devolveu à PGR em 19/03/2026", "pendente: sem denúncia nem arquivamento", "pend"),
 ("Cartão de vacina. Origem: Operação Venire (mai/2023)", "PF (indiciou em mar/2024 com base em Cid)", "STF, Moraes", "arquivado quanto a ele (28/03/2025): só a palavra do delator", "arq"),
 ("Abin paralela. Origem: Operação Última Milha (out/2023)", "PF (36 indiciados em jun/2025); PGR pediu 1ª instância", "STF, Moraes", "arquivado quanto a ele (20/07/2026): fatos englobados na AP 2.668", "arq"),
 ("Interferência na PF (INQ 4.831). Origem: denúncia de Moro (abr/2020)", "PF concluiu sem indícios em 2022 e de novo em abr/2026", "STF, Celso de Mello, depois Moraes (reabriu em out/2025)", "sem indícios; aguarda a PGR", "arq"),
 ("Covaxin, CPI da Covid, vazamento do TSE, 7/9 eleitoral", "PGR (Aras e Lindôra pediram arquivamentos); PF", "STF: Rosa Weber, Toffoli, Moraes, Mendonça", "Covaxin e petições da CPI arquivadas; vazamento sem denúncia; 7/9: PGR pediu arquivar", "arq"),
 ("Coação (INQ 4.995). Origem: atuação de Eduardo nos EUA (2025)", "PF indiciou (ago/2025); PGR não o denunciou", "STF, Moraes: cautelares (tornozeleira) desde jul/2025", "investigado, não denunciado", "inv"),
 ("Michelle Bolsonaro", "candidata ao Senado pelo DF · nunca indiciada"),
 ("Joias sauditas (destinatária dos pacotes)", "PF", "STF, Moraes", "não indiciada 'por ausência de provas de envolvimento' (jul/2024)", "arq"),
 ("Cheques de Queiroz, R$ 89 mil. Origem: Coaf (2018); Crusoé (2020)", "PGR (Aras): sem indícios", "STF: Marco Aurélio; plenário confirmou", "arquivado (jul/2021)", "arq"),
 ("Flávio Bolsonaro", "senador · candidato a presidente"),
 ("Rachadinha na Alerj. Origem: Coaf (jul/2018); Queiroz", "MP-RJ (Gaeco): denúncia em 04/11/2020", "27ª Vara; Órgão Especial do TJ-RJ; STJ; STF 2ª Turma", "provas anuladas (STJ e STF, 2021); denúncia rejeitada (16/05/2022); sem reabertura", "arq"),
 ("Mansão do Lago Sul. Origem: registro da compra (fev/2021)", "MPDFT (arquivou); ação popular de Erika Kokay", "TJDFT (1ª Vara Cível; 4ª Turma Cível)", "improcedente (01/07/2025)", "arq"),
 ("Calúnia contra Lula. Origem: post de 03/01/2026", "PF concluiu pelo crime (jun/2026); PGR aguarda oitiva ou retratação", "STF, Moraes", "inquérito em curso", "inv"),
 ("Dark Horse e Master. Origem: Intercept (mai/2026)", "PF", "STF, Mendonça (autorizou em 23/07/2026)", "inquérito em curso (ver consolidado)", "inv"),
 ("CPI da Covid (incitação). Origem: Pet 10.064", "PF; PGR pediu arquivar (2022)", "STF, Dino (reabriu em set/2025)", "inquérito em sigilo", "inv"),
 ("Eleitoral: vídeo de IA; carta de Jair", "Federação Brasil da Esperança; MP Eleitoral", "TSE (Nunes Marques)", "multa rejeitada 4x3 (06/09/2026); carta em análise", "arq"),
 ("Eduardo Bolsonaro", "ex-deputado, nos EUA · condenação sem trânsito"),
 ("Coação no curso do processo (AP 2.782). Origem: atuação nos EUA (2025)", "PF (INQ 4.995); PGR denunciou em 22/09/2025", "STF, 1ª Turma, relator Moraes (Dino, Zanin, Cármen Lúcia)", "condenado a 4 anos e 2 meses, semiaberto (16/06/2026); embargos em 11–18/09; sem trânsito", "cond"),
 ("Perda de mandato. Origem: faltas acima de um terço das sessões", "Mesa da Câmara (Hugo Motta)", "Mesa da Câmara", "declarada em 18/12/2025", "cond"),
 ("'Novo AI-5' (2019); posts sobre urnas (2026)", "Partidos (Conselho de Ética); TSE (Kassio)", "Conselho de Ética; TSE", "AI-5 arquivado 12x5 (2021); posts removidos por liminar (31/08/2026)", "arq"),
 ("Carlos Bolsonaro", "ex-vereador · candidato ao Senado por SC"),
 ("Rachadinha na Câmara do Rio. Origem: Época (2019)", "MP-RJ: arquivou quanto a ele (set/2024); subprocurador reabriu (fev/2026), 26 investigados", "1ª Vara Criminal Especializada (RJ)", "investigado; nunca denunciado; 7 ex-assessores denunciados", "inv"),
 ("Abin paralela. Origem: Última Milha (2023)", "PF indiciou (jun/2025) como 'núcleo político'; MPF de 1ª instância", "STF, Moraes → Justiça Federal do DF (20/07/2026)", "indiciado, sem denúncia", "reu"),
 ("'Gabinete do ódio'. Origem: CPMI das Fake News (2019); INQ 4781", "PF (relatório de 2020)", "STF, Moraes", "sem denúncia em sete anos; CPMI encerrada sem relatório", "inv"),
 ("Domicílio eleitoral em SC (2026)", "MP Eleitoral (84ª Promotoria, São José)", "TRE-SC (registro deferido em análise)", "arquivado (16/07/2026)", "arq"),
 ("Jair Renan Bolsonaro", "vereador em Balneário Camboriú · ações trancadas"),
 ("Empréstimo com faturamento fictício. Origem: Operação Nexum (PCDF, 2023)", "PCDF; MPDFT (denúncia recebida em 27/03/2024)", "5ª Vara Criminal de Brasília; TJDFT; STJ", "TJDFT e STJ trancaram as ações (2025 a fev/2026): sem pena", "arq"),
 ("Tráfico de influência. Origem: O Globo (2021)", "PF-DF: encerrou sem indiciamento (ago/2022); Abin paralela teria produzido provas a favor", "MPF", "encerrado", "arq"),
]

def wrap(txt, n, maxl=4):
    words = txt.split(); lines = []; line = ""
    for w in words:
        if len(line + " " + w) > n and line: lines.append(line); line = w
        else: line = (line + " " + w).strip()
    if line: lines.append(line)
    if len(lines) > maxl: lines = lines[:maxl]; lines[-1] = lines[-1][:n-1].rstrip(" ,;") + "…"
    return lines

def quadro():
    COL_W = [520, 400, 400, 420]; ROW_H, SEC_H = 66, 44
    W = 60 + sum(COL_W) + 40 + 60
    top = 150
    H = top + sum(SEC_H if len(r) == 2 else ROW_H for r in ROWS) + 150
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Inter, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="{SURF}"/>']
    o.append(f'<text x="40" y="48" font-size="30" font-weight="700" fill="{INK}">A família Bolsonaro diante da Justiça: quem investiga, quem julga, em que estado está cada caso</text>')
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">Uma linha por caso · cor da última coluna = estado em 07/09/2026 · o caso Master e o Dark Horse estão no consolidado · fontes e defesas em bolsonaro_2026/README.md</text>')
    x = 60
    xs = []
    for (k, t), w in zip(COLS, COL_W):
        xs.append(x)
        o.append(f'<rect x="{x}" y="{top-46}" width="{w-10}" height="40" rx="8" fill="{INK}" opacity="0.06"/>')
        o.append(f'<text x="{x+14}" y="{top-20}" font-size="13" font-weight="700" fill="{INK}">{esc(t)}</text>')
        x += w
    y = top
    for r in ROWS:
        if len(r) == 2:
            nome, sub = r
            o.append(f'<text x="60" y="{y+26}" font-size="18" font-weight="700" fill="{INK}">{esc(nome)}</text>')
            o.append(f'<text x="{60+len(nome)*10.5+14}" y="{y+26}" font-size="12.5" fill="{INK2}">{esc(sub)}</text>')
            o.append(f'<line x1="60" y1="{y+SEC_H-4}" x2="{W-60}" y2="{y+SEC_H-4}" stroke="{INK}" stroke-width="1.2"/>')
            y += SEC_H; continue
        caso, inv, jul, est, key = r
        col = EST[key][0]
        o.append(f'<line x1="60" y1="{y+ROW_H}" x2="{W-60}" y2="{y+ROW_H}" stroke="{GRID}" stroke-width="1"/>')
        cells = [caso, inv, jul, est]
        for i, (cx, w, txt) in enumerate(zip(xs, COL_W, cells)):
            is_est = i == 3
            o.append(f'<rect x="{cx+0.5}" y="{y+4}" width="{w-11}" height="{ROW_H-8}" rx="6" fill="{"#ffffff"}" stroke="{col if is_est else GRID}" stroke-width="{2.6 if is_est else 1}"/>')
            if is_est:
                o.append(f'<rect x="{cx+0.5}" y="{y+4}" width="8" height="{ROW_H-8}" rx="3" fill="{col}"/>')
            lines = wrap(txt, int((w-30)/6.1), 4)
            yy = y + ROW_H/2 - (len(lines)-1)*6.2 + 4
            for j, ln in enumerate(lines):
                o.append(f'<text x="{cx+(18 if is_est else 12)}" y="{yy+j*12.4:.0f}" font-size="{10.6 if i else 10.8}" font-weight="{"600" if (i==0 and j==0) else "400"}" fill="{INK}">{esc(ln)}</text>')
            if i < 3:
                ax = cx + w - 10
                o.append(f'<text x="{ax+1}" y="{y+ROW_H/2+5}" font-size="14" fill="{INK2}">›</text>')
        y += ROW_H
    ly = y + 34
    o.append(f'<text x="60" y="{ly}" font-size="14" font-weight="700" fill="{INK}">Estado do caso (cor da última coluna)</text>')
    lx = 60
    for k, (c, lab) in EST.items():
        o.append(f'<rect x="{lx}" y="{ly+14}" width="34" height="18" rx="4" fill="none" stroke="{c}" stroke-width="2.6"/>')
        o.append(f'<text x="{lx+42}" y="{ly+28}" font-size="12.5" fill="{INK}">{esc(lab)}</text>')
        lx += 42 + len(lab)*6.6 + 40
    o.append(f'<text x="60" y="{ly+64}" font-size="12" fill="{INK2}">Só Jair tem condenação definitiva; Eduardo, condenação sem trânsito em julgado; Flávio, Carlos, Michelle e Jair Renan não têm condenação. Réu não é culpado; indiciado não é réu; denúncia rejeitada por forma não é absolvição de mérito. CC BY 4.0, Rafael B. Brotto.</text>')
    o.append('</svg>')
    return "\n".join(o), W, H

here = pathlib.Path(__file__).parent
s, W, H = quadro()
(here/"mapa_investiga_julga.svg").write_text(s, encoding="utf-8")
(here/"mapa_investiga_julga.html").write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{s}', encoding="utf-8")
import fitz
d = fitz.open(str(here/"mapa_investiga_julga.svg")); pix = d[0].get_pixmap(dpi=110); pix.save(str(here/"mapa_investiga_julga.png"))
print("mapa_investiga_julga", W, H, pix.width, pix.height)
