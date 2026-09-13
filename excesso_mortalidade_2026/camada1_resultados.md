# Camada 1: resultados (setembro de 2026)

Pergunta: a alta de óbitos por parada cardíaca e arritmias (I46-I49) e por embolia pulmonar (I26) desde 2020 é real, é mudança de codificação, acompanha a infecção ou acompanha a vacinação?

## A. Codificação e investigação

Fração de óbitos investigados (campo TPPOS = S) por ano:

| Ano | I46-I49 | investigados | R00-R99 | investigados | todos os óbitos investigados |
|---|---|---|---|---|---|
| 2019 | 10.378 | 10,9% | 74.972 | 14,0% | 14,7% |
| 2021 | 13.286 | 12,4% | 94.134 | 13,3% | 20,7% |
| 2024 | 14.915 | 14,1% | 69.088 | 14,4% | 17,0% |

A investigação não caiu; ela subiu um pouco. A parada cardíaca continua sendo pouco investigada em qualquer ano.

Taxa padronizada por idade, óbitos por 100 mil, padrão Brasil 2019:

| Grupo | 2013 | 2019 | 2021 | 2024 | 2019 a 2024 |
|---|---|---|---|---|---|
| Parada e arritmias I46-I49 | 4,8 | 5,0 | 6,1 | 6,2 | +24% |
| Infarto e isquêmicas I20-I25 | 50,2 | 46,0 | 43,7 | 39,5 | −14% |
| Cerebrovascular I60-I69 | 58,8 | 48,6 | 46,9 | 44,2 | −9% |
| Hipertensão I10 | 13,9 | 12,8 | 18,2 | 14,7 | +15% |
| Soma parada + isquêmicas + AVC | 113,8 | 99,6 | 96,7 | 89,9 | −10% |
| Circulatório total | 198,9 | 175,0 | 174,1 | 166,4 | −5% |
| Mal definidas R | 40,8 | 35,8 | 42,9 | 29,3 | −18% |
| Circulatório + R | 239,7 | 210,8 | 217,0 | 195,7 | −7% |

No país inteiro, a soma das causas cardíacas agudas caiu 10% e a soma de circulatório com mal definidas caiu 7%. O aumento de 1,2 por 100 mil na parada cardíaca é pequeno diante da queda de 11 por 100 mil em infarto e AVC. Isso é o padrão de substituição de código: causas específicas migrando para códigos pouco úteis, como I46 e I10.

## B. Heterogeneidade por estado

Variação da participação da parada cardíaca em todos os óbitos, 2019 para 2024, em pontos percentuais, com as variações de infarto+AVC e de mal definidas:

| UF | parada | infarto+AVC | R | óbitos I46-I49 2019 | 2024 |
|---|---|---|---|---|---|
| RJ | +0,92 | −2,14 | −0,92 | 1.182 | 2.572 |
| AC | +0,90 | −1,30 | −1,66 | 13 | 52 |
| DF | +0,84 | −2,18 | −0,48 | 89 | 244 |
| CE | +0,49 | −2,99 | −0,58 | 334 | 683 |
| SP | +0,08 | | | 2.502 | 3.162 |
| MG | −0,04 | | | 1.474 | 1.645 |
| ES | −0,30 | −0,33 | −0,63 | 203 | 150 |

Correlações entre estados, variação 2019 a 2024:
- parada versus óbitos por covid por 100 mil em 2020 a 2022: −0,01
- parada versus cobertura de segunda dose: −0,01
- parada versus infarto+AVC: −0,22
- parada versus mal definidas: −0,06

A alta se concentra em poucos estados, sobretudo Rio de Janeiro, e não acompanha nem a carga de covid nem a cobertura vacinal. Onde a parada subiu mais, infarto e AVC caíram mais. É assinatura de prática local de certificação, não de exposição uniforme.

## C. Tempo por estado

Mês em que a média móvel de três meses de I46-I49 superou em 30% a média de 2019, comparado ao pico de covid de 2020 ou 2021 e ao mês em que a primeira dose atingiu 30% da população (arquivo `dados/camada1_uf_timing.csv`):
- alta iniciada antes de 30% de primeira dose: 17 de 26 estados
- alta iniciada até o mês do pico de covid: 14 de 26
- em 12 estados a alta já aparece entre janeiro e maio de 2020
- Rio de Janeiro, Rio Grande do Sul, Santa Catarina e Rondônia: alta só em 2022

Nenhum estado mostra alta iniciando na janela de vacinação em massa, junho a agosto de 2021, sem ter subido antes.

## D. Adultos de 20 a 49 anos, óbitos por 100 mil

| Causa | 2013 | 2019 | 2021 | 2024 | 2019 a 2024 |
|---|---|---|---|---|---|
| Parada e arritmias | 0,61 | 0,63 | 0,97 | 0,92 | +46% |
| Infarto e isquêmicas | 9,36 | 8,67 | 8,83 | 9,09 | +5% |
| AVC | 8,28 | 7,22 | 7,60 | 7,57 | +5% |
| Hipertensão | 1,65 | 1,38 | 2,26 | 1,81 | +31% |
| Embolia pulmonar | 1,05 | 1,28 | 1,31 | 1,72 | +34% |
| Circulatório total | 31,84 | 28,85 | 29,95 | 31,78 | +10% |
| Mal definidas | 12,89 | 12,68 | 15,04 | 12,03 | −5% |

Aqui o quadro é diferente. Infarto e AVC vinham caindo desde 2013 e passaram a subir a partir de 2021. O circulatório total subiu 10% e as mal definidas caíram, então não é migração de R para I. Nessa faixa há alta real de mortalidade cardiovascular, iniciada em 2021 e mantida até 2024, além da embolia pulmonar.

## E. O que ficou fora

- Internações do SIH e procedimentos do SIA: o FTP e o TabNet do DATASUS só respondem em HTTP simples, que o proxy desta sessão não encaminha. Precisa de exportações do TabNet ou execução local.
- Vacinação por faixa etária e fabricante por estado: o microdado existe na API do Ministério (apidadosabertos.saude.gov.br, rotas /vacinacao/doses-aplicadas-pni-2021 a 2024) mas só paginado em lotes de mil registros, inviável para centenas de milhões de linhas. A rota /vacinacao/esavi, eventos adversos notificados, tem o mesmo limite e é candidata a coleta parcial.

## Leitura

1. No conjunto da população, a alta de parada cardíaca é majoritariamente recodificação, concentrada em poucos estados, sem relação com covid nem com cobertura vacinal, e com queda maior nas causas específicas.
2. Entre 20 e 49 anos há alta real de mortalidade cardiovascular e tromboembólica a partir de 2021, de cerca de 10% no capítulo e 34% na embolia pulmonar, que não se explica por codificação.
3. O início da alta, por estado, precede a vacinação e coincide com a chegada da pandemia. Isso pesa contra a vacina como gatilho inicial e não exclui contribuição dela na persistência, que só dado individual separa.
