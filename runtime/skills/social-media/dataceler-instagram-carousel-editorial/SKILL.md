---
name: dataceler-instagram-carousel-editorial
description: Use when creating or revising Instagram carousel posts for Dataceler. Produces sourced editorial arguments, deterministic 1080 × 1350 slides, a complementary caption, mobile-size visual QA, and an approval-ready package without publishing.
version: 0.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Instagram, Carousel, Dataceler, AI, Editorial, Pillow, QA]
    related_skills: [dataceler-e-joao-linkedin-infografico-editorial]
---

# Carrosséis de Instagram da Dataceler

## Visão geral

Use esta skill para criar e revisar carrosséis editoriais do perfil institucional `@dataceler`. Ela cobre pesquisa, tese, roteiro, renderização determinística, legenda, correções solicitadas pelo usuário, controle de qualidade e empacotamento.

O resultado é um conjunto real de PNGs verificados, não apenas uma ideia, roteiro ou prompt. Esta skill não publica no Instagram e não autoriza publicação.

Carregue `references/approved-pattern-v1.md` quando precisar reproduzir o padrão visual e os aprendizados do primeiro carrossel aprovado.

Carregue `references/instagram-x-style-carousels.md` quando a referência editorial vier de threads ou posts do X; use o ritmo narrativo sem copiar interface, identidade, selo ou composição de terceiros.

## Quando usar

- “Crie um carrossel para a Dataceler.”
- “Transforme esta notícia de IA em 10 slides.”
- “Faça um post em carrossel inspirado no estilo de uma thread do X.”
- “Corrija a formatação dos slides.”
- “Centralize números, círculos, badges ou CTAs.”
- “Escreva a legenda do carrossel.”
- “Entregue os PNGs e um ZIP para aprovação.”

Não use para:

- carrossel estilo Twitter/X — use `joao-dataceler-instagram-carrossel-twitter-editorial`, que duplica o template oficial no Canva;
- infográfico isolado de uma única imagem;
- apresentação corporativa ou deck;
- conteúdo autoral de João Cordeiro sem indicação explícita;
- publicação automática no Instagram.

## Identidade fixa

- Perfil: **Dataceler**.
- Handle: `@dataceler`.
- Avatar: símbolo oficial preto da Dataceler sobre fundo branco.
- Formato padrão: **1080 × 1350**, PNG, modo RGB.
- Voz: institucional, executiva, clara e orientada a aplicação empresarial.
- Público: empresários, gestores, profissionais não técnicos e pessoas aprendendo IA.
- CTA prioritária: pergunta específica que gere comentários úteis.
- Não usar selo de verificação se o perfil público não estiver verificado.

A estética pode adotar o ritmo editorial de posts do X — avatar, nome, handle, texto curto e continuidade — sem simular uma publicação real, copiar uma interface completa ou reproduzir a identidade de outro criador.

## Entradas necessárias

1. Tema, fonte ou autorização para selecionar um tema atual.
2. Quantidade de slides; quando o usuário disser dez, entregar exatamente dez.
3. Referência visual, quando fornecida.
4. Objetivo editorial: educação, análise, autoridade ou conversa.
5. Ativos oficiais da marca ou caminho validado do logo.

Se o usuário autorizar a seleção do tema, pesquise sinais atuais e escolha pelo conjunto: relevância para negócios, fonte primária disponível, mecanismo explicável e potencial evergreen. Não alegue ter medido toda a internet.

## Fluxo canônico

```text
fontes → tese → roteiro → sistema visual → render → QA → revisão → legenda → pacote → aprovação
```

## Procedimento

### 1. Verifique as fontes

- Leia todas as URLs e arquivos fornecidos.
- Para fatos atuais, pesquise e confirme em fonte primária.
- Separe em notas:
  - fatos atribuíveis;
  - interpretação editorial da Dataceler;
  - hipóteses;
  - afirmações proibidas ou não verificadas.
- Não invente estatísticas, resultados, cases, disponibilidade de produto ou experiência de cliente.

**Concluído quando:** cada afirmação factual do roteiro tem fonte ou foi removida.

### 2. Defina uma tese empresarial

A tese precisa responder:

1. O que aconteceu ou qual erro merece atenção?
2. Qual mecanismo explica isso?
3. Qual é o “so what?” para uma empresa?
4. Qual princípio continua válido depois que a tendência passar?
5. Qual decisão ou pergunta fecha o argumento?

