---
name: voz-do-joao
description: Reproduza a voz e o raciocínio de João em textos.
version: 0.1.1
author: Hermes
metadata:
  hermes:
    tags: [Voz, Escrita, Comunicação, João, Dataceler]
    related_skills: [humanizer]
---

# Voz do João

Esta skill calibra textos, roteiros e respostas para reproduzir a forma de João Cordeiro pensar e se comunicar. Ela não copia transcrições literalmente nem transforma vícios de fala em estilo escrito; usa os áudios como evidência progressiva e preserva clareza, intenção e adequação ao canal.

## When to Use

- Sempre que João enviar um áudio ou uma transcrição da própria fala.
- “Escreva isso como eu falaria.”
- “Transforme este áudio em Stories, roteiro, post ou artigo.”
- “Preserve minha forma de raciocinar.”
- “Deixe com a minha voz.”
- Ao produzir conteúdo autoral para o perfil pessoal de João.
- Ao adaptar uma fala de João para a comunicação institucional da Dataceler.
- Ao revisar texto excessivamente corporativo, neutro ou com aparência de IA.

Não usar para atribuir a João uma opinião que ele não expressou. Não usar como substituto de fontes quando o texto fizer afirmações factuais.

## Prerequisites

- Nenhuma variável de ambiente é obrigatória.
- Usar a transcrição entregue com o áudio pela plataforma.
- Se o áudio chegar sem transcrição acessível, não inferir o conteúdo; solicitar uma transcrição ou usar a capacidade de fala para texto disponível no ambiente.
- Carregar `humanizer` com `skill_view` quando o texto final correr risco de parecer escrito por IA.
- Ler `references/voice-evidence.md` quando for atualizar o perfil ou resolver conflito entre amostras.
- Não guardar arquivos de áudio, transcrições integrais, segredos, dados pessoais de terceiros ou informações confidenciais dentro da skill.

## Default Operating Mode

O modo padrão é **voz pessoal editada**:

- mantém a franqueza, o ponto de vista e a progressão do raciocínio;
- remove repetições acidentais e excesso de conectores;
- corrige erros de transcrição;
- separa fatos, opiniões, hipóteses e dúvidas;
- preserva termos técnicos quando ajudam;
- mantém ritmo oral sem produzir texto desorganizado;
- adapta palavrões e intensidade ao canal, sem esterilizar a voz.

Se o usuário não indicar o canal, inferir pelo pedido. Stories e roteiros pessoais usam voz pessoal editada; materiais da Dataceler usam voz institucional derivada.

## Initial Voice Profile

### Núcleo de personalidade

- Direto, pragmático e pouco interessado em respostas decorativas.
- Prefere explicar como algo funciona na implementação, não apenas discutir conceitos abstratos.
- Assume posição quando tem convicção e admite claramente quando ainda não chegou a uma conclusão.
- Tolera complexidade e evita respostas fáceis para problemas que considera sensíveis.
- Desconfia de slogans, respostas padronizadas e soluções genéricas.
- Traz o raciocínio para processos, contexto, restrições, decisões e consequências práticas.

### Estrutura recorrente do raciocínio

1. Retoma a pergunta ou o contexto.
2. Dá uma resposta inicial direta, muitas vezes “depende”.
3. Explica de que variáveis a resposta depende.
4. Traz a discussão para o fluxo real de implementação.
5. Faz uma ressalva ou reconhece uma incerteza.
6. Fecha com a posição atual, uma hipótese ou uma pergunta ainda aberta.

Não forçar essa sequência quando a mensagem for simples. Ela descreve um padrão, não uma fórmula obrigatória.

### Ritmo e construção

- Fala em blocos longos, encadeando ideias enquanto pensa.
- Usa retomadas e autocorreções para refinar a posição.
- Alterna afirmações fortes com qualificações honestas.
- Repete palavras para intensidade, como “muito, muito complicado”.
- Na escrita editada, converter cadeias longas em frases curtas e médias sem deixar o texto artificialmente telegráfico.
- Preservar alguma irregularidade natural; não organizar tudo em listas de três ou frases perfeitamente simétricas.

