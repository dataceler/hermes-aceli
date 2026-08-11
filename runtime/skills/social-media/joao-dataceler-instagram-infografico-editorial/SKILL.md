---
name: joao-dataceler-instagram-infografico-editorial
description: Crie infográficos de Instagram para João e Dataceler.
version: 0.4.0
author: Hermes
---

# Infográficos de Instagram — João e Dataceler

Crie ou revise infográficos de uma única imagem para os feeds de João Cordeiro e Dataceler. Esta skill governa a transformação de informação em composição visual legível, saveable e coerente com cada identidade. Ela não governa carrosséis, Reels, Stories, legendas ou publicação.

O repertório visual foi aprendido com 47 imagens e quatro vídeos fornecidos como referências de **design apenas**. Títulos, listas, marcas, dados, teses, assuntos e argumentos dessas amostras não são fontes editoriais e não podem ser reutilizados.

Para João e Dataceler, use o **Higgsfield CLI como renderer padrão** de novas imagens e infográficos. Carregue `higgsfield-generate` e consulte `references/higgsfield-gpt-image-2.md`. Só use outro motor quando o usuário pedir explicitamente ou quando uma limitação material impedir fidelidade; declare a exceção.

## When to Use

Use esta skill quando o usuário pedir:

- um infográfico de uma única imagem para Instagram;
- uma cheat sheet, mapa, matriz, comparação ou guia visual;
- revisão de hierarquia, densidade ou legibilidade de um infográfico;
- adaptação de conteúdo aprovado para 1080 × 1350;
- design de infográfico para o perfil de João ou da Dataceler;
- aplicação de novos aprendizados visuais enviados com `/learn`.

Não use para:

- carrossel estilo Twitter;
- carrossel bem produzido;
- Reels, Stories ou motion design;
- LinkedIn — use `dataceler-e-joao-linkedin-infografico-editorial`;
- inventar conteúdo, dados, exemplos ou posicionamentos.

## Prerequisites

Antes de criar, confirme ou recupere:

1. perfil de destino: João ou Dataceler;
2. conteúdo-fonte autorizado;
3. objetivo visual: comparar, categorizar, explicar processo, mapear relações ou resumir;
4. chamada principal que deve sobreviver à leitura em miniatura;
5. identidade visual aplicável;
6. CTA, assinatura ou rodapé, se houver.

Em comparações de produtos, ferramentas ou serviços atuais, consulte documentação oficial dos dois lados, registre a data da verificação e não declare vencedor sem benchmark comparável. Para comparação bilateral, carregue `references/validated-two-column-comparison.md`.

Para a Dataceler, use a paleta e os ativos oficiais; referências externas ensinam **papéis de cor**, não cores para copiar. Para João, use apenas identidade já aprovada ou peça direção quando a escolha alterar significativamente o posicionamento visual.

## How to Run

Fluxo canônico:

```text
fonte aprovada → relação informacional → família de layout →
hierarquia → sistema de cards → renderização → QA móvel → revisão
```

1. Leia a fonte real com `read_file`, `web_extract` ou ferramenta equivalente.
2. Defina uma única relação informacional dominante.
3. Escolha uma família de layout pela estrutura, não pela moda. Em comparações bilaterais, use `references/validated-two-column-comparison.md`.
4. Esboce a hierarquia antes de estilizar.
5. Renderize pelo Higgsfield CLI por padrão. Para GPT Image 2, siga `references/higgsfield-gpt-image-2.md`; preserve texto-fonte e use uma arte aprovada como referência quando existir.
6. Converta a saída para 1080 × 1350 RGB sem cortar conteúdo essencial. Não presuma suporte nativo a 4:5.
7. Execute `scripts/check_instagram_infographic.py` para validar dimensões, modo e miniatura.
8. Inspecione o PNG real em tamanho normal e em 270 × 338, incluindo cada palavra quando houver texto gerado por modelo.
9. Faça no máximo uma correção generativa localizada; se ela introduzir novos erros, volte ao artefato aprovado ou a uma composição determinística autorizada.
10. Corrija até não haver bloqueador visual e reinspecione a nova renderização.

