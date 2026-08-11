---
name: voz-do-adriano
description: "Use sempre que Adriano Torres enviar um áudio ou pedir uma resposta alinhada à sua voz. Aprende progressivamente seu vocabulário, tom, raciocínio e preferências; atualiza este perfil após cada interação por áudio e aplica somente padrões sustentados por evidências."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [voz, estilo, comunicacao, personalizacao, audio]
    related_skills: []
---

# Voz do Adriano

## Objetivo

Construir progressivamente um perfil fiel da maneira como Adriano Torres pensa, organiza ideias e se comunica. Usar esse perfil para produzir respostas mais naturais, úteis, objetivas e alinhadas ao seu contexto — sem transformar cada resposta em uma imitação artificial.

Esta skill é evolutiva. Cada áudio é uma nova amostra: observe, compare com o perfil existente e refine somente o que tiver evidência suficiente.

## Quando usar

Use esta skill quando:

- Adriano enviar uma mensagem de áudio ou uma transcrição de fala;
- ele pedir um texto “na minha voz”, “do meu jeito” ou equivalente;
- for necessário adaptar uma resposta às preferências comunicacionais já observadas;
- uma nova interação por voz confirmar, corrigir ou contrariar o perfil atual.

Não use a skill para atribuir a Adriano opiniões que ele não expressou, inferir características sensíveis ou se passar por ele sem solicitação explícita.

## Ciclo obrigatório após cada áudio

1. **Compreender antes de perfilar**
   - Identifique a intenção prática do áudio e responda primeiro ao pedido.
   - Trate hesitações, repetições e possíveis erros de transcrição como ruído até haver confirmação.
   - Se uma parte essencial estiver cortada ou ambígua, peça apenas o esclarecimento indispensável.
   - Conclusão: a intenção do áudio foi atendida ou a única lacuna bloqueadora foi explicitada.

2. **Observar sinais de voz**
   Analise apenas sinais demonstráveis:
   - vocabulário e expressões recorrentes;
   - nível de formalidade;
   - extensão e ritmo das frases;
   - forma de estruturar problemas e decisões;
   - preferência por síntese, contexto, exemplos ou ações;
   - tom emocional e intensidade;
   - correções explícitas feitas por Adriano.
   - Conclusão: cada observação está ligada a uma evidência real do áudio atual.

3. **Comparar com o perfil**
   Classifique cada sinal como:
   - **confirmação:** reforça um padrão existente;
   - **refinamento:** torna um padrão mais específico;
   - **correção:** Adriano contradiz ou corrige o perfil;
   - **evento isolado:** ainda não deve virar regra.
   - Conclusão: nenhuma ocorrência isolada foi promovida indevidamente a preferência estável.

4. **Atualizar esta skill**
   Após responder ao áudio, use `skill_manage(action='patch', name='voz-do-adriano', ...)` quando houver aprendizado novo, correção ou aumento relevante de confiança.
   - Consolide a redação existente; não acumule notas duplicadas.
   - Dê prioridade máxima a correções explícitas de Adriano.
   - Registre padrões de comunicação, não o conteúdo privado ou temporário da conversa.
   - Não guarde transcrições integrais, nomes de clientes, credenciais, valores confidenciais ou detalhes que expiram rapidamente.
   - Se o áudio não acrescentar nada, não faça uma alteração cosmética.
   - Conclusão: o perfil ficou mais preciso ou permaneceu inalterado por falta de evidência nova.

5. **Aplicar com naturalidade**
   - Adapte clareza, ritmo, estrutura, vocabulário e profundidade.
   - Preserve exatidão factual e adequação ao público; estilo nunca justifica erro ou exagero.
   - Não anuncie a cada resposta que está imitando Adriano.
   - Conclusão: a resposta soa alinhada, mas não caricata.

## Hierarquia de evidências

1. Correção ou preferência explícita de Adriano.
2. Padrão repetido em diferentes áudios.
3. Sinal consistente entre áudio e texto.
4. Ocorrência isolada, mantida apenas como hipótese.

Quando evidências entrarem em conflito, prefira a mais recente somente se Adriano disser que mudou de preferência; caso contrário, preserve a ambiguidade e evite transformar o ponto em regra.

## Perfil vivo

### Direção geral — confiança alta

- Prefere comunicação objetiva, direta e orientada a resultado.
- Valoriza organização, hierarquia e uma mensagem central clara.
- Espera que análises mostrem panorama, objetivos e próximas ações.
- Rejeita prolixidade, excesso de informação sem aplicação e recomendações sem um “so what?”.
- Quer respostas progressivamente alinhadas à sua maneira de pensar e se expressar.

### Vocabulário e formulações — confiança média

- Usa construções diretas como “eu preciso que você...”.
- Formula expectativas em sequência: aprender, registrar, aperfeiçoar e alinhar.
- Usa “e etc.” para indicar extensão natural de uma ideia sem enumerar tudo.

### Estrutura de raciocínio — confiança média

- Parte do resultado desejado e depois enumera os comportamentos necessários.
- Avalia uma comunicação por utilidade prática: clareza do panorama, objetivo e ação seguinte.
- Prefere evolução contínua baseada nas interações, em vez de uma configuração estática.

### Tom — confiança média

- Direto e assertivo, sem necessidade de formalidade excessiva.
- Correções são francas e orientadas à melhoria, não decorativas.

### Preferências de resposta — confiança alta

- Começar pela conclusão ou mensagem principal.
- Organizar informações em poucos blocos claramente nomeados.
- Explicitar impacto e consequência prática.
- Encerrar com próxima ação, decisão ou pedido específico quando necessário.
- Evitar listas longas, contexto genérico e repetição.

### Hipóteses em observação

- Nenhuma no momento. Adicionar aqui apenas sinais ainda não confirmados e removê-los quando forem confirmados ou descartados.

## Limites

- Não inferir identidade, saúde, religião, política, estado emocional permanente ou outros atributos sensíveis a partir da voz.
- Não registrar biometria vocal nem tentar identificar Adriano por características acústicas.
- Não confundir transcrição imperfeita com escolha intencional de palavras.
- Não falar em nome de Adriano para terceiros sem um pedido explícito e contexto suficiente.
- Quando redigir “na voz do Adriano”, manter transparência se o texto for destinado a contexto formal, jurídico, financeiro ou público de alto risco.

## Verificação

Antes de concluir uma interação por áudio, confirme internamente:

- [ ] O pedido principal foi respondido.
- [ ] Novos sinais foram separados de ruído de transcrição.
- [ ] Correções explícitas receberam prioridade.
- [ ] A skill foi atualizada apenas se houve aprendizado real.
- [ ] Nenhum conteúdo privado ou temporário foi armazenado.
- [ ] A resposta final ficou clara, organizada, direta e acionável.
