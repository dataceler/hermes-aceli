---
name: dataceler-youtube-diagnostico
description: Diagnostique gargalos de vídeos e canais no YouTube.
version: 0.2.0
author: Hermes
metadata:
  hermes:
    tags: [YouTube, Diagnóstico, Conteúdo, Analytics, Dataceler]
    related_skills: [dataceler-youtube-estudo-diario, dataceler-youtube-producao-semanal, dataceler-youtube-evergreen-editorial, youtube-content]
---

# Diagnóstico de Vídeos e Canais da Dataceler

Diagnostica vídeos e canais pequenos em três camadas: interesse do tema, transformação entregue e adequação do formato. Não atribui baixo desempenho automaticamente ao algoritmo, não promete crescimento e não usa uma única métrica como prova; depende de evidências do vídeo, da embalagem, do público e, quando disponíveis, dos analytics.

## When to Use

- “Por que este vídeo teve poucas visualizações?”
- “Analise o que está travando meu canal.”
- “Meu título e minha thumbnail estão ruins?”
- “O conteúdo é útil, mas ninguém assiste.”
- “Diagnostique tema, conteúdo e formato deste vídeo.”
- “Descubra qual gargalo devo corrigir primeiro.”
- “Compare este vídeo com o que o público do nicho espera.”
- “Transforme os dados deste vídeo em uma melhoria para o próximo ciclo.”

## Prerequisites

- Nenhuma variável de ambiente é obrigatória.
- URL ou ID do vídeo e identificação do público pretendido.
- Para vídeo público: título, thumbnail, descrição, transcrição e métricas públicas disponíveis.
- Para canal próprio: analytics somente leitura, quando autorizados; não solicitar acesso de escrita.
- Acesso a `web_extract` ou `browser_navigate` para coletar a página oficial.
- Acesso a `vision_analyze` para inspecionar thumbnail, enquadramento, foco e exposição.
- Carregar `youtube-content` para recuperar transcrições quando necessário.
- Acesso opcional ao MCP oficial do vidIQ; algumas chamadas consomem créditos.
- Ferramentas vidIQ úteis: `mcp__vidiq__vidiq_get_videos_by_ids`, `mcp__vidiq__vidiq_video_transcript`, `mcp__vidiq__vidiq_channel_analytics`, `mcp__vidiq__vidiq_video_comments`, `mcp__vidiq__vidiq_similar_channels` e `mcp__vidiq__vidiq_outliers`.
- Para retenção de canal próprio, usar `mcp__vidiq__vidiq_channel_analytics` com `report="audience_retention"` e `filters="video==VIDEO_ID"`.
- Fonte-base do método: `https://www.youtube.com/watch?v=2KWSuuQT9ZY`.
- Para detectar vídeos com desempenho relativo excepcional em canais de qualquer tamanho, consulte `references/channel-outlier-monitoring.md` antes de implementar ou revisar o monitor.

## How to Run

1. Carregue esta skill e `youtube-content` com `skill_view`.
2. Colete página, título, thumbnail e descrição com `web_extract` ou `browser_navigate`.
3. Recupere a transcrição com `youtube-content` ou `mcp__vidiq__vidiq_video_transcript`.
4. Use `vision_analyze` para revisar thumbnail e quadros representativos do vídeo.
5. Se o canal for autorizado, consulte analytics somente leitura; se não for, declare a ausência desses dados.
6. Salve o diagnóstico com `write_file` e encaminhe apenas a correção prioritária para as skills editorial e de produção.
7. Não altere título, thumbnail, descrição ou publicação sem autorização explícita.

## Quick Reference

- Camada 1: tema interessante.
- Camada 2: conteúdo que gera transformação.
- Camada 3: formato familiar e áudio aceitável.
- Tema forte: dor, desejo, curiosidade ou dúvida relevante.
- Conteúdo útil: problema → ferramenta ou explicação → aplicação.
- Transformação: dúvida, dor ou crença errada → clareza, direção e ação.
- Formato: áudio, enquadramento, foco, exposição e linguagem visual.
- `web_extract`: metadados e página oficial.
- `browser_navigate`: conteúdo dinâmico do YouTube.
- `vision_analyze`: thumbnail e apresentação visual.
- `youtube-content`: transcrição.
- `mcp__vidiq__vidiq_get_videos_by_ids`: metadados públicos.
- `mcp__vidiq__vidiq_video_transcript`: transcrição via vidIQ.
- `mcp__vidiq__vidiq_channel_analytics`: analytics de canal próprio.
- `mcp__vidiq__vidiq_video_comments`: linguagem e reações do público.
- `write_file`: relatório de diagnóstico.
- Handoff editorial: `dataceler-youtube-evergreen-editorial`.
- Handoff operacional: `dataceler-youtube-producao-semanal`.

