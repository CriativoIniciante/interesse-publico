# -*- coding: utf-8 -*-
"""Rodada 2: séries 2013-2024 do SIM por causa e idade, taxas por 100 mil e padronizadas por idade."""
import pandas as pd, numpy as np, json
a = pd.read_csv("dados/sim_agregado_2008_2023.csv"); b = pd.read_csv("dados/sim_agregado_consolidado_2016_2024.csv")
sim = pd.concat([a[(a.ano>=2013)&(a.ano<=2023)], b[b.ano==2024]], ignore_index=True)
sim.to_csv("dados/sim_agregado_2013_2024.csv", index=False)
pop = pd.read_csv("dados/populacao_brasil_faixa_etaria_2000_2024.csv", index_col=0); pop.index=pop.index.astype(int)
band = {"From 0 to 4 years":"0-9","From 5 to 9 years":"0-9","From 10 to 14 years":"10-19","From 15 to 19 years":"10-19","From 20 to 24 years":"20-29","From 25 to 29 years":"20-29","From 30 to 34 years":"30-39","From 35 to 39 years":"30-39","From 40 to 44 years":"40-49","From 45 to 49 years":"40-49","From 50 to 54 years":"50-59","From 55 to 59 years":"50-59","From 60 to 64 years":"60-69","From 65 to 69 years":"60-69","From 70 to 74 years":"70-79","From 75 to 79 years":"70-79","From 80 years or more":"80+"}
pb = pop.drop(columns=["Total"]).T; pb["band"]=[band[i] for i in pb.index]; pb = pb.groupby("band").sum().T; pb.index=pb.index.astype(int)
bands = ["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"]
std = pb.loc[2019, bands]; std = std/std.sum()   # população padrão: Brasil 2019
years = list(range(2013,2025))
def rates(sub):  # sub: df with ano, faixa, obitos -> age-specific rates and ASR
    t = sub.groupby(["ano","faixa"]).obitos.sum().unstack().reindex(index=years, columns=bands).fillna(0)
    r = t / pb.loc[years, bands] * 1e5
    asr = (r * std).sum(axis=1)
    return t, r, asr
out = {"years": years, "bands": bands, "pop": pb.loc[years, bands].astype(int).to_dict(orient="list")}
# 1) all-cause and groups by year
tot = sim.groupby("ano").obitos.sum().reindex(years)
out["all"] = {"count": tot.astype(int).tolist()}
_, r, asr = rates(sim); out["all"]["asr"] = asr.round(1).tolist(); out["all"]["rate_by_band"] = r.round(1).to_dict(orient="list")
grp_names = {"circulatorio":"Circulatório (I00-I99)","neoplasias":"Neoplasias (C00-D48)","respiratorio":"Respiratório (J00-J99)","externas":"Causas externas (V01-Y98)","covid":"Covid-19 (U07, B34.2)","endocrino_diabetes":"Endócrinas e diabetes (E00-E90)","infecciosas":"Infecciosas (A00-B99)","mal_definidas":"Mal definidas (R00-R99)","digestivo":"Digestivo (K00-K93)","neuro_mentais":"Neurológicas e mentais (F, G)","geniturinario":"Geniturinário (N00-N99)","outras":"Demais capítulos"}
out["groups"] = {}
for g,name in grp_names.items():
    s = sim[sim.grupo==g]; t,r,asr = rates(s)
    out["groups"][g] = {"label":name, "count": t.sum(axis=1).astype(int).tolist(), "asr": asr.round(1).tolist(), "rate_by_band": r.round(1).to_dict(orient="list")}
