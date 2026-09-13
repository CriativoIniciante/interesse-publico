# Camada 2: guia para o dado individual

Objetivo: separar, em adultos jovens, sequela de infecção, efeito da vacinação, mudança de acesso e codificação como causas da alta de mortalidade cardiovascular e tromboembólica desde 2021. Dados agregados não separam porque quase todo adulto teve infecção e vacinação no mesmo período. Só o dado por pessoa, com datas, separa.

## 1. A pergunta em termos causais

Para cada exposição E, dose k da plataforma P, ou infecção, e cada desfecho Y, embolia pulmonar, infarto, miocardite, parada cardíaca, AVC: a taxa de Y nos dias 1 a 7, 8 a 21 e 22 a 42 após E é maior que a taxa da mesma pessoa fora dessas janelas? Para infecção, janelas de 1 a 30, 31 a 90 e 91 a 365 dias.

## 2. O desenho: série de casos autocontrolada, SCCS

Só entram pessoas que tiveram o desfecho. O período de observação de cada uma é dividido em janelas de risco e tempo basal, e o modelo pergunta em qual janela o evento caiu, dado que caiu em alguma. Como a comparação é dentro da pessoa, tudo que não muda no tempo, sexo, genética, doença prévia, pobreza, se cancela. Sazonalidade e ondas entram como faixas de calendário. O método está descrito no tutorial de Whitaker e Farrington, recuperado do PubMed [DOI](https://doi.org/10.1002/sim.2302).

O script `camada2_sccs_simulacao.py` simula 400 mil pessoas com verdade conhecida, dose com risco 1,5 vezes e infecção com risco 4 vezes, e recupera 1,57 e 4,39 usando só os 6.309 casos. A pequena superestimativa é uma lição: quando o desfecho é morte, a pessoa não pode ser vacinada depois, e a observação termina no evento. Isso viola uma premissa do método e exige a extensão para observação dependente do evento, ou o uso de desfechos não fatais, internação, como principal e morte como secundário.

Premissas que precisam ser verdadeiras ou tratadas:
- o evento não altera a chance de exposição posterior: tratar com janela de pré-exposição de 14 dias antes da dose, que absorve o adiamento de vacina por sintomas;
- eventos recorrentes ou independentes: usar o primeiro evento por pessoa;
- a exposição infecção é mal registrada: o SIVEP-Gripe só capta casos graves e o e-SUS Notifica os testados; infecções não registradas diluem o efeito da infecção e empurram o contraste a favor da hipótese vacinal. Sorologia de rotina não existe em escala; a solução é análise de sensibilidade com fração de infecções não observadas.

Desenhos complementares: coorte pareada emulando um ensaio, com pareamento por idade, sexo, município e semana de vacinação, para comparar plataformas entre si; caso-cruzado para desfechos agudos.

## 3. O dado necessário e onde existe

Por pessoa: data de nascimento, sexo, município; data, plataforma e lote de cada dose; data de cada infecção registrada; internações com CID e datas; óbito com data e causa básica.

| Sistema | Conteúdo | Chave |
|---|---|---|
| PNI e RNDS | todas as doses, plataforma, lote, data | CPF e CNS |
| SIVEP-Gripe | SRAG com RT-PCR, internação, desfecho | CPF e CNS |
| e-SUS Notifica | casos leves testados | CPF |
| SIH-SUS | internações do SUS, CID principal | CNS |
| SIM | óbito, causa básica | nome, data de nascimento, nome da mãe |

Os dados identificados não são públicos, por força da LGPD. O pareamento nacional já foi construído e usado. A coorte de 100 milhões do CIDACS, Fiocruz Bahia, descrita por Barreto e colegas [DOI](https://doi.org/10.1093/ije/dyab213), pareia esses sistemas, e os estudos de efetividade vacinal de Cerqueira-Silva e colegas usaram exatamente as bases de notificação, internação e vacinação pareadas [DOI](https://doi.org/10.1016/S1473-3099(22)00140-2). A infraestrutura para responder à sua pergunta existe. O que não existe é a pergunta feita com esse desenho e esses desfechos, em escala nacional.

## 4. Caminhos de acesso, do mais viável ao mais lento

1. Parceria com grupo que já opera o pareamento: CIDACS, Instituto de Saúde Coletiva da UFBA, e grupos de epidemiologia da USP, UFMG, UFRJ e Fiocruz Rio. Você entra como pesquisador clínico, com a pergunta e o protocolo; eles entram com dado e estatística. É o caminho que já produziu publicações em meses.
2. Pedido formal ao Ministério da Saúde de dados identificados para pesquisa, com projeto aprovado em Comitê de Ética via Plataforma Brasil e termo de responsabilidade. A base legal é o uso para pesquisa previsto na LGPD. Demora de seis a doze meses.
3. Secretaria estadual de saúde, onde estados como São Paulo mantêm o pareamento vacinação e SIVEP próprio. Mais rápido, menor escala.
4. Registro prospectivo no seu serviço: morte súbita, embolia, infarto, miocardite e AVC abaixo de 50 anos, com datas de cada dose e de cada infecção, coletadas na admissão. Pequeno, mas responde no nível do paciente que você vê e serve de piloto para o pedido maior.

## 5. Protocolo mínimo, para registrar antes de olhar o dado

- População: residentes no Brasil de 18 a 59 anos, janeiro de 2021 a dezembro de 2023.
- Exposições: cada dose por plataforma, CoronaVac, ChAdOx1, BNT162b2, Ad26.COV2.S; cada infecção registrada.
- Desfechos, primeiro evento: internação ou óbito por I26, I21-I22, I40-I41, I46-I49, I60-I64, D68.5-D68.6 e trombose com trombocitopenia. Internação como principal, óbito como secundário.
- Janelas: 1 a 7, 8 a 21, 22 a 42 dias após dose; 1 a 30, 31 a 90, 91 a 365 após infecção; pré-exposição de 14 dias.
- Ajustes: faixas de calendário de 30 dias; idade em faixas de 5 anos.
- Sensibilidade: excluir quem se infectou e vacinou com menos de 30 dias de intervalo; variar a fração de infecções não observadas; repetir por sexo.
- Poder: em 2024 houve cerca de 1.600 óbitos por embolia pulmonar entre 20 e 49 anos e dezenas de milhares de internações; com três doses em mais de 60 milhões de adultos, o estudo detecta razões de 1,2 em janelas de 21 dias.
- Registro público do protocolo antes da análise, código aberto, e um estatístico independente do proponente rodando a análise principal.

## 6. Vieses que derrubam estudos desse tipo

- Vacinado saudável: quem está doente adia a dose; sem a janela de pré-exposição, a vacina parece proteger de tudo.
- Causalidade reversa: sintomas prodrômicos do evento impedem a dose.
- Infecção não registrada: a maior fonte de erro contra a hipótese infecciosa e a favor da vacinal.
- Observação dependente do evento quando o desfecho é morte.
- Riscos competitivos: a covid mata primeiro quem morreria de outra coisa, o que reduz artificialmente outras causas em 2020 e 2021 e as infla depois.

## 7. O que posso fazer daqui

Escrever o protocolo completo no formato da Plataforma Brasil, adaptar o script de simulação para a estrutura real do dado pareado, redigir a carta de solicitação ao Ministério ou à secretaria, e montar o formulário do registro prospectivo do seu serviço. Nenhum desses passos consome dado que eu não tenha.