## Procedure

1. **Abra o caso e preserve a evidência.**
   - Crie com `write_file` um relatório usando esta estrutura:

```markdown
# Diagnóstico — vídeo ou canal
- URL ou ID:
- Canal:
- Público pretendido:
- Data da análise:
- Dados disponíveis:
- Dados ausentes:

## Evidência
- Tema:
- Título:
- Thumbnail:
- Promessa da abertura:
- Transformação entregue:
- Formato e áudio:
- Métricas públicas:
- Analytics privados, se autorizados:
- Comentários relevantes:

## Diagnóstico em três camadas
- Tema: forte | incerto | gargalo
- Conteúdo: forte | incerto | gargalo
- Formato: forte | incerto | gargalo

## Prioridade
- Gargalo principal:
- Evidência:
- Mudança recomendada:
- Métrica ou sinal para observar:
- O que não mudar neste teste:
```

   - Diferencie explicitamente fatos observados, hipóteses e dados ausentes.
   - A etapa termina quando a análise pode ser reproduzida a partir dos links, arquivos e métricas registrados.

2. **Separe tema de título e thumbnail.**
   - Defina o tema como o assunto ou problema oferecido ao público; trate título e thumbnail como embalagem.
   - Pergunte se o tema toca uma dor, desejo, curiosidade ou dúvida forte do público específico.
   - Verifique se a escolha partiu de demanda, perguntas, comentários, pesquisa ou experiência observável, e não apenas da vontade do criador.
   - Não tente salvar um tema sem interesse apenas tornando a embalagem mais chamativa.
   - A etapa termina com uma frase verificável: “Este público teria motivo para assistir porque ___”.

3. **Audite a promessa da embalagem.**
   - Compare tema, título e thumbnail como três elementos distintos.
   - Marque termos vagos como “a verdade”, “tudo sobre” ou “você precisa saber” quando não especificarem tensão, consequência ou benefício.
   - Confirme que o título posiciona o público e cria curiosidade específica sem prometer algo que o vídeo não entrega.
   - Confirme que a thumbnail comunica uma única ideia e complementa o título.
   - Use `vision_analyze` na imagem real; não avalie thumbnail apenas pelo texto alternativo.
   - A etapa termina quando a promessa pode ser repetida em uma frase e localizada na abertura e no conteúdo.

4. **Avalie sinais de interesse sem tirar conclusão automática.**
   - Registre visualizações, idade do vídeo, tamanho do canal e qualquer dado público disponível.
   - Para canal próprio, use impressões e taxa de cliques para qualificar a hipótese de tema ou embalagem.
   - Poucas visualizações podem ser compatíveis com tema fraco, mas não provam sozinhas a causa; canal novo, distribuição limitada e amostra pequena também importam.
   - Não transforme a afirmação promocional “99% dos canais” em estatística validada.
   - A etapa termina com a hipótese classificada como `sustentada`, `possível` ou `sem dados suficientes`.

5. **Teste se o conteúdo gera transformação.**
   - Leia a transcrição completa; não confunda quantidade de informação com utilidade.
   - Registre o estado de entrada do espectador: dúvida, dor, crença errada ou tarefa.
   - Registre o estado de saída prometido: clareza, direção, decisão ou vontade de agir.
   - Verifique se o vídeo identifica o problema, escolhe a ferramenta ou explicação adequada e mostra como aplicá-la.
   - Rejeite conteúdo que apenas despeja conceitos ou ferramentas sem ordem e próximo passo.
   - A etapa termina quando existe um antes e depois concreto, ambos sustentados pelo roteiro.

6. **Audite abertura e condução.**
   - Confirme que a abertura cria motivo para continuar e introduz a promessa sem excesso de contexto.
   - Verifique se cada bloco aproxima o espectador da transformação, em vez de acumular informação lateral.
   - Para canal próprio, use retenção para localizar abandono; sem analytics, trate ritmo e clareza como avaliação qualitativa.
   - Não atribua queda de retenção a uma causa única sem observar o trecho correspondente.
   - A etapa termina com os pontos de abandono conhecidos ou, na falta deles, com os trechos de maior risco identificados como hipótese.

