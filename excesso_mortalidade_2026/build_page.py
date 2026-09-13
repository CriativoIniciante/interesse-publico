# -*- coding: utf-8 -*-
"""Gera a página HTML 'Excesso de Mortes no Brasil' a partir de dados/resumo_v1.json."""
import json, pandas as pd, numpy as np
d = json.load(open("dados/resumo_v1.json"))
ex = pd.DataFrame(d["excess"]).set_index("year")
pop = pd.read_csv("dados/populacao_brasil_faixa_etaria_2000_2024.csv", index_col=0); pop.index = pop.index.astype(int)
o = pop[["From 60 to 64 years","From 65 to 69 years","From 70 to 74 years","From 75 to 79 years","From 80 years or more"]].sum(axis=1); u = pop.Total - o
w = 0.70
frozen = {y: ex.loc[2019,"deaths"]*(w*o.loc[y]/o.loc[2019] + (1-w)*u.loc[y]/u.loc[2019]) for y in range(2020,2024)}
years = [int(y) for y in ex.index]
series = {
  "years": years,
  "deaths": [int(ex.loc[y,"deaths"]) for y in years],
  "expected_rate": [round(float(ex.loc[y,"expected_deaths"])) for y in years],
  "expected_count": [round(float(ex.loc[y,"expected_count_trend"])) for y in years],
  "expected_aging": [round(float(ex.loc[y,"expected_aging"])) for y in years],
  "expected_frozen": {str(y): round(v) for y,v in frozen.items()},
  "covid_rc": {str(y): (None if pd.isna(ex.loc[y,"covid_rc"]) else int(ex.loc[y,"covid_rc"])) for y in years},
  "pop": [int(ex.loc[y,"pop"]) for y in years],
  "share60": [round(float(ex.loc[y,"share60plus"]),1) for y in years],
}
rc = pd.DataFrame(d["rc_groups"]).set_index("year")
groups = {
  "years": [int(y) for y in rc.index],
  "covid": [int(v) for v in rc["covid_all"]],
  "cardio": [int(v) for v in rc["cardio_total"]],
  "resp": [int(v) for v in (rc["deaths_sars"]+rc["deaths_pneumonia"]+rc["deaths_respiratory_failure"])],
  "sepsis": [int(v) for v in rc["deaths_septicemia"]],
  "others": [int(v) for v in (rc["deaths_others"]+rc["deaths_indeterminate"])],
}
order = ["9-","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"]
labels = {"9-":"0 a 9 anos","10-19":"10 a 19","20-29":"20 a 29","30-39":"30 a 39","40-49":"40 a 49","50-59":"50 a 59","60-69":"60 a 69","70-79":"70 a 79","80+":"80 ou mais"}
rates = {}
for k,name in [("cardio","Cardiovascular total"),("heart_attack","Infarto"),("stroke","AVC")]:
    r = pd.DataFrame(d["cardio_age_rates"][k]); r.columns = [int(c) for c in r.columns]
    rates[k] = {"label": name, "bands": [{"band": b, "label": labels[b], "values": [round(float(r.loc[b,y]),1) for y in [2019,2020,2021,2022]]} for b in order]}
counts = {}
for k in ["cardio","heart_attack","stroke"]:
    cc = pd.DataFrame(d["cardio_age_counts"][k]); cc.columns=[int(c) for c in cc.columns]
    cc.loc["80+"] = cc.loc[["80-89","90-99","100+"]].sum()
    counts[k] = {b: [int(cc.loc[b,y]) for y in [2019,2020,2021,2022]] for b in order}
DATA = {"series": series, "groups": groups, "rates": rates, "counts": counts}
data_js = json.dumps(DATA, ensure_ascii=False)

