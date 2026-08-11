---
name: dataceler-youtube-producao-semanal
description: Execute uma rotina semanal de produção para o YouTube.
version: 0.1.0
author: Hermes
metadata:
  hermes:
    tags: [YouTube, Produção, Rotina, Vídeo, Dataceler]
    related_skills: [dataceler-youtube-estudo-diario, dataceler-youtube-evergreen-editorial, youtube-content]
---

# Produção Semanal de YouTube da Dataceler

Executa um ciclo previsível de terça a segunda para transformar pesquisa em um vídeo publicado, preservando apenas as etapas essenciais. Não promete concluir o primeiro vídeo em uma semana nem substitui competência editorial, gravação ou edição; organiza o trabalho para que a repetição reduza decisões e dispersão. Não exige software específico e pode funcionar com cerca de uma hora dedicada por dia, ajustada à realidade da produção.

## When to Use

- “Este é o processo que vou usar para criar vídeos no YouTube.”
- “Organize a produção do próximo vídeo da Dataceler.”
- “Monte minha rotina semanal de YouTube.”
- “Tenho uma hora por dia para produzir um vídeo.”
- “O que devo fazer hoje no ciclo de produção?”
- “Leve esta pauta da pesquisa até a publicação.”
- “Estou perdido entre tema, thumbnail, roteiro e edição.”
- “Quero produzir com consistência sem seguir toda novidade do algoritmo.”

## Prerequisites

- Nenhuma variável de ambiente é obrigatória.
- Reservar um bloco diário de produção; usar uma hora por dia como referência inicial, não como limite rígido.
- Definir a segunda-feira como dia-padrão de publicação e executar o ciclo principal de terça a segunda.
- Carregar `dataceler-youtube-estudo-diario` para manter o estudo do nicho em paralelo.
- Carregar `dataceler-youtube-evergreen-editorial` para escolher tema, tese, fontes, título, thumbnail e roteiro.
- Acesso a `web_search` e `web_extract` para pesquisa e verificação.
- Acesso opcional ao MCP oficial do vidIQ para temas, palavras-chave, outliers, títulos, thumbnails, comentários e analytics; chamadas podem consumir créditos.
- Acesso a `vision_analyze` quando houver uma thumbnail para revisar.
- Um arquivo central por ciclo para registrar entregáveis, pendências e conclusão de cada dia.
- Fonte-base do processo: `https://www.youtube.com/watch?v=tQcHKn2E90Y`.

## How to Run

1. Carregue esta skill, `dataceler-youtube-estudo-diario` e `dataceler-youtube-evergreen-editorial` com `skill_view`.
2. Crie o arquivo do ciclo com `write_file` usando o modelo da Procedure.
3. Em cada dia, leia o ciclo com `read_file`, execute apenas a etapa prevista e atualize o status com `patch`.
4. Use `web_search`, `web_extract` e, quando necessário, vidIQ para pesquisar; não invente o tema apenas por intuição.
5. Use `vision_analyze` para revisar a thumbnail antes da gravação e antes da publicação.
6. Prepare arquivos e metadados com `write_file`; publicação ou alteração do canal exige autorização explícita.

## Quick Reference

- Ciclo: terça → segunda.
- Diário: estudar o tema do canal.
- Terça: pesquisar tema + esboçar título e thumbnail.
- Quarta: criar abertura e roteiro + ajustar embalagem.
- Quinta: gravar.
- Sexta: editar.
- Sábado: continuar e concluir a edição.
- Domingo: reserva opcional.
- Segunda: finalizar, revisar e publicar.
- Essenciais: tema, thumbnail, título, abertura, audiovisual básico, conteúdo, edição e monetização.
- `skill_view`: carregar processo de estudo e estratégia editorial.
- `web_search`: descobrir demandas, perguntas e fontes.
- `web_extract`: confirmar fontes e claims.
- vidIQ opcional: demanda, concorrência, embalagem e desempenho.
- `vision_analyze`: revisar thumbnail.
- `write_file`: criar o plano semanal e os entregáveis.
- `read_file`: verificar o estado do ciclo.
- `patch`: atualizar status sem apagar o histórico.