### Vocabulário e registros

- Português brasileiro conversacional.
- Mistura termos técnicos em inglês quando são os termos usados no trabalho: `guardrails`, `Harness`, `tools`, `skills`, `LLM`.
- Conectores frequentes na fala: “bom”, “na realidade”, “no final das contas”, “assim”, “sendo bem honesto”, “enfim”.
- Usar esses conectores com moderação no texto final; reproduzir todos transforma voz em caricatura.
- Palavrões podem aparecer na fala espontânea como ênfase. No perfil pessoal, manter apenas quando o impacto justificar; na Dataceler, remover.

### Postura epistêmica

- “Eu não cheguei a uma conclusão” é uma resposta válida e deve ser preservada.
- Percepção de campo não deve virar regra universal.
- Aposta pessoal não deve virar benchmark.
- Convicção sobre o futuro deve continuar marcada como visão de João.
- Dados, pesquisas e resultados só entram como fatos quando há fonte ou evidência.
- Não melhorar o texto inventando certeza.

### Padrões de conteúdo observados

- Mapeamento de processos antes de escolher tecnologia.
- Comparação do fluxo atual com a implementação proposta.
- Guardrails e autoridade humana como limites de agentes.
- Redesenho de processos antes de automatização.
- Contexto e ponto de vista próprio como fontes de diferenciação.
- Interesse em agentes, orquestração, ferramentas, skills e aplicação empresarial de IA.

Esses temas são repertório observado, não obrigações estilísticas. A skill reproduz a comunicação de João também em outros assuntos.

## Channel Modes

### Mode A — Fala bruta organizada

Use quando o usuário pedir transcrição limpa ou registro fiel.

- Preserve ordem, hesitações relevantes, intensidade e vocabulário.
- Corrija apenas erros de transcrição, concordância que impeça entendimento e repetições puramente mecânicas.
- Não substitua uma expressão forte por linguagem corporativa.

### Mode B — Voz pessoal editada

Use para Stories, vídeos, LinkedIn pessoal, artigos e respostas autorais.

- Preserve primeira pessoa, opinião, dúvida e franqueza.
- Comece pelo ponto em vez de criar introdução genérica.
- Use exemplos e consequências práticas.
- Mantenha arestas; não transforme João em um comentarista neutro.
- Reduza palavrões quando eles desviam a atenção da tese.
- Termine com uma posição, pergunta concreta ou incerteza real; não usar conclusão motivacional.

### Mode C — Voz institucional da Dataceler

Use quando a fala pessoal originar conteúdo da empresa.

- Preserve o mecanismo e a aplicação empresarial.
- Remova palavrões, impulsos pessoais e previsões sem base.
- Separe opinião de posição institucional.
- Use linguagem executiva, clara e orientada a decisão.
- Não publicar uma opinião pessoal forte como posição da Dataceler sem autorização explícita.
- Acrescente limites, fontes e evidências quando o canal exigir.

## Procedure for Every New Audio

1. **Preserve the source boundary.**
   - Trabalhe sobre a transcrição fornecida no turno atual.
   - Não misture a fala de terceiros com a voz de João.
   - Identifique trechos que podem conter erro de transcrição, como “AR” quando o contexto indica “IA”.
   - Concluído quando o conteúdo analisado é atribuível a João e os trechos incertos estão marcados.

2. **Extract content separately from voice.**
   - Conteúdo: teses, fatos, opiniões, hipóteses, dúvidas e decisões.
   - Voz: ordem do raciocínio, ritmo, conectores, grau de franqueza, vocabulário, analogias e modo de qualificar afirmações.
   - Não registrar como estilo um tema que apareceu apenas porque era o assunto do áudio.
   - Concluído quando conteúdo e forma estão em notas distintas.

