# Grupo de Trabalho "Conciliação Carteiras Adquiridas" — BRB, abril e maio de 2025

**Documentos:** dois relatórios finais do mesmo grupo de trabalho interno do Banco de Brasília.

| | Relatório I | Relatório Final (Retificado) |
|---|---|---|
| Portaria | DIFIC – 2025/004, de 26/2/2025 | DIFIC – 2025/006, de 7/4/2025 |
| Conclusão | 4/4/2025 | 19/5/2025 |
| Extensão | 40 páginas | 48 páginas |
| Acervo | `Inq 5026/00795` | `Inq 5026/00794` |
| Classificação no original | "#21 Reservado Externo" | "#21 Reservado Externo" |

**Composição:** quatro colaboradores da SUOPE e um da SUPVA, em dedicação exclusiva. Assinam o relatório final Susana Alvarenga Ofugi (coordenadora), Ludmyla Silva Bastos, Leonardo dos Reis Andrade, Igor Silva Bueno e Daniel Alencar do Vale.

**Nota sobre dados pessoais.** Os relatórios nomeiam clientes e transcrevem CPFs. Números de CPF, telefones de particulares e endereços residenciais foram omitidos desta transcrição, assim como os nomes dos tomadores de crédito que figuram como reclamantes. Os nomes de empregados do Banco Master e do BRB citados no exercício de função são mantidos.

---

## Por que estes dois documentos importam

O relatório independente que o BRB encomendou ao Machado Meyer com apoio da Kroll, um ano depois, resume este episódio em uma linha: o banco formou "um grupo de trabalho para revisão dos processos de cessão, o qual identificou, ainda em abril de 2025, falhas graves e indícios relevantes de potenciais irregularidades em porção significativa das operações com o Master". Os dois relatórios abaixo são esse grupo de trabalho falando por si. Eles antecedem em sete meses a Operação Compliance Zero, em seis o laudo do Banco Central que chegaria às mesmas conclusões e em quase um ano o relatório da Kroll.

O que eles mostram é que, em abril e maio de 2025, cinco funcionários do BRB, trabalhando com planilhas e chamadas de Teams gravadas, já tinham reconstituído quase inteiro o desenho da fraude: a originadora sem autorização do Banco Central, os contratos assinados depois da data que carregam, os lastros que nunca chegaram, as averbações que não existiam, os contratos em série com a mesma parcela e o mesmo prazo. E que o banco seguiu comprando.

---

## I. Relatório de 4 de abril de 2025 — o que a análise de dados encontrou

### Achados e indícios

> **7.1 Achados / Indícios**
>
> Os principais achados referem-se a:
>
> - Contratos "iguais": mesmo valor de parcela, prazo e saldo total para diversos contratos.
> - Vício de origem (primeira parcela não paga).
> - Contratos comprados desde a primeira parcela.
> - Cadastro (perfil etário, renda etc.).
> - (Des)padronização na numeração dos contratos.
> - Padronização nos contratos liquidados no Analítico PRE.
> - Registros em Ouvidoria sem reconhecimento de contratação junto ao Banco Master.

### A padronização da numeração

> "Na análise macro das operações de crédito adquirida foi identificada a existência de **24.481 clientes com padronização do número do contrato, compreendo 114.626 contratos**, concentrados em convênios CD GOV BA.
>
> Por 'padronização' entende-se aqueles contratos, de um mesmo cliente, separados em sua numeração por **exatamente 1, 10 ou 100 contratos**, originados em ordem cronológica aleatória. Caso a codificação dos contratos Credcesta siga uma lógica sequencial, ressalta-se a baixa probabilidade de originação de contratos, para um mesmo cliente, com esse intervalo numérico exato entre eles."

### A padronização das parcelas

Sobre o arquivo "ARQUIVO ANALÍTICO MOVIMENTACAO FINANCEIRA_PMT-25.02 ATE 10.03_241.052.381,04.xlsx":

> - "ao ordenar os dados por contrato e parcela, as primeiras 146 parcelas da base também ficam alinhadas em ordem crescente de CPF's e parcelas com numeração 61 e 62.
> - Clientes Homônimos (exemplo: 'Maria Aparecida da Silva') com diversas parcelas de valores iguais (incluindo duplicações completas).
> - Várias ocorrências de contratos sequenciais por cliente.
> - Identificadas **115.468 parcelas de número 1 com valor de R$ 339,77** (contratos feitos no mesmo dia — DT_PAGTO_ORIG)."

