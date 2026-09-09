# A leitura do dia: como a história é consolidada enquanto acontece

**O que é.** Uma rotina diária, complementar aos dossiês deste repositório. Todo dia as notícias são lidas por três lentes (o que a grande imprensa diz, o que a imprensa independente de vários campos diz, o que as pessoas estão dizendo e buscando), comparadas entre si e contra a fonte primária, graduadas pela mesma régua de prova dos dossiês, e o que sobrevive vai para a [linha do tempo](linha_do_tempo_2026.md). Os dossiês são atualizados quando um fato do dia os toca. A intenção é que, ao fim de um ano, a história do Brasil de 2026 esteja escrita como aconteceu, com a prova ao lado de cada frase, e não como o lado que vencer vai contá-la.

**Para que serve.** Os dois valores declarados do repositório, busca da verdade e ação virtuosa, em forma de hábito diário:

1. que qualquer leitor consiga separar fato de alegação no mesmo dia em que a manchete sai, e veja de onde cada versão vem;
2. que cada dia registre um motivo verificável de orgulho do país e um ponto onde é preciso coragem para se posicionar, sempre com o que uma pessoa comum pode fazer e o link;
3. que a memória pública de cada escândalo não dependa de quem ganhou a disputa em torno dele.

Começou em 09/09/2026. A primeira leitura está em [2026/2026-09-09.md](2026/2026-09-09.md).

---

## 1. As três lentes

| Lente | O que é | Fontes (perfil declarado em [fontes.json](fontes.json)) | Como ler |
|---|---|---|---|
| **Mainstream** | grandes grupos de imprensa | G1, Folha, UOL, CNN Brasil, Veja, BBC News Brasil | costuma ter mais apuração, mais acesso a documento e mais dependência de fonte oficial e de anúncio. Lê-se pela notícia: o fato e o documento por trás dele |
| **Independente** | veículos menores, de vários campos declarados | Gazeta do Povo e Revista Oeste (conservador), O Antagonista e Crusoé (Empiricus), JOTA e Conjur (jurídico), Nexo, Poder360, Metrópoles, Congresso em Foco, Agência Pública, Intercept, CartaCapital, Brasil 247, GGN (progressista) | cobre o que a grande imprensa não cobre e enquadra com mais tese. Lê-se em pares opostos, um conservador e um progressista sobre o mesmo tema, anotando o que cada um destaca e o que omite |
| **Popular** | o que as pessoas buscam, comentam e compartilham | Google Trends Brasil, Reddit (r/brasil, r/brasilivre), tendências do X, monitoramentos publicados, comentários | não é fonte de fato; é a medida do que a rua já acredita antes da prova. Lê-se para saber onde a checagem precisa chegar e que crenças estão se formando |

Duas lentes auxiliares entram em toda leitura: **oficial** (assessorias do STF, Senado, Câmara, Planalto, TCU, Agência Brasil: fonte primária, mas versão de quem fala) e **checagem** (Aos Fatos, Lupa, Comprova).

## 2. Equalizar não é tirar a média

A rotina compara as lentes para achar o fato, não para ficar no meio. Sete regras:

1. **Concordância entre lentes é indício, não prova.** Dez manchetes iguais podem vir da mesma nota de assessoria. Um documento vale mais que todas.
2. **A verdade não fica no meio.** Quando um lado tem o documento e o outro tem a tese, a leitura fica com o documento, e diz isso.
3. **Rotula-se a afirmação, não o autor.** Um veículo com campo declarado pode acertar; um veículo sem campo pode errar. A régua é por frase.
4. **A omissão é dado.** O que uma lente não noticiou, quando as outras noticiaram, fica registrado.
5. **A defesa entra sempre.** Toda pessoa nomeada tem sua versão registrada, ou a nota "sem manifestação localizada até a hora do corte".
6. **Manchete de hoje é [A] até prova.** Só vira [R] quando a reportagem reproduz o documento, e [P] quando o documento foi lido na origem.
7. **Opinião popular é medida, nunca fonte.** Registra-se o volume, o tom e a crença. Uma crença falsa é registrada como erro em circulação, com a checagem ao lado, sem desprezo por quem acredita.

## 3. A régua de prova

A mesma dos dossiês, aplicada a cada linha:

| Letra | Significa | Na leitura do dia |
|---|---|---|
| **[P]** | prova formal | decisão judicial, ato oficial, documento lido na origem, admissão do próprio envolvido |
| **[R]** | relato documentado | reportagem que reproduz documento ou trecho literal |
| **[A]** | alegação | fonte anônima, coluna, declaração de campanha, "segundo apurou", post em rede |
| **[N]** | refutado | a fonte primária ou a checagem contradiz a afirmação |
| **[O]** | inocência formal | absolvição, arquivamento, prescrição ou anulação (o texto diz qual) |

A letra de um fato pode mudar com os dias. A linha do tempo guarda a letra do dia e a letra final, para que se veja o que foi dito e o que se provou.

## 4. O que a leitura do dia produz

Um arquivo por dia em `diario/AAAA/AAAA-MM-DD.md`, seguindo o [modelo](_modelo_do_dia.md):

