# Evidências de design visual

## Escopo

Este arquivo registra somente padrões visuais observados nas referências enviadas pelo usuário.

- Amostras estáticas: 47.
- Vídeos: 4.
- Frames analisados por vídeo: 6, distribuídos entre 5% e 90% da duração.
- Proibição: não registrar temas, afirmações, listas, dados, marcas ou textos das amostras como conhecimento editorial.
- Artefato de inspeção: `/root/.hermes/artifacts/instagram-infographic-design-learning/manifest.json`.

## Escala de confiança

- **Confirmado:** recorrente em muitas amostras ou diretamente verificado.
- **Recorrente:** aparece em várias amostras, com variações.
- **Provável:** útil, mas precisa de mais exemplos ou testes.
- **Insuficiente:** não há evidência para virar regra.

## Padrões confirmados

### 1. Orientação vertical e leitura descendente

A maioria das peças usa composição vertical, com título no topo, corpo modular e assinatura no final. A leitura começa por uma faixa de alto contraste e avança por blocos bem delimitados.

Aplicação:

- usar 1080 × 1350 como padrão de feed;
- construir topo, corpo e rodapé como zonas distintas;
- manter ordem de leitura evidente.

### 2. Título como âncora

O título ocupa uma faixa própria ou um bloco dominante. Palavras-chave recebem uma segunda cor, marcador, fundo ou sublinhado.

Aplicação:

- título em até duas linhas;
- alto contraste;
- destaque pontual, não colorização indiscriminada;
- preservar leitura em miniatura.

### 3. Grade modular

Cards, colunas e módulos se repetem com dimensões, alinhamentos e espaçamentos consistentes. A repetição reduz esforço cognitivo e permite escaneamento.

Aplicação:

- definir colunas e gutters antes de inserir conteúdo;
- padronizar padding, bordas, raios e posição dos rótulos;
- usar um sistema de cards por peça.

### 4. Cabeçalhos categóricos

Subseções são separadas por faixas, pills ou cabeçalhos coloridos. A cor atua como orientação e agrupamento.

Aplicação:

- uma cor dominante da marca;
- uma cor de destaque;
- tints para categorias;
- não usar cores que não carreguem função.

### 5. Ícone antes do detalhe

Ícones, números ou avatares aparecem como ponto de entrada dos módulos. Depois vêm rótulo e explicação.

Aplicação:

```text
ícone ou número → rótulo → detalhe
```

Manter uma única família de ícones e escala estável.

### 6. Rodapé de autoria

Muitas peças encerram com uma barra de assinatura, handle ou CTA. O rodapé é visualmente separado, porém subordinado.

Aplicação:

- 4–7% da altura;
- uma ação curta;
- marca ou autoria sem aparência de anúncio desconectado.

## Famílias recorrentes

### Matriz ou comparação

Características:

- colunas ou lados simétricos;
- critérios repetidos;
- linhas e bordas que sustentam comparação;
- destaque por cor ou rótulo.

Risco: muitas colunas geram texto pequeno. Para mobile, usar no máximo três colunas textuais ou transformar opções em faixas empilhadas.

### Grade de cards

Características:

- módulos equivalentes;
- número ou ícone no topo;
- título curto;
- descrição limitada;
- tints ou bordas por categoria.

É a família mais flexível e mais recorrente.

### Hub-and-spoke e mapa radial

Características:

- núcleo forte;
- ramos ou setores;
- categorias em volta;
- conectores que orientam relações.

Risco: excesso de rótulos nas bordas. Limitar satélites ou migrar detalhes para cards externos.

### Camadas concêntricas

Características:

- níveis aninhados;
- cor por camada;
- leitura do centro para fora ou vice-versa.

Adequado para hierarquia e abstração, não para listas independentes.

### Fluxo e processo

Características:

- etapas numeradas;
- conectores ortogonais ou setas;
- direção explícita;
- alternância controlada de cor.

Risco: linhas cruzadas e caminhos ambíguos. Manter um sentido principal.

### Guia denso ou bento

Características:

- módulos de tamanhos diferentes;
- combinação de tabelas, listas, pequenos diagramas e ícones;
- alta percepção de utilidade.

Risco confirmado: letra pequena e sobrecarga. Usar a organização modular, mas reduzir o volume para Instagram.

### Listas categorizadas

Características:

- cabeçalhos por grupo;
- linhas curtas;
- ícone + rótulo;
- pouca descrição.

Funciona quando os itens são curtos. Não converter cada linha em parágrafo.

## Tipografia recorrente

- sans-serif pesada no título;
- sans-serif neutra no corpo;
- caixa alta em título e categorias;
- rótulos em bold;
- corpo menor e regular;
- destaques com cor de fundo ou marcador.

Melhoria necessária sobre várias referências:

- limitar pesos;
- evitar corpo abaixo do limiar móvel;
- não centralizar parágrafos;
- não reduzir fonte para acomodar conteúdo excessivo.

## Cor recorrente

Dois territórios aparecem:

1. fundo claro, texto escuro, uma cor dominante e tints categóricos;
2. fundo escuro, texto claro e acentos saturados.

Aprendizado permitido: papéis de cor e contraste.

Aprendizado proibido: copiar paletas externas. Cada perfil deve usar sua identidade aprovada.

## Espaçamento, bordas e divisórias

Padrões recorrentes:

- margem externa constante;
- gutters pequenos, porém regulares;
- bordas finas em tabelas;
- cards arredondados em grades mais amigáveis;
- separadores tracejados em materiais mais editoriais;
- fundos suaves para agrupar regiões.

Regra prática: primeiro alinhar e espaçar; depois adicionar borda. Se o agrupamento já estiver claro, a borda pode ser desnecessária.

## Legibilidade móvel

### Fortes

- 2–3 colunas;
- 6–12 cards;
- título curto;
- rótulos de uma linha;
- ícones grandes;
- contraste claro entre zonas;
- comparação empilhada;
- fluxos com poucas etapas.

### Fracos

- 4–6 colunas com parágrafos;
- dezenas de microcards;
- corpo fino e condensado;
- paletas com muitas cores equivalentes;
- logos pequenos demais;
- rodapés extensos;
- matrizes cuja leitura exige zoom.

Os padrões fracos são evidência do que evitar, não preferência do usuário.

## Evidência dos vídeos

Durações verificadas:

- 6,95 s;
- 5,52 s;
- 3,00 s;
- 4,98 s.

Nos seis frames distribuídos de cada vídeo, o layout permaneceu materialmente igual. Não foi confirmada uma linguagem de transição, zoom, pan, revelação progressiva ou animação tipográfica.

Classificação:

- design estático exibido em vídeo: **confirmado**;
- motion design reutilizável: **insuficiente**;
- ritmo de transição: **insuficiente**.

## O que não virou regra

- assuntos das peças;
- textos, listas, dados ou afirmações;
- marcas e logos exibidos;
- paletas exatas;
- fontes exatas não identificadas;
- animação;
- frequência editorial;
- uso do mesmo acabamento para João e Dataceler;
- densidade máxima observada.

## Atualização futura

Ao receber novas referências com `/learn`:

1. inspecionar o arquivo original;
2. registrar apenas propriedades visuais;
3. comparar com esta base;
4. classificar como confirmado, recorrente, provável ou insuficiente;
5. alterar a skill apenas quando houver evidência nova;
6. nunca importar conteúdo ou tese da referência.