### Um caso concreto

O relatório abre um item para clientes individuais. O primeiro é o de uma aposentada de 70 anos, com **16 contratos abertos** e saldo contábil de R$ 253.218,99, distribuídos por cinco convênios distintos — CD GOV BA (Asteba), CD GOV BA (Asseba), CD INSS, GOV BA e CD GOV BA —, com renda presumida de R$ 41.400,00.

### Os lastros: 399 pedidos, 399 problemas

Em 21 de março de 2025 o grupo selecionou 399 contratos e pediu ao Master os lastros, com prazo até o dia 25. Chegaram em duas levas: 205 contratos em 26 de março, 194 em 28 de março.

Avaliação comum às duas partes:

> - "Documentos sem validação e assinatura do cliente.
> - Não há padrão na numeração dos contratos."

Parte I, avaliação detalhada de 27 arquivos:

> - "14 não apresentam a formalização do cliente.
> - Documentos assinados somente pelo Banco Master.
> - Parcelas com valor maior que R$ 3 mil são de contratos 'Saque Refinanciamento' e maior que 15% da margem consignável para o produto CredCesta.
> - Não há incidência de juros Pró-Rata da data do contrato para a 1ª parcela."

Parte II — a leva de 28 de março:

> - "**Todos os 194 contratos recepcionados tiveram as CCBs geradas e assinadas neste mesmo dia (28/03/2025) pelo Banco Master.**
> - Todos os documentos não possuem a formalização do cliente.
> - No geral, todos os contratos com numeração iniciadas com 999, 41, 13 e que possuem letras, não possuem formalização do cliente.
> - Não há retenção de IOF nas operações.
> - Não há incidência de juros Pró-Rata da data do contrato para a 1ª parcela.
> - Margens extrapoladas para averbação conforme exemplo a seguir.
>
> MARGEM R$ 1.691,91 · VALOR PARCELAS R$ 2.447,70"

Isto é: pedidos os lastros de uma amostra em 21 de março, o Master produziu 194 cédulas de crédito bancário no dia 28 de março — todas assinadas naquele dia, todas sem assinatura do cliente — para operações supostamente contratadas meses antes.

### Os padrões por prefixo

O relatório isola três famílias de numeração e descreve, para cada uma, o mesmo desenho:

- **Contratos iniciados com 999** — clientes que "alternam a numeração dos contratos, embora as datas das CCBs correspondam a meses diferentes e não sigam uma ordem cronológica, mantendo, entretanto, um prazo idêntico. Esse padrão se repete em diversos outros contratos."
- **Contratos iniciados com 41** — clientes que "possuem três contratos cada, com o mesmo valor de parcela e prazo. Embora as datas das CCBs correspondam a meses diferentes e não sigam uma ordem cronológica, a numeração dos contratos é sequencial."
- **Contratos iniciados com 13** — "a próxima dupla de clientes apresenta o mesmo número de contratações, com o mesmo valor das parcelas e prazo da dupla anterior. Esse padrão se repete sequencialmente em diversos outros contratos."

Em todos os três: "Não há incidência de juros Pró-Rata da data do contrato para a 1ª parcela."

---

## II. Relatório final de 19 de maio de 2025 — o que aconteceu quando o BRB foi cobrar

### O saldo

| | Devido | Recebido |
|---|---:|---:|
| Conciliação julho/2024 a março/2025 — PLA | R$ 50.473.921,20 | — |
| Atualização DI | R$ 21.804.274,50 | — |
| Operações para recompra — vício de originação | R$ 3.047.908,41 | — |
| Multa (até 30/4/2025) | R$ 20.015.701,20 | — |
| Mora (até 30/4/2025) | R$ 29.750.141,20 | — |
| Repasse devido — parcelas de abril/2025 | R$ 395.684.514,37 | R$ 341.050.773,98 |
| Parcelas com liquidação antecipada — analíticos de abril | R$ 49.280.124,08 | — |
| PLA de parcelas PRÉ — analíticos de abril | R$ 32.693.392,28 | — |
| Atualização DI — parcelas de abril | R$ 4.204.787,53 | — |
| **Total** | **R$ 606.954.764,77** | **R$ 341.050.773,98** |
| **Pendente** | | **R$ 265.903.990,79** |