1. **Cabeçalho**: data, hora de corte, fontes que falharam na coleta.
2. **O dia em três linhas.**
2b. **Termômetro popular**: tabela com volume, tom e crença dominante por comunidade, e o que a rua ignorou. Diz como cada rede foi lida e o que faltou medir.
3. **Temas do dia** (de três a seis). Para cada um: o que aconteceu (fatos com letra e link); o que cada lente diz, com as palavras das manchetes; onde divergem e o que cada uma omite; defesas registradas; o que ainda não se sabe; qual item da [lista de vigilância da República](../republica_2026/README.md#7-o-que-ficar-atento-agora-setembro-de-2026-a-2027) o tema toca.
4. **Alegações em circulação**: o que está sendo repetido sem documento, com a origem rastreada.
5. **Checagens do dia**: o que os checadores derrubaram ou confirmaram.
6. **Mundo em três linhas.**
7. **Orgulho do dia**: um fato positivo verificável (instituição que funcionou, pessoa, ciência, cultura), com a mesma régua. Orgulho é o que se constata, não o que se declara.
8. **Onde é preciso coragem**: o que o dia pede de um cidadão, com uma ação concreta e o link, tirada da [seção 8.2 do dossiê da República](../republica_2026/README.md#82-o-que-cabe-a-cada-pessoa-com-o-link).
9. **Para a linha do tempo**: as linhas que sobrevivem, com letra.
10. **Método e ressalvas**: o que não foi lido na origem, nota de uso de IA com revisão humana.

## 5. As virtudes que a rotina treina

Sem sermão: cada seção do dia exercita uma virtude clássica, e é por isso que a estrutura é essa.

- **Prudência** (seções 3, 4 e 5): distinguir fato de alegação antes de formar opinião; perguntar quem decidiu, com que regra, quem se beneficiou, e se o mesmo tratamento seria dado ao outro lado, as [sete perguntas do checklist do cidadão](../republica_2026/README.md#51-o-checklist-do-cidadão-sete-perguntas-que-não-dependem-de-partido).
- **Justiça** (regras 3, 5 e 7): a mesma régua para todos os campos; a defesa sempre registrada; a crença errada tratada com respeito.
- **Coragem** (seção 8): nomear o que está documentado mesmo quando o nome é poderoso ou é do próprio campo, e usar o que a lei já permite (LAI, ouvidorias, ação popular, iniciativa popular) em vez de só se indignar.
- **Temperança** (regras 1, 2 e 6): não repetir o barulho, não compartilhar sem checar, não trocar um capturador por outro.
- **Orgulho do lugar** (seção 7): o país que funciona registrado com a mesma exigência do país que falha. Um povo que só conhece os próprios escândalos não tem de onde tirar coragem.

## 6. Como a história se consolida

```
coleta (06:00)  →  leitura do dia  →  linha do tempo  →  dossiês tocados  →  capítulo do mês
   raw/            AAAA/AAAA-MM-DD.md   linha_do_tempo_2026.md   (corte atualizado)   AAAA/mes_MM.md
```

- **Dia**: a leitura, como descrita acima.
- **Linha do tempo** ([linha_do_tempo_2026.md](linha_do_tempo_2026.md)): só acrescenta, nunca apaga. Uma linha por fato que sobreviveu à leitura, com data, letra, link e o dossiê que toca. É o esqueleto da história de 2026 como aconteceu.
- **Semana** (toda sexta, dentro do arquivo do dia): o que mudou de letra na semana ([A] que virou [R] ou [N]); qual dossiê teve o corte atualizado; o que a semana ensinou sobre as próprias lentes (quem acertou primeiro, quem errou e corrigiu, quem errou e não corrigiu).
- **Mês** (`AAAA/mes_MM.md`): o mês em uma página, com a lista de vigilância revisada. É o material que, um dia, vira aula.
- **Correção**: a linha errada não é apagada; recebe "corrigido em DATA" e o motivo. O repositório já fez isso com os próprios dossiês ([seção 6 do consolidado](../consolidado_2005_2026/README.md#6-o-que-corrigimos-nas-nossas-próprias-pesquisas)).

## 7. Guarda eleitoral

Vale até o fim do segundo turno de 2026 (25/10) e em toda eleição futura:

- nenhuma recomendação de voto, nenhum adjetivo sobre candidato ou partido, a mesma régua para todos os campos;
- pesquisa eleitoral só com registro no TSE, contratante, amostra, margem de erro e datas de campo; nunca "quem vai ganhar";
- declaração de campanha é [A] por natureza e entra como declaração: quem, quando, onde;
- um escândalo que atinge um campo é lido com a mesma exigência de um que atinge o outro, e a leitura diz quando só um campo o noticiou.

## 8. Fluxo técnico e custo

- **06:00**: o [coletor](coletor.py), agendado no Windows por [instalar_coletor.ps1](instalar_coletor.ps1), lê as fontes de [fontes.json](fontes.json) e grava título, hora, link e resumo do próprio feed em `raw/` (pasta ignorada pelo git; nada de texto integral, nada publicado). Só biblioteca padrão do Python.
- **Manhã**: a leitura é feita com auxílio de IA (Claude) a partir do material coletado, abrindo as matérias-chave e as fontes primárias, com o mesmo brief para as três lentes.
- **Revisão humana**: o autor lê, corta e corrige antes de publicar. Custo alvo: dez minutos por dia.
- **Publicação**: commit e push em nome do autor. O site do repositório passará a publicar a leitura do dia quando a rotina estiver madura.
- **Falhas conhecidas**: feeds que quebram ou mudam de endereço; a lista é mantida em `fontes.json` e cada leitura diz quais fontes falharam.

## 9. Ressalvas

A rotina lê o que está publicado; o que não foi publicado não existe aqui. A letra de um fato pode subir ou cair com o tempo, e a linha do tempo registra a mudança. Compilado com auxílio de IA (Claude) a partir exclusivamente de fontes publicadas, com revisão do autor. Licença CC BY 4.0. Correções por issue ou pull request.