7. **Audite formato e áudio.**
   - Priorize inteligibilidade do áudio antes de câmera, iluminação ou edição sofisticada.
   - Inspecione distância do microfone, volume, ruído, reverberação e consistência; se o áudio não estiver acessível, registre a limitação.
   - Use `vision_analyze` para verificar enquadramento excessivamente próximo, falta de foco e exposição estourada.
   - Compare o formato com referências do nicho para entender o que o público reconhece, sem copiar identidade ou apresentação.
   - Prefira uma execução simples e familiar a recursos visuais que prejudiquem compreensão.
   - A etapa termina quando cada problema técnico tem evidência observável e uma correção específica.

8. **Analise referências sem copiar.**
   - Observe canais semelhantes e canais de outros nichos que resolvam problemas comparáveis de abertura, explicação ou apresentação.
   - Registre o que fazem, como fazem e uma hipótese de por que funciona.
   - Extraia convenções: distância de câmera, densidade de cortes, estrutura da abertura, tipo de exemplo e nível de produção.
   - Adapte princípios ao posicionamento da Dataceler; não reproduza roteiro, thumbnail, identidade visual ou personalidade.
   - A etapa termina quando cada referência gerou um princípio aplicável, não uma peça para imitação.

9. **Escolha um gargalo principal.**
   - Classifique tema, conteúdo e formato como `forte`, `incerto` ou `gargalo`.
   - Escolha como prioridade o problema com evidência mais forte e maior impacto provável sobre a jornada do espectador.
   - Defina uma mudança observável para o próximo vídeo ou, se seguro, para a embalagem do vídeo atual.
   - Declare o que permanecerá igual para evitar alterar muitas variáveis simultaneamente.
   - A etapa termina com uma prioridade, uma intervenção e um sinal de sucesso.

10. **Converta diagnóstico em prática recorrente.**
    - Se o tema ou conteúdo estiver fraco, carregue `dataceler-youtube-estudo-diario` e aprofunde o assunto por 30 minutos diários com registro.
    - Se faltar demanda ou embalagem, carregue `dataceler-youtube-evergreen-editorial` para refazer tema, promessa, título e thumbnail.
    - Se o problema for execução, insira a correção no próximo ciclo de `dataceler-youtube-producao-semanal`.
    - Pratique em horário reservado; não espere inspiração para corrigir uma habilidade.
    - A etapa termina quando a correção aparece como tarefa e critério verificável no próximo ciclo.

## Pitfalls

- **Culpar o algoritmo primeiro.** Verifique tema, transformação e formato antes de concluir que a distribuição é a causa.
- **Tratar baixa visualização como prova.** É um sinal insuficiente sem idade do vídeo, tamanho do canal, impressões e contexto.
- **Confundir tema com embalagem.** Título e thumbnail fortes não criam interesse inexistente no assunto.
- **Avaliar apenas a thumbnail.** Tema, título e thumbnail são três elementos diferentes.
- **Despejar informação.** Um bom vídeo dá ordem, ferramenta e aplicação; não entrega uma caixa de peças soltas.
- **Ignorar áudio.** Produção simples pode funcionar, mas fala distante, baixa ou incompreensível cria atrito crítico.
- **Copiar referências.** Aprenda convenções antes de romper regras, sem reproduzir identidade de outros canais.
- **Usar IA como autoridade.** Diagnósticos automáticos são hipóteses; valide contra vídeo, público e dados.
- **Mudar tudo de uma vez.** Sem variável preservada, o próximo resultado não ensina o que funcionou.
- **Comprar equipamento antes de testar.** Primeiro aproxime a captação, controle ambiente e compare amostras.
- **Transformar “99%” em estatística.** O número faz parte da promessa do vídeo-fonte e não foi demonstrado como pesquisa.
- **Confundir promoção com método.** Curso, agente pago e links de afiliado não são requisitos desta skill.
- **Alterar canal sem autorização.** Diagnosticar é reversível; editar título, thumbnail ou publicação exige aprovação explícita.

## Verification

Use `read_file` no relatório final e confirme em uma única revisão que ele contém evidência separada para tema, título, thumbnail, transformação, abertura, formato e áudio; distingue fato de hipótese; identifica um único gargalo principal; recomenda uma mudança observável; preserva ao menos uma variável; e encaminha a correção para o próximo ciclo — sem esses elementos, o diagnóstico não está concluído.