### As reuniões que não aconteceram

> "Após o recebimento das Cartas, foram agendadas reuniões, que tiveram diversos reagendamentos. Tiveram **4 pedidos de remarcação por parte do Banco Master** desde 04/04/2025, primeira data marcada (...)
>
> No dia 14/04/2025 o Banco Master declinou a reunião. A solicitação de remarcação foi discutida via Grupo de Whatsapp app onde foi solicitado que até às 18h informassem nova data e hora para reunião e **até o momento não obtive resposta**."

Três cartas foram enviadas — DIFIC/SUOPE 2025/001 e 002, em 2 de abril, e a 2025/003, em 2 de maio, compilando as duas anteriores. O sumário executivo registra o resultado:

> "**A CARTA DIFIC/SUOPE – 2025/003 não teve nenhum de seus itens atendidos.** Dois itens foram respondidos parcialmente."

### A consulta assistida: as averbações que não apareceram

O contrato entre os dois bancos obrigava o Master a dar ao BRB acesso ao sistema da processadora conveniada ao órgão consignante, para conferir se os descontos em folha existiam. O grupo selecionou uma amostra de 57 CPFs, 284 contratos. Conseguiu duas sessões.

**8 de abril de 2025**, 48 minutos e 46 segundos, gravada. Foram consultados 15 CPFs, 47 contratos: **apenas 8 estavam averbados** — 3 de Cartão Benefício e 5 de Empréstimo Consignado. "Os outros 39 contratos não tiveram a averbação comprovada."

Aos 6 minutos, quando o grupo apontou que o valor averbado não fechava nem somado com os quatro contratos adquiridos, a equipe do Master respondeu:

> "E aí tem a operação que o banco (Master) comprou da **Associação** e cedeu para o BRB, que aí são outros valores. Mas aí a averbação é feita pela Associação, não pelo Banco (Master)."

Era a primeira vez que o grupo de trabalho ouvia falar nisso. O relatório registra a frase seguinte: "mesmo sem o conhecimento formal da aquisição de carteiras oriundas de terceiros (Associação), o GT decidiu prosseguir com as consultas".

Nos CPFs seguintes: 1 de 7 contratos averbado; 1 de 6; no convênio da Bahia, 1 de 8 — e esse único era um refinanciamento de saque benefício contratado em 6 de setembro de 2024 em 36 parcelas de R$ 5.054,06 e refinanciado em 4 de dezembro em 48 parcelas de R$ 5.039,76.

Aos 45 minutos, a equipe do Master interrompeu a reunião. Aos 47, o grupo pediu que ao menos se consultasse o convênio do INSS. A resposta:

> "A gente tem algumas coisas também de INSS que vêm da Associação. Acho que prefiro que a gente faça isso tudo de uma vez só."

**17 de abril de 2025**, 1 hora 26 minutos, gravada — e só aconteceu porque um gerente do BRB que estava fisicamente na sede do Master pediu a reunião ali. Foram analisados 23 CPFs, 126 contratos: **64 averbados**, 62 sem comprovação possível, "por se tratar de contratos firmados por meio de 'Associações'". Sobre por que não se podia consultar esses:

> "É, eles falaram (Associação) que não consegue fazer a consulta assistida, não tem ainda autorização lá pelo jurídico, né?"

No primeiro CPF do INSS, o valor total reservado da margem era R$ 1.406,87, contra R$ 2.038,68 de parcelas mensais dos seis contratos que o BRB tinha comprado. "Em todos os quatro benefícios do INSS consultados, verificou-se que os valores averbados são inferiores aos valores somados das parcelas dos contratos adquiridos pelo BRB."

Aos 42 minutos, perguntado qual era o produto contratado via Associações, o Master informou que era Cartão Benefício — "embora a regra do produto não permita averbação por mais de uma instituição".

Aos 1h18, o grupo pediu o nome da Associação. "A equipe não soube confirmar essa informação."

### As visitas técnicas a São Paulo