sub_names = {"infarto_agudo_i21_i22":"Infarto agudo (I21-I22)","cerebrovascular_i60_i69":"AVC e cerebrovasculares (I60-I69)","embolia_pulmonar_i26":"Embolia pulmonar (I26)","trombose_venosa_i80_i82":"Trombose venosa (I80-I82)","miocardite_i40_i41":"Miocardite (I40-I41)","cardiomiopatia_i42_i43":"Cardiomiopatias (I42-I43)","parada_arritmia_i46_i49":"Parada cardíaca e arritmias (I46-I49)","insuf_cardiaca_i50":"Insuficiência cardíaca (I50)","hipertensao_i10":"Hipertensão (I10)","cancer_pulmao_c34":"Câncer de pulmão (C34)","cancer_mama_c50":"Câncer de mama (C50)","cancer_prostata_c61":"Câncer de próstata (C61)","cancer_colorretal_c18_c21":"Câncer colorretal (C18-C21)","cancer_hematologico_c81_c96":"Cânceres hematológicos (C81-C96)","cancer_pancreas_c25":"Câncer de pâncreas (C25)","alzheimer_g30":"Alzheimer (G30)","diabetes_e10_e14":"Diabetes (E10-E14)","pneumonia_j12_j18":"Pneumonia (J12-J18)","sepse_a40_a41":"Sepse (A40-A41)"}
out["subs"] = {}
for g,name in sub_names.items():
    s = sim[sim.subgrupo==g]; t,r,asr = rates(s)
    out["subs"][g] = {"label":name, "count": t.sum(axis=1).astype(int).tolist(), "asr": asr.round(2).tolist(), "rate_by_band": r.round(2).to_dict(orient="list")}
# cancer total C00-C97 = all cancer subs (malignant) 
canc = sim[sim.subgrupo.str.startswith("cancer_", na=False)]; t,r,asr = rates(canc)
out["subs"]["cancer_c00_c97"] = {"label":"Câncer, todos (C00-C97)","count": t.sum(axis=1).astype(int).tolist(),"asr": asr.round(2).tolist(),"rate_by_band": r.round(2).to_dict(orient="list")}
# 2) monthly series 2018-2024 for selected groups by band (counts) + monthly all-cause + covid
m = sim[sim.ano>=2018].copy(); m["ym"] = m.ano.astype(str)+"-"+m.mes.astype(int).astype(str).str.zfill(2)
months = sorted(m.ym.unique())
out["months"] = months
def monthly(sub, by_band=False):
    if by_band:
        t = sub.groupby(["ym","faixa"]).obitos.sum().unstack().reindex(index=months, columns=bands).fillna(0).astype(int)
        return t.to_dict(orient="list")
    return sub.groupby("ym").obitos.sum().reindex(months).fillna(0).astype(int).tolist()
out["monthly"] = {"all": monthly(m), "covid": monthly(m[m.grupo=="covid"]), "circulatorio": monthly(m[m.grupo=="circulatorio"], True),
  "infarto": monthly(m[m.subgrupo=="infarto_agudo_i21_i22"], True), "avc": monthly(m[m.subgrupo=="cerebrovascular_i60_i69"], True),
  "embolia": monthly(m[m.subgrupo=="embolia_pulmonar_i26"], True), "miocardite": monthly(m[m.subgrupo=="miocardite_i40_i41"], True),
  "parada": monthly(m[m.subgrupo=="parada_arritmia_i46_i49"], True), "neoplasias": monthly(m[m.grupo=="neoplasias"], True), "mal_definidas": monthly(m[m.grupo=="mal_definidas"], True)}
json.dump(out, open("dados/resumo_v2.json","w"), ensure_ascii=False)
pd.set_option("display.width",250); pd.set_option("display.max_columns",30)
print("=== all-cause count and ASR"); print(pd.DataFrame({"count":tot.astype(int),"asr":out["all"]["asr"]}))
print("=== groups ASR (per 100k, std 2019)"); print(pd.DataFrame({g:out["groups"][g]["asr"] for g in grp_names}, index=years).round(1))
print("=== groups counts"); print(pd.DataFrame({g:out["groups"][g]["count"] for g in grp_names}, index=years))
print("=== subs ASR"); print(pd.DataFrame({g:out["subs"][g]["asr"] for g in out["subs"]}, index=years).round(2).T)
for g in ["cancer_c00_c97","infarto_agudo_i21_i22","cerebrovascular_i60_i69","embolia_pulmonar_i26","trombose_venosa_i80_i82","miocardite_i40_i41","parada_arritmia_i46_i49"]:
    print("=== rate by band:", g); print(pd.DataFrame(out["subs"][g]["rate_by_band"], index=years).round(2))
