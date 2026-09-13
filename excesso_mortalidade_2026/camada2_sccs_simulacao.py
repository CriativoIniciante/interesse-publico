# -*- coding: utf-8 -*-
"""Série de casos autocontrolada (SCCS) em 80 linhas, com dados simulados.
Cada pessoa tem: data da dose 1 e 2, data de infecção (ou nenhuma) e data do evento.
Verdade simulada: dose eleva o risco em 1,5x nos dias 1-21; infecção eleva em 4x nos dias 1-30.
O modelo deve recuperar esses números só com os casos, sem grupo controle."""
import numpy as np, pandas as pd, statsmodels.api as sm
rng = np.random.default_rng(7)
N, T = 400_000, 730                     # pessoas, dias de observação (2 anos)
IRR_DOSE, IRR_INF, W_DOSE, W_INF = 1.5, 4.0, 21, 30
base = 2e-5                             # risco diário basal (evento raro, p.ex. embolia)
d1 = rng.integers(60, 400, N); d2 = d1 + rng.integers(21, 90, N)
inf = np.where(rng.random(N) < 0.5, rng.integers(0, T, N), -1)   # metade se infecta em data aleatória
sazonal = 1 + 0.3*np.sin(2*np.pi*np.arange(T)/365)               # confundidor temporal
def rr(i, t):
    r = sazonal[t]
    if 0 < t-d1[i] <= W_DOSE or 0 < t-d2[i] <= W_DOSE: r *= IRR_DOSE
    if inf[i] >= 0 and 0 < t-inf[i] <= W_INF: r *= IRR_INF
    return r
# simula o primeiro evento de cada pessoa
events = []
for i in range(N):
    haz = base*np.array([rr(i,t) for t in range(T)])
    u = rng.random(T); hit = np.where(u < haz)[0]
    if len(hit): events.append((i, hit[0]))
print(f"casos: {len(events)} em {N} pessoas")
# tabela pessoa-período: para cada caso, divide os 730 dias em blocos com exposição constante
rows = []
for i, te in events:
    cuts = sorted(set([0, T] + [c for c in [d1[i]+1, d1[i]+W_DOSE+1, d2[i]+1, d2[i]+W_DOSE+1] + ([inf[i]+1, inf[i]+W_INF+1] if inf[i] >= 0 else []) if 0 < c < T]))
    for a, b in zip(cuts[:-1], cuts[1:]):
        t = a
        rows.append(dict(id=i, dias=b-a, dose=int(0 < t-d1[i] <= W_DOSE or 0 < t-d2[i] <= W_DOSE), infec=int(inf[i] >= 0 and 0 < t-inf[i] <= W_INF),
                         estacao=int((a % 365)//91), evento=int(a <= te < b)))
df = pd.DataFrame(rows)
# SCCS = verossimilhança condicional por pessoa: dado que a pessoa teve 1 evento, em qual período ele caiu?
# P(evento no período j) = exp(x_j b) * dias_j / soma_k exp(x_k b) * dias_k  -> efeitos fixos da pessoa cancelam
from scipy.optimize import minimize
X = pd.get_dummies(df[["dose","infec","estacao"]].astype(str), drop_first=True).astype(float)
names = list(X.columns); Xv = X.values; logt = np.log(df.dias.values); ev = df.evento.values; ids = df.id.values
def nll(b):
    eta = Xv @ b + logt
    tot = pd.Series(np.exp(eta)).groupby(ids).transform("sum").values
    return -np.sum(ev * (eta - np.log(tot)))
res = minimize(nll, np.zeros(Xv.shape[1]), method="BFGS")
H = np.linalg.inv(res.hess_inv) if False else None
# erro-padrão por Hessiana numérica
eps=1e-4; b=res.x; n=len(b); Hm=np.zeros((n,n))
for a in range(n):
    for c in range(n):
        ea=np.eye(n)[a]*eps; ec=np.eye(n)[c]*eps
        Hm[a,c]=(nll(b+ea+ec)-nll(b+ea-ec)-nll(b-ea+ec)+nll(b-ea-ec))/(4*eps*eps)
se = np.sqrt(np.diag(np.linalg.inv(Hm)))
for k, verdade in [("dose_1", IRR_DOSE), ("infec_1", IRR_INF)]:
    j = names.index(k)
    print(f"{k:8s} IRR estimado {np.exp(b[j]):.2f} (IC95% {np.exp(b[j]-1.96*se[j]):.2f} a {np.exp(b[j]+1.96*se[j]):.2f}) | verdade {verdade}")