**15 a 17 de abril.** Conciliado o valor devido apontado no relatório de abril: R$ 15,5 milhões, dos quais o Master reconheceu R$ 14,5 milhões e pagou no dia 17. Identificada e comunicada a necessidade de recompra de cerca de R$ 2,7 milhões, "em razão da constatação de vícios de originação, no total de **5.866 contratos** apresentam a primeira parcela não paga. No entanto, o tema não foi tratado pela equipe durante a visita, e, até o presente momento, as operações em questão ainda não foram recompradas."

Pontos de atenção da visita:

> - "A equipe do Master apresentou grandes dificuldades em realizar os cálculos necessários para efetuar os repasses.
> - **Todo o controle da carteira de crédito é realizado de forma manual via Excel.**
> - Apresentaram pouco conhecimento das parcelas adquiridas por meio das Associações.
> - Área de cobrança em fase inicial.
> - Demora em resposta a questionamentos por parte do BRB."

**29 e 30 de abril.** Reunião com Alberto Felix, responsável pelas cessões de carteira no Master, que confirmou que havia operações originadas em outras instituições, "denominadas 'Associações'". Reunião com Allan Machado, responsável pela conciliação dos repasses, que explicou como o dinheiro das operações de terceiros circulava:

> "O Sr. Allan esclareceu que o repasse financeiro ocorre **via débito em aplicações financeiras desses terceiros**, o que inviabiliza a comprovação de vínculo direto com os repasses dos órgãos pagadores ou com os processos de averbação."

Pedidos os comprovantes de crédito e averbação das operações originadas nas "Associações", foi respondido que seriam solicitados aos originadores — "porém não houve retorno".

A análise da relação de produtos entregue confirmou a fronteira temporal:

> "As operações originadas no Banco Master foram, **majoritariamente, vendidas ao BRB em 2024**. As carteiras cedidas em **2025 são compostas, quase em sua totalidade, por operações originadas por terceiros**, e foi verificada, ainda, a inclusão de operações não pertencentes ao produto CredCesta."

Foram identificadas **134.798 operações** adquiridas pelo BRB que sequer constavam da relação de produtos.

E, finalmente, o nome:

> "O questionamento acerca da instituição originadora das operações não originadas pelo Banco Master foi reiterado. Em resposta, o Sr. Alberto Felix informou que tais operações foram originadas sob o CNPJ nº 57.965.351/0001-54, pertencente à empresa **Tirreno Consultoria Promotoria de Crédito e Participações S.A.**"

Era 30 de abril de 2025. O BRB estava comprando carteiras dessa origem desde janeiro.

### O que o BRB descobriu sobre a Tirreno em duas semanas

Em 5 de maio o Master disponibilizou os contratos com a Tirreno. O grupo os examinou:

> "Embora os contratos tenham sido assinados manualmente, **não foram apresentados registros cartorários** deles. Constatou-se, ainda, que a referida empresa, **constituída em 04 de novembro de 2024**, **não possui atividades econômicas compatíveis** com as de uma sociedade de crédito, financiamento ou investimento, conforme consulta CNPJ no site da Receita Federal, tampouco foi, **em qualquer momento, autorizada a operar pelo Banco Central do Brasil** como instituição financeira, conforme certidão emitida no site do Bacen."

Pedida reunião para 9 de maio, o Master recusou e propôs 13 de maio. No dia 13 compareceu sem os responsáveis. Em 15 de maio enviou 26 contratos de cessão entre ele e a Tirreno e finalmente sentou para conversar, por 35 minutos e 29 segundos.

### Os 26 contratos

> "Os 26 contratos encaminhados em 15 de maio de 2025 referem-se aos instrumentos contratuais e termos de cessão firmados entre o Banco Master e a Tirreno no período compreendido entre 24 de dezembro de 2024 e 24 de abril de 2025. Tais contratos totalizam a aquisição de direitos creditórios no montante de **R$ 6.347.984.262,66**, conforme os valores estipulados na cláusula denominada 'Preço de Aquisição'.
>
> **Todos os contratos foram assinados manualmente, tendo o reconhecimento de firma ocorrido apenas em 13 de maio de 2025.** A assinatura física e o reconhecimento posterior podem levantar questionamentos quanto à tempestividade e à formalização adequada dos documentos, sobretudo considerando o volume e a relevância financeira das operações envolvidas.
>
> Outro ponto que merece destaque diz respeito à dinâmica das cessões: os créditos são adquiridos pelo Banco Master e, **já no primeiro dia útil subsequente, são transferidos ao BRB**. Essa velocidade na revenda (...) impõe a necessidade de atenção especial quanto à conformidade documental, à efetiva transferência de risco e à adequação contábil.
>
> Chama também atenção o fato de ter sido registrada uma aquisição de carteira pelo Banco Master junto à Tirreno **no dia 4 de março de 2025 — terça-feira de Carnaval — data considerada feriado nacional, sem expediente bancário**. Essa operação, realizada em um dia não útil, suscita dúvidas quanto à regularidade do trâmite e à observância dos procedimentos operacionais usuais."