## Procedure

1. **Abra um ciclo de terça a segunda.**
   - Crie com `write_file` um arquivo por vídeo usando este modelo:

```markdown
# Ciclo de produção — título de trabalho
- Público:
- Problema ou decisão:
- Publicação-alvo: segunda-feira, AAAA-MM-DD
- Tempo diário disponível:
- Status geral: planejando

## Estudo diário
- Pergunta em investigação:
- Caderno central:

## Terça — tema e embalagem inicial
- [ ] Tema pesquisado
- [ ] Fontes iniciais registradas
- [ ] Título de trabalho
- [ ] Conceito de thumbnail

## Quarta — abertura e roteiro
- [ ] Promessa alinhada ao título e à thumbnail
- [ ] Abertura escrita
- [ ] Roteiro concluído
- [ ] Thumbnail ajustada

## Quinta — gravação
- [ ] Áudio e imagem testados
- [ ] Vídeo gravado

## Sexta e sábado — edição
- [ ] Corte principal
- [ ] Recursos visuais necessários
- [ ] Áudio revisado
- [ ] Exportação concluída

## Domingo — reserva opcional
- [ ] Pendências críticas resolvidas ou “não utilizado”

## Segunda — publicação
- [ ] Arquivo final revisado
- [ ] Título e thumbnail finais
- [ ] Descrição, fontes, capítulos e CTA
- [ ] Publicação autorizada
- [ ] Vídeo publicado ou agendado

## Aprendizados do ciclo
- Funcionou:
- Travou:
- Ajuste para o próximo ciclo:
```

   - Defina uma entrega observável para cada dia e mantenha apenas uma etapa principal em andamento.
   - A etapa termina quando o arquivo possui publicação-alvo, público, problema e tempo disponível.

2. **Preserve apenas o essencial.**
   - Restrinja o ciclo a: tema, thumbnail, título, abertura, audiovisual básico, conteúdo, edição e estratégia de monetização.
   - Trate novidades de algoritmo, formatos da moda e ferramentas como opcionais até que resolvam uma necessidade comprovada do vídeo.
   - Prefira imagem e áudio básicos bem executados a uma produção sofisticada que quebre a rotina.
   - A etapa termina quando toda tarefa da semana contribui diretamente para um dos elementos essenciais.

3. **Mantenha o estudo diário em paralelo.**
   - Use `dataceler-youtube-estudo-diario` nos intervalos disponíveis, como pausa, deslocamento ou antes de dormir.
   - Registre fontes, perguntas, explicações e padrões no caderno central.
   - O estudo alimenta a semana, mas não substitui o bloco diário de produção.
   - A etapa termina quando a pergunta investigada e o caderno estão ligados ao ciclo atual.

4. **Terça: pesquise o tema e esboce a embalagem.**
   - Use `web_search`, `web_extract` e, se útil, vidIQ para encontrar problemas e temas com interesse provável do público.
   - Não retire a ideia apenas da própria cabeça; conecte-a a demanda, pergunta, evidência ou observação real.
   - Defina um título de trabalho e um conceito de thumbnail antes do roteiro.
   - Título e thumbnail devem expressar uma promessa coerente, sem repetir exatamente a mesma mensagem.
   - A terça termina somente com tema pesquisado, fontes registradas e embalagem inicial compreensível.

5. **Quarta: escreva abertura e roteiro; refine a embalagem.**
   - Carregue `dataceler-youtube-evergreen-editorial` para formular tese, estrutura, aplicação e limites.
   - Escreva a abertura para entregar rapidamente a promessa criada na terça.
   - Construa o roteiro conectando título, thumbnail, abertura e conteúdo; não trate esses elementos como peças independentes.
   - Ajuste título e thumbnail durante o roteiro quando a promessa se mostrar imprecisa.
   - A quarta termina quando o roteiro pode ser gravado e a promessa aparece no conteúdo.

6. **Quinta: grave com o básico bem feito.**
   - Teste áudio, enquadramento, iluminação e materiais de apoio antes da tomada principal.
   - Grave seguindo o roteiro, preservando naturalidade e clareza.
   - Registre imediatamente trechos ausentes ou tomadas que precisam ser refeitas.
   - Não adie a gravação para aperfeiçoar equipamento sem necessidade concreta.
   - A quinta termina com o material principal gravado e as pendências identificadas.

