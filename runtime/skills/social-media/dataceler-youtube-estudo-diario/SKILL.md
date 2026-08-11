---
name: dataceler-youtube-estudo-diario
description: Transforme estudo diário em vídeos úteis no YouTube.
version: 0.1.0
author: Hermes
metadata:
  hermes:
    tags: [YouTube, Pesquisa, Conteúdo, Rotina, Dataceler]
    related_skills: [dataceler-youtube-evergreen-editorial, youtube-content]
---

# Estudo Diário para Vídeos da Dataceler

Transforma o estudo diário do tema do canal em matéria-prima para ideias, roteiros, exemplos, títulos e thumbnails. Não substitui pesquisa factual, planejamento editorial, gravação, edição ou publicação; organiza o hábito-base que melhora a pessoa que cria os vídeos. Depende de pelo menos 30 minutos diários, fontes variadas e um único caderno de conhecimento.

## When to Use

- “Este é o processo que vou seguir para criar vídeos.”
- “Faça meu estudo diário para o canal da Dataceler.”
- “Transforme o que estudei em uma pauta de YouTube.”
- “Organize minhas anotações em ideias, roteiro e embalagem.”
- “Estou sem ideias para vídeos e preciso retomar a rotina.”
- “Quero estudar IA todos os dias para produzir conteúdo melhor.”
- “Registre padrões de temas, títulos e explicações do meu nicho.”

## Prerequisites

- Nenhuma variável de ambiente é obrigatória.
- Definir o tema do canal e o público que será ajudado; para a Dataceler, assumir IA aplicada a empresários, gestores, pessoas não técnicas e profissionais de TI.
- Escolher um único caderno ou arquivo para todas as anotações do tema; não distribuir o conhecimento entre arquivos sem um índice central.
- Acesso a `web_search` e `web_extract` para estudar fontes públicas e verificar afirmações.
- Acesso opcional ao MCP oficial do vidIQ para pesquisar palavras-chave, canais, vídeos, comentários e tendências; respeitar o saldo de créditos.
- Carregar `dataceler-youtube-evergreen-editorial` quando uma anotação virar pauta completa.
- Fonte-base do método: `https://www.youtube.com/watch?v=SMlbt1CQoWw`.

## How to Run

1. Carregue esta skill com `skill_view`.
2. Use `web_search` para descobrir materiais e `web_extract` para estudar as fontes selecionadas.
3. Quando relevante, use as ferramentas MCP do vidIQ para observar demanda, linguagem, vídeos e padrões do nicho.
4. Crie o caderno único com `write_file`; nas sessões seguintes, leia-o com `read_file` e acrescente a nova entrada com `patch`.
5. Quando houver uma ideia madura, carregue `dataceler-youtube-evergreen-editorial` e converta-a em pacote editorial.
6. Não publique, agende ou altere o canal sem autorização explícita.

## Quick Reference

- Duração mínima: 30 minutos por dia.
- Intenção: ajudar o público, não apenas falar do interesse do criador.
- Fontes: vídeos em diferentes idiomas, livros, cursos e materiais primários.
- Registro: um único caderno de conhecimento.
- `web_search`: descoberta de fontes, perguntas e linguagem.
- `web_extract`: leitura e verificação de fontes.
- `read_file`: recuperar o histórico do caderno.
- `write_file`: criar o caderno inicial.
- `patch`: acrescentar uma nova sessão sem apagar o histórico.
- vidIQ opcional: palavras-chave, outliers, comentários e tendências.
- Saída diária: aprendizado registrado e possível aplicação editorial.
- Handoff: `dataceler-youtube-evergreen-editorial`.

## Procedure

1. **Fixe o hábito angular.**
   - Reserve pelo menos 30 minutos diários para estudar o tema do canal.
   - Trate a sessão como compromisso recorrente, não como atividade feita apenas quando faltar pauta.
   - Não tente melhorar todas as competências do YouTube simultaneamente; use o estudo como alavanca para ideias, roteiro, exemplos, embalagem e comunicação.
   - A etapa termina quando o período foi dedicado ao tema e o aprendizado foi registrado.

2. **Comece pela pessoa que será ajudada.**
   - Escreva uma pergunta, dificuldade ou decisão real do público.
   - Direcione o estudo para compreender e explicar melhor essa necessidade.
   - Rejeite temas escolhidos apenas porque o criador quer falar deles, sem interesse provável para o público.
   - A etapa termina com uma frase: “Este estudo pode ajudar [público] a [resultado ou decisão]”.

3. **Varie as fontes.**
   - Assista a vídeos do nicho em português e, quando possível, em outros idiomas, usando tradução ou dublagem disponível.
   - Leia livros, documentação, estudos e materiais primários relacionados ao tema.
   - Use cursos quando eles aprofundarem uma competência do nicho.
   - Não transforme YouTube na única fonte de aprendizado.
   - A etapa termina quando a sessão identifica claramente o material estudado e sua origem.