print("=== circulatorio rate by band"); print(pd.DataFrame(out["groups"]["circulatorio"]["rate_by_band"], index=years).round(1))
print("=== mal definidas rate by band"); print(pd.DataFrame(out["groups"]["mal_definidas"]["rate_by_band"], index=years).round(1))

# ---- complementos para a página: comparações por período e variações
out2 = json.load(open("dados/resumo_v2.json"))
def chg(a,b): return None if not a else round((b/a-1)*100,1)
comp = {}
for key, coll in [("groups", out2["groups"]), ("subs", out2["subs"])]:
    comp[key] = {}
    for g, v in coll.items():
        asr = v["asr"]; yi = {y:i for i,y in enumerate(years)}
        comp[key][g] = {"label": v["label"], "asr_2015": asr[yi[2015]], "asr_2019": asr[yi[2019]], "asr_2021": asr[yi[2021]], "asr_2022": asr[yi[2022]], "asr_2024": asr[yi[2024]],
                        "chg_2015_2019": chg(asr[yi[2015]], asr[yi[2019]]), "chg_2019_2024": chg(asr[yi[2019]], asr[yi[2024]]), "chg_2019_2021": chg(asr[yi[2019]], asr[yi[2021]]),
                        "count_2019": v["count"][yi[2019]], "count_2024": v["count"][yi[2024]],
                        "band_chg_2019_2024": {b: chg(v["rate_by_band"][b][yi[2019]], v["rate_by_band"][b][yi[2024]]) for b in bands},
                        "band_chg_2019_2022": {b: chg(v["rate_by_band"][b][yi[2019]], v["rate_by_band"][b][yi[2022]]) for b in bands}}
out2["comp"] = comp
# tendência pré-pandemia da taxa padronizada geral (2013-2019) projetada
asr_all = np.array(out2["all"]["asr"]); yrs = np.array(years)
s,i = np.polyfit(yrs[:7], asr_all[:7], 1); out2["all"]["asr_trend"] = [round(s*y+i,1) for y in years]
out2["all"]["asr_excess_pct"] = [round((a/(s*y+i)-1)*100,1) for a,y in zip(asr_all, years)]
json.dump(out2, open("dados/resumo_v2.json","w"), ensure_ascii=False)
print("=== ASR all vs trend"); print(pd.DataFrame({"asr":out2["all"]["asr"],"trend":out2["all"]["asr_trend"],"exc%":out2["all"]["asr_excess_pct"]}, index=years))
print("=== chg 2019->2024 groups"); print(pd.DataFrame({g:[c["chg_2019_2024"], c["chg_2019_2021"], c["chg_2015_2019"]] for g,c in comp["groups"].items()}, index=["19-24","19-21","15-19"]).T)
print("=== chg 2019->2024 subs"); print(pd.DataFrame({g:[c["chg_2019_2024"], c["chg_2019_2021"], c["chg_2015_2019"], c["count_2019"], c["count_2024"]] for g,c in comp["subs"].items()}, index=["19-24","19-21","15-19","n2019","n2024"]).T)
mo = out2["monthly"]; import pandas as pd
mm = pd.DataFrame({"all":mo["all"],"covid":mo["covid"]}, index=out2["months"])
for k in ["parada","embolia","infarto","miocardite"]:
    mm[k+"_30_59"] = np.array(mo[k]["30-39"])+np.array(mo[k]["40-49"])+np.array(mo[k]["50-59"])
    mm[k+"_60+"] = np.array(mo[k]["60-69"])+np.array(mo[k]["70-79"])+np.array(mo[k]["80+"])
print("=== monthly 2020-2022 selected"); print(mm.loc["2020-01":"2022-12"].to_string())