7. **Sexta e sábado: edite até uma versão publicável.**
   - Comece pelo corte principal; remova erros, pausas inúteis e repetições que não ajudam.
   - Adicione apenas recursos visuais necessários para compreensão ou ritmo.
   - Revise áudio e exporte uma versão completa.
   - Use o sábado para continuar a edição quando a experiência ainda for limitada.
   - A etapa termina com arquivo exportado que pode ser revisado do início ao fim.

8. **Domingo: use como reserva, não como desculpa.**
   - Acione o domingo somente para pendências críticas de gravação, edição ou exportação.
   - Não introduza novas ideias, ferramentas ou mudanças de escopo que não corrijam um problema real.
   - Se não houver pendência, registre `não utilizado` e preserve o descanso.
   - A etapa termina sem pendências que impeçam a revisão de segunda.

9. **Segunda: finalize e publique.**
   - Assista ao arquivo final e confirme que a promessa da embalagem foi entregue.
   - Feche título, thumbnail, descrição, fontes, capítulos e CTA para comentários.
   - Use `vision_analyze` para uma última revisão da thumbnail quando o arquivo estiver disponível.
   - Se a edição ainda não terminou, use o bloco de segunda para concluí-la antes de preparar a publicação.
   - O agente só publica ou agenda após autorização explícita; sem autorização, entregue o pacote pronto ao usuário.
   - A etapa termina com vídeo publicado, agendado ou pacote final aprovado e pronto para ação humana.

10. **Feche e repita o ciclo.**
    - Registre o que funcionou, o maior gargalo e um único ajuste para a semana seguinte.
    - Não redesenhe todo o processo por causa de uma semana difícil.
    - Aceite que os primeiros vídeos podem exigir mais de uma semana; mantenha a ordem das etapas e aprenda pela repetição.
    - Abra o próximo ciclo com a pergunta alimentada pelo estudo diário.
    - A etapa termina quando o próximo ciclo tem ponto de partida e somente um ajuste operacional foi escolhido.

## Pitfalls

- **Confundir a referência com garantia.** Uma hora por dia é um exemplo de organização, não promessa de publicar semanalmente desde o primeiro ciclo.
- **Esperar resultado em seis a doze meses.** O prazo citado é experiência do autor, não previsão para a Dataceler.
- **Espalhar energia.** Novidades, formatos e ferramentas não entram no ciclo sem impacto claro sobre um elemento essencial.
- **Inventar tema.** Pesquisa e evidência devem anteceder título, thumbnail e roteiro.
- **Criar embalagem depois da gravação.** O processo exige pelo menos a ideia de título e thumbnail antes do roteiro e da câmera.
- **Desalinhar promessa e conteúdo.** Título, thumbnail, abertura e roteiro devem contar a mesma história.
- **Superproduzir.** Audiovisual e edição básicos bem feitos são suficientes para sustentar a rotina inicial.
- **Mudar a rotina toda semana.** Ajuste um gargalo por ciclo; repetição é parte central do método.
- **Considerar a primeira semana fracassada.** Iniciantes provavelmente levarão mais de um ciclo para concluir o primeiro vídeo.
- **Transformar domingo em expansão de escopo.** Use-o apenas como reserva para pendências críticas.
- **Confundir promoção com processo.** Cursos, links e ofertas do vídeo-fonte não fazem parte da rotina.
- **Publicar sem aprovação.** Preparação é reversível; publicação e mudanças no canal exigem autorização explícita.

## Verification

Use `read_file` no arquivo do ciclo e confirme em uma única revisão que: o tema foi pesquisado; título e thumbnail existiam antes do roteiro; abertura e roteiro foram concluídos antes da gravação; gravação antecedeu edição; o arquivo final entrega a promessa; cada dia tem status; e o vídeo está publicado, agendado ou explicitamente pronto para aprovação — se a sequência não puder ser comprovada pelo registro, o processo não foi concluído.