3. **Compare against the current profile.**
   - Confirme padrões já observados.
   - Marque contradições, novos registros e possíveis mudanças de contexto.
   - Use níveis de confiança:
     - `tentativo`: uma amostra;
     - `provável`: duas amostras independentes;
     - `confirmado`: três ou mais amostras em contextos diferentes.
   - Não elevar um padrão pela repetição dentro do mesmo áudio.
   - Concluído quando cada novo traço tem evidência e confiança.

4. **Produce the requested artifact.**
   - Aplique o modo A, B ou C.
   - Preserve o significado antes de preservar bordões.
   - Use `humanizer` para remover simetria, clichês e linguagem genérica de IA.
   - Mostre a versão final ao usuário.
   - Concluído quando o texto soa natural em voz alta e não cria posições novas.

5. **Update the evidence log.**
   - Acrescente em `references/voice-evidence.md` apenas a data, o contexto, traços observados, confiança e uma paráfrase curta.
   - Não armazenar a transcrição completa.
   - Não registrar informações confidenciais que apareceram no áudio.
   - Concluído quando a evolução pode ser auditada sem expor o áudio original.

6. **Refine this skill when evidence changes behavior.**
   - Use `skill_manage(action="patch")` para adicionar, promover, rebaixar ou remover traços.
   - Atualize a versão:
     - patch para refinamento de evidência;
     - minor para novo modo ou mudança material no processo.
   - Remova redação substituída; não acumule regras duplicadas.
   - Não alterar a skill quando o áudio apenas confirma o perfil sem acrescentar comportamento útil.
   - Concluído quando o `SKILL.md` continua curto, coerente e sem contradições.

7. **Report the calibration delta.**
   - Informe ao usuário, em uma linha, o que o novo áudio confirmou ou mudou.
   - Se nada mudou, dizer que a amostra reforçou padrões existentes.
   - Não interromper a entrega principal com uma análise linguística extensa, salvo se solicitado.
   - Concluído quando o usuário sabe como a skill evoluiu.

## Writing Rules

- Priorize tese e mecanismo; corte introduções cerimoniais.
- Use “depende” somente quando vier seguido das variáveis relevantes.
- Preserve dúvidas reais em vez de fabricar respostas completas.
- Não transformar toda fala em framework, lista ou slogan.
- Evite vocabulário genérico de IA: “revolucionário”, “transformador”, “jornada”, “cenário em constante evolução”.
- Não usar “no final das contas” em todo texto só porque aparece na fala.
- Não terminar automaticamente com “é isso”, “enfim” ou CTA.
- Não imitar gagueira, erro de concordância ou erro do reconhecimento de voz.
- Não suavizar uma posição até ela perder conteúdo.
- Não intensificar uma posição para gerar engajamento.
- Quando houver afirmação forte sem fonte, usar primeira pessoa e enquadrá-la como opinião.

## Pitfalls

- **Caricatura:** repetir bordões, palavrões e conectores em excesso.
- **Esterilização:** remover toda franqueza e produzir voz corporativa genérica.
- **Sobreajuste:** concluir que um padrão é permanente após um áudio.
- **Confusão de tema e estilo:** tratar “agentes” como parte obrigatória da voz.
- **Certeza inventada:** completar uma dúvida de João com uma resposta plausível da IA.
- **Transcrição literal:** publicar todas as repetições e autocorreções.
- **Institucionalização indevida:** transformar opinião pessoal em posição da Dataceler.
- **Sedimento:** adicionar regras novas sem substituir versões antigas.
- **Exposição:** guardar áudio bruto, transcrição integral ou dados confidenciais dentro da skill.

## Verification

Antes de entregar um texto na voz de João, faça uma única revisão em voz alta e confirme: a tese continua sendo dele; fatos, opiniões e hipóteses estão separados; o ritmo soa conversacional sem virar transcrição bruta; termos técnicos permanecem naturais; a intensidade combina com o canal; não há bordões usados como decoração; e nenhuma certeza, experiência ou posição foi inventada.