## Quick Reference

### Famílias de layout

| Relação | Layout recomendado |
|---|---|
| A versus B | divisão bilateral ou matriz comparativa |
| grupos equivalentes | grade modular de cards |
| sequência | fluxo numerado, trilha ou etapas conectadas |
| conceito central e satélites | hub-and-spoke ou mapa radial |
| camadas de abstração | anéis concêntricos ou níveis empilhados |
| guia abrangente | bento grid com módulos de tamanhos controlados |
| categorias com itens curtos | colunas categorizadas com ícone + rótulo |
| decisão por critérios | tabela ou matriz com linhas bem separadas |

### Parâmetros para 1080 × 1350

- margem externa: 48–72 px;
- faixa de título: aproximadamente 10–16% da altura;
- título: 64–96 px, até duas linhas;
- subtítulo: 30–42 px;
- cabeçalho de card: 30–42 px;
- corpo: preferencialmente 28–36 px;
- rodapé: aproximadamente 4–7% da altura;
- raio dos cards: 12–24 px quando houver cantos arredondados;
- bordas: 2–4 px, com contraste suficiente;
- colunas: até três para conteúdo textual; quatro apenas com rótulos muito curtos.

Os valores são pontos de partida, não substituem inspeção óptica.

### Sistema de cor

Use papéis consistentes:

1. fundo principal;
2. texto principal;
3. cor dominante da marca;
4. cor de destaque;
5. tints categóricos para distinguir módulos.

Um infográfico deve funcionar com uma cor dominante e um destaque. Cores adicionais precisam carregar significado, não decoração.

## Procedure

### 1. Proteja a origem do conteúdo

- Separe explicitamente conteúdo e design.
- Use apenas fatos, textos e argumentos da fonte autorizada para a peça atual.
- Referências visuais não autorizam copiar suas frases, listas, logos ou estrutura editorial.
- Registre lacunas; não as preencha com conteúdo plausível.

Conclusão: todo texto da peça é rastreável à fonte atual, não às amostras visuais.

### 2. Escolha a relação informacional dominante

Pergunte o que o leitor precisa perceber em primeiro lugar:

- contraste;
- agrupamento;
- ordem;
- dependência;
- hierarquia;
- visão geral.

Escolha uma família principal. Misture layouts somente quando uma região secundária realmente exigir outra relação.

Conclusão: o layout explica a informação antes mesmo da leitura detalhada.

### 3. Construa a hierarquia em quatro níveis

1. **Gancho visual:** título curto e dominante.
2. **Orientação:** subtítulo ou legenda que explica como ler.
3. **Estrutura:** categorias, etapas ou critérios.
4. **Detalhe:** descrições curtas, exemplos ou notas.

Use peso, tamanho, contraste e posição nessa ordem. Não tente produzir hierarquia apenas com cor.

Conclusão: título, estrutura e ação principal continuam identificáveis em miniatura.

### 4. Aplique uma grade rígida

- Alinhe título, módulos e rodapé a eixos compartilhados.
- Mantenha gutters constantes.
- Repita dimensões, bordas, raios e padding em cards equivalentes.
- Quebre a grade apenas para destacar um elemento realmente prioritário.
- Prefira módulos maiores a muitas caixas minúsculas.

Conclusão: a peça parece um sistema, não uma colagem.

### 5. Faça cards autoexplicativos

Cada card deve conter, quando necessário:

```text
número ou ícone → rótulo curto → detalhe essencial
```

- Um card, uma mensagem.
- Use números para sequência; ícones para reconhecimento; cores para agrupamento.
- Preserve a mesma posição relativa de ícone, rótulo e corpo.
- Evite colocar logo, ícone decorativo e número competindo no mesmo canto.

Conclusão: cards equivalentes são escaneados sem reaprender o padrão.

### 6. Use tipografia para leitura rápida

- Prefira uma família sans-serif de alta legibilidade.
- Use no máximo dois pesos principais e, se necessário, um terceiro para legenda.
- Reserve caixa alta para títulos, categorias e micro-rótulos.
- Evite parágrafos centralizados; centralização funciona melhor em títulos curtos.
- Limite blocos de corpo a poucas linhas.
- Não comprima fonte para salvar uma estrutura superlotada; reduza conteúdo ou módulos.