O reconhecimento de firma em 13 de maio é a data que a Polícia Federal reencontraria, dez meses depois, dentro do celular de Daniel Vorcaro: no dia 12, uma lista de pendências enviada pelo então presidente do BRB registrava que os contratos com a Tirreno não estavam reconhecidos em cartório.

### O que o Master explicou em 15 de maio

> - "**Parceria operacional com a Tirreno:** O Banco Master informou que a Tirreno atua como parceira na estruturação de carteiras de crédito consignado, por meio de prestadores de serviço terceirizados que originam as carteiras e que também dá o crédito como funding dessas originações. Essa estrutura envolve a originação das operações por terceiros, com posterior formalização junto a Tirreno e que relaciona uma terceira empresa **SCD/Cartus**, que também ficou pendente de esclarecimento.
> - **Natureza das operações:** Foi esclarecido que as operações **não se originam de concessões diretas de crédito bancário**. Em vez disso, trata-se de **assistências financeiras** firmadas com os tomadores, que, via contrato e com base em **cláusula de mandato**, são 'bancarizadas' pelo Banco Master.
> - **Negociação e contabilização das carteiras:** O Banco Master informou que realiza a aquisição de carteiras da Tirreno **exclusivamente nas operações em que estas são posteriormente cedidas ao BRB**. Além disso, foi ressaltado que tais operações **não são registradas no balanço patrimonial do Banco Master**."

A reunião terminou com o Master comprometido a responder no mesmo dia. "Contudo, até a conclusão deste relatório, tal resposta não foi encaminhada."

Seis itens ficaram pendentes, entre eles a "Certidão de inteiro teor das CCB – sistema de escrituração", a "Cláusula de Mandato Cliente > Tirreno e Tirreno > Master" e o "Extrato da conta reserva".

### As reclamações

Dois clientes em particular — uma aposentada e um beneficiário do INSS — abriram, respectivamente, 19 e 12 reclamações, por Ouvidoria do Banco Central, Reclame Aqui, Telebanco e SAC do BRB. Os relatos:

> "...Relata que antes o valor cobrado era de R$ 96,00 e após a cessão aumentou para R$ 339,50 em 95 vezes (...) e deseja contestar a alteração de parcela."
>
> "...Recentemente apareceram mais 03 contratos (...) aos quais não reconheço, pois em nenhum momento fiz estes empréstimos. Fiz contato com a central de relacionamento do BRB e a atendente me disse para procurar o Banco Master, ao ligar no Banco Master/Credcesta solicitei meus contratos vigentes e o atendente me informou que só havia os 2 contratos de 60x o qual eu reconheço."

O BRB escreveu ao Master em 11 de abril pedindo providências, e de novo em 7 de maio. "Até o encerramento deste relatório, a instituição não havia respondido aos questionamentos."

> "Conforme levantamento realizado pela Ouvidoria até o dia 19 de maio de 2025, foram registradas **476 ocorrências de clientes relacionadas ao Banco Master**."

### Os achados do relatório final

Aos sete achados de abril, o relatório de maio acrescenta dois:

> - "Desde janeiro 2025 foi observado que **os repasses mensais devidos pelo Banco Master somente são honrados quando o BRB realiza novas compras de carteira**.
> - Contratos com mesmo número na originadora que contratos previamente adquiridos e recomprados, porém, com informações divergentes."

O segundo é detalhado. Em 30 de abril de 2025 havia 86 operações nessa situação. As originais, todas do convênio com o Governo da Bahia, tinham sido compradas nas tranches 30 e 31 de dezembro de 2023, por R$ 1.323.762,19, e recompradas pelo Master em 12 de fevereiro de 2025 por R$ 1.562.619,75. As novas, com os mesmos números de contrato mas outros clientes, outros valores e outros vencimentos, foram compradas nas tranches 59, 63 e 64, em 11 e 25 de abril de 2025, por R$ 1.356.141,90 — e "nenhuma operação pertencia ao convênio com o governo da Bahia".

