# -*- coding: utf-8 -*-
"""Agrega o microdado do SIM (colunas ANO, DTOBITO, IDADE, SEXO, CAUSABAS) em
contagens por ano, mês, faixa etária, sexo e grupo de causa (CID-10)."""
import pandas as pd, numpy as np, sys, re
src = sys.argv[1] if len(sys.argv)>1 else "/home/user/simdata/sim_slim.parquet"
out = sys.argv[2] if len(sys.argv)>2 else "dados/sim_agregado_2008_2023.csv"
df = pd.read_parquet(src)
df["ANO"] = pd.to_numeric(df["ANO"], errors="coerce").astype("Int64")
d = pd.to_datetime(df["DTOBITO"], errors="coerce")
df["mes"] = d.dt.month.astype("Int64")
# idade SIM: 1=min,2=h,3=meses,4=anos(00-99),5=anos(100+),9/None=ignorada
s = df["IDADE"].astype("string").str.strip()
unit = s.str[0]; val = pd.to_numeric(s.str[1:], errors="coerce")
age = pd.Series(np.nan, index=df.index)
age[unit.isin(["0","1","2","3"])] = 0
age[unit=="4"] = val[unit=="4"]
age[unit=="5"] = 100 + val[unit=="5"]
bins = [-1,9,19,29,39,49,59,69,79,200]
labels = ["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"]
df["faixa"] = pd.cut(age, bins=bins, labels=labels).astype("string").fillna("ignorada")
df["sexo"] = df["SEXO"].astype("string").str[:1].str.upper().map({"M":"M","F":"F"}).fillna("I")
c = df["CAUSABAS"].astype("string").str.upper().str.strip()
c3 = c.str[:3]
letter = c.str[0]; num = pd.to_numeric(c.str[1:3], errors="coerce")
def between(l, a, b):  # ICD-10 range within one letter
    return (letter==l) & (num>=a) & (num<=b)
grp = pd.Series("outras", index=df.index, dtype="string")
# capítulos principais (ordem importa: o último que casar prevalece)
grp[letter.isin(list("VWXY"))] = "externas"
grp[letter=="C"] = "neoplasias"
grp[between("D",0,48)] = "neoplasias"
grp[letter=="I"] = "circulatorio"
grp[letter=="J"] = "respiratorio"
grp[letter=="E"] = "endocrino_diabetes"
grp[letter.isin(["A","B"])] = "infecciosas"
grp[letter=="R"] = "mal_definidas"
grp[letter=="K"] = "digestivo"
grp[letter=="N"] = "geniturinario"
grp[letter.isin(["F","G"])] = "neuro_mentais"
grp[(c3=="B34") & (c.str[3]=="2")] = "covid"
grp[c3.isin(["U07","U09","U10"])] = "covid"
df["grupo"] = grp
# subgrupos de interesse
sub = pd.Series("", index=df.index, dtype="string")
sub[between("I",21,22)] = "infarto_agudo"
sub[between("I",20,25) & ~between("I",21,22)] = "isquemica_outras"
sub[between("I",60,69)] = "cerebrovascular"
sub[c3=="I26"] = "embolia_pulmonar"
sub[between("I",80,82)] = "trombose_venosa"
sub[between("I",30,52) & ~between("I",30,33) & (c3!="I26")] = "cardio_outras_i30_i52"
sub[c3.isin(["I40","I41","I51"]) ] = "miocardite_cardiomiopatia_i40_i41_i51"
sub[between("I",42,43)] = "cardiomiopatia_i42_i43"
sub[between("I",46,49)] = "parada_arritmia_i46_i49"
sub[c3=="I50"] = "insuf_cardiaca_i50"
sub[c3=="I10"] = "hipertensao_i10"
sub[between("C",0,97)] = "cancer_c00_c97"
sub[c3=="C34"] = "cancer_pulmao_c34"
sub[c3=="C50"] = "cancer_mama_c50"
sub[c3=="C61"] = "cancer_prostata_c61"
sub[between("C",18,21)] = "cancer_colorretal_c18_c21"
sub[between("C",81,96)] = "cancer_hematologico_c81_c96"
sub[c3=="C25"] = "cancer_pancreas_c25"
sub[c3=="C16"] = "cancer_estomago_c16"
sub[c3=="G30"] = "alzheimer_g30"
sub[c3.isin(["E10","E11","E12","E13","E14"])] = "diabetes_e10_e14"
sub[between("J",12,18)] = "pneumonia_j12_j18"
sub[c3.isin(["A40","A41"])] = "sepse_a40_a41"
df["subgrupo"] = sub
agg = df.groupby(["ANO","mes","faixa","sexo","grupo","subgrupo"], observed=True).size().reset_index(name="obitos")
agg.to_csv(out, index=False)
print("saved", out, agg.shape)
print(agg.groupby("ANO")["obitos"].sum().tail(12))
print(agg[agg.ANO==2019].groupby("grupo")["obitos"].sum().sort_values(ascending=False))