Evite transformar notícia em resumo. A tendência é a entrada; a consequência empresarial é o conteúdo.

**Concluído quando:** a tese é específica, discutível, sustentada e útil para o público da Dataceler.

### 3. Estruture o arco do carrossel

Para dez slides, use como ponto de partida:

1. Gancho específico.
2. Acontecimento ou evidência primária.
3. O que mudou de fato.
4. Mecanismo ou arquitetura acessível.
5. Consequência empresarial.
6. Aplicações potenciais, rotuladas como análise.
7. Risco, limite ou contraponto.
8. Modelo de controle e responsabilidade.
9. Ação estreita, mensurável e reversível.
10. Síntese e pergunta para comentários.

Uma lâmina deve carregar uma ideia principal. Corte repetições antes de reduzir tipografia.

**Concluído quando:** cada slide avança o argumento e a sequência funciona sem a legenda.

### 4. Construa o sistema visual

Padrão inicial:

- fundo branco ou creme;
- carvão para texto principal;
- bronze como acento, não decoração dominante;
- bastante espaço negativo;
- cabeçalho discreto com avatar, nome e handle;
- tipografia sem serifa com hierarquia forte;
- rodapé e indicação de continuidade consistentes;
- evidências visuais somente quando legíveis;
- contraste escuro em slides de alerta quando servir ao argumento.

Não dependa de modelos de imagem para renderizar texto. Para slides densos, diagramas, setas, círculos e botões, prefira Pillow ou HTML/CSS determinístico.

**Concluído quando:** o sistema é reconhecível como Dataceler e não como cópia da referência.

### 5. Renderize artefatos reais

Estrutura recomendada:

```text
instagram-dataceler-{tema}/
├── source.md
├── structured-content.md
├── caption.md
├── assets/
├── scripts/render_carousel.py
├── slides/slide-01.png ...
├── contact-sheet.jpg
├── verification.json
└── dataceler-{tema}-carousel.zip
```

Regras:

- nomes sequenciais com zero à esquerda;
- 1080 × 1350;
- modo RGB;
- texto e elementos dentro da área segura;
- arquivos não vazios;
- render completo após mudança no código-fonte.

**Concluído quando:** todos os PNGs existem e abrem com quantidade, dimensões e modo corretos.

### 5A. Produza uma versão editável no Canva quando solicitado

Use o Canva MCP oficial já autenticado; o `@canva/cli` isolado serve principalmente ao desenvolvimento de aplicativos e não substitui as ferramentas de design.

Fluxo verificado para carrossel multipágina:

1. chamar `generate-design` com briefing completo e exigir exatamente dez páginas em um único design;
2. escolher um candidato que exponha dez miniaturas;
3. chamar `create-design-from-candidate` uma única vez;
4. verificar com `get-design`, `get-design-pages` e `get-design-content`;
5. se o Canva materializar o candidato como apresentação 16:9, criar uma cópia com `resize-design` em 1080 × 1350;
6. confirmar/commit apenas a cópia vertical, sem sobrescrever o original;
7. reler o design final e confirmar dez páginas, 1080 × 1350, conteúdo editável, título e URL.

Não trate o URL de um candidato como design materializado. Não entregue uma apresentação 16:9 como carrossel vertical. URLs de miniaturas podem exigir autenticação e retornar `403` fora do MCP; quando isso impedir a inspeção, declare a limitação e peça revisão no Canva em vez de inventar QA visual.

**Concluído quando:** existe um design editável real, com ID, URL, dez páginas e dimensões 1080 × 1350 verificados por leitura independente; nada foi publicado.

### 6. Centralize pela geometria real

Nunca posicione números, CTAs, badges ou rótulos apenas por tentativa visual.

Use a caixa real do glifo:

```python
left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
tw, th = right - left, bottom - top
x = x1 + (x2 - x1 - tw) / 2 - left
y = y1 + (y2 - y1 - th) / 2 - top
draw.text((x, y), text, font=font, fill=color)
```

Depois, valide o centro óptico no PNG integral e em tamanho de feed. Caracteres diferentes podem parecer desalinhados mesmo quando usam a mesma coordenada de origem.

**Concluído quando:** números, CTAs, badges e nós estão centralizados horizontal e verticalmente em suas formas.

