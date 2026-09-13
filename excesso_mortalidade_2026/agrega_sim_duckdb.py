# -*- coding: utf-8 -*-
"""Agrega microdados do SIM em contagens por ano, mês, faixa etária, sexo, grupo e subgrupo CID-10, usando DuckDB."""
import duckdb, sys
src = sys.argv[1]; out = sys.argv[2]; kind = sys.argv[3] if len(sys.argv)>3 else "jpvmm"
con = duckdb.connect(); con.execute("PRAGMA threads=4; PRAGMA memory_limit='6GB';")
if kind == "jpvmm":
    base = f"""SELECT CAST(ANO AS INTEGER) AS ano, EXTRACT(month FROM CAST(DTOBITO AS DATE)) AS mes, IDADE AS idade, SEXO AS sexo_raw, CAUSABAS AS cb FROM read_parquet('{src}')"""
elif kind == "consolidado":
    base = f"""SELECT CAST(substr(DTOBITO,5,4) AS INTEGER) AS ano, CAST(substr(DTOBITO,3,2) AS INTEGER) AS mes, IDADE AS idade, SEXO AS sexo_raw, CAUSABAS AS cb FROM read_parquet('{src}')"""
elif kind == "csv24":
    base = f"""SELECT CAST(substr(DTOBITO,5,4) AS INTEGER) AS ano, CAST(substr(DTOBITO,3,2) AS INTEGER) AS mes, IDADE AS idade, SEXO AS sexo_raw, CAUSABAS AS cb FROM read_csv('{src}', delim=';', header=true, quote='"', all_varchar=true, ignore_errors=true)"""
q = f"""
WITH b AS ({base}),
d AS (
  SELECT ano, mes,
    CASE WHEN idade IS NULL OR length(trim(idade))<3 THEN NULL
         WHEN substr(trim(idade),1,1) IN ('0','1','2','3') THEN 0
         WHEN substr(trim(idade),1,1)='4' THEN TRY_CAST(substr(trim(idade),2,2) AS INTEGER)
         WHEN substr(trim(idade),1,1)='5' THEN 100+TRY_CAST(substr(trim(idade),2,2) AS INTEGER)
         ELSE NULL END AS age,
    CASE WHEN upper(substr(sexo_raw,1,1))='M' OR sexo_raw='1' THEN 'M' WHEN upper(substr(sexo_raw,1,1))='F' OR sexo_raw='2' THEN 'F' ELSE 'I' END AS sexo,
    upper(trim(cb)) AS cb, substr(upper(trim(cb)),1,1) AS L, TRY_CAST(substr(upper(trim(cb)),2,2) AS INTEGER) AS n, substr(upper(trim(cb)),1,3) AS c3
  FROM b),
e AS (
  SELECT ano, mes, sexo,
    CASE WHEN age IS NULL THEN 'ignorada' WHEN age<=9 THEN '0-9' WHEN age<=19 THEN '10-19' WHEN age<=29 THEN '20-29' WHEN age<=39 THEN '30-39' WHEN age<=49 THEN '40-49' WHEN age<=59 THEN '50-59' WHEN age<=69 THEN '60-69' WHEN age<=79 THEN '70-79' ELSE '80+' END AS faixa,
    CASE WHEN c3 IN ('U07','U09','U10') OR cb LIKE 'B342%' THEN 'covid'
         WHEN L IN ('V','W','X','Y') THEN 'externas'
         WHEN L='C' OR (L='D' AND n<=48) THEN 'neoplasias'
         WHEN L='I' THEN 'circulatorio'
         WHEN L='J' THEN 'respiratorio'
         WHEN L='E' THEN 'endocrino_diabetes'
         WHEN L IN ('A','B') THEN 'infecciosas'
         WHEN L='R' THEN 'mal_definidas'
         WHEN L='K' THEN 'digestivo'
         WHEN L='N' THEN 'geniturinario'
         WHEN L IN ('F','G') THEN 'neuro_mentais'
         ELSE 'outras' END AS grupo,
    CASE WHEN L='I' AND n BETWEEN 21 AND 22 THEN 'infarto_agudo_i21_i22'
         WHEN L='I' AND n BETWEEN 20 AND 25 THEN 'isquemica_outras_i20_i25'
         WHEN L='I' AND n BETWEEN 60 AND 69 THEN 'cerebrovascular_i60_i69'
         WHEN c3='I26' THEN 'embolia_pulmonar_i26'
         WHEN L='I' AND n BETWEEN 80 AND 82 THEN 'trombose_venosa_i80_i82'
         WHEN c3 IN ('I40','I41') THEN 'miocardite_i40_i41'
         WHEN L='I' AND n BETWEEN 42 AND 43 THEN 'cardiomiopatia_i42_i43'
         WHEN L='I' AND n BETWEEN 46 AND 49 THEN 'parada_arritmia_i46_i49'
         WHEN c3='I50' THEN 'insuf_cardiaca_i50'
         WHEN c3='I10' THEN 'hipertensao_i10'
         WHEN c3='I51' THEN 'cardiopatia_mal_definida_i51'
         WHEN L='I' THEN 'circulatorio_outras'
         WHEN c3='C34' THEN 'cancer_pulmao_c34'
         WHEN c3='C50' THEN 'cancer_mama_c50'
         WHEN c3='C61' THEN 'cancer_prostata_c61'
         WHEN L='C' AND n BETWEEN 18 AND 21 THEN 'cancer_colorretal_c18_c21'
         WHEN L='C' AND n BETWEEN 81 AND 96 THEN 'cancer_hematologico_c81_c96'
         WHEN c3='C25' THEN 'cancer_pancreas_c25'
         WHEN c3='C16' THEN 'cancer_estomago_c16'
         WHEN L='C' AND n<=97 THEN 'cancer_outros_c00_c97'
         WHEN L='C' OR (L='D' AND n<=48) THEN 'neoplasia_in_situ_benigna_d00_d48'
         WHEN c3='G30' THEN 'alzheimer_g30'
         WHEN c3 IN ('E10','E11','E12','E13','E14') THEN 'diabetes_e10_e14'
         WHEN L='J' AND n BETWEEN 12 AND 18 THEN 'pneumonia_j12_j18'
         WHEN c3 IN ('A40','A41') THEN 'sepse_a40_a41'
         ELSE '' END AS subgrupo
  FROM d)
SELECT ano, mes, faixa, sexo, grupo, subgrupo, COUNT(*) AS obitos FROM e GROUP BY ALL ORDER BY ano, mes, faixa, sexo, grupo, subgrupo
"""
con.execute(f"COPY ({q}) TO '{out}' (HEADER, DELIMITER ',')")
print("saved", out)
print(con.execute(f"SELECT ano, SUM(obitos) FROM read_csv('{out}') GROUP BY ano ORDER BY ano").fetchdf().tail(14))
print(con.execute(f"SELECT grupo, SUM(obitos) FROM read_csv('{out}') WHERE ano=2019 GROUP BY grupo ORDER BY 2 DESC").fetchdf())