Conclusão: o leitor distingue títulos, rótulos e detalhes sem esforço.

### 7. Use ícones, logos e conectores com função

- Ícones devem compartilhar família visual, espessura e escala.
- Logos só entram quando forem parte legítima da informação atual.
- Em comparações entre produtos com identidades fortes, use o logo legítimo de cada opção no respectivo cabeçalho; letras, iniciais ou glifos genéricos enfraquecem reconhecimento quando o ativo real está disponível.
- Consulte a página oficial do produto e as diretrizes de marca antes de baixar ou adaptar um logo. Se a marca proibir recoloração, preserve o arquivo como fornecido.
- Equilibre logos por **peso óptico**, não por dimensões idênticas; preserve proporção com `contain` e respeite área de respiro.
- Confine a paleta de cada produto à sua coluna, cabeçalho e conclusão correspondente. Mantenha critérios, divisórias, grade compartilhada e autoria em base neutra ou na identidade do perfil publicador.
- Use tints claros nas células e a cor saturada nos cabeçalhos; a paleta deve distinguir os lados sem reduzir contraste ou transformar a peça em colagem.
- Linhas e setas devem indicar sequência, dependência ou agrupamento.
- Não use conectores apenas para preencher espaço.
- Em fluxos, mantenha um sentido de leitura explícito: cima–baixo ou esquerda–direita.

Conclusão: cada símbolo e cor acelera a interpretação, e as marcas comparadas permanecem distintas dentro de uma composição editorial unificada.

### 8. Controle a densidade

O repertório de referência mostra que alta densidade gera sensação de utilidade, mas frequentemente sacrifica leitura móvel. Adote a estrutura, não o excesso.

- Até três colunas para texto.
- Prefira 6–12 módulos legíveis a dezenas de microblocos.
- Se o conteúdo exigir letra pequena, migre para carrossel bem produzido ou divida o escopo.
- Preserve áreas de respiro entre título, corpo e rodapé.
- Use divisórias leves antes de adicionar fundos, sombras e ornamentos.

Conclusão: nenhuma informação crítica depende de ampliar a imagem.

### 9. Diferencie João e Dataceler

**João**

- pode usar assinatura humana, retrato discreto ou marca pessoal;
- aceita mais contraste editorial e ênfase autoral;
- deve parecer lúcido, direto e ensinável, não institucional genérico.

**Dataceler**

- usa identidade oficial, geometria precisa e tom mais sistemático;
- prioriza clareza operacional, modelos e aplicação empresarial;
- evita estética gamer, neon excessivo e variedade cromática sem função.

A estrutura visual pode ser compartilhada; voz, assinatura e intensidade institucional não.

### 10. Trate o rodapé como encerramento

- Use rodapé para assinatura, handle, CTA curto ou marca.
- Não repita o título.
- Mantenha contraste, respiro e altura controlada.
- O rodapé não pode parecer banner publicitário desconectado.

Conclusão: a peça termina com autoria clara sem competir com o conteúdo.

### 11. Renderize e verifique

- Gere o arquivo final em 1080 × 1350 RGB, salvo como PNG.
- Implemente overflow guards para limitar linhas e falhar antes que o texto colida; quando um guard falhar, encurte a copy antes de reduzir a fonte.
- Meça a largura real do título e da metadata do rodapé; não estime a margem direita por coordenada fixa.
- Verifique modo, transparência e contraste do logo contra o fundo final; um ativo oficial pode ter versão branca ou fundo embutido inadequado à composição.
- Execute `scripts/check_instagram_infographic.py IMAGE --create-thumbnail` para validar dimensões, modo e gerar a miniatura.
- Inspecione o PNG com `vision_analyze`.
- Inspecione também a miniatura de 270 × 338 para simular o feed.
- Verifique ortografia, clipping, alinhamento, contraste, escala de ícones e ordem de leitura.
- Corrija e renderize novamente; a inspeção anterior não valida automaticamente a nova renderização.