### Os lastros, de novo

> "Em relação aos lastros das operações das carteiras adquiridas do Banco Master, o Banco BRB teve acesso **somente às 399 CCBs** que foram solicitadas e detalhadas no Relatório Final I, de 04/04/2025. Conforme já avaliado, **mais de 200 CCBs dessa amostra apresentaram ausência de documentos comprobatórios ou má formalização**. (...) Até o fechamento desse relatório, o Banco BRB **não recebeu nenhum lastro adicional**, além dos solicitados na amostra inicial, de 21/03/2025, tampouco a documentação complementar das cédulas recebidas anteriormente."

O parecer jurídico interno sobre uma única cédula da amostra (Requisição nº 396.235) concluiu:

> "Por todo o exposto, conclui-se pela necessidade de complementação da documentação de comprovação da existência, validade e eficácia dos créditos cedidos (...) deve-se notificar o Banco Master S/A para fornecer documentos a seguir, sendo que, em não sendo apresentados, serão aplicadas as penalidades contratuais, são eles: a) CCBs escriturais cedidas, constantes no sistema de escrituração e; b) **certidão de inteiro teor de todas as CCBs escriturais cedidas ao BRB, desde a primeira tranche**."

### A carta que não foi enviada

O relatório lista as cláusulas do contrato que o Master não estava cumprindo — que os créditos fossem de cartão de benefício consignado nos termos da lei; que o crédito tivesse sido efetivado em conta dos devedores; que atendessem aos critérios de elegibilidade e exigibilidade; que os documentos comprobatórios fossem entregues em 10 dias para 50 casos e em 90 dias para a totalidade; que fosse dado acesso à consulta da processadora; que houvesse relatório de conformidade de auditor independente em 90 dias — e registra que redigiu a cobrança formal, a CARTA DIFIC/SUOPE 2025/004, de 2 de maio de 2025. E então:

> "**A correspondência não teve autorização de envio ao cedente**, porém consta de todos os dispositivos imprescindíveis para a eficácia do crédito adquirido e que não foram atendidos até o fechamento desse relatório."

### O tamanho da coisa

Levantamento do produto CredCesta até 30 de abril de 2025:

- Total de tranches: **63**
- Clientes: **615.147**
- Contratos adquiridos: **1.912.200**
- Parcelas: aproximadamente **137 milhões**
- Saldo futuro adquirido: **R$ 38.513 milhões**
- Saldo contábil em aberto: **R$ 9.666 milhões**
- Saldo contábil adquirido, líquido de recompra: **R$ 8.049 milhões**

### Outros dois nomes

O primeiro aditamento ao contrato, de 4 de abril de 2025, criou a conta escrow por onde deveria passar "todo o fluxo financeiro de arrecadação das parcelas", com prazo até 5 de maio, e nomeou como Agente de Conciliação a **WNT Gestora de Recursos Ltda** (CNPJ 28.529.686/0001-21), com sede na Faria Lima. "Até o fechamento desse relatório, o processo de abertura e manutenção da Conta Escrow não havia sido concluído" — e, na visita de 29 e 30 de abril, "o representante do Banco Master demonstrou resistência à atualização contratual".

O relatório de conformidade previsto no contrato seria feito pela **Deloitte**. Alberto Felix informou em 29 de abril que a auditoria demandaria "no mínimo, três meses para abranger toda a carteira, iniciando-se pelo tranche mais antigo". O grupo de trabalho analisou a proposta e a contestou tecnicamente, mostrando que o tamanho de amostra proposto era insuficiente — pelos próprios parâmetros da proposta, "a amostra deve ser de 399,89 contratos, pelo menos" — e que faltava estratificação. O questionamento foi enviado ao Master em 14 de maio. "Até o fechamento deste relatório o Banco BRB não teve retorno."

---

## Fonte

Acervo do STF disponibilizado em 11 de setembro de 2026, Inq 5.026, documentos `00794` (Relatório Final Retificado, Portaria DIFIC – 2025/006) e `00795` (Relatório Final, Portaria DIFIC – 2025/004), juntados como petição.