html = r'''<title>Excesso de Mortes no Brasil</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Public+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  color-scheme:light;
  --page:#f4f5f2; --surface:#fcfcfb; --surface-2:#eef0ec;
  --ink:#151715; --ink-2:#4f524d; --muted:#858880; --grid:#e1e2dc; --axis:#c3c4bd; --border:rgba(21,23,21,.12);
  --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; --s4:#eda100; --s5:#e87ba4; --other:#b9bbb4;
  --o1:#86b6ef; --o2:#5598e7; --o3:#2a78d6; --o4:#1c5cab;
  --wash:rgba(42,120,214,.10); --accent:#1c5cab; --tip-bg:#151715; --tip-ink:#f6f6f2;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    color-scheme:dark;
    --page:#111312; --surface:#1a1a19; --surface-2:#232523;
    --ink:#f1f1ec; --ink-2:#c3c2b7; --muted:#8f918a; --grid:#2c2c2a; --axis:#3a3b38; --border:rgba(255,255,255,.12);
    --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500; --s5:#d55181; --other:#5a5c57;
    --o1:#9ec5f4; --o2:#6da7ec; --o3:#3987e5; --o4:#256abf;
    --wash:rgba(57,135,229,.14); --accent:#86b6ef; --tip-bg:#f1f1ec; --tip-ink:#151715;
  }
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --page:#111312; --surface:#1a1a19; --surface-2:#232523;
  --ink:#f1f1ec; --ink-2:#c3c2b7; --muted:#8f918a; --grid:#2c2c2a; --axis:#3a3b38; --border:rgba(255,255,255,.12);
  --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500; --s5:#d55181; --other:#5a5c57;
  --o1:#9ec5f4; --o2:#6da7ec; --o3:#3987e5; --o4:#256abf;
  --wash:rgba(57,135,229,.14); --accent:#86b6ef; --tip-bg:#f1f1ec; --tip-ink:#151715;
}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font-family:"Public Sans",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:40px 24px 80px}
.eyebrow{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
h1{font-family:"Newsreader",Georgia,serif;font-weight:500;font-size:clamp(34px,5vw,52px);line-height:1.05;margin:10px 0 14px;letter-spacing:-.01em;text-wrap:balance}
h2{font-family:"Newsreader",Georgia,serif;font-weight:500;font-size:28px;line-height:1.15;margin:6px 0 10px;text-wrap:balance}
h3{font-size:15px;font-weight:600;margin:0 0 6px}
p{max-width:68ch;margin:0 0 14px}
.dek{font-size:19px;color:var(--ink-2);max-width:62ch}
a{color:var(--accent)}
section{margin-top:56px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:28px 0 0}
.tile{background:var(--surface);border:1px solid var(--border);padding:16px 18px;border-radius:6px}
.tile .label{font-size:13px;color:var(--ink-2)}
.tile .value{font-size:34px;font-weight:600;line-height:1.1;margin:6px 0 4px}
.tile .delta{font-size:13px;color:var(--ink-2)}
figure{margin:18px 0 0;background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:18px 18px 12px}
figure .ftitle{font-weight:600;font-size:15px;margin:0 0 2px}
figure .fsub{font-size:13px;color:var(--ink-2);margin:0 0 12px}
.legend{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:13px;color:var(--ink-2);margin:6px 0 10px}
.legend span{display:inline-flex;align-items:center;gap:7px}
.sw{width:12px;height:12px;border-radius:2px;display:inline-block}
.ln{width:18px;height:2px;display:inline-block;border-radius:1px}
svg{display:block;width:100%;height:auto;font-family:"Public Sans",system-ui,sans-serif}
.axis text{fill:var(--muted);font-size:12px;font-variant-numeric:tabular-nums}
.axis line{stroke:var(--grid);stroke-width:1}
.axis .base{stroke:var(--axis)}
.dl{fill:var(--ink-2);font-size:12px;font-weight:500}
.dl.strong{fill:var(--ink);font-weight:600}
.pt{font-size:12px;fill:var(--ink);font-weight:600}
.panel-title{font-size:13px;fill:var(--ink);font-weight:600}
.bar{transition:opacity .12s}
.bar:hover,.bar:focus{opacity:.82;outline:none}
.hit{fill:transparent;cursor:crosshair}
details{margin:8px 0 0}
summary{cursor:pointer;font-size:13px;color:var(--accent);font-weight:500;list-style:none;padding:6px 0}
summary::-webkit-details-marker{display:none}
summary::before{content:"▸ ";color:var(--muted)}
details[open] summary::before{content:"▾ "}
.tscroll{overflow-x:auto}
table{border-collapse:collapse;font-size:13px;width:100%;margin-top:6px}
th,td{padding:6px 10px;text-align:right;border-bottom:1px solid var(--grid);white-space:nowrap;font-variant-numeric:tabular-nums}
th:first-child,td:first-child{text-align:left}
thead th{color:var(--ink-2);font-weight:600;border-bottom:1px solid var(--axis)}
.tip{position:fixed;pointer-events:none;background:var(--tip-bg);color:var(--tip-ink);padding:8px 10px;border-radius:4px;font-size:12.5px;line-height:1.4;z-index:20;display:none;max-width:280px;box-shadow:0 4px 14px rgba(0,0,0,.18)}
.tip b{font-weight:600;font-size:13px}
.tip .row{display:flex;gap:8px;align-items:center;justify-content:space-between}
.tip .k{display:inline-block;width:12px;height:2px;margin-right:6px;vertical-align:middle}
.callout{border-left:3px solid var(--accent);background:var(--surface);padding:14px 18px;margin:18px 0;border-radius:0 6px 6px 0}
.callout p:last-child{margin-bottom:0}
.filters{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 12px}
.filters button{font:inherit;font-size:13px;font-weight:500;padding:6px 12px;border:1px solid var(--border);background:var(--surface);color:var(--ink-2);border-radius:4px;cursor:pointer}
.filters button[aria-pressed="true"]{background:var(--ink);color:var(--surface);border-color:var(--ink)}
.filters button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px 18px}
.mini{padding:4px 0}
ol,ul{max-width:70ch;padding-left:22px}
li{margin-bottom:6px}
.src{font-size:14px;color:var(--ink-2)}
code{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.92em;background:var(--surface-2);padding:1px 5px;border-radius:3px}
.kv{display:grid;grid-template-columns:max-content 1fr;gap:6px 16px;font-size:14px;max-width:70ch}
.kv dt{color:var(--ink-2)}
.kv dd{margin:0}
@media (prefers-reduced-motion: reduce){.bar{transition:none}}
@media (max-width:640px){.wrap{padding:28px 16px 60px} h2{font-size:24px}}
</style>

<div class="wrap">
<header>
  <div class="eyebrow">Caderno de investigação · mortalidade · Brasil · rodada 1</div>
  <h1>Excesso de Mortes no Brasil</h1>
  <p class="dek">O que os registros de óbito mostram sobre 2020 a 2023, quanto do aumento é covid, o que aconteceu com as outras causas naturais e como a mortalidade cardiovascular mudou por idade.</p>
  <div class="tiles">
    <div class="tile"><div class="label">Mortes por todas as causas em 2021</div><div class="value" id="t1"></div><div class="delta" id="t1d"></div></div>
    <div class="tile"><div class="label">Excesso acumulado 2020 a 2023</div><div class="value" id="t2"></div><div class="delta">faixa entre os três modelos de esperado</div></div>
    <div class="tile"><div class="label">Óbitos por covid registrados 2020 a 2022</div><div class="value" id="t3"></div><div class="delta">Registro Civil, causa básica ou associada</div></div>
  </div>
</header>

<section>
  <div class="eyebrow">1 · O que foi possível medir</div>
  <h2>Três fontes primárias, cada uma com um limite</h2>
  <p>Os totais anuais de 2015 a 2023 vêm do Sistema de Informações sobre Mortalidade, o SIM, via a base World Mortality Dataset, que copia o SIM mês a mês. A população por faixa etária vem da série revisada do DATASUS empacotada no projeto brpop. Os óbitos por grupo de causa e por idade vêm do Portal da Transparência do Registro Civil, raspado pelo projeto brazil-civil-registry-data até janeiro de 2023.</p>
  <div class="callout">
    <p><strong>O que ainda falta.</strong> O microdado do SIM por causa básica em CID-10, que permitiria separar câncer, tromboembolismo e cada capítulo cardiovascular de 2013 a 2024, está bloqueado para esta sessão em todos os espelhos testados. A seção 6 explica como obter essas tabelas no TabNet em poucos minutos.</p>
  </div>
</section>

<section>
  <div class="eyebrow">2 · Mortalidade geral</div>
  <h2>As mortes subiram 15% em 2020 e 37% em 2021, e ainda não voltaram à tendência</h2>
  <p>A linha cinza é o número de mortes esperado se a taxa bruta de mortalidade tivesse seguido a tendência de 2015 a 2019, aplicada à população real de cada ano. A área azul é o excesso.</p>
  <figure id="figA">
    <div class="ftitle">Mortes por todas as causas, Brasil, 2015 a 2023</div>
    <div class="fsub">Óbitos registrados no SIM por ano de ocorrência, em milhões</div>
    <div class="legend"><span><i class="ln" style="background:var(--s1)"></i>observado</span><span><i class="ln" style="background:var(--muted)"></i>esperado, tendência 2015 a 2019</span><span><i class="sw" style="background:var(--wash);border:1px solid var(--s1)"></i>excesso</span></div>
    <div id="chartA"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableA"></div></details>
  </figure>
</section>

<section>
  <div class="eyebrow">3 · Excesso versus covid</div>
  <h2>Em 2020 a covid explica todo o excesso. De 2021 em diante, não</h2>
  <p>Em 2020, o excesso e os óbitos por covid do Registro Civil praticamente coincidem, e as outras causas naturais até caem um pouco. Em 2021 sobra um excesso não explicado por covid de cerca de 65 mil mortes, em 2022 de cerca de 85 mil e em 2023, com a covid quase zerada, o excesso restante depende inteiramente de como se estima o esperado.</p>
  <figure id="figB">
    <div class="ftitle">Excesso de mortes e óbitos por covid, 2020 a 2023</div>
    <div class="fsub">Excesso pelo modelo de tendência da taxa bruta; covid conforme o Registro Civil, que ainda não consolidou 2023</div>
    <div class="legend"><span><i class="sw" style="background:var(--s1)"></i>excesso de mortes</span><span><i class="sw" style="background:var(--s2)"></i>óbitos por covid</span></div>
    <div id="chartB"></div>
    <details open><summary>Os três modelos de esperado, lado a lado</summary><div class="tscroll" id="tableB"></div></details>
  </figure>
  <div class="callout">
    <p><strong>Por que o esperado importa tanto.</strong> A população com 60 anos ou mais cresceu 14% entre 2019 e 2023, contra 2% da população total. Se a taxa de mortalidade por idade de 2019 fosse simplesmente congelada e aplicada à população envelhecida, o esperado de 2023 seria maior que o observado, e o excesso desapareceria. Se a queda histórica das taxas por idade tivesse continuado, o excesso de 2023 seria de cerca de 85 mil. A resposta honesta é que o excesso de 2022 e 2023 está entre zero e esse valor, e só o microdado do SIM por idade fecha essa conta.</p>
  </div>
</section>

<section>
  <div class="eyebrow">4 · Outras causas naturais</div>
  <h2>Respiratórias caíram, cardiovasculares subiram, o resto ficou parecido</h2>
  <p>Sua hipótese era que as mortes por outras causas diminuíram enquanto as de covid aumentaram. Para as causas respiratórias, é o que os dados mostram: pneumonia, insuficiência respiratória e SRAG somadas caíram 26 mil em 2020 e 33 mil em 2021 em relação a 2019, o que é compatível com reclassificação para covid e com a queda de circulação de outros vírus. Para as cardiovasculares, o movimento foi o oposto: subiram 20 mil em 2020, 47 mil em 2021 e 50 mil em 2022.</p>
  <figure id="figC">
    <div class="ftitle">Óbitos por causas naturais por grupo, Registro Civil, 2018 a 2022</div>
    <div class="fsub">Classificação por palavras-chave da declaração de óbito, como publicada no portal da transparência</div>
    <div class="legend"><span><i class="sw" style="background:var(--s2)"></i>covid</span><span><i class="sw" style="background:var(--s3)"></i>cardiovascular</span><span><i class="sw" style="background:var(--s4)"></i>respiratórias</span><span><i class="sw" style="background:var(--s5)"></i>septicemia</span><span><i class="sw" style="background:var(--other)"></i>outras e indeterminadas</span></div>
    <div id="chartC"></div>
    <details><summary>Ver como tabela, com variação em relação a 2019</summary><div class="tscroll" id="tableC"></div></details>
  </figure>
</section>

<section>
  <div class="eyebrow">5 · Cardiovascular por idade</div>
  <h2>A alta cardiovascular concentrou-se entre 30 e 69 anos, e começou em 2020, antes das vacinas</h2>
  <p>Cada painel mostra a taxa de óbitos por 100 mil habitantes da faixa etária, de 2019 a 2022, com escala própria. O rótulo é a variação acumulada até 2022. Entre 30 e 59 anos as taxas subiram de 34% a 62%. Acima de 80 anos caíram. O primeiro degrau, de 2019 para 2020, ocorreu antes da vacinação, que começou em janeiro de 2021, o que é uma pista importante para separar as hipóteses.</p>
  <figure id="figD">
    <div class="ftitle">Mortalidade cardiovascular por faixa etária, óbitos por 100 mil, 2019 a 2022</div>
    <div class="fsub">Registro Civil com idade informada, dividido pela população da faixa, série DATASUS 2024</div>
    <div class="filters" id="filtersD" role="group" aria-label="Indicador"></div>
    <div class="legend" id="legendD"></div>
    <div class="grid3" id="chartD"></div>
    <details><summary>Ver como tabela</summary><div class="tscroll" id="tableD"></div></details>
  </figure>
  <div class="callout">
    <p><strong>Quatro hipóteses cabem nesses números, e só dados finos separam elas.</strong> Primeira: covid causa infarto, AVC e miocardite, e 2020 e 2021 foram os anos de maior circulação do vírus. Segunda: atraso de atendimento na pandemia, com hospitais lotados e pessoas evitando emergência. Terceira: mudança de codificação, já que o Registro Civil classifica por palavras da declaração e uma parada cardíaca em paciente com covid pode cair em qualquer coluna. Quarta: efeito adverso da vacinação, que a partir de 2021 atingiu justamente essas faixas em ondas. O teste mais direto é a série mensal do SIM por CID-10 e idade: se a alta acompanha as ondas de infecção, pesa a primeira; se acompanha as ondas de vacinação por faixa etária, pesa a quarta. Essa é a próxima tabela a buscar.</p>
  </div>
</section>

<section>
  <div class="eyebrow">6 · Próximo passo</div>
  <h2>As tabelas do TabNet que fecham a análise</h2>
  <p>O TabNet do DATASUS gera tabelas agregadas do SIM que resolvem tudo o que ficou em aberto, em arquivos pequenos. Endereço: <code>tabnet.datasus.gov.br</code>, menu Estatísticas Vitais, Mortalidade desde 1996 pela CID-10, Óbitos por ocorrência, Brasil por Região e UF.</p>
  <ol>
    <li><strong>Óbitos por ano e capítulo.</strong> Linha: Ano do óbito. Coluna: Capítulo CID-10. Períodos: 2013 a 2023. Exportar com "Copia como .CSV".</li>
    <li><strong>Óbitos por ano e faixa etária.</strong> Linha: Faixa etária. Coluna: Ano do óbito. Mesmos períodos.</li>
    <li><strong>Câncer por idade.</strong> Repetir a tabela 2 com o filtro Capítulo CID-10 igual a II, neoplasias.</li>
    <li><strong>Cardiovascular por idade.</strong> Repetir com Capítulo IX, aparelho circulatório, e depois com Categoria CID-10 igual a I21 e I22, infarto agudo, e I60 a I69, cerebrovasculares.</li>
    <li><strong>Tromboembolismo.</strong> Repetir com Categoria CID-10 igual a I26, embolia pulmonar, e I80 a I82, trombose venosa.</li>
    <li><strong>Dados preliminares de 2024 e 2025.</strong> No mesmo menu, a opção "Óbitos preliminares" traz as mesmas tabelas para os anos ainda não fechados.</li>
  </ol>
  <p>Cole os arquivos aqui ou coloque na pasta <code>mortalidade/dados</code> do repositório. Com eles, a rodada 2 traz os gráficos de 2013 a 2025 por causa e idade que você pediu, com taxas padronizadas por idade.</p>
</section>

<section>
  <div class="eyebrow">7 · Fontes e método</div>
  <h2>De onde vem cada número</h2>
  <dl class="kv">
    <dt>Mortes anuais</dt><dd>SIM, Ministério da Saúde, via World Mortality Dataset de Karlinsky e Kobak, arquivo world_mortality.csv, meses de 2015 a 2023 somados.</dd>
    <dt>População por idade</dt><dd>Estimativas DATASUS, série revisada 2024, por município, sexo e faixa etária, somadas para o Brasil, a partir do pacote brpop de Raphael Saldanha.</dd>
    <dt>Causas naturais por grupo</dt><dd>Portal da Transparência do Registro Civil, painel de causas naturais, raspado pelo projeto brazil-civil-registry-data, tabela por estado e tabela detalhada por sexo e idade.</dd>
    <dt>Esperado, modelo 1</dt><dd>Regressão linear do número de mortes de 2015 a 2019, projetada.</dd>
    <dt>Esperado, modelo 2</dt><dd>Regressão linear da taxa bruta por 100 mil de 2015 a 2019, multiplicada pela população de cada ano.</dd>
    <dt>Esperado, modelo 3</dt><dd>Taxa de 2019 congelada e aplicada a um índice populacional que dá peso de 70% à população com 60 anos ou mais, a parcela das mortes que ocorre nessa idade.</dd>
    <dt>Limites</dt><dd>O Registro Civil registra cerca de 5% menos óbitos que o SIM e classifica causas por palavras da declaração, não por CID. A faixa "80 ou mais" soma as faixas 80 a 89, 90 a 99 e 100 ou mais do portal. Óbitos sem idade informada, abaixo de 0,6% do total, foram excluídos das taxas.</dd>
  </dl>
</section>
</div>
<div class="tip" id="tip" role="status" aria-live="polite"></div>

<script>
const DATA = __DATA__;
const fmt = new Intl.NumberFormat('pt-BR');
const fmt1 = new Intl.NumberFormat('pt-BR',{maximumFractionDigits:1});
const fmt2 = new Intl.NumberFormat('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
const mil = v => v>=1e6 ? fmt2.format(v/1e6)+' mi' : fmt.format(Math.round(v/1000))+' mil';
const pct = (a,b) => (a/b-1)*100;
const sgn = v => (v>0?'+':'')+fmt1.format(v)+'%';
const NS='http://www.w3.org/2000/svg';
function el(tag,attrs,parent){const e=document.createElementNS(NS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e;}
function txt(x,y,s,cls,attrs,parent){const t=el('text',Object.assign({x,y,class:cls||''},attrs||{}),parent);t.textContent=s;return t;}
const tip=document.getElementById('tip');
function showTip(html,x,y){tip.replaceChildren(...html);tip.style.display='block';moveTip(x,y);}
function moveTip(x,y){const w=tip.offsetWidth,h=tip.offsetHeight;let L=x+14,T=y+14;if(L+w>innerWidth-8)L=x-w-14;if(T+h>innerHeight-8)T=y-h-14;tip.style.left=L+'px';tip.style.top=T+'px';}
function hideTip(){tip.style.display='none';}
function tipRows(title,rows){const out=[];const b=document.createElement('b');b.textContent=title;out.push(b);rows.forEach(r=>{const d=document.createElement('div');d.className='row';const l=document.createElement('span');if(r.color){const k=document.createElement('i');k.className='k';k.style.background=r.color;l.appendChild(k);}l.appendChild(document.createTextNode(r.label));const v=document.createElement('strong');v.textContent=r.value;d.append(l,v);out.push(d);});return out;}
function table(container,head,rows){const t=document.createElement('table');const th=document.createElement('thead');const tr=document.createElement('tr');head.forEach(h=>{const c=document.createElement('th');c.textContent=h;tr.appendChild(c);});th.appendChild(tr);t.appendChild(th);const tb=document.createElement('tbody');rows.forEach(r=>{const tr=document.createElement('tr');r.forEach(v=>{const c=document.createElement('td');c.textContent=v;tr.appendChild(c);});tb.appendChild(tr);});t.appendChild(tb);container.replaceChildren(t);}
const S=DATA.series, css=getComputedStyle(document.documentElement);
const col=n=>css.getPropertyValue(n).trim();

/* tiles */
const i21=S.years.indexOf(2021), i19=S.years.indexOf(2019);
document.getElementById('t1').textContent=mil(S.deaths[i21]);
document.getElementById('t1d').textContent=sgn(pct(S.deaths[i21],S.deaths[i19]))+' em relação a 2019';
const idx2020=S.years.indexOf(2020);
const exRate=S.years.map((y,i)=>S.deaths[i]-S.expected_rate[i]), exCount=S.years.map((y,i)=>S.deaths[i]-S.expected_count[i]);
const exFrozen=S.years.map((y,i)=>y>=2020?S.deaths[i]-S.expected_frozen[y]:null);
const sum=a=>a.reduce((s,v)=>s+(v||0),0);
const cum=[sum(exRate.slice(idx2020)),sum(exCount.slice(idx2020)),sum(exFrozen.slice(idx2020))];
document.getElementById('t2').textContent=fmt.format(Math.round(Math.min(...cum)/1000))+' a '+fmt.format(Math.round(Math.max(...cum)/1000))+' mil';
document.getElementById('t3').textContent=mil(sum([2020,2021,2022].map(y=>S.covid_rc[y])));

/* Chart A: line observed vs expected */
(function(){
  const W=960,H=400,m={t:24,r:150,b:40,l:64};const w=W-m.l-m.r,h=H-m.t-m.b;
  const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Mortes observadas e esperadas por ano'});
  const ys=S.years, y0=1000000,y1=2000000;
  const x=i=>m.l+i*(w/(ys.length-1)), y=v=>m.t+h-(v-y0)/(y1-y0)*h;
  const ax=el('g',{class:'axis'},svg);
  for(let v=y0;v<=y1;v+=200000){el('line',{x1:m.l,x2:m.l+w,y1:y(v),y2:y(v),class:v===y0?'base':''},ax);txt(m.l-10,y(v)+4,fmt1.format(v/1e6).replace('.',',')+' mi','',{'text-anchor':'end'},ax);}
  ys.forEach((yr,i)=>txt(x(i),H-14,yr,'',{'text-anchor':'middle'},ax));
  // excess wash 2019..2023
  let d='';for(let i=i19;i<ys.length;i++)d+=(i===i19?'M':'L')+x(i)+','+y(S.deaths[i]);for(let i=ys.length-1;i>=i19;i--)d+='L'+x(i)+','+y(S.expected_rate[i]);d+='Z';
  el('path',{d,fill:col('--wash')},svg);
  const line=(arr,color,width)=>el('path',{d:arr.map((v,i)=>(i?'L':'M')+x(i)+','+y(v)).join(''),fill:'none',stroke:color,'stroke-width':width,'stroke-linejoin':'round','stroke-linecap':'round'},svg);
  line(S.expected_rate,col('--muted'),2);
  line(S.deaths,col('--s1'),2);
  S.deaths.forEach((v,i)=>{el('circle',{cx:x(i),cy:y(v),r:6,fill:col('--surface')},svg);el('circle',{cx:x(i),cy:y(v),r:4,fill:col('--s1')},svg);});
  // direct labels
  txt(x(i21),y(S.deaths[i21])-12,mil(S.deaths[i21]),'dl strong',{'text-anchor':'middle'},svg);
  txt(x(ys.length-1)+10,y(S.deaths[ys.length-1])+4,'observado '+mil(S.deaths[ys.length-1]),'dl strong',{},svg);
  txt(x(ys.length-1)+10,y(S.expected_rate[ys.length-1])+14,'esperado '+mil(S.expected_rate[ys.length-1]),'dl',{},svg);
  txt(x(i19),y(S.deaths[i19])+20,mil(S.deaths[i19]),'dl',{'text-anchor':'middle'},svg);
  // crosshair
  const cross=el('line',{x1:0,x2:0,y1:m.t,y2:m.t+h,stroke:col('--axis'),'stroke-width':1,visibility:'hidden'},svg);
  const hit=el('rect',{x:m.l,y:m.t,width:w,height:h,class:'hit'},svg);
  hit.addEventListener('pointermove',e=>{const r=svg.getBoundingClientRect();const px=(e.clientX-r.left)*W/r.width;const i=Math.max(0,Math.min(ys.length-1,Math.round((px-m.l)/(w/(ys.length-1)))));cross.setAttribute('x1',x(i));cross.setAttribute('x2',x(i));cross.setAttribute('visibility','visible');
    showTip(tipRows(ys[i],[{label:'observado',value:fmt.format(S.deaths[i]),color:col('--s1')},{label:'esperado',value:fmt.format(S.expected_rate[i]),color:col('--muted')},{label:'excesso',value:(exRate[i]>0?'+':'')+fmt.format(Math.round(exRate[i]))},{label:'por 100 mil',value:fmt1.format(S.deaths[i]/S.pop[i]*1e5)}]),e.clientX,e.clientY);});
  hit.addEventListener('pointerleave',()=>{cross.setAttribute('visibility','hidden');hideTip();});
  document.getElementById('chartA').appendChild(svg);
  table(document.getElementById('tableA'),['Ano','Mortes','População','Por 100 mil','Esperado, modelo 2','Excesso','Excesso %'],ys.map((yr,i)=>[yr,fmt.format(S.deaths[i]),fmt.format(S.pop[i]),fmt1.format(S.deaths[i]/S.pop[i]*1e5),fmt.format(S.expected_rate[i]),fmt.format(Math.round(exRate[i])),sgn(exRate[i]/S.expected_rate[i]*100)]));
})();

/* Chart B: grouped bars excess vs covid */
(function(){
  const yrs=[2020,2021,2022,2023];const W=960,H=340,m={t:30,r:24,b:40,l:64};const w=W-m.l-m.r,h=H-m.t-m.b;
  const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Excesso de mortes e óbitos por covid por ano'});
  const y1=500000;const y=v=>m.t+h-v/y1*h;const band=w/yrs.length;
  const ax=el('g',{class:'axis'},svg);
  for(let v=0;v<=y1;v+=100000){el('line',{x1:m.l,x2:m.l+w,y1:y(v),y2:y(v),class:v===0?'base':''},ax);txt(m.l-10,y(v)+4,fmt.format(v/1000)+' mil','',{'text-anchor':'end'},ax);}
  yrs.forEach((yr,i)=>txt(m.l+band*(i+.5),H-14,yr,'',{'text-anchor':'middle'},ax));
  const bw=24,gap=10;
  yrs.forEach((yr,i)=>{const j=S.years.indexOf(yr);const vals=[{v:exRate[j],c:col('--s1'),l:'excesso de mortes'},{v:S.covid_rc[yr]||0,c:col('--s2'),l:'óbitos por covid'}];
    vals.forEach((o,k)=>{const cx=m.l+band*(i+.5)+(k-.5)*(bw+gap);const top=y(Math.max(o.v,0));const hh=Math.max(0,y(0)-top);
      const p=el('path',{d:`M${cx-bw/2},${y(0)} L${cx-bw/2},${top+4} Q${cx-bw/2},${top} ${cx-bw/2+4},${top} L${cx+bw/2-4},${top} Q${cx+bw/2},${top} ${cx+bw/2},${top+4} L${cx+bw/2},${y(0)} Z`,fill:o.c,class:'bar',tabindex:0,role:'img','aria-label':`${yr} ${o.l}: ${fmt.format(Math.round(o.v))}`},svg);
      const near = Math.abs(vals[0].v-vals[1].v)/Math.max(vals[0].v,vals[1].v,1) < 0.15;
      txt(cx,top-8-(k===1&&near?14:0),mil(o.v),'dl',{'text-anchor':'middle'},svg);
      const note = (yr===2023&&k===1)?' (ano incompleto no Registro Civil)':'';
      const show=(e)=>showTip(tipRows(yr,[{label:o.l+note,value:fmt.format(Math.round(o.v)),color:o.c}]),e.clientX||0,e.clientY||0);
      p.addEventListener('pointermove',show);p.addEventListener('pointerleave',hideTip);p.addEventListener('focus',e=>{const r=p.getBoundingClientRect();showTip(tipRows(yr,[{label:o.l,value:fmt.format(Math.round(o.v)),color:o.c}]),r.left+r.width/2,r.top);});p.addEventListener('blur',hideTip);
    });});
  document.getElementById('chartB').appendChild(svg);
  const rows=yrs.map(yr=>{const j=S.years.indexOf(yr);return [yr,fmt.format(S.deaths[j]),fmt.format(Math.round(exCount[j])),fmt.format(Math.round(exRate[j])),fmt.format(Math.round(exFrozen[j])),S.covid_rc[yr]!=null?fmt.format(S.covid_rc[yr]):'—',fmt.format(Math.round(exRate[j]-(S.covid_rc[yr]||0)))];});
  rows.push(['Soma',fmt.format(sum(yrs.map(yr=>S.deaths[S.years.indexOf(yr)]))),fmt.format(Math.round(cum[1])),fmt.format(Math.round(cum[0])),fmt.format(Math.round(cum[2])),fmt.format(sum(yrs.map(yr=>S.covid_rc[yr]||0))),fmt.format(Math.round(cum[0]-sum(yrs.map(yr=>S.covid_rc[yr]||0))))]);
  table(document.getElementById('tableB'),['Ano','Mortes','Modelo 1: tendência de mortes','Modelo 2: tendência da taxa','Modelo 3: só envelhecimento','Covid, Registro Civil','Não covid, modelo 2'],rows);
})();

/* Chart C: stacked columns natural causes by group */
(function(){
  const G=DATA.groups;const keys=[['covid','--s2','covid'],['cardio','--s3','cardiovascular'],['resp','--s4','respiratórias'],['sepsis','--s5','septicemia'],['others','--other','outras e indeterminadas']];
  const W=960,H=420,m={t:20,r:24,b:40,l:64};const w=W-m.l-m.r,h=H-m.t-m.b;
  const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':'Óbitos por causas naturais por grupo e ano'});
  const y1=1800000;const y=v=>m.t+h-v/y1*h;const band=w/G.years.length;const bw=24;
  const ax=el('g',{class:'axis'},svg);
  for(let v=0;v<=y1;v+=300000){el('line',{x1:m.l,x2:m.l+w,y1:y(v),y2:y(v),class:v===0?'base':''},ax);txt(m.l-10,y(v)+4,v?fmt1.format(v/1e6).replace('.',',')+' mi':'0','',{'text-anchor':'end'},ax);}
  G.years.forEach((yr,i)=>txt(m.l+band*(i+.5),H-14,yr,'',{'text-anchor':'middle'},ax));
  G.years.forEach((yr,i)=>{let acc=0;const cx=m.l+band*(i+.5);const total=keys.reduce((s,k)=>s+G[k[0]][i],0);
    keys.forEach(([k,c,l],ki)=>{const v=G[k][i];if(!v)return;const yb=y(acc),yt=y(acc+v);const hh=yb-yt;const isTop=ki===keys.length-1||keys.slice(ki+1).every(kk=>!G[kk[0]][i]);
      const gapTop = 1, gapBot = (acc===0?0:1);
      const r=el('rect',{x:cx-bw/2,y:yt+gapTop,width:bw,height:Math.max(0,hh-gapTop-gapBot),fill:col(c),class:'bar',tabindex:0,role:'img','aria-label':`${yr} ${l}: ${fmt.format(v)}`},svg);
      const show=(px,py)=>showTip(tipRows(yr+' · '+l,[{label:'óbitos',value:fmt.format(v),color:col(c)},{label:'participação',value:fmt1.format(v/total*100)+'%'},{label:'total natural',value:fmt.format(total)}]),px,py);
      r.addEventListener('pointermove',e=>show(e.clientX,e.clientY));r.addEventListener('pointerleave',hideTip);r.addEventListener('focus',()=>{const b=r.getBoundingClientRect();show(b.left+b.width/2,b.top);});r.addEventListener('blur',hideTip);
      acc+=v;});
    txt(cx,y(total)-8,mil(total),'dl strong',{'text-anchor':'middle'},svg);
    // side labels for the two series the section is about
    const cv=G.cardio[i], rv=G.resp[i];
    const yc=y(G.covid[i]+cv/2), yr2=y(G.covid[i]+cv+rv/2);
    txt(cx+bw/2+8,yc+4,mil(cv),'dl',{},svg);
    txt(cx+bw/2+8,yr2+4,mil(rv),'dl',{},svg);
    if(G.covid[i]>50000) txt(cx+bw/2+8,y(G.covid[i]/2)+4,mil(G.covid[i]),'dl',{},svg);
  });
  document.getElementById('chartC').appendChild(svg);
  const b=G.years.indexOf(2019);
  table(document.getElementById('tableC'),['Ano','Total natural','Covid','Cardiovascular','vs 2019','Respiratórias','vs 2019','Septicemia','vs 2019','Outras e indet.','vs 2019'],G.years.map((yr,i)=>{const tot=keys.reduce((s,k)=>s+G[k[0]][i],0);const d=(k)=>i===b?'':(G[k][i]-G[k][b]>0?'+':'')+fmt.format(G[k][i]-G[k][b]);return [yr,fmt.format(tot),fmt.format(G.covid[i]),fmt.format(G.cardio[i]),d('cardio'),fmt.format(G.resp[i]),d('resp'),fmt.format(G.sepsis[i]),d('sepsis'),fmt.format(G.others[i]),d('others')];}));
})();

/* Chart D: small multiples by age band, ordinal ramp for years */
(function(){
  const R=DATA.rates;const yrs=[2019,2020,2021,2022];const ramp=['--o1','--o2','--o3','--o4'];
  const filt=document.getElementById('filtersD'),leg=document.getElementById('legendD'),grid=document.getElementById('chartD');
  leg.replaceChildren(...yrs.map((y,i)=>{const s=document.createElement('span');const sw=document.createElement('i');sw.className='sw';sw.style.background=col(ramp[i]);s.append(sw,document.createTextNode(String(y)));return s;}));
  let current='cardio';
  Object.keys(R).forEach(k=>{const b=document.createElement('button');b.type='button';b.textContent=R[k].label;b.setAttribute('aria-pressed',k===current?'true':'false');b.addEventListener('click',()=>{current=k;[...filt.children].forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));render();});filt.appendChild(b);});
  function render(){
    const set=R[current];grid.replaceChildren();
    set.bands.forEach(bd=>{const W=300,H=170,m={t:30,r:12,b:26,l:44};const w=W-m.l-m.r,h=H-m.t-m.b;
      const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,class:'mini',role:'img','aria-label':set.label+' '+bd.label});
      const mx=Math.max(...bd.values);const nice=Math.pow(10,Math.floor(Math.log10(mx)));const y1=Math.ceil(mx/nice*1.15*2)/2*nice;const y=v=>m.t+h-v/y1*h;
      const ax=el('g',{class:'axis'},svg);
      [0,y1/2,y1].forEach(v=>{el('line',{x1:m.l,x2:m.l+w,y1:y(v),y2:y(v),class:v===0?'base':''},ax);txt(m.l-6,y(v)+4,fmt1.format(v),'',{'text-anchor':'end'},ax);});
      txt(m.l,16,bd.label,'panel-title',{},svg);
      const ch=pct(bd.values[3],bd.values[0]);
      txt(W-m.r,16,sgn(ch)+' até 2022','dl strong',{'text-anchor':'end'},svg);
      const band=w/4,bw=22;
      bd.values.forEach((v,i)=>{const cx=m.l+band*(i+.5);const top=y(v);
        const p=el('path',{d:`M${cx-bw/2},${y(0)} L${cx-bw/2},${top+4} Q${cx-bw/2},${top} ${cx-bw/2+4},${top} L${cx+bw/2-4},${top} Q${cx+bw/2},${top} ${cx+bw/2},${top+4} L${cx+bw/2},${y(0)} Z`,fill:col(ramp[i]),class:'bar',tabindex:0,role:'img','aria-label':`${bd.label} ${yrs[i]}: ${fmt1.format(v)} por 100 mil`},svg);
        txt(cx,H-8,yrs[i],'',{'text-anchor':'middle',class:'axis'},svg).style.fill=col('--muted');
        const n=DATA.counts[current][bd.band][i];
        const show=(px,py)=>showTip(tipRows(bd.label+' · '+yrs[i],[{label:'por 100 mil',value:fmt1.format(v),color:col(ramp[i])},{label:'óbitos',value:fmt.format(n)},{label:'vs 2019',value:i?sgn(pct(v,bd.values[0])):'—'}]),px,py);
        p.addEventListener('pointermove',e=>show(e.clientX,e.clientY));p.addEventListener('pointerleave',hideTip);p.addEventListener('focus',()=>{const b=p.getBoundingClientRect();show(b.left+b.width/2,b.top);});p.addEventListener('blur',hideTip);
      });
      grid.appendChild(svg);});
    table(document.getElementById('tableD'),['Faixa etária','2019','2020','2021','2022','Variação 2019 a 2022','Óbitos 2019','Óbitos 2022'],set.bands.map(bd=>[bd.label,...bd.values.map(v=>fmt1.format(v)),sgn(pct(bd.values[3],bd.values[0])),fmt.format(DATA.counts[current][bd.band][0]),fmt.format(DATA.counts[current][bd.band][3])]));
  }
  render();
})();
</script>
'''
open("excesso-mortes-brasil.html","w").write(html.replace("__DATA__", data_js))
print("written", len(html)+len(data_js), "bytes")
