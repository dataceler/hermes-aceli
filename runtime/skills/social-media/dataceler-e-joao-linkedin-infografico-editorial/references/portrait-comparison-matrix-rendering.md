# Matrizes comparativas em formato retrato

Use esta referência ao criar infográficos 1080 × 1350 com três ou mais opções e vários critérios. Ela registra o padrão de composição e QA que evita matrizes tecnicamente corretas, mas ilegíveis no feed.

## Escolha de estrutura

Em retrato, prefira **faixas comparativas empilhadas** quando três colunas estreitas exigiriam texto pequeno. Cada faixa representa uma opção e repete os mesmos critérios nas mesmas posições.

Estrutura recomendada:

```text
cabeçalho e tese
→ escala ou eixo de decisão
→ faixa da opção 1
→ faixa da opção 2
→ faixa da opção 3
→ regra de decisão
→ autoria e fontes
```

Dentro de cada faixa:

1. identidade da opção;
2. quem decide;
3. melhor contexto;
4. controle necessário;
5. ação principal;
6. exemplo, explicitamente rotulado quando hipotético.

## Regras de composição

- Reserve uma coluna fixa para nome, número e nível de autonomia.
- Posicione a divisória somente depois de medir o título e o subtítulo mais longos.
- Repita os critérios nas mesmas coordenadas em todas as faixas.
- Preserve um gutter visível entre rótulo e conteúdo; dois textos que apenas “não se sobrepõem” ainda podem parecer colados.
- Não reduza toda a tipografia para acomodar uma célula longa. Primeiro condense o rótulo sem alterar o significado; depois redistribua a grade.
- Use contraste adicional na opção de maior autonomia ou risco, sem transformar cor em ranking de qualidade.
- Uma escala “mais autonomia” deve deixar explícito que mais autonomia exige mais controle; não implica que o nível mais alto seja melhor.

## Guardas programáticos

O renderizador deve interromper quando uma célula ultrapassar seu limite:

```python
lines = wrap_lines(draw, text, font, width)
if len(lines) > max_lines:
    raise ValueError(f"Overflow: {text!r}")
```

Também valide:

- dimensão 1080 × 1350;
- modo RGB;
- arquivo não vazio;
- caixas de texto abaixo do limite da seção;
- centralização por `textbbox` para números, badges e botões.

Guardas programáticos não substituem QA visual: elas detectam overflow conhecido, não colisão óptica, falta de gutter ou hierarquia ruim.

## QA visual obrigatório

Inspecione o PNG integral e em tamanho de feed. Procure especificamente:

- título da opção invadindo o primeiro critério;
- subtítulo encostando na divisória;
- rótulo “exemplo hipotético” colado ao exemplo;
- última linha cortada em callouts próximos ao rodapé;
- grid técnico competindo com o conteúdo;
- exemplos com peso visual maior que a tese;
- texto claro com contraste insuficiente em faixa escura;
- logo deformado ou excessivamente pequeno.

Faça nova inspeção depois de cada correção. A peça está pronta somente quando não há bloqueadores reais.

## Limite de escopo

Este padrão pertence a infográficos de uma imagem. Regras específicas de sequência, paginação, CTA final e navegação de carrossel devem ficar na skill de carrossel, não nesta referência.
