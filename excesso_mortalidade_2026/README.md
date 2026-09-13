# Caderno de investigação: mortalidade no Brasil

Rodada 2 (setembro de 2026), substitui a rodada 1. Pergunta: a mortalidade geral subiu na pandemia? Quanto foi covid? O que aconteceu com as outras causas e com a mortalidade cardiovascular por idade?

## Arquivos

- `excesso-mortes-brasil.html`: relatório com gráficos interativos. Gerado por `build_page.py`.
- `build_page.py`: monta a página a partir de `dados/resumo_v1.json`.
- `dados/excesso_mortalidade_brasil_2015_2023.csv`: mortes anuais (SIM via World Mortality Dataset), população, taxa bruta, três modelos de esperado e excesso.
- `dados/populacao_brasil_faixa_etaria_2000_2024.csv`: população por faixa etária, série revisada DATASUS 2024, somada para o Brasil (pacote brpop).
- `dados/populacao_ufrn_projecao_2010_2030.csv`: projeção UFRN por faixa etária, usada para 2025 em diante.
- `dados/registro_civil_causas_anual_2018_2022.csv`: óbitos por causas naturais por grupo, Portal da Transparência do Registro Civil (projeto brazil-civil-registry-data).
- `dados/resumo_v1.json`: agregados usados pela página.

## Fontes primárias

- SIM, Ministério da Saúde, via https://github.com/akarlinsky/world_mortality (arquivo world_mortality.csv).
- População: https://github.com/rfsaldanha/brpop (data-raw, séries DATASUS 2024 e UFRN).
- Registro Civil: https://github.com/capyvara/brazil-civil-registry-data.

## O que falta para a rodada 2

Tabelas do TabNet (SIM) por ano, capítulo CID-10 e faixa etária, 2013 a 2023, mais óbitos preliminares 2024 e 2025. Instruções na seção 6 do relatório. Colocar os CSV em `dados/tabnet/`.

## Rodada 2

Com a rede liberada, o caderno passou a usar o microdado do SIM de 2013 a 2024 por causa básica CID-10 e idade, e o Registro Civil até agosto de 2026.

- `agrega_sim_duckdb.py`: agrega o microdado (parquet ou CSV do OpenDataSUS) em contagens por ano, mês, faixa etária, sexo, grupo e subgrupo CID-10. Uso: `python3 agrega_sim_duckdb.py <arquivo> <saida.csv> <jpvmm|consolidado|csv24>`.
- `analise_rodada2.py`: taxas por faixa etária e padronizadas por idade (padrão Brasil 2019), séries mensais, comparações; gera `dados/resumo_v2.json`.
- `build_page_v2.py`: gera o relatório `excesso-mortes-brasil.html`.
- `dados/sim_agregado_2013_2024.csv`: agregado usado na análise (2013 a 2023 da cópia jpvmm/dataSUS_deaths, 2024 da cópia jgchaicoski/datasus_sim).
- `dados/sim_agregado_2008_2023.csv`, `dados/sim_agregado_consolidado_2016_2024.csv`, `dados/sim_agregado_2024_csv.csv`: agregados de cada cópia, para conferência.
- `dados/registro_civil_obitos_mensal_2015_2026.csv`: registros de óbito por mês, API do Portal da Transparência.
- `dados/registro_civil_causas_naturais_mensal_2023_2026.csv`: causas naturais por grupo e mês, mesma API.

Camada 1: resultados em `camada1_resultados.md`, scripts `camada1_codificacao.py`, dados em `dados/camada1_*.csv`.

Camada 2: guia em `camada2_guia.md`, simulação do desenho em `camada2_sccs_simulacao.py`.

Validação: os totais anuais das cópias coincidem com os oficiais do SIM de 2013 a 2020 e 2022; 2021 e 2023 são versões anteriores do arquivo, 1,2% e 1,3% abaixo do final; 2024 é preliminar. Os microdados brutos (1,2 GB) não estão no repositório; as fontes são https://huggingface.co/datasets/jpvmm/dataSUS_deaths e https://huggingface.co/datasets/jgchaicoski/datasus_sim.
