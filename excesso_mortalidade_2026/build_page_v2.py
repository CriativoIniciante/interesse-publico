# -*- coding: utf-8 -*-
"""Rodada 2: gera 'Excesso de Mortes no Brasil' a partir de dados/resumo_v2.json, resumo_v1.json e Registro Civil."""
import json, pandas as pd, numpy as np
v2 = json.load(open("dados/resumo_v2.json")); v1 = json.load(open("dados/resumo_v1.json"))
years = v2["years"]; bands = v2["bands"]
pop = pd.read_csv("dados/populacao_brasil_faixa_etaria_2000_2024.csv", index_col=0); pop.index = pop.index.astype(int)
tot_pop = {int(y): int(pop.loc[y,"Total"]) for y in years}
tot_pop[2025] = int(tot_pop[2024]*(tot_pop[2024]/tot_pop[2023]))
deaths = dict(zip(years, v2["all"]["count"]))
official_final = {2021: 1855622, 2023: 1485653}
scale = {y: official_final[y]/deaths[y] for y in official_final}
for y,v in official_final.items(): deaths[y] = v
asr_all = [round(a*scale.get(y,1.0),1) for a,y in zip(v2["all"]["asr"], years)]
asr_trend = v2["all"]["asr_trend"]; asr_exc = [round((a/t-1)*100,1) for a,t in zip(asr_all, asr_trend)]
yi0 = {y:i for i,y in enumerate(years)}
def sg(v): return ("+" if v>0 else "")+f"{v:.1f}".replace(".",",")+"%"
txt_asr = f"Em 2023 a taxa padronizada ficou {sg((asr_all[yi0[2023]]/asr_all[yi0[2019]]-1)*100)} em relação a 2019 e {sg(asr_exc[yi0[2023]])} acima da tendência de queda que vinha de antes. Em 2024 ficou {sg((asr_all[yi0[2024]]/asr_all[yi0[2019]]-1)*100)} em relação a 2019 e {sg(asr_exc[yi0[2024]])} acima da tendência."
# modelo 2 (tendência da taxa bruta 2015-2019) estendido a 2024
base_y = [2015,2016,2017,2018,2019]; rate = {y: deaths[y]/tot_pop[y]*1e5 for y in years}
s,i = np.polyfit(base_y, [rate[y] for y in base_y], 1)
expected = {y: (s*y+i)*tot_pop[y]/1e5 for y in years}
covid = dict(zip(years, v2["groups"]["covid"]["count"]))
rc = pd.read_csv("dados/registro_civil_obitos_mensal_2015_2026.csv"); rcy = rc.groupby("ano").obitos_rc.sum()
ratio = deaths[2024]/rcy.loc[2024]; est2025 = int(rcy.loc[2025]*ratio)
rcm = rc.pivot(index="mes", columns="ano", values="obitos_rc")
rcn = pd.read_csv("dados/registro_civil_causas_naturais_mensal_2023_2026.csv")
rcn["natural"] = rcn[["COVID","SRAG","PNEUMONIA","INSUFICIENCIA_RESPIRATORIA","SEPTICEMIA","INDETERMINADA","OUTRAS"]].sum(axis=1)
rcn_y = rcn.groupby("ano")[["natural","COVID","PNEUMONIA","SRAG","INSUFICIENCIA_RESPIRATORIA","SEPTICEMIA"]].sum()
jan_aug = lambda y: int(rc[(rc.ano==y)&(rc.mes<=8)].obitos_rc.sum())
DATA = {
 "years": years, "bands": bands, "deaths": [deaths[y] for y in years], "pop": [tot_pop[y] for y in years],
 "expected": [round(expected[y]) for y in years], "covid": [covid[y] for y in years],
 "asr": asr_all, "asr_trend": asr_trend, "asr_exc": asr_exc,
 "est2025": est2025, "pop2025": tot_pop[2025], "rc_years": {int(k): int(v) for k,v in rcy.items()}, "rc_ratio": round(ratio,4),
 "rc_monthly": {int(c): [None if pd.isna(x) else int(x) for x in rcm[c]] for c in rcm.columns if c>=2023},
 "rc_nat": {int(k): {c: int(v) for c,v in row.items()} for k,row in rcn_y.iterrows()},
 "jan_aug_2025": jan_aug(2025), "jan_aug_2026": jan_aug(2026),
 "groups": v2["groups"], "subs": v2["subs"], "comp": v2["comp"], "months": v2["months"], "monthly": v2["monthly"], "popband": v2["pop"],
}
nc = {y: round(deaths[y]-expected[y]-covid[y]) for y in [2021,2022,2023,2024]}
txt_exc = f"Em 2020 o excesso é menor que as mortes por covid: outras causas caíram. Em 2021 sobram cerca de {round(nc[2021]/1000)} mil mortes acima da covid, em 2022 cerca de {round(nc[2022]/1000)} mil, em 2023 cerca de {round(nc[2023]/1000)} mil e em 2024 cerca de {round(nc[2024]/1000)} mil. Este modelo, porém, não desconta o envelhecimento: pela taxa padronizada, 2023 e 2024 ficam {sg(asr_exc[yi0[2023]])} e {sg(asr_exc[yi0[2024]])} acima da tendência, o que equivale a algo entre {round(asr_exc[yi0[2023]]/100*deaths[2023]/1000)} mil e {round(asr_exc[yi0[2024]]/100*deaths[2024]/1000)} mil mortes por ano. Parte disso é covid não reconhecida como causa básica, parte é o que a seção 4 mostra: mortes mal definidas, hipertensão e diabetes como causa básica subiram em 2020 e 2021, sinal de óbitos sem investigação adequada em um sistema sobrecarregado."
data_js = json.dumps(DATA, ensure_ascii=False)
css = open("build_page.py").read().split("<style>")[1].split("</style>")[0]
html = r'''<title>Excesso de Mortes no Brasil</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Public+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>__CSS__
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:8px 16px}
.mini2{padding:2px 0}
.band{fill:var(--surface-2)}
.note{font-size:13px;color:var(--ink-2);margin:6px 0 0}
.correction{border-left:3px solid var(--s2)}
.tag{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;padding:2px 6px;border:1px solid var(--border);border-radius:3px;color:var(--ink-2);margin-left:6px;vertical-align:middle}
</style>

<div class="wrap">
<header>
  <div class="eyebrow">Caderno de investigação · mortalidade · Brasil · rodada 2</div>
  <h1>Excesso de Mortes no Brasil</h1>
  <p class="dek">Microdados do SIM de 2013 a 2024 por causa básica em CID-10 e idade, Registro Civil até agosto de 2026, e taxas padronizadas por idade. O que subiu, o que caiu e o que continua em aberto.</p>
  <div class="tiles">
    <div class="tile"><div class="label">Mortalidade padronizada por idade, 2024 vs 2019</div><div class="value" id="t1"></div><div class="delta">óbitos por 100 mil, população padrão de 2019</div></div>
    <div class="tile"><div class="label">Óbitos por covid como causa básica, 2020 a 2024</div><div class="value" id="t2"></div><div class="delta">SIM, códigos U07 e B34.2</div></div>
    <div class="tile"><div class="label">Câncer, taxa padronizada 2024 vs 2019</div><div class="value" id="t3"></div><div class="delta">C00 a C97, todas as idades</div></div>
    <div class="tile"><div class="label">Parada cardíaca e arritmias, 2024 vs 2019</div><div class="value" id="t4"></div><div class="delta">I46 a I49, taxa padronizada</div></div>
  </div>
</header>

<section>
  <div class="eyebrow">1 · Fontes desta rodada</div>
  <h2>O microdado completo, validado contra os totais oficiais</h2>
  <p>Com a rede liberada, obtive duas cópias públicas do microdado do SIM, extraídas do DATASUS pela biblioteca PySUS e publicadas no Hugging Face. Os totais anuais coincidem exatamente com os números oficiais de 2013 a 2020 e 2022. Para 2021 e 2023 as cópias trazem uma versão anterior do arquivo, com 1,2% e 1,3% menos registros que a versão final; nos totais gerais usei os números finais oficiais e ajustei a taxa padronizada na mesma proporção, e na composição por causa usei as cópias. O ano de 2024 é preliminar. Cada óbito foi classificado pela causa básica em CID-10 e pela idade, e as taxas foram calculadas com a população por faixa etária do DATASUS e padronizadas pela estrutura etária de 2019, o que remove o efeito do envelhecimento.</p>
  <div class="callout correction">
    <p><strong>Correção da rodada 1.</strong> O gráfico anterior de mortalidade cardiovascular por idade usava a classificação por palavras-chave do Registro Civil e mostrava altas de 34% a 62% entre 30 e 59 anos. Com a causa básica em CID-10 do SIM, a alta do capítulo circulatório nessas faixas foi de 3% a 13% até 2024, e a taxa padronizada do capítulo inteiro caiu 5%. O que subiu de fato foi um subgrupo específico, parada cardíaca e arritmias, detalhado na seção 6. A rodada 1 estava errada nesse ponto e este relatório a substitui.</p>
  </div>
</section>

<section>
  <div class="eyebrow">2 · Mortalidade geral, 2013 a 2025</div>
  <h2>Em número de mortes, 2024 ficou acima de 2019. Descontado o envelhecimento, voltou ao nível de 2019</h2>
  <p>O primeiro gráfico mostra o total de mortes. O ponto de 2025 é uma estimativa a partir do Registro Civil, corrigida pela razão entre SIM e Registro Civil em 2024. O segundo mostra a taxa padronizada por idade, que responde à pergunta certa: a probabilidade de morrer, para uma pessoa da mesma idade, está maior ou menor que antes?</p>
  <figure>
    <div class="ftitle">Mortes por todas as causas, 2013 a 2025</div>
    <div class="fsub">SIM por ano de ocorrência; 2024 preliminar; 2025 estimado pelo Registro Civil</div>
    <div class="legend"><span><i class="ln" style="background:var(--s1)"></i>observado</span><span><i class="ln" style="background:var(--muted)"></i>esperado, tendência da taxa bruta 2015 a 2019</span><span><i class="sw" style="background:var(--o1)"></i>estimativa 2025</span></div>
    <div id="chartA"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableA"></div></details>
  </figure>
  <figure>
    <div class="ftitle">Taxa de mortalidade padronizada por idade, 2013 a 2024</div>
    <div class="fsub">Óbitos por 100 mil habitantes, população padrão Brasil 2019; linha cinza é a tendência linear de 2013 a 2019</div>
    <div class="legend"><span><i class="ln" style="background:var(--s1)"></i>taxa padronizada</span><span><i class="ln" style="background:var(--muted)"></i>tendência pré-pandemia</span></div>
    <div id="chartA2"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableA2"></div></details>
  </figure>
  <p>Lidas juntas, as duas curvas dizem o seguinte. __TXT_ASR__ O crescimento no número absoluto de mortes entre 2019 e 2024 é quase todo envelhecimento: a população com 60 anos ou mais cresceu 14% nesse período.</p>
</section>

<section>
  <div class="eyebrow">3 · Excesso versus covid</div>
  <h2>Com a causa básica do SIM, o excesso não explicado por covid aparece em 2021 e 2022</h2>
  <figure>
    <div class="ftitle">Excesso de mortes e óbitos por covid como causa básica, 2020 a 2024</div>
    <div class="fsub">Excesso pelo modelo de tendência da taxa bruta, que não desconta o envelhecimento além do crescimento populacional</div>
    <div class="legend"><span><i class="sw" style="background:var(--s1)"></i>excesso de mortes</span><span><i class="sw" style="background:var(--s2)"></i>covid, causa básica no SIM</span></div>
    <div id="chartB"></div>
    <details open><summary>Ver como tabela</summary><div class="tscroll" id="tableB"></div></details>
  </figure>
  <p>__TXT_EXC__</p>
</section>

<section>
  <div class="eyebrow">4 · Por capítulo da CID-10</div>
  <h2>Cada capítulo, com o envelhecimento descontado</h2>
  <p>Cada painel tem escala própria. O rótulo é a variação da taxa padronizada de 2019 para 2024. Abaixo de cada linha, a área cinza marca 2020 a 2022.</p>
  <figure>
    <div class="ftitle">Taxa padronizada por idade por capítulo, 2013 a 2024</div>
    <div class="fsub">Óbitos por 100 mil, população padrão 2019</div>
    <div class="grid3" id="chartC"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableC"></div></details>
  </figure>
</section>

<section>
  <div class="eyebrow">5 · Câncer</div>
  <h2>A mortalidade por câncer caiu em 2020 e 2021 e ainda não voltou ao nível de 2019</h2>
  <p>Em número de mortes, o câncer subiu de 231 mil em 2019 para 259 mil em 2024. Descontado o envelhecimento, a taxa caiu 5% em 2020 e 2021 e estava 2% abaixo de 2019 em 2024. A queda de 2020 e 2021 é o padrão esperado quando uma epidemia mata antes pessoas frágeis, que teriam morrido de câncer meses depois, e quando parte dessas mortes recebe covid como causa básica. Não há sinal, nesses dados, de aumento generalizado de mortalidade por câncer após 2021. Os cânceres que sobem, colorretal e pâncreas, já subiam antes de 2019.</p>
  <figure>
    <div class="ftitle">Câncer por localização, taxa padronizada por idade</div>
    <div class="fsub">Óbitos por 100 mil, população padrão 2019; variação de 2019 para 2024 no rótulo</div>
    <div class="grid3" id="chartD"></div>
    <details><summary>Ver como tabela, com taxas por faixa etária em 2019, 2022 e 2024</summary><div class="tscroll" id="tableD"></div></details>
  </figure>
</section>

<section>
  <div class="eyebrow">6 · Cardiovascular e tromboembolismo por CID-10</div>
  <h2>Infarto e AVC continuam caindo. Parada cardíaca, arritmias e embolia pulmonar subiram e não voltaram</h2>
  <p>Este é o achado mais importante da rodada. Dentro do capítulo circulatório, as duas maiores causas, infarto agudo e doença cerebrovascular, seguem a queda de longo prazo. Já os óbitos com causa básica em parada cardíaca e arritmias subiram 21% em 2021 e estavam 25% acima de 2019 em 2024. A embolia pulmonar caiu em 2020, quando muitos desses óbitos receberam covid como causa básica, e desde 2022 está acima do nível pré-pandemia, 17% em 2024. A miocardite dobrou em taxa, mas partindo de 100 óbitos por ano no país inteiro.</p>
  <figure>
    <div class="ftitle">Causas cardiovasculares e tromboembólicas, taxa padronizada por idade</div>
    <div class="fsub">Óbitos por 100 mil, população padrão 2019; variação de 2019 para 2024 no rótulo</div>
    <div class="grid3" id="chartE"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableE"></div></details>
  </figure>
  <figure>
    <div class="ftitle">Parada cardíaca e arritmias, e embolia pulmonar, por faixa etária</div>
    <div class="fsub">Variação da taxa por 100 mil de 2019 para 2022 e para 2024, com os óbitos de 2024</div>
    <div class="tscroll" id="tableF"></div>
  </figure>
  <div class="callout">
    <p><strong>O que esses códigos significam.</strong> Parada cardíaca, I46, é o que a Organização Mundial da Saúde chama de código pouco útil: descreve como o coração parou, não por quê. Quando um médico atesta parada cardíaca sem investigar, o óbito cai aqui. A alta a partir de 2020 coincide com a alta das causas mal definidas em 2020 e 2021, mas com uma diferença: as mal definidas voltaram a cair em 2023 e 2024, e a parada cardíaca não. Isso torna menos provável que seja só piora de codificação. As explicações candidatas são sequelas cardíacas da infecção por covid, que atingiu a maior parte da população, atraso no atendimento de emergências, e efeito adverso da vacinação. A próxima seção testa o que dá para testar com dados agregados.</p>
  </div>
</section>

<section>
  <div class="eyebrow">7 · Teste de tempo</div>
  <h2>As altas acompanham as ondas de infecção e, depois, não descem</h2>
  <p>Cada série está indexada à sua média mensal de 2018 e 2019, igual a 100, para caber em um eixo só. A linha laranja é o número de mortes por covid em escala própria, que marca as ondas de infecção. As faixas cinzas marcam, de forma aproximada, os períodos em que cada grupo etário recebeu as doses iniciais e os reforços, conforme o calendário nacional.</p>
  <figure>
    <div class="ftitle">Mortes mensais, indexadas à média de 2018 e 2019</div>
    <div class="fsub">SIM, faixa etária selecionada para as três causas; covid em todas as idades, em escala própria com o pico igual a 200</div>
    <div class="filters" id="filtersG" role="group" aria-label="Faixa etária"></div>
    <div class="legend" id="legendG"></div>
    <div id="chartG"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableG"></div></details>
  </figure>
  <p>Entre 30 e 59 anos, as mortes por parada cardíaca e arritmias sobem já em abril de 2020, antes de qualquer vacina, e fazem picos em maio de 2020, março de 2021 e janeiro de 2022, os três meses de pico da covid. As doses iniciais dessa faixa foram aplicadas entre maio e agosto de 2021, durante a descida da onda Gama, e a série não faz um pico próprio nesse intervalo. A embolia pulmonar cai em 2020 e sobe de forma sustentada a partir de meados de 2021, sem pico alinhado às janelas de vacinação. O que os dados agregados mostram, portanto, é uma alta que acompanha as ondas de infecção e depois se mantém em um patamar mais alto. Eles não conseguem separar sequela de infecção de efeito de vacina para uma pessoa individual, porque quase todos os adultos tiveram as duas exposições no mesmo período. Isso exige dado individual com data de vacinação e data de infecção, que existe no DATASUS, mas não é público.</p>
</section>

<section>
  <div class="eyebrow">8 · 2025 e 2026</div>
  <h2>O Registro Civil aponta 2025 no mesmo patamar de 2024 e 2026 um pouco abaixo</h2>
  <figure>
    <div class="ftitle">Registros de óbito por mês, 2023 a 2026</div>
    <div class="fsub">Portal da Transparência do Registro Civil, todas as causas; o mês mais recente ainda recebe registros atrasados</div>
    <div class="legend" id="legendH"></div>
    <div id="chartH"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableH"></div></details>
  </figure>
  <p id="p2025"></p>
</section>

<section>
  <div class="eyebrow">9 · Leitura honesta</div>
  <h2>O que se sustenta, o que caiu e o que ficou em aberto</h2>
  <ul>
    <li><strong>Se sustenta:</strong> a pandemia produziu cerca de 820 mil mortes acima do esperado em 2020, 2021 e 2022, das quais 703 mil com covid como causa básica. Outras causas caíram em 2020, sobretudo respiratórias e câncer, como você havia suposto.</li>
    <li><strong>Se sustenta:</strong> descontado o envelhecimento, a mortalidade de 2023 e 2024 voltou ao nível de 2019, embora acima da tendência de queda anterior.</li>
    <li><strong>Caiu:</strong> a alta cardiovascular de 34% a 62% entre 30 e 59 anos da rodada 1 era artefato da classificação do Registro Civil. Pelo SIM, infarto e AVC caíram em todas as faixas.</li>
    <li><strong>Caiu:</strong> não há aumento de mortalidade por câncer após 2021. A taxa padronizada continua abaixo de 2019.</li>
    <li><strong>Em aberto:</strong> parada cardíaca e arritmias 25% acima de 2019, embolia pulmonar 17% acima, miocardite dobrada em números pequenos. A alta começa com as ondas de infecção e não regride. Separar sequela de covid, atraso de atendimento, codificação e vacinação exige dado individual.</li>
    <li><strong>Limites:</strong> 2021 e 2023 com versões anteriores do SIM, 1,2% e 1,3% abaixo do final; 2024 preliminar; 2025 estimado; causa básica depende da qualidade do atestado, que piorou em 2020 e 2021 e melhorou depois.</li>
  </ul>
</section>

<section>
  <div class="eyebrow">10 · Fontes e método</div>
  <h2>De onde vem cada número</h2>
  <dl class="kv">
    <dt>Microdado do SIM</dt><dd>Cópias públicas jpvmm/dataSUS_deaths e jgchaicoski/datasus_sim no Hugging Face, extraídas do DATASUS via PySUS; validadas contra os totais oficiais por ano. Agregação em <code>agrega_sim_duckdb.py</code>, classificação em <code>analise_rodada2.py</code>.</dd>
    <dt>Grupos de causa</dt><dd>Causa básica em CID-10. Covid: U07.1, U07.2, U09, U10 e B34.2. Câncer: C00 a C97. Circulatório: I00 a I99, com subgrupos I21-I22, I60-I69, I26, I80-I82, I40-I41, I42-I43, I46-I49, I50, I10. Mal definidas: capítulo R.</dd>
    <dt>População</dt><dd>Estimativas DATASUS por município, sexo e faixa etária, série revisada 2024, somadas para o Brasil, via pacote brpop. 2025 extrapolado pelo crescimento de 2024.</dd>
    <dt>Padronização</dt><dd>Método direto, faixas de dez anos, população padrão igual à estrutura etária do Brasil em 2019.</dd>
    <dt>Registro Civil</dt><dd>API do Portal da Transparência, totais mensais de registros de óbito de 2015 a agosto de 2026 e causas naturais por grupo de 2023 a 2026. Razão SIM 2024 sobre Registro Civil 2024 usada para estimar 2025.</dd>
    <dt>Calendário vacinal</dt><dd>Janelas aproximadas do Plano Nacional de Operacionalização: 75 anos ou mais entre fevereiro e março de 2021; 60 a 74 entre março e abril; 50 a 59 em maio e junho; 30 a 49 entre junho e agosto; 18 a 29 em agosto e setembro; reforços de 60 ou mais a partir de setembro de 2021 e de 18 ou mais a partir de novembro; quarta dose de 50 ou mais entre maio e julho de 2022.</dd>
  </dl>
</section>
</div>
<div class="tip" id="tip" role="status" aria-live="polite"></div>

<script>
const DATA = __DATA__;
const fmt = new Intl.NumberFormat('pt-BR'); const fmt1 = new Intl.NumberFormat('pt-BR',{maximumFractionDigits:1}); const fmt2 = new Intl.NumberFormat('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
const mil = v => v>=1e6 ? fmt2.format(v/1e6)+' mi' : fmt.format(Math.round(v/1000))+' mil';
const pct = (a,b) => (a/b-1)*100; const sgn = v => (v>0?'+':'')+fmt1.format(v)+'%';
const NS='http://www.w3.org/2000/svg';
function el(tag,attrs,parent){const e=document.createElementNS(NS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e;}
function txt(x,y,s,cls,attrs,parent){const t=el('text',Object.assign({x,y,class:cls||''},attrs||{}),parent);t.textContent=s;return t;}
const tip=document.getElementById('tip');
function showTip(nodes,x,y){tip.replaceChildren(...nodes);tip.style.display='block';const w=tip.offsetWidth,h=tip.offsetHeight;let L=x+14,T=y+14;if(L+w>innerWidth-8)L=x-w-14;if(T+h>innerHeight-8)T=y-h-14;tip.style.left=L+'px';tip.style.top=T+'px';}
function hideTip(){tip.style.display='none';}
function tipRows(title,rows){const out=[];const b=document.createElement('b');b.textContent=title;out.push(b);rows.forEach(r=>{const d=document.createElement('div');d.className='row';const l=document.createElement('span');if(r.color){const k=document.createElement('i');k.className='k';k.style.background=r.color;l.appendChild(k);}l.appendChild(document.createTextNode(r.label));const v=document.createElement('strong');v.textContent=r.value;d.append(l,v);out.push(d);});return out;}
function table(container,head,rows){const t=document.createElement('table');const th=document.createElement('thead');const tr=document.createElement('tr');head.forEach(h=>{const c=document.createElement('th');c.textContent=h;tr.appendChild(c);});th.appendChild(tr);t.appendChild(th);const tb=document.createElement('tbody');rows.forEach(r=>{const tr=document.createElement('tr');r.forEach(v=>{const c=document.createElement('td');c.textContent=v;tr.appendChild(c);});tb.appendChild(tr);});t.appendChild(tb);container.replaceChildren(t);}
const css=getComputedStyle(document.documentElement); const col=n=>css.getPropertyValue(n).trim();
const Y=DATA.years, yi=Object.fromEntries(Y.map((y,i)=>[y,i]));
const niceMax=(mx)=>{const p=Math.pow(10,Math.floor(Math.log10(mx)));const c=mx/p;const m=c<=1?1:c<=2?2:c<=2.5?2.5:c<=3?3:c<=4?4:c<=5?5:c<=6?6:c<=8?8:10;return m*p;};
function barPath(cx,bw,y0,top){return `M${cx-bw/2},${y0} L${cx-bw/2},${top+4} Q${cx-bw/2},${top} ${cx-bw/2+4},${top} L${cx+bw/2-4},${top} Q${cx+bw/2},${top} ${cx+bw/2},${top+4} L${cx+bw/2},${y0} Z`;}

/* tiles */
document.getElementById('t1').textContent=sgn(pct(DATA.asr[yi[2024]],DATA.asr[yi[2019]]));
document.getElementById('t2').textContent=mil(DATA.covid.slice(yi[2020]).reduce((s,v)=>s+v,0));
document.getElementById('t3').textContent=sgn(DATA.comp.subs.cancer_c00_c97.chg_2019_2024);
document.getElementById('t4').textContent=sgn(DATA.comp.subs.parada_arritmia_i46_i49.chg_2019_2024);

/* generic line chart with optional wash between series 0 and 1 */
function lineChart(target,{W=960,H=380,m={t:26,r:150,b:40,l:64},xs,series,y0,y1,ystep,yfmt,xlabels,shade,endLabels,tipFn,extra}){
  const w=W-m.l-m.r,h=H-m.t-m.b;const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img'});
  const x=i=>m.l+i*(w/(xs.length-1)), y=v=>m.t+h-(v-y0)/(y1-y0)*h;
  if(shade) shade.forEach(([a,b,label])=>{const r=el('rect',{x:x(a),y:m.t,width:x(b)-x(a),height:h,class:'band'},svg);if(label)txt(x(a)+4,m.t+12,label,'dl',{},svg);});
  const ax=el('g',{class:'axis'},svg);
  for(let v=y0;v<=y1+1e-9;v+=ystep){el('line',{x1:m.l,x2:m.l+w,y1:y(v),y2:y(v),class:Math.abs(v-y0)<1e-9?'base':''},ax);txt(m.l-10,y(v)+4,yfmt(v),'',{'text-anchor':'end'},ax);}
  (xlabels||xs).forEach((lab,i)=>{if(lab!==null&&lab!==undefined&&lab!=='')txt(x(i),H-14,lab,'',{'text-anchor':'middle'},ax);});
  if(extra) extra(svg,x,y);
  series.forEach(s=>{const pts=s.values.map((v,i)=>v==null?null:[x(i),y(v)]);let d='',pen=false;pts.forEach(p=>{if(!p){pen=false;return;}d+=(pen?'L':'M')+p[0]+','+p[1];pen=true;});
    el('path',{d,fill:'none',stroke:s.color,'stroke-width':s.width||2,'stroke-linejoin':'round','stroke-linecap':'round',opacity:s.opacity||1},svg);
    if(s.markers) pts.forEach(p=>{if(!p)return;el('circle',{cx:p[0],cy:p[1],r:6,fill:col('--surface')},svg);el('circle',{cx:p[0],cy:p[1],r:4,fill:s.color},svg);});
    if(s.points) s.points.forEach(([i,v,label])=>{el('circle',{cx:x(i),cy:y(v),r:7,fill:col('--surface')},svg);el('circle',{cx:x(i),cy:y(v),r:5,fill:s.color},svg);if(label)txt(x(i),y(v)-12,label,'dl strong',{'text-anchor':'middle'},svg);});
  });
  if(endLabels) endLabels.forEach(([i,v,label,strong,dy])=>txt(x(i)+10,y(v)+4+(dy||0),label,strong?'dl strong':'dl',{},svg));
  const cross=el('line',{x1:0,x2:0,y1:m.t,y2:m.t+h,stroke:col('--axis'),'stroke-width':1,visibility:'hidden'},svg);
  const hit=el('rect',{x:m.l,y:m.t,width:w,height:h,class:'hit'},svg);
  hit.addEventListener('pointermove',e=>{const r=svg.getBoundingClientRect();const px=(e.clientX-r.left)*W/r.width;const i=Math.max(0,Math.min(xs.length-1,Math.round((px-m.l)/(w/(xs.length-1)))));cross.setAttribute('x1',x(i));cross.setAttribute('x2',x(i));cross.setAttribute('visibility','visible');showTip(tipFn(i),e.clientX,e.clientY);});
  hit.addEventListener('pointerleave',()=>{cross.setAttribute('visibility','hidden');hideTip();});
  document.getElementById(target).appendChild(svg);
}

/* Chart A: deaths 2013-2025 */
(function(){
  const xs=[...Y,2025]; const obs=[...DATA.deaths,null]; const exp=[...DATA.expected,null];
  const y0=1000000,y1=2000000;
  lineChart('chartA',{xs,series:[{values:exp,color:col('--muted')},{values:obs,color:col('--s1'),markers:true,points:[[xs.length-1,DATA.est2025,'']]}],y0,y1,ystep:200000,yfmt:v=>fmt2.format(v/1e6).replace(/,00$/,'')+' mi',
    endLabels:[[xs.length-1,DATA.est2025,'2025: '+mil(DATA.est2025)+' est.',true,0],[xs.length-2,DATA.expected[yi[2024]],'esperado '+mil(DATA.expected[yi[2024]]),false,16]],
    extra:(svg,x,y)=>{let d='';for(let i=yi[2019];i<Y.length;i++)d+=(i===yi[2019]?'M':'L')+x(i)+','+y(DATA.deaths[i]);for(let i=Y.length-1;i>=yi[2019];i--)d+='L'+x(i)+','+y(DATA.expected[i]);d+='Z';el('path',{d,fill:col('--wash')},svg);txt(x(yi[2021]),y(DATA.deaths[yi[2021]])-12,mil(DATA.deaths[yi[2021]]),'dl strong',{'text-anchor':'middle'},svg);txt(x(yi[2024]),y(DATA.deaths[yi[2024]])-12,'2024: '+mil(DATA.deaths[yi[2024]]),'dl strong',{'text-anchor':'middle'},svg);},
    tipFn:i=>{if(i===xs.length-1)return tipRows('2025 (estimativa)',[{label:'Registro Civil',value:fmt.format(DATA.rc_years[2025])},{label:'estimativa em escala SIM',value:fmt.format(DATA.est2025)}]);return tipRows(xs[i],[{label:'observado',value:fmt.format(DATA.deaths[i]),color:col('--s1')},{label:'esperado',value:fmt.format(DATA.expected[i]),color:col('--muted')},{label:'excesso',value:fmt.format(DATA.deaths[i]-DATA.expected[i])},{label:'covid, causa básica',value:fmt.format(DATA.covid[i])}]);}});
  const rows=Y.map((yr,i)=>[yr,fmt.format(DATA.deaths[i]),fmt.format(DATA.pop[i]),fmt1.format(DATA.deaths[i]/DATA.pop[i]*1e5),fmt.format(DATA.expected[i]),fmt.format(DATA.deaths[i]-DATA.expected[i]),fmt.format(DATA.covid[i])]);
  rows.push(['2025 est.',fmt.format(DATA.est2025),fmt.format(DATA.pop2025),fmt1.format(DATA.est2025/DATA.pop2025*1e5),'—','—','—']);
  table(document.getElementById('tableA'),['Ano','Mortes','População','Por 100 mil','Esperado','Excesso','Covid (SIM)'],rows);
})();

/* Chart A2: ASR */
(function(){
  lineChart('chartA2',{H:340,xs:Y,series:[{values:DATA.asr_trend,color:col('--muted')},{values:DATA.asr,color:col('--s1'),markers:true}],y0:600,y1:900,ystep:50,yfmt:v=>fmt.format(v),
    endLabels:[[Y.length-1,DATA.asr[Y.length-1],'2024: '+fmt1.format(DATA.asr[Y.length-1]),true,-6],[Y.length-1,DATA.asr_trend[Y.length-1],'tendência '+fmt1.format(DATA.asr_trend[Y.length-1]),false,14]],
    extra:(svg,x,y)=>{txt(x(yi[2021]),y(DATA.asr[yi[2021]])-12,fmt1.format(DATA.asr[yi[2021]]),'dl strong',{'text-anchor':'middle'},svg);txt(x(yi[2019]),y(DATA.asr[yi[2019]])+20,'2019: '+fmt1.format(DATA.asr[yi[2019]]),'dl',{'text-anchor':'middle'},svg);},
    tipFn:i=>tipRows(Y[i],[{label:'taxa padronizada',value:fmt1.format(DATA.asr[i]),color:col('--s1')},{label:'tendência 2013-2019',value:fmt1.format(DATA.asr_trend[i]),color:col('--muted')},{label:'diferença',value:sgn(DATA.asr_exc[i])},{label:'vs 2019',value:sgn(pct(DATA.asr[i],DATA.asr[yi[2019]]))}])});
  table(document.getElementById('tableA2'),['Ano','Taxa padronizada','Tendência','Diferença','vs 2019'],Y.map((yr,i)=>[yr,fmt1.format(DATA.asr[i]),fmt1.format(DATA.asr_trend[i]),sgn(DATA.asr_exc[i]),sgn(pct(DATA.asr[i],DATA.asr[yi[2019]]))]));
})();

/* Chart B: excess vs covid bars 2020-2024 */
(function(){
  const yrs=[2020,2021,2022,2023,2024];const W=960,H=340,m={t:30,r:24,b:40,l:64};const w=W-m.l-m.r,h=H-m.t-m.b;
  const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img'});const y1=500000;const y=v=>m.t+h-v/y1*h;const band=w/yrs.length;
  const ax=el('g',{class:'axis'},svg);for(let v=0;v<=y1;v+=100000){el('line',{x1:m.l,x2:m.l+w,y1:y(v),y2:y(v),class:v===0?'base':''},ax);txt(m.l-10,y(v)+4,fmt.format(v/1000)+' mil','',{'text-anchor':'end'},ax);}
  yrs.forEach((yr,i)=>txt(m.l+band*(i+.5),H-14,yr,'',{'text-anchor':'middle'},ax));
  const bw=24,gap=10;
  yrs.forEach((yr,i)=>{const j=yi[yr];const vals=[{v:DATA.deaths[j]-DATA.expected[j],c:col('--s1'),l:'excesso de mortes'},{v:DATA.covid[j],c:col('--s2'),l:'covid, causa básica'}];const near=Math.abs(vals[0].v-vals[1].v)/Math.max(vals[0].v,vals[1].v,1)<0.15;
    vals.forEach((o,k)=>{const cx=m.l+band*(i+.5)+(k-.5)*(bw+gap);const top=y(Math.max(o.v,0));const p=el('path',{d:barPath(cx,bw,y(0),top),fill:o.c,class:'bar',tabindex:0,role:'img','aria-label':`${yr} ${o.l}: ${fmt.format(Math.round(o.v))}`},svg);txt(k===0?cx+bw/2-2:cx-bw/2+2,top-8,mil(o.v),'dl',{'text-anchor':k===0?'end':'start'},svg);
      const show=(px,py)=>showTip(tipRows(yr,[{label:o.l,value:fmt.format(Math.round(o.v)),color:o.c}]),px,py);p.addEventListener('pointermove',e=>show(e.clientX,e.clientY));p.addEventListener('pointerleave',hideTip);p.addEventListener('focus',()=>{const b=p.getBoundingClientRect();show(b.left+b.width/2,b.top);});p.addEventListener('blur',hideTip);});});
  document.getElementById('chartB').appendChild(svg);
  const rows=yrs.map(yr=>{const j=yi[yr];const ex=DATA.deaths[j]-DATA.expected[j];return [yr,fmt.format(DATA.deaths[j]),fmt.format(DATA.expected[j]),fmt.format(Math.round(ex)),fmt.format(DATA.covid[j]),fmt.format(Math.round(ex-DATA.covid[j]))];});
  const sum=k=>yrs.reduce((s,yr)=>s+k(yi[yr]),0);rows.push(['Soma',fmt.format(sum(j=>DATA.deaths[j])),fmt.format(sum(j=>DATA.expected[j])),fmt.format(Math.round(sum(j=>DATA.deaths[j]-DATA.expected[j]))),fmt.format(sum(j=>DATA.covid[j])),fmt.format(Math.round(sum(j=>DATA.deaths[j]-DATA.expected[j]-DATA.covid[j])))]);
  table(document.getElementById('tableB'),['Ano','Mortes','Esperado','Excesso','Covid, causa básica','Excesso não covid'],rows);
})();

/* small multiples of ASR series */
function smallMultiples(target,items,{W=300,H=192,decimals=1}={}){
  const grid=document.getElementById(target);grid.replaceChildren();
  items.forEach(it=>{const m={t:50,r:12,b:24,l:46};const w=W-m.l-m.r,h=H-m.t-m.b;const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,class:'mini2',role:'img','aria-label':it.label});
    const vals=it.values;const mx=Math.max(...vals);const y1=niceMax(mx*1.12);const y=v=>m.t+h-v/y1*h;const x=i=>m.l+i*(w/(vals.length-1));
    el('rect',{x:x(yi[2020])-(w/(vals.length-1))/2,y:m.t,width:(w/(vals.length-1))*3,height:h,class:'band'},svg);
    const ax=el('g',{class:'axis'},svg);[0,y1/2,y1].forEach(v=>{el('line',{x1:m.l,x2:m.l+w,y1:y(v),y2:y(v),class:v===0?'base':''},ax);txt(m.l-6,y(v)+4,new Intl.NumberFormat('pt-BR',{maximumFractionDigits:decimals}).format(v),'',{'text-anchor':'end'},ax);});
    [2013,2019,2024].forEach(yr=>txt(x(yi[yr]),H-8,yr,'',{'text-anchor':'middle'},ax));
    txt(m.l,16,it.label,'panel-title',{},svg);
    const ch=pct(vals[yi[2024]],vals[yi[2019]]);txt(m.l,34,'2019 a 2024: '+sgn(ch),'dl strong',{},svg);
    el('path',{d:vals.map((v,i)=>(i?'L':'M')+x(i)+','+y(v)).join(''),fill:'none',stroke:col('--s1'),'stroke-width':2,'stroke-linejoin':'round'},svg);
    [yi[2019],yi[2024]].forEach(i=>{el('circle',{cx:x(i),cy:y(vals[i]),r:5,fill:col('--surface')},svg);el('circle',{cx:x(i),cy:y(vals[i]),r:3.5,fill:col('--s1')},svg);});
    const cross=el('line',{x1:0,x2:0,y1:m.t,y2:m.t+h,stroke:col('--axis'),'stroke-width':1,visibility:'hidden'},svg);
    const hit=el('rect',{x:m.l,y:m.t,width:w,height:h,class:'hit'},svg);
    hit.addEventListener('pointermove',e=>{const r=svg.getBoundingClientRect();const px=(e.clientX-r.left)*W/r.width;const i=Math.max(0,Math.min(vals.length-1,Math.round((px-m.l)/(w/(vals.length-1)))));cross.setAttribute('x1',x(i));cross.setAttribute('x2',x(i));cross.setAttribute('visibility','visible');showTip(tipRows(it.label+' · '+Y[i],[{label:'por 100 mil',value:new Intl.NumberFormat('pt-BR',{maximumFractionDigits:2}).format(vals[i]),color:col('--s1')},{label:'óbitos',value:fmt.format(it.counts[i])},{label:'vs 2019',value:sgn(pct(vals[i],vals[yi[2019]]))}]),e.clientX,e.clientY);});
    hit.addEventListener('pointerleave',()=>{cross.setAttribute('visibility','hidden');hideTip();});
    grid.appendChild(svg);});
}
function asrTable(target,items,decimals=1){const f=new Intl.NumberFormat('pt-BR',{maximumFractionDigits:decimals});table(document.getElementById(target),['Causa','2013','2015','2019','2020','2021','2022','2023','2024','2019→2024','Óbitos 2019','Óbitos 2024'],items.map(it=>[it.label,...[2013,2015,2019,2020,2021,2022,2023,2024].map(y=>f.format(it.values[yi[y]])),sgn(pct(it.values[yi[2024]],it.values[yi[2019]])),fmt.format(it.counts[yi[2019]]),fmt.format(it.counts[yi[2024]])]));}
(function(){
  const gs=['circulatorio','neoplasias','respiratorio','externas','mal_definidas','endocrino_diabetes','infecciosas','neuro_mentais','digestivo'];
  const items=gs.map(g=>({label:DATA.groups[g].label,values:DATA.groups[g].asr,counts:DATA.groups[g].count}));
  smallMultiples('chartC',items);asrTable('tableC',items);
})();
(function(){
  const ss=['cancer_c00_c97','cancer_pulmao_c34','cancer_colorretal_c18_c21','cancer_mama_c50','cancer_prostata_c61','cancer_hematologico_c81_c96','cancer_pancreas_c25'];
  const items=ss.map(g=>({label:DATA.subs[g].label,values:DATA.subs[g].asr,counts:DATA.subs[g].count}));
  smallMultiples('chartD',items,{decimals:1});
  const f=new Intl.NumberFormat('pt-BR',{maximumFractionDigits:1});
  const rb=DATA.subs.cancer_c00_c97.rate_by_band;
  table(document.getElementById('tableD'),['Câncer C00-C97, faixa etária','2019','2022','2024','2019→2024'],DATA.bands.map(b=>[b,f.format(rb[b][yi[2019]]),f.format(rb[b][yi[2022]]),f.format(rb[b][yi[2024]]),sgn(pct(rb[b][yi[2024]],rb[b][yi[2019]]))]));
})();
(function(){
  const ss=['infarto_agudo_i21_i22','cerebrovascular_i60_i69','insuf_cardiaca_i50','hipertensao_i10','parada_arritmia_i46_i49','cardiomiopatia_i42_i43','embolia_pulmonar_i26','trombose_venosa_i80_i82','miocardite_i40_i41'];
  const items=ss.map(g=>({label:DATA.subs[g].label,values:DATA.subs[g].asr,counts:DATA.subs[g].count}));
  smallMultiples('chartE',items,{decimals:2});asrTable('tableE',items,2);
  const f=new Intl.NumberFormat('pt-BR',{maximumFractionDigits:2});
  const rows=[];['parada_arritmia_i46_i49','embolia_pulmonar_i26'].forEach(g=>{const s=DATA.subs[g];DATA.bands.forEach(b=>{const r=s.rate_by_band[b];const n24=Math.round(r[yi[2024]]*DATA.popband[b][yi[2024]]/1e5);rows.push([s.label,b,f.format(r[yi[2019]]),f.format(r[yi[2022]]),f.format(r[yi[2024]]),sgn(pct(r[yi[2022]],r[yi[2019]])),sgn(pct(r[yi[2024]],r[yi[2019]])),fmt.format(n24)]);});});
  table(document.getElementById('tableF'),['Causa','Faixa','2019','2022','2024','2019→2022','2019→2024','Óbitos 2024'],rows);
})();

/* Chart G: monthly indexed */
(function(){
  const M=DATA.months;const base=M.map((m,i)=>m<'2020-01');
  const sumB=(obj,bs)=>M.map((m,i)=>bs.reduce((s,b)=>s+obj[b][i],0));
  const groups={'30-59':['30-39','40-49','50-59'],'60+':['60-69','70-79','80+'],'todas':DATA.bands};
  const filt=document.getElementById('filtersG'),leg=document.getElementById('legendG');let cur='30-59';
  Object.keys(groups).forEach(k=>{const b=document.createElement('button');b.type='button';b.textContent=k==='todas'?'Todas as idades':k+' anos';b.setAttribute('aria-pressed',k===cur?'true':'false');b.addEventListener('click',()=>{cur=k;[...filt.children].forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));render();});filt.appendChild(b);});
  const defs=[['parada','Parada cardíaca e arritmias (I46-I49)','--s1'],['embolia','Embolia pulmonar (I26)','--s3'],['infarto','Infarto agudo (I21-I22)','--s4']];
  leg.replaceChildren(...[...defs.map(d=>[d[1],d[2],'ln']),['covid, todas as idades, escala própria com pico em 200','--s2','ln'],['janelas de vacinação: 1 doses iniciais, 2 reforço, 3 quarta dose','--surface-2','sw']].map(([l,c,k])=>{const s=document.createElement('span');const i=document.createElement('i');i.className=k;i.style.background=col(c);if(k==='sw')i.style.border='1px solid var(--axis)';s.append(i,document.createTextNode(l));return s;}));
  const vacc={'30-59':[['2021-05','2021-08','1'],['2021-11','2022-02','2'],['2022-05','2022-07','3']],'60+':[['2021-02','2021-04','1'],['2021-09','2021-11','2'],['2022-03','2022-06','3']],'todas':[['2021-02','2021-09','1'],['2021-09','2022-02','2'],['2022-03','2022-07','3']]};
  function index(vals){const bvals=vals.filter((v,i)=>base[i]);const mean=bvals.reduce((s,v)=>s+v,0)/bvals.length;return vals.map(v=>v/mean*100);}
  function render(){document.getElementById('chartG').replaceChildren();const bs=groups[cur];
    const series=defs.map(([k,l,c])=>({key:k,label:l,color:col(c),raw:sumB(DATA.monthly[k],bs),values:index(sumB(DATA.monthly[k],bs))}));
    const cmax=Math.max(...DATA.monthly.covid);const cov=DATA.monthly.covid.map(v=>v/cmax*200);series.push({key:'covid',label:'covid, escala própria',color:col('--s2'),raw:DATA.monthly.covid,values:cov,width:1.5});
    const mx=Math.max(...series.flatMap(s=>s.values));const y1=niceMax(mx*1.08);
    const xl=M.map(m=>m.endsWith('-01')?m.slice(0,4):'');
    const shade=vacc[cur].map(([a,b,l])=>[M.indexOf(a),M.indexOf(b),l]);
    lineChart('chartG',{H:420,m:{t:26,r:40,b:40,l:56},xs:M,xlabels:xl,series:series.map(s=>({values:s.values,color:s.color,width:s.width||2})),y0:0,y1,ystep:y1/5,yfmt:v=>fmt.format(v),shade,
      extra:(svg,x,y)=>{el('line',{x1:x(0),x2:x(M.length-1),y1:y(100),y2:y(100),stroke:col('--axis'),'stroke-width':1},svg);txt(x(M.length-1)+6,y(100)+4,'100','dl',{},svg);},
      tipFn:i=>tipRows(M[i],series.map(s=>({label:s.label+(s.key==='covid'?' (óbitos)':' (índice, óbitos)'),value:s.key==='covid'?fmt.format(s.raw[i]):fmt1.format(s.values[i])+' · '+fmt.format(s.raw[i]),color:s.color})))});
    table(document.getElementById('tableG'),['Mês',...series.map(s=>s.key==='covid'?'Covid, óbitos':s.label+', óbitos'),...defs.map(d=>d[1]+', índice')],M.map((m,i)=>[m,...series.map(s=>fmt.format(s.raw[i])),...series.slice(0,3).map(s=>fmt1.format(s.values[i]))]));
  }
  render();
})();

/* Chart H: RC monthly 2023-2026 */
(function(){
  const yrs=Object.keys(DATA.rc_monthly).map(Number).sort();const ramp=['--o1','--o2','--o3','--o4'];const leg=document.getElementById('legendH');
  leg.replaceChildren(...yrs.map((y,i)=>{const s=document.createElement('span');const sw=document.createElement('i');sw.className='ln';sw.style.background=col(ramp[i]);s.append(sw,document.createTextNode(String(y)));return s;}));
  const xs=[1,2,3,4,5,6,7,8,9,10,11,12];const series=yrs.map((y,i)=>({values:DATA.rc_monthly[y].map(v=>v==null?null:v),color:col(ramp[i]),markers:false}));
  const mnames=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
  lineChart('chartH',{H:340,m:{t:26,r:70,b:40,l:64},xs,xlabels:mnames,series,y0:90000,y1:160000,ystep:10000,yfmt:v=>fmt.format(v/1000)+' mil',
    endLabels:yrs.map((y,i)=>{const v=DATA.rc_monthly[y];let last=-1;for(let k=0;k<12;k++)if(v[k]!=null)last=k;return [last,v[last],String(y),i===yrs.length-1,0];}),
    tipFn:i=>tipRows(mnames[i],yrs.map((y,k)=>({label:String(y),value:DATA.rc_monthly[y][i]==null?'—':fmt.format(DATA.rc_monthly[y][i]),color:col(ramp[k])})))});
  table(document.getElementById('tableH'),['Mês',...yrs.map(String)],xs.map((m,i)=>[mnames[i],...yrs.map(y=>DATA.rc_monthly[y][i]==null?'—':fmt.format(DATA.rc_monthly[y][i]))]));
  const rc=DATA.rc_years;const n=DATA.rc_nat;
  document.getElementById('p2025').textContent=`No Registro Civil, 2025 fechou com ${fmt.format(rc[2025])} registros de óbito, ${sgn(pct(rc[2025],rc[2024]))} em relação a 2024, o que em escala do SIM corresponde a cerca de ${mil(DATA.est2025)} mortes e a uma taxa bruta de ${fmt1.format(DATA.est2025/DATA.pop2025*1e5)} por 100 mil, praticamente igual à de 2024. De janeiro a agosto de 2026 foram ${fmt.format(DATA.jan_aug_2026)} registros, ${sgn(pct(DATA.jan_aug_2026,DATA.jan_aug_2025))} em relação ao mesmo período de 2025, com o mês de agosto ainda incompleto. Entre as causas naturais, a covid caiu de ${fmt.format(n[2024].COVID)} óbitos em 2024 para ${fmt.format(n[2025].COVID)} em 2025, enquanto pneumonia subiu de ${fmt.format(n[2024].PNEUMONIA)} para ${fmt.format(n[2025].PNEUMONIA)} e septicemia de ${fmt.format(n[2024].SEPTICEMIA)} para ${fmt.format(n[2025].SEPTICEMIA)}. A causa cardiovascular por CID em 2025 só estará disponível quando o SIM preliminar de 2025 for publicado.`;
})();
</script>
'''
open("excesso-mortes-brasil.html","w").write(html.replace("__CSS__", css).replace("__DATA__", data_js).replace("__TXT_ASR__", txt_asr).replace("__TXT_EXC__", txt_exc))
print("written", len(html)+len(data_js)+len(css), "bytes; est2025", est2025, "ratio", round(ratio,4), "pop2025", tot_pop[2025])
