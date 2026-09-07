# -*- coding: utf-8 -*-
"""Quadro por ministro: cinco blocos por pessoa, cada célula com o peso da prova na borda.
Gera quadro_ministros.svg/.html/.png (PNG via PyMuPDF). Dados em DADOS abaixo; texto completo
e fontes em ../README.md. Régua: P prova formal · R relato documentado · A alegação · N refutado · O inocência formal."""
import html, pathlib

SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e0dfd9"
RED, AMB, GRN, BLU = "#d03b3b", "#c48a14", "#0ca30c", "#2a78d6"
COLS = [
 ("pat", "PATRIMÔNIO, FAMÍLIA E CONFLITOS", "escritórios, institutos, eventos pagos"),
 ("pub", "RECURSOS PÚBLICOS", "carros, aviões, passagens, gabinete"),
 ("apu", "APURAÇÕES FORMAIS", "CNJ, Senado, PGR, TCU, exterior"),
 ("dec", "DECISÕES QUE MUDARAM REGRAS", "atos institucionais, com data"),
 ("dcl", "DECLARAÇÕES", "falas públicas controversas"),
]
PESO = {
 "P": (INK, 2.6, "", "prova formal: decisão, documento oficial, operação, admissão"),
 "R": (INK2, 1.3, "", "relato documentado: reportagem com documento"),
 "A": (INK2, 1.3, "6 4", "alegação: fonte anônima, coluna, delação sem corroboração"),
 "N": (RED, 1.6, "", "refutado pela fonte primária"),
 "O": (GRN, 1.6, "", "inocência formal: arquivado, absolvido, prescrito"),
 "-": (GRID, 1.0, "", "sem registro relevante encontrado"),
}
def esc(s): return html.escape(s, quote=True)

