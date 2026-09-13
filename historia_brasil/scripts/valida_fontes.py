#!/usr/bin/env python3
"""Valida historia-brasil/fontes.yaml.

Regras (CONTRIBUINDO.md, seção 6): campos obrigatórios, ids únicos,
`verificado` booleano, `tipo` na lista permitida, feeds como lista de URLs.
Uso: python3 valida_fontes.py [caminho]. Sai com 1 se houver erro.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("erro: pyyaml ausente (pip install pyyaml)")
    sys.exit(2)

TIPOS = {
    "agencia_publica", "grande_veiculo", "independente", "verificador",
    "oficial", "arquivo_terceiro", "retrospectivo", "modelo",
}
OBRIGATORIOS = {"id", "nome", "tipo", "feeds", "verificado"}
ID_RE = re.compile(r"^[a-z0-9_]+$")
URL_RE = re.compile(r"^https?://\S+$")


def valida(caminho: Path) -> list[str]:
    erros: list[str] = []
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    if not isinstance(dados, dict) or "fontes" not in dados:
        return ["raiz precisa ser um mapa com a chave 'fontes'"]
    for chave in ("versao", "testado_em"):
        if chave not in dados:
            erros.append(f"falta a chave de topo '{chave}'")
    fontes = dados["fontes"]
    if not isinstance(fontes, list) or not fontes:
        return erros + ["'fontes' precisa ser uma lista não vazia"]

    vistos: set[str] = set()
    for i, f in enumerate(fontes):
        rotulo = f"fontes[{i}]" + (f" ({f.get('id')})" if isinstance(f, dict) and f.get("id") else "")
        if not isinstance(f, dict):
            erros.append(f"{rotulo}: precisa ser um mapa")
            continue
        faltam = OBRIGATORIOS - set(f)
        if faltam:
            erros.append(f"{rotulo}: faltam campos {sorted(faltam)}")
        fid = f.get("id")
        if isinstance(fid, str):
            if not ID_RE.match(fid):
                erros.append(f"{rotulo}: id deve ter só a-z, 0-9 e _")
            if fid in vistos:
                erros.append(f"{rotulo}: id repetido")
            vistos.add(fid)
        if f.get("tipo") not in TIPOS:
            erros.append(f"{rotulo}: tipo '{f.get('tipo')}' fora da lista {sorted(TIPOS)}")
        if not isinstance(f.get("verificado"), bool):
            erros.append(f"{rotulo}: 'verificado' deve ser true ou false")
        feeds = f.get("feeds")
        if not isinstance(feeds, list) or not feeds:
            erros.append(f"{rotulo}: 'feeds' deve ser lista não vazia")
        else:
            for u in feeds:
                if not isinstance(u, str) or not URL_RE.match(u):
                    erros.append(f"{rotulo}: feed inválido: {u!r}")
        if f.get("verificado") is True and not f.get("teste"):
            erros.append(f"{rotulo}: fonte verificada precisa do campo 'teste' com o resultado")
    return erros


def main() -> int:
    caminho = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "fontes.yaml"
    erros = valida(caminho)
    if erros:
        print(f"{caminho}: {len(erros)} erro(s)")
        for e in erros:
            print("  -", e)
        return 1
    n = len(yaml.safe_load(caminho.read_text(encoding="utf-8"))["fontes"])
    print(f"{caminho}: ok, {n} fontes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
