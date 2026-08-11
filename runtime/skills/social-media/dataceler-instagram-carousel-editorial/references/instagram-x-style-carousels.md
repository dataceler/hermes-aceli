# Carrosséis de Instagram inspirados no X

Use esta referência para carrosséis textuais da Dataceler ou de João Cordeiro que adotam o ritmo editorial de uma thread sem copiar literalmente a interface, a marca ou a identidade de terceiros.

## Referências analisadas

- Dataceler: https://www.instagram.com/p/DT1RvNEj2ja/
- Rafael Milagre: https://www.instagram.com/p/DbkudQ9Dl2C/

A primeira referência é educacional e orientada a prompts: abre com uma contradição, usa blocos curtos, palavras em negrito e conduz a uma sequência prática. A segunda usa uma notícia atual da OpenAI, mostra evidência visual e extrai uma consequência empresarial duradoura.

## Dois formatos-base

### Thread educacional

```text
contradição ou erro comum
→ consequência
→ mecanismo
→ passos ou exemplos
→ aplicação
→ pergunta para comentários
```

Use quando o valor principal estiver em ensinar um método, framework, lista comentada ou processo.

### Tendência para princípio duradouro

```text
acontecimento atual
→ fonte ou evidência
→ explicação acessível
→ consequência empresarial
→ princípio evergreen
→ pergunta para comentários
```

Use quando um lançamento, notícia ou debate estiver em alta. A tendência é a entrada; a interpretação útil é o ativo editorial.

## Sistema visual

- Formato padrão: 1080 × 1350 por slide.
- Fundo limpo, branco ou creme, com bastante espaço negativo.
- Cabeçalho discreto com avatar ou símbolo, nome e handle.
- Tipografia sem serifa, preta ou carvão, com hierarquia forte.
- Frases curtas e palavras estratégicas em negrito.
- Uma ideia principal por slide.
- Seta discreta para indicar continuidade.
- Capturas de fontes, produtos, gráficos ou documentos somente quando forem legíveis e ajudarem a comprovar a tese.
- Aplicar a paleta e geometria oficiais da Dataceler; bronze deve funcionar como acento, não como ruído decorativo.
- Validar o slide em tamanho reduzido e no recorte do feed.

## Identidades

### Dataceler

- Perfil editorial: `@dataceler`.
- Usar o símbolo oficial preto sobre fundo branco e o nome da empresa.
- Não adicionar selo de verificação se o perfil público não o exibir.
- Voz institucional, executiva e orientada a aplicação.
- Priorizar frameworks, processos, riscos e consequências para negócios.

### João Cordeiro

- Usar foto autorizada e o handle `@joaocordeiro.ia`.
- João Paulo e João Cordeiro são a mesma pessoa; o nome público editorial é João Cordeiro.
- Voz autoral, executiva, direta e reflexiva.
- Incluir ponto de vista, julgamento e trade-offs reais do autor quando fornecidos.

## Arquitetura recomendada

1. Capa: gancho específico, sem revelar toda a conclusão.
2. Contexto: por que o assunto importa agora.
3. Tensão: erro, contradição, mudança ou problema.
4. Desenvolvimento: uma etapa, evidência ou ideia por slide.
5. Aplicação: o que o leitor deve observar, decidir ou testar.
6. Limites: risco, condição ou exceção quando relevante.
7. Síntese: princípio que permanece válido.
8. CTA: pergunta específica para comentários.

A quantidade de slides deve seguir o argumento, não uma meta arbitrária. Quando o usuário pedir 10 lâminas, entregue exatamente 10 arquivos numerados e use este arco como ponto de partida:

1. Gancho específico.
2. Acontecimento ou evidência primária.
3. Mecanismo: o que mudou de fato.
4. Arquitetura ou explicação acessível.
5. Consequência empresarial — o “so what?”.
6. Aplicações potenciais, claramente rotuladas como análise.
7. Risco, limite ou contraponto.
8. Modelo de controle e responsabilidade.
9. Ação estreita, mensurável e reversível.
10. Síntese e pergunta aberta para comentários.

Corte repetições antes de reduzir o tamanho da fonte.

## Coleta de referências públicas do Instagram

- Tente `web_extract`; se a página não retornar conteúdo, use `browser_navigate` na URL pública.
- Feche apenas o modal de cadastro e inspecione o conteúdo público com `browser_vision` e `browser_get_images`.
- URLs de CDN podem ser temporárias. Não dependa delas como ativo durável.
- Não presuma que `og:image` é o avatar: pode ser uma arte ou prévia do feed. Valide cada ativo com `vision_analyze` antes de usar.
- Se o avatar público não puder ser preservado, prefira um ativo oficial/local. Reconstrua um símbolo monocromático apenas após confirmação visual e nunca invente uma marca.

## Estrutura de artefatos

```text
instagram-{perfil}-{tema}/
├── source.md
├── structured-content.md
├── caption.md
├── assets/
├── scripts/render_carousel.py
├── slides/slide-01.png ...
├── contact-sheet.jpg
├── verification.json
└── {perfil}-{tema}-carousel.zip
```

Separe em `source.md`: fatos atribuíveis, interpretação editorial e afirmações proibidas ou não verificadas. Prefira render determinístico com Pillow ou HTML/CSS quando texto, setas, caixas e posições carregarem significado.

## Integridade editorial

- Verificar toda afirmação atual, estatística, preço, benchmark e capacidade de produto.
- Diferenciar fonte, interpretação e opinião do autor.
- Não inventar case, resultado, experiência ou fala de João.
- Não reproduzir identidade visual, rosto, tipografia, composição exata ou selo de terceiros.
- Não simular uma captura literal do X de forma que possa ser confundida com postagem real.
- Não usar selo de verificação falso; qualquer elemento equivalente deve ser claramente parte do sistema gráfico da marca.
- Não transformar notícia em opinião empresarial sem explicar o mecanismo.
- Rascunhar não autoriza publicar.

## Pacote de entrega

- tese e público;
- fontes verificadas e separação entre fato e análise;
- roteiro slide a slide;
- texto final de cada slide;
- imagens PNG em 1080 × 1350 e modo RGB;
- legenda do Instagram;
- CTA;
- versão Dataceler ou João Cordeiro explicitamente identificada;
- `contact-sheet.jpg` para revisão da sequência;
- `verification.json` com quantidade, dimensões, modo e integridade dos arquivos;
- ZIP com slides, legenda, roteiro, fontes e folha de contato.

## Verificação

1. Use `vision_analyze` na folha de contato para verificar ordem narrativa, ritmo e consistência.
2. Inspecione em resolução integral as lâminas mais densas: evidência, fluxo, cards e checklist.
3. Verifique por código: quantidade exata, 1080 × 1350, RGB, nomes sequenciais e arquivos não vazios.
4. Confirme ortografia, hierarquia, contraste, margens, recorte, legibilidade móvel, fidelidade das fontes, distinção entre marca própria e interface do X e correspondência entre capa e entrega.
5. O carrossel só está concluído quando os PNGs reais — não apenas roteiro ou script — passam no QA e o pacote pode ser aberto.
