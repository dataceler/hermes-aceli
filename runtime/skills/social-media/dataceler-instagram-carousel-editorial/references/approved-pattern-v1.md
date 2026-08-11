# Padrão aprovado v1 — carrossel Dataceler

## Origem

Este padrão foi extraído do primeiro carrossel institucional aprovado pelo usuário: um post de dez lâminas sobre GPT-Live, com linguagem visual inspirada no ritmo editorial de posts do X, mas sem copiar a interface ou a identidade de terceiros.

A aprovação veio com a ressalva de que ainda existem pontos de evolução. Trate este documento como base mínima, não como limite criativo.

## Elementos aprovados

- Formato 1080 × 1350.
- Fundo creme claro na maior parte da sequência.
- Carvão para texto principal.
- Bronze como cor de destaque.
- Cabeçalho com símbolo preto da Dataceler em fundo branco, nome e `@dataceler`.
- Contador de lâminas no canto superior direito.
- Rodapé discreto com “IA aplicada a negócios” e indicação de continuidade.
- Tipografia sem serifa, grande e limpa.
- Um slide escuro para marcar alerta ou contraponto.
- Evidência visual acompanhada de fonte.
- Encerramento com pergunta específica para comentários.

## Sequência aprovada

1. Gancho forte e curto.
2. Evidência primária.
3. Comparação antes/depois.
4. Explicação do mecanismo.
5. Consequência operacional.
6. Aplicações potenciais.
7. Alerta ou risco.
8. Modelo de governança.
9. Checklist de adoção.
10. Síntese e CTA.

## Correções que viraram padrão

### Processos no slide 5

A primeira composição usava quatro cards horizontais comprimidos. Ela foi rejeitada por formatação.

Padrão corrigido:

- usar linha do tempo com quatro nós;
- distribuir centros em intervalos regulares;
- colocar setas entre os nós, sem encostar nos círculos;
- centralizar números e rótulos por bounding box;
- separar o fluxo do bloco de conclusão;
- manter fonte da evidência fora do bloco principal.

### Slide de alerta

A primeira composição misturava parágrafos e um card de forma pouco estruturada.

Padrão corrigido:

- badge com largura suficiente e texto centralizado;
- título dominante em duas linhas;
- card neutro para explicar o risco;
- card bronze separado para a consequência;
- alinhamento e espaçamento vertical consistentes.

### Círculos numerados

A primeira versão posicionava números com coordenadas fixas e foi rejeitada nos slides 8 e 9.

Padrão corrigido:

- medir `textbbox` para cada glifo;
- centralizar horizontal e verticalmente dentro da elipse;
- validar números diferentes individualmente;
- revisar em tamanho integral e reduzido.

### CTA

A primeira versão posicionava “COMENTE AQUI” manualmente e foi rejeitada.

Padrão corrigido:

- medir a caixa real do texto;
- centralizar dentro do retângulo arredondado;
- validar centro óptico, não apenas matemático;
- manter contraste branco sobre carvão.

## Regras de evolução

- Não repetir exatamente a mesma composição em todos os carrosséis.
- Preservar identidade, legibilidade e disciplina editorial.
- Variar os componentes conforme o argumento: comparação, processo, matriz, cards, checklist ou evidência.
- Tratar feedback de formatação como regressão a ser corrigida no renderizador.
- Nunca atualizar a skill de infográfico com regras exclusivas deste formato.

## QA mínimo

1. Gerar folha de contato das dez lâminas.
2. Abrir individualmente slides com fluxo, círculos, CTA, cards escuros e evidência.
3. Conferir números e CTAs por bounding box.
4. Conferir 1080 × 1350, RGB, nomes sequenciais e arquivos não vazios.
5. Atualizar o ZIP somente após a legenda final.
6. Entregar para aprovação sem publicar.