4. **Registre tudo em um único caderno.**
   - Se o caderno ainda não existir, crie-o com `write_file` usando esta estrutura:

```markdown
## AAAA-MM-DD — tema estudado
- Fonte:
- Pergunta do público:
- Aprendizado central:
- Linha de raciocínio:
- Exemplo útil:
- Termos e linguagem observados:
- Padrão de título ou thumbnail:
- Possível aplicação em vídeo:
- Dúvida que permanece:
```

   - Nas sessões seguintes, use `read_file` antes de estudar e `patch` para acrescentar a entrada.
   - Preserve o histórico; não reescreva anotações antigas para fazê-las parecer mais corretas do que eram.
   - A etapa termina quando a nova entrada pode ser localizada no caderno central.

5. **Estude conteúdo e forma.**
   - Registre a ideia aprendida e também como ela foi explicada.
   - Observe linhas de raciocínio, exemplos, termos recorrentes, perguntas, promessas e padrões de títulos.
   - Para thumbnails, registre a tensão ou transformação comunicada, sem copiar a identidade visual da fonte.
   - Separe aprendizado factual de opinião, experiência pessoal e argumento comercial.
   - A etapa termina quando a anotação contém ao menos um aprendizado de conteúdo e uma observação sobre comunicação.

6. **Extraia matéria-prima editorial.**
   - Converta a anotação em possíveis ingredientes: problema, tese, explicação, exemplo, contraponto, título, thumbnail e pergunta ainda aberta.
   - Não force cada sessão a produzir uma pauta; acumular conhecimento também é resultado válido.
   - Marque como candidata somente a ideia que ajuda o público e pode ser defendida com fonte, demonstração ou experiência claramente identificada.
   - A etapa termina com a anotação classificada como `continuar estudando`, `ideia candidata` ou `pronta para pauta`.

7. **Evite copiar; sintetize.**
   - Não reproduza roteiro, título, thumbnail, personalidade ou promessa da fonte.
   - Combine aprendizados de fontes diferentes com a experiência e o posicionamento da Dataceler.
   - Preserve links e atribuições para afirmações que dependam de terceiros.
   - A etapa termina quando é possível explicar o que a Dataceler acrescenta à ideia.

8. **Converta conhecimento em pauta.**
   - Quando uma anotação estiver `pronta para pauta`, carregue `dataceler-youtube-evergreen-editorial` com `skill_view`.
   - Entregue a ela: público, problema, aprendizado central, fontes, exemplos, termos observados, possíveis títulos e conceito de thumbnail.
   - Use a skill editorial para pesquisa complementar, tese, embalagem, roteiro, fontes, CTA e métricas.
   - A etapa termina somente quando a promessa do vídeo deriva do conhecimento acumulado e aparece no conteúdo planejado.

9. **Mantenha o ciclo.**
   - Continue o estudo diário mesmo quando já houver vídeos em produção.
   - Use novas sessões para aprofundar dúvidas, corrigir lacunas e alimentar próximas pautas.
   - Se as ideias diminuírem, examine primeiro a frequência e a qualidade do estudo antes de perseguir novas ferramentas.
   - A etapa termina quando a próxima sessão de estudo já tem uma pergunta de partida.

## Pitfalls

- **Chamar isto de processo completo de produção.** O método é a base de conhecimento; gravação, edição, publicação e análise pertencem a outras etapas.
- **Consumir passivamente.** Assistir sem registrar raciocínio, exemplo e aplicação não constrói o caderno.
- **Estudar apenas pelo YouTube.** Combine vídeos com livros, cursos, documentação e fontes primárias.
- **Espalhar anotações.** Um caderno central evita que boas ideias desapareçam entre aplicativos e arquivos.
- **Estudar sem público.** Conhecimento que não melhora uma decisão ou compreensão do público não vira automaticamente uma boa pauta.
- **Copiar embalagem.** Registre padrões, mas crie título e thumbnail coerentes com a Dataceler.
- **Tratar anedota como prova.** O autor relata experiência própria e de alunos; isso não garante crescimento para outro canal.
- **Prometer resultado em 30 minutos.** Trinta minutos é a duração diária recomendada, não prazo para crescimento ou garantia de desempenho.
- **Confundir promoção com método.** Recomendações de cursos e links comerciais do vídeo-fonte não fazem parte do processo.
- **Buscar atalhos.** O método depende de exposição recorrente, prática e aprofundamento ao longo do tempo.

## Verification

Use `read_file` no caderno central e confirme em uma única revisão que a entrada mais recente contém data, fonte, pergunta do público, aprendizado central, linha de raciocínio, exemplo ou aplicação, observação de linguagem e classificação editorial; a skill só funcionou se o registro puder alimentar uma próxima sessão ou uma pauta sem depender da memória do criador.