Conclusão: o artefato real passa em tamanho integral e miniatura.

## Pitfalls

- **Copiar o conteúdo das referências.** O aprendizado autorizado é apenas visual.
- **Confundir densidade com valor.** Muitas caixas e letras pequenas não tornam a peça melhor.
- **Usar cinco ou mais colunas textuais.** Isso falha no feed móvel.
- **Criar título longo.** O título deve orientar a leitura em poucos segundos; meça sua largura e preserve a margem direita.
- **Diminuir fonte para resolver overflow.** Encurte a copy, reduza critérios ou migre para carrossel antes de sacrificar leitura móvel.
- **Presumir que o logo oficial está pronto.** Verifique fundo, alpha, versão cromática e contraste na composição real.
- **Substituir marcas reconhecíveis por iniciais genéricas.** Em comparações legítimas, use os logos reais quando disponíveis e autorizados; preserve proporção, respiro e regras de uso.
- **Misturar as paletas dos dois lados.** Confine cada identidade à própria coluna e mantenha a grade compartilhada neutra; caso contrário, a comparação perde orientação visual.
- **Posicionar metadata por estimativa.** Alinhe o rodapé pela largura renderizada do texto.
- **Colorir cada card sem semântica.** A paleta vira ruído.
- **Misturar famílias de ícones.** Logos, line art, emojis e 3D juntos quebram consistência.
- **Forçar conteúdo em uma imagem.** Troque para carrossel quando a legibilidade exigir.
- **Copiar paletas externas.** Use os papéis de cor aprendidos com a identidade aprovada.
- **Assumir motion design.** Os vídeos de calibração permaneceram visualmente estáticos nos frames amostrados; não há regra confirmada de transição.
- **Assumir 4:5 nativo no GPT Image 2.** O contrato validado oferece 3:4, não 4:5; recorte central pode remover título e rodapé. Use extensão horizontal do fundo conforme a referência Higgsfield.
- **Confiar na tipografia gerada sem ler cada palavra.** Aparência convincente não prova fidelidade: o modelo pode abreviar critérios e reescrever conclusões.
- **Entrar em ciclos de correção generativa.** Faça uma correção localizada; se surgirem novos erros, interrompa e use o artefato aprovado ou composição determinística autorizada.
- **Usar a mesma personalidade nos dois perfis.** Compartilhe sistema, não identidade.
- **Publicar sem autorização.** Criar e revisar não autoriza postar.

## Verification

A skill funcionou somente se todos os itens abaixo forem verdadeiros:

- perfil de destino identificado;
- conteúdo rastreável à fonte atual;
- comparações atuais baseadas em documentação oficial dos dois lados e com data de verificação;
- nenhum vencedor declarado sem benchmark comparável;
- nenhum texto, dado, tese ou lista veio das referências visuais;
- uma relação informacional dominante;
- família de layout coerente com essa relação;
- título legível em miniatura;
- no máximo três colunas de texto;
- cards equivalentes com alinhamento e padding consistentes;
- cores com função semântica;
- ícones coerentes;
- conectores com direção clara;
- rodapé discreto e alinhado pela largura real do texto;
- logo com versão cromática e contraste adequados ao fundo;
- em comparação co-branded, logos reais inspecionados, paletas confinadas aos respectivos lados e grade compartilhada neutra;
- diretrizes de marca respeitadas, sem recoloração ou deformação proibida;
- PNG 1080 × 1350 RGB existente;
- Higgsfield CLI usado como renderer padrão, ou exceção material explicitamente documentada;
- quando houver texto gerado por modelo, cada palavra e acento comparados com a fonte autorizada;
- verificação mecânica executada com `scripts/check_instagram_infographic.py`;
- inspeção do arquivo real concluída;
- miniatura 270 × 338 legível;
- nova renderização reinspecionada após qualquer correção;
- nenhuma publicação executada sem autorização.

Consulte `references/visual-design-evidence.md` para os padrões observados, `references/validated-two-column-comparison.md` para comparações bilaterais já testadas e `references/higgsfield-gpt-image-2.md` para geração 3:4, correção textual e adaptação segura para 4:5.
