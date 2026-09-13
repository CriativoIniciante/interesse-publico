## O que muda

<!-- Uma ou duas frases. -->

## Por quê

<!-- Link para a issue, para a evidência (hash ou URL) ou para o trecho do método que motiva a mudança. -->

## Camada

- [ ] 0, governo (carta, método, regras)
- [ ] 2, descrição (metadados, `fontes.yaml`)
- [ ] 3, interpretação (análise, dossiê)
- [ ] código (coletor, script)
- [ ] correção de erro (`corrige:` no título)

Camada 1 (evidência, manifestos, carimbos) não aceita pull request de pessoa. Só o coletor escreve ali.

## Checagens de quem propõe

- [ ] Toda afirmação nova aponta para evidência preservada, com hash ou link.
- [ ] Não removi nem alterei nada em `evidencia/`, `manifestos/`, `carimbos/`, `dossies/`, `erratas/`.
- [ ] Não incluí segredo, chave ou credencial.
- [ ] Não incluí dado pessoal de pessoa privada além do que está na fonte pública citada.
- [ ] Saída de modelo de linguagem, se houver, traz modelo, versão e hash do prompt.
- [ ] Mudança em `fontes.yaml`, se houver, traz justificativa pelos critérios 2.1 e resultado do teste.
- [ ] Commits com `Signed-off-by` (`git commit -s`).

## Declaração

<!-- Se a mudança é da camada 3: declare conflitos de interesse com o tema ou com as pessoas citadas, ou escreva "nenhum". -->

## Para o revisor

- [ ] Camada 2 ou código: um mantenedor.
- [ ] Camada 3: dois mantenedores, um que não escreveu, convicções declaradas diferentes. Indício de ilícito: protocolo 5.2 do método cumprido, direito de resposta registrado.
- [ ] Camada 0, carta: 14 dias abertos e assinatura de todos os mantenedores.