# (nome, subtítulo, {col: (peso, texto)}) — preenchido a partir do README
DADOS = [
 ("EM EXERCÍCIO", "", None),
 ("Edson Fachin", "presidente · Dilma, 2015", {
   "pat": ("P", "dupla atividade como procurador e advogado (1990–2006) e apoio a Dilma em 2010, questionados na sabatina; nada além"),
   "pub": ("-", ""),
   "apu": ("R", "4 pedidos de impeachment desde 2021, nenhum admitido"),
   "dec": ("P", "anulou as condenações de Lula por incompetência (2021); ADPF das favelas; armas (2022–23); conduz a crise Moraes–Mendonça (set/2026)"),
   "dcl": ("P", "sobre Moraes: 'esteve onde precisava estar' (08/01/2026)")}),
 ("Alexandre de Moraes", "vice-presidente · Temer, 2017", {
   "pat": ("R", "patrimônio imobiliário de R$ 8,6 mi (2017) para R$ 31,5 mi, R$ 23,4 mi à vista, via holding da esposa (Estadão, abr/2026); escritório da esposa passou de 27 a 159 processos no STJ/STF"),
   "pub": ("R", "154 voos da FAB (2023–25) com lista sigilosa por 5 anos; R$ 248 mil em viagens de assessores; uso fora do rito da assessoria do TSE"),
   "apu": ("P", "vistos revogados e sanção Magnitsky dos EUA (jul/2025, revogada dez/2025); 66 pedidos de impeachment; ação na Flórida pendente"),
   "dec": ("P", "relator do inquérito das fake news (2019–); X e Starlink (2024); 1.399 condenados do 8/1; AP 2.668: Bolsonaro, 27a3m; prisão preventiva (nov/2025)"),
   "dcl": ("R", "'querem me derrubar faz tempo', 'cabeças vão rolar' (fev/2026)")}),
 ("Gilmar Mendes", "decano · FHC, 2002", {
   "pat": ("R", "IDP: contrato sem licitação com TJ-BA (2012), CBF Academy (2023–) com Gilmar relator da ação da CBF; Fórum de Lisboa com 64 grupos com causas no STF (2025); esposa sócia do escritório Bermudes"),
   "pub": ("R", "R$ 112 mil em passagens em 2 anos; esposa em voos da FAB; 'manda ele enfiar isso na b...' (2018)"),
   "apu": ("R", "18 pedidos de impeachment (2015–20), 7 ativos; impedimentos arguidos pela PGR (2017) negados por ele; ONU sobre o marco temporal"),
   "dec": ("P", "suspeição de Moro (2021); anulou Dirceu (2024); maconha 40 g (2024); foro ampliado (2025); suspendeu trechos da lei do impeachment de ministros (dez/2025)"),
   "dcl": ("R", "'lei feita por bêbados'; 'você e Deltan roubavam galinhas juntos'; 'Janot já estava bêbado' (2026)")}),
 ("Cármen Lúcia", "Lula, 2006", {
   "pat": ("-", ""),
   "pub": ("R", "10 voos da FAB em 2024, ano em que presidia o TSE"),
   "apu": ("P", "pedido de impeachment de 3 senadores pela frase dos '213 milhões de pequenos tiranos' (jul/2025); 5 acumulados"),
   "dec": ("P", "desempate contra o HC de Lula (2018); reconheceu a suspeição de Moro (2021); TSE 2022: desmonetização de canais; regras de IA de 2024; condenou Bolsonaro"),
   "dcl": ("P", "'213 milhões de pequenos tiranos soberanos' (jun/2025)")}),
 ("Dias Toffoli", "Lula, 2009", {
   "pat": ("P", "irmãos no resort Tayayá (2020–25); suspendeu multa de R$ 10,3 bi da J&F, cliente da esposa em outra causa, após votar pela queda da regra do CPC (2023); Odebrecht 'amigo do amigo' (alegação)"),
   "pub": ("R", "R$ 350 mil em viagens no 1º semestre de 2020; 3 voos da FAB como único passageiro; Marrocos R$ 67 mil"),
   "apu": ("O", "delação de Cabral (R$ 4 mi ao escritório da esposa) anulada pelo plenário (2021); 25 pedidos de impeachment, nenhum admitido"),
   "dec": ("P", "abriu de ofício o inquérito das fake news (2019); suspendeu processos com dados do Coaf a pedido de Flávio (2019); anulou as provas da Odebrecht (2023)"),
   "dcl": ("P", "'movimento de 1964', não golpe (2018); prisão de Lula foi 'armação' (2023)")}),
 ("Luiz Fux", "2ª Turma · Dilma, 2011", {
   "pat": ("P", "procurou Dirceu, réu do mensalão, por apoio à indicação (2010, admitido); filha no TJ-RJ (2016); filho com 544 processos no STF/STJ após a posse, Fux julgou clientes dele em outras instâncias"),
   "pub": ("P", "liminar estendeu o auxílio-moradia a toda a magistratura (2014–18), impacto bilionário"),
   "apu": ("O", "impeachment pelo auxílio-moradia não recebido (2016); pedido da 'Vaza Jato' parado; 2 ativos"),
   "dec": ("P", "juiz das garantias suspenso (2020); André do Rap (2020); absolveu Bolsonaro (set/2025) e pediu a 2ª Turma (out/2025)"),
   "dcl": ("P", "'Deus tenha piedade do Rio de Janeiro' (abr/2026)")}),
 ("Kassio Nunes Marques", "presidente do TSE · Bolsonaro, 2020", {
   "pat": ("R", "currículo contestado (Messina, La Coruña, Salamanca; 'inconsistências de 11%'); indicação via Ciro Nogueira e Flávio; esposa em gabinete de senador; filho: R$ 27,7 mi em fundos e R$ 281,6 mil de consultoria paga por Master e JBS"),
   "pub": ("-", ""),
   "apu": ("R", "33 representações no CNJ como desembargador (32 por atraso); 1 pedido de impeachment (2025)"),
   "dec": ("P", "cultos na pandemia (2021, revogada); contra a inelegibilidade de Bolsonaro (2023); TSE 2026: suspendeu pesquisa a pedido do PL, extinguiu ação contra Dark Horse, mandou Eduardo remover posts"),
   "dcl": ("P", "'em algumas comunidades da Espanha, qualquer curso após a graduação pode receber a denominação postgrado' (2020)")}),
 ("André Mendonça", "relator do Master · Bolsonaro, 2021", {
   "pat": ("R", "Instituto Iter (2023–26) com ex-integrantes do governo Bolsonaro: 55 contratos públicos, 54 sem licitação, R$ 10,8 mi; viagem a Israel paga pela Conib enquanto relata ação de federada"),
   "pub": ("-", ""),
   "apu": ("P", "PGR abriu apuração sobre uso da LSN contra críticos (2021); Moraes pediu providências contra ele com relatório sem valor probatório (set/2026)"),
   "dec": ("P", "pediu inquéritos pela LSN contra jornalistas (2020); votos mais brandos no 8/1; único voto pelo impedimento de Moraes e Dino (2025); 16 prisões no INSS"),
   "dcl": ("R", "'Deus me proporcionou ocupar uma posição institucional de relevo' (jun/2026)")}),
 ("Cristiano Zanin", "1ª Turma · Lula, 2023", {
   "pat": ("R", "advogado de Lula por 10 anos; esposa em 14 ações no STF (2023); dados fiscais expostos por Dallagnol (set/2026)"),
   "pub": ("R", "3 voos da FAB (2024); Fórum de Lisboa 2024"),
   "apu": ("P", "impedimento no caso Bolsonaro rejeitado por 10 a 0 (2025); 3 pedidos de impeachment"),
   "dec": ("P", "suspendeu a desoneração da folha (2024); negou levar Bolsonaro ao plenário e votou pela condenação (2025)"),
   "dcl": ("P", "'sou grato ao presidente Lula por ter indicado meu nome' (2023)")}),
 ("Flávio Dino", "presidente da 1ª Turma · Lula, 2023", {
   "pat": ("R", "representação à PGR por 'nepotismo cruzado': esposa e cunhada em gabinetes de aliados (dez/2024); sem desfecho"),
   "pub": ("R", "SW4 blindada do TJ-MA usada pela família (nov/2025); PF fez busca contra o jornalista por ordem de Moraes (mar/2026); Dino: cessão a pedido da segurança do STF"),
   "apu": ("P", "7 pedidos de impeachment; pedidos na PGR quando ministro da Justiça ('agora a polícia eu tenho'; 'dama do tráfico')"),
   "dec": ("P", "emendas: R$ 4,2 bi bloqueados (2024), Valdemar e Cunha (2026), emendas de líder nulas (ago/2026); ADPF 1178 contra efeitos de leis estrangeiras (2025)"),
   "dcl": ("P", "'coloque a Teresa como vice, essa chapa vai ficar imbatível' (mai/2025)")}),
 ("RECÉM-SAÍDOS E A 11ª CADEIRA", "", None),
 ("Luís Roberto Barroso", "aposentado em out/2025 · Dilma, 2013", {
   "pat": ("R", "apartamento de US$ 4,1 mi em Miami em nome de empresa da família; 6 eventos num mês com partes em processos no STF (2025); abriu escritório em abr/2026"),
   "pub": ("R", "voo da FAB Miami–Boa Vista–Brasília com Zanin (2024)"),
   "apu": ("O", "pedidos de impeachment por 'perdeu, mané' e 'derrotamos o bolsonarismo', arquivados"),
   "dec": ("P", "vencido na prisão em 2ª instância (2019); mandou instalar a CPI da Covid (2021); presidiu o STF na Magnitsky"),
   "dcl": ("P", "'perdeu, mané' (2022); 'nós derrotamos o bolsonarismo' (2023)")}),
 ("Ricardo Lewandowski", "aposentado em 2023 · ministro da Justiça 2024–26", {
   "pat": ("R", "R$ 6,5 mi do Master ao escritório da família, R$ 5,25 mi já ministro; filho contratado por entidade investigada no INSS (2024)"),
   "pub": ("R", "jato da FAB de Brasília a SP para solenidade seguida do casamento do presidente do TCU (fev/2024)"),
   "apu": ("O", "MBL pediu impeachment pelo 'fatiamento' (2016), sem andamento"),
   "dec": ("P", "revisor do mensalão (2012); presidiu o impeachment de Dilma e aceitou o 'fatiamento' (2016); deu à defesa de Lula a leniência da Odebrecht (2020)"),
   "dcl": ("-", "")}),
 ("Jorge Messias", "indicado por Lula, rejeitado pelo Senado (42 a 34, 29/04/2026)", {
   "pat": ("P", "AGU desde 2023; 'Bessias' do grampo Dilma–Lula (2016), nunca investigado pelo episódio"),
   "pub": ("-", ""),
   "apu": ("P", "primeira rejeição de um indicado ao STF desde 1894; cadeira vaga desde 18/10/2025"),
   "dec": ("-", ""),
   "dcl": ("P", "'nem ativismo, nem passivismo'; 'sou totalmente contra o aborto' (sabatina, 2026)")}),
]

