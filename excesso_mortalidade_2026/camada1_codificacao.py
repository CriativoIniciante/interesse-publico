# -*- coding: utf-8 -*-
"""Camada 1, frente A: parada cardiaca (I46-I49) versus codificacao. Investigacao, UF, R99, e serie estadual."""
import duckdb, pandas as pd
con = duckdb.connect()
src = "/home/user/simdata/sim_consolidado.parquet"
base = f"""
WITH b AS (
  SELECT CAST(substr(DTOBITO,5,4) AS INT) ano, CAST(substr(DTOBITO,3,2) AS INT) mes,
         substr(CAST(CODMUNRES AS VARCHAR),1,2) uf, CAUSABAS c, CAST(TPPOS AS VARCHAR) TPPOS, DTINVESTIG, CAST(LOCOCOR AS VARCHAR) LOCOCOR, CAST(IDADE AS VARCHAR) IDADE
  FROM read_parquet('{src}') WHERE TIPOBITO <> 'Fetal' AND DTOBITO IS NOT NULL AND length(DTOBITO)=8)
"""
# 1) investigacao dos obitos I46-I49 e R99 por ano
q1 = base + """
SELECT ano,
  SUM(CASE WHEN c BETWEEN 'I46' AND 'I499' THEN 1 ELSE 0 END) parada,
  SUM(CASE WHEN c BETWEEN 'I46' AND 'I499' AND (TPPOS='S' OR DTINVESTIG IS NOT NULL) THEN 1 ELSE 0 END) parada_investigada,
  SUM(CASE WHEN c LIKE 'R%' THEN 1 ELSE 0 END) r_codes,
  SUM(CASE WHEN c LIKE 'R%' AND (TPPOS='S' OR DTINVESTIG IS NOT NULL) THEN 1 ELSE 0 END) r_investigado,
  SUM(CASE WHEN c BETWEEN 'I46' AND 'I499' AND LOCOCOR='3' THEN 1 ELSE 0 END) parada_domicilio,
  COUNT(*) total
FROM b WHERE ano BETWEEN 2016 AND 2024 GROUP BY ano ORDER BY ano"""
d1 = con.execute(q1).df()
d1["parada_inv_pct"] = (d1.parada_investigada/d1.parada*100).round(1)
d1["r_inv_pct"] = (d1.r_investigado/d1.r_codes*100).round(1)
d1["parada_mais_r"] = d1.parada + d1.r_codes
print("=== investigacao (TPPOS ou data de investigacao) por ano"); print(d1[["ano","parada","parada_inv_pct","r_codes","r_inv_pct","parada_mais_r"]].to_string(index=False))
# 2) por UF: variacao 2019->2024 da parada e do R, e correlacao
q2 = base + """
SELECT uf, ano,
  SUM(CASE WHEN c BETWEEN 'I46' AND 'I499' THEN 1 ELSE 0 END) parada,
  SUM(CASE WHEN c LIKE 'R%' THEN 1 ELSE 0 END) r_codes,
  SUM(CASE WHEN c BETWEEN 'I46' AND 'I499' AND (TPPOS='S' OR DTINVESTIG IS NOT NULL) THEN 1 ELSE 0 END) parada_inv,
  SUM(CASE WHEN c IN ('U071','U072','U099','U109','B342') OR c LIKE 'U07%' THEN 1 ELSE 0 END) covid,
  COUNT(*) total
FROM b WHERE ano BETWEEN 2016 AND 2024 AND uf BETWEEN '11' AND '53' GROUP BY uf, ano"""
d2 = con.execute(q2).df()
d2.to_csv("dados/camada1_uf_ano_parada_r_covid.csv", index=False)
p = d2.pivot(index="uf", columns="ano", values="parada"); r = d2.pivot(index="uf", columns="ano", values="r_codes"); t = d2.pivot(index="uf", columns="ano", values="total")
ufn = {"11":"RO","12":"AC","13":"AM","14":"RR","15":"PA","16":"AP","17":"TO","21":"MA","22":"PI","23":"CE","24":"RN","25":"PB","26":"PE","27":"AL","28":"SE","29":"BA","31":"MG","32":"ES","33":"RJ","35":"SP","41":"PR","42":"SC","43":"RS","50":"MS","51":"MT","52":"GO","53":"DF"}
out = pd.DataFrame({"UF":[ufn[u] for u in p.index],
  "parada_2019":p[2019].values, "parada_2024":p[2024].values,
  "parada_var":((p[2024]/p[2019]-1)*100).round(0).values,
  "parada_pct_total_2019":(p[2019]/t[2019]*100).round(2).values, "parada_pct_total_2024":(p[2024]/t[2024]*100).round(2).values,
  "r_pct_total_2019":(r[2019]/t[2019]*100).round(1).values, "r_pct_total_2024":(r[2024]/t[2024]*100).round(1).values})
out["r_var_pp"] = (out.r_pct_total_2024-out.r_pct_total_2019).round(1)
out["parada_var_pp"] = (out.parada_pct_total_2024-out.parada_pct_total_2019).round(2)
print("=== por UF: parada como % de todos os obitos, e R como %"); print(out.sort_values("parada_var", ascending=False).to_string(index=False))
print("correlacao entre variacao (pp) da parada e variacao (pp) do R por UF: %.2f" % out.parada_var_pp.corr(out.r_var_pp))
# 3) serie mensal por UF de parada 30-59 e covid, para o painel
q3 = base + """
SELECT uf, ano, mes,
  SUM(CASE WHEN c BETWEEN 'I46' AND 'I499' AND substr(IDADE,1,1)='4' AND CAST(substr(IDADE,2,2) AS INT) BETWEEN 30 AND 59 THEN 1 ELSE 0 END) parada_30_59,
  SUM(CASE WHEN c BETWEEN 'I46' AND 'I499' AND ((substr(IDADE,1,1)='4' AND CAST(substr(IDADE,2,2) AS INT)>=60) OR substr(IDADE,1,1)='5') THEN 1 ELSE 0 END) parada_60mais,
  SUM(CASE WHEN c = 'I26' OR c LIKE 'I26%' THEN 1 ELSE 0 END) embolia,
  SUM(CASE WHEN c IN ('U071','U072','U099','U109','B342') OR c LIKE 'U07%' THEN 1 ELSE 0 END) covid,
  COUNT(*) total
FROM b WHERE ano BETWEEN 2018 AND 2024 AND uf BETWEEN '11' AND '53' GROUP BY uf, ano, mes ORDER BY uf, ano, mes"""
d3 = con.execute(q3).df(); d3["UF"] = d3.uf.map(ufn); d3.to_csv("dados/camada1_uf_mensal_parada_embolia_covid.csv", index=False)
print("serie mensal por UF salva:", d3.shape)