### 7. Escolha layouts adequados ao retrato

Não comprima quatro ou mais cards em uma linha se rótulos e setas perderem espaço.

Ordem de preferência:

1. linha do tempo com nós;
2. fluxo vertical;
3. grade 2 × 2;
4. cards horizontais somente quando cada rótulo couber com folga.

Não reduza fonte para salvar uma composição inadequada.

**Concluído quando:** rótulos, setas e margens permanecem legíveis em tela pequena.

### 8. Execute QA em duas escalas

**Visão do conjunto:** analise `contact-sheet.jpg` para narrativa, ritmo, consistência e alternância visual.

**Visão individual:** abra em resolução integral todos os slides com:

- números dentro de círculos;
- botões e CTAs;
- setas e fluxos;
- quatro ou mais cards;
- texto sobre fundo escuro;
- imagens de evidência;
- parágrafos longos.

Verifique:

- ortografia;
- cortes e sobreposições;
- margens e área segura;
- contraste;
- hierarquia;
- centralização óptica;
- tamanho em celular;
- fidelidade da fonte;
- avatar e handle corretos.

**Concluído quando:** a folha de contato e cada slide sensível passam sem bloqueadores.

### 9. Trate feedback como teste de regressão

Quando o usuário apontar um problema:

1. admita objetivamente;
2. localize a causa no renderizador;
3. corrija o código-fonte, não apenas o PNG;
4. rerenderize o conjunto;
5. reinspecione os slides afetados;
6. preserve tudo que já foi aprovado;
7. atualize o ZIP e o relatório de verificação.

Não declare sucesso antes de abrir os arquivos corrigidos.

**Concluído quando:** cada item do feedback está resolvido e verificado individualmente.

### 10. Escreva uma legenda complementar

A legenda deve aprofundar o mecanismo ou a consequência, sem repetir slide por slide.

Estrutura recomendada:

```text
gancho complementar
→ mecanismo
→ impacto empresarial
→ risco ou critério
→ ação recomendada
→ pergunta específica
→ fontes e hashtags restritas
```

Prefira data absoluta a “hoje” quando a legenda puder ser publicada depois. Evite venda agressiva e CTA genérica.

**Concluído quando:** a legenda agrega informação, contém CTA útil e não contradiz o carrossel.

### 11. Empacote e peça aprovação

O ZIP deve incluir:

- slides;
- legenda;
- roteiro;
- fontes;
- folha de contato;
- relatório de verificação.

Confirme por código a quantidade, dimensões, modo e integridade. Entregue a prévia e o pacote para aprovação.

Não publique automaticamente. Aprovação do material não equivale a autorização para postagem.

**Concluído quando:** o pacote abre, contém a revisão atual e o usuário pode aprovar sem depender dos arquivos-fonte.

## Armadilhas

- Aprovar apenas pela folha de contato e não abrir slides sensíveis.
- Centralizar texto com deslocamentos manuais fixos.
- Comprimir processos horizontais em tela vertical.
- Usar “hoje” em legenda que pode envelhecer.
- Repetir o carrossel inteiro na legenda.
- Usar a imagem `og:image` como avatar sem validá-la.
- Falsificar selo de verificação.
- Copiar a interface ou identidade de outro criador.
- Tratar aplicação potencial como resultado comprovado.
- Corrigir PNG sem corrigir o renderizador.
- Atualizar uma skill de infográfico com aprendizados exclusivos de carrossel.
- Publicar sem autorização explícita.

## Verificação final

- [ ] Perfil `@dataceler` e avatar oficial corretos.
- [ ] Quantidade exata de slides.
- [ ] Todos os slides em 1080 × 1350, RGB e não vazios.
- [ ] Uma ideia principal por lâmina.
- [ ] Fonte, análise e hipótese claramente separadas.
- [ ] CTA específica e centralizada.
- [ ] Números e rótulos centralizados por bounding box.
- [ ] Layouts densos inspecionados individualmente.
- [ ] Folha de contato sem quebra de narrativa.
- [ ] Legenda complementar e datada de forma durável.
- [ ] ZIP contém a revisão mais recente.
- [ ] Nenhuma publicação ocorreu sem autorização.

A skill só funcionou quando os PNGs reais, a legenda e o pacote final passaram no QA e foram entregues para aprovação.