def wrap(txt, n, maxl=5):
    words = txt.split(); lines = []; line = ""
    for w in words:
        if len(line + " " + w) > n and line: lines.append(line); line = w
        else: line = (line + " " + w).strip()
    if line: lines.append(line)
    if len(lines) > maxl: lines = lines[:maxl]; lines[-1] = lines[-1][:n-1].rstrip(" ,;") + "…"
    return lines

def quadro(dados, titulo, sub, out_svg, out_html, out_png, corte):
    NAME_W, COL_W, ROW_H, SEC_H = 230, 300, 78, 34
    W = 60 + NAME_W + 5*COL_W + 60
    top = 150
    H = top + sum(SEC_H if d[2] is None else ROW_H for d in dados) + 190
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Inter, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="{SURF}"/>']
    o.append(f'<text x="40" y="48" font-size="30" font-weight="700" fill="{INK}">{esc(titulo)}</text>')
    o.append(f'<text x="40" y="76" font-size="15" fill="{INK2}">{esc(sub)}</text>')
    x0 = 60 + NAME_W
    for i, (k, t, s) in enumerate(COLS):
        cx = x0 + i*COL_W
        o.append(f'<rect x="{cx}" y="{top-52}" width="{COL_W-6}" height="46" rx="8" fill="{INK}" opacity="0.06"/>')
        o.append(f'<text x="{cx+14}" y="{top-32}" font-size="13" font-weight="700" fill="{INK}">{esc(t)}</text>')
        o.append(f'<text x="{cx+14}" y="{top-14}" font-size="11.5" fill="{INK2}">{esc(s)}</text>')
    y = top
    for nome, subt, cells in dados:
        if cells is None:
            o.append(f'<text x="60" y="{y+24}" font-size="13" font-weight="700" letter-spacing="1" fill="{INK2}">{esc(nome)}</text>')
            o.append(f'<line x1="60" y1="{y+SEC_H-2}" x2="{W-60}" y2="{y+SEC_H-2}" stroke="{INK}" stroke-width="1"/>')
            y += SEC_H; continue
        o.append(f'<line x1="60" y1="{y+ROW_H}" x2="{W-60}" y2="{y+ROW_H}" stroke="{GRID}" stroke-width="1"/>')
        o.append(f'<text x="60" y="{y+ROW_H/2}" font-size="14.5" font-weight="700" fill="{INK}">{esc(nome)}</text>')
        for j, ln in enumerate(wrap(subt, 34, 2)):
            o.append(f'<text x="60" y="{y+ROW_H/2+15+j*12}" font-size="10.5" fill="{INK2}">{esc(ln)}</text>')
        for i, (k, _, _) in enumerate(COLS):
            cx = x0 + i*COL_W
            peso, txt = cells.get(k, ("-", ""))
            pcol, pw, pdash, _ = PESO[peso]
            dash = f' stroke-dasharray="{pdash}"' if pdash else ''
            o.append(f'<rect x="{cx+0.5}" y="{y+3.5}" width="{COL_W-7}" height="{ROW_H-7}" rx="6" fill="{"#ffffff" if peso != "-" else "none"}" stroke="{pcol}" stroke-width="{pw}"{dash}/>')
            if peso != "-":
                o.append(f'<text x="{cx+COL_W-14}" y="{y+16}" font-size="10.5" font-weight="700" text-anchor="end" fill="{pcol}">{peso}</text>')
                lines = wrap(txt, 46)
                yy = y + ROW_H/2 - (len(lines)-1)*6 + 4
                for j, ln in enumerate(lines):
                    o.append(f'<text x="{cx+12}" y="{yy+j*12:.0f}" font-size="10.2" fill="{INK}">{esc(ln)}</text>')
        y += ROW_H
    ly = y + 30
    o.append(f'<text x="60" y="{ly}" font-size="14" font-weight="700" fill="{INK}">Como ler a borda (peso da prova mais forte na célula)</text>')
    lx = 60
    for k, (pcol, pw, pdash, lab) in PESO.items():
        dash = f' stroke-dasharray="{pdash}"' if pdash else ''
        o.append(f'<rect x="{lx}" y="{ly+16}" width="34" height="18" rx="4" fill="none" stroke="{pcol}" stroke-width="{pw}"{dash}/>')
        o.append(f'<text x="{lx+42}" y="{ly+30}" font-size="12" fill="{INK}">{k} = {esc(lab)}</text>')
        lx += 42 + len(lab)*6.4 + 36
        if lx > W - 400: lx = 60; ly += 30
    o.append(f'<text x="60" y="{ly+64}" font-size="12" fill="{INK2}">O caso Banco Master está fora deste quadro (ver consolidado_2005_2026). Ninguém aqui foi condenado por nada do que está listado. Estado em {corte}. Texto completo, defesas e fontes em ministros_stf_2026/README.md. CC BY 4.0, Rafael B. Brotto.</text>')
    o.append('</svg>')
    svg = "\n".join(o)
    out_svg.write_text(svg, encoding="utf-8")
    out_html.write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:{SURF}}}</style>{svg}', encoding="utf-8")
    import fitz
    d = fitz.open(str(out_svg)); pix = d[0].get_pixmap(dpi=110); pix.save(str(out_png))
    return W, H, pix.width, pix.height

if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    if not DADOS:
        print("DADOS vazio: preencha a partir do README antes de gerar."); raise SystemExit(1)
    print(quadro(DADOS, "Os ministros do STF, um a um: o que está documentado fora do caso Master",
                 "Célula = bloco de fatos · letra e borda = peso da prova mais forte · estado em 07/09/2026 · detalhes e fontes em ministros_stf_2026/README.md",
                 here/"quadro_ministros.svg", here/"quadro_ministros.html", here/"quadro_ministros.png", "07/09/2026"))
