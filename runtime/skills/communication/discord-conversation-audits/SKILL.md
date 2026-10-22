---
name: discord-conversation-audits
description: "Use for Discord conversation audits. Verify coverage."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [discord, audit, knowledge-management, privacy]
    related_skills: [hermes-agent]
---

# Auditorias de conversas no Discord

## When to Use

Use ao auditar canais, tópicos ou threads Discord acessíveis para consolidar contexto operacional, decisões, pendências e preferências de trabalho.

## Objetivo

Transformar histórico autorizado e acessível de um servidor Discord em contexto operacional pesquisável, sem alegar cobertura que não ocorreu, reter histórico bruto desnecessariamente ou executar ações de escrita/administração.

## Escopo e limites

- Audite somente servidores, canais, threads e mensagens aos quais o bot já tenha acesso legítimo.
- DMs privadas só entram no escopo se o bot já participar delas; nunca prometa acesso retroativo a mensagens privadas.
- Extraia decisões, responsáveis, preferências de trabalho, pendências, ideias recorrentes, discordâncias e critérios de decisão.
- Não grave o histórico bruto completo em memória permanente. Use um artefato privado pesquisável para evidência e salve em memória/skills somente aprendizados duráveis e não sensíveis.
- Mantenha ações de escrita e administração bloqueadas durante a auditoria: não enviar mensagens, criar tópicos, editar permissões, fixar, apagar ou alterar cargos.

## Procedimento

### 1. Definir cobertura antes de ler

1. Registre o objetivo, os participantes-alvo, os canais/categorias pretendidos e o tipo de síntese esperado.
2. Declare que a cobertura é limitada ao que o bot pode visualizar e ao histórico que a integração consegue buscar.
3. Para uma auditoria ampla, obtenha autorização explícita para examinar todos os canais e threads acessíveis; para escopos seletivos, preserve as exclusões.

### 2. Verificar pré-requisitos no Discord e no Hermes

1. Confirme no Discord que o **cargo já atribuído ao bot** tem **Ver canais** e **Ler histórico de mensagens** nas categorias relevantes; privilégios de categoria devem ser herdados pelos canais, com revisão apenas das exceções privadas. Ajustes no Developer Portal só definem permissões solicitadas em novos convites e não corrigem, por si só, o cargo de um bot já instalado.
2. Configure acesso por categoria, não por tópico individual, e revise somente canais ou threads privados, dessicronizados ou com negações explícitas; isso reduz erro operacional e evita abrir acesso além do escopo.
3. Confirme no Discord Developer Portal os intents **Server Members Intent** e **Message Content Intent**. Sem o segundo, mensagens podem chegar sem texto; sem o primeiro, a identificação por membro pode falhar.
4. Na sessão originada pelo Discord, confirme que as ações de leitura estão realmente disponíveis antes de iniciar: `list_guilds`, `list_channels`, `search_members` e `fetch_messages`.
5. Execute uma leitura histórica mínima no canal que disparou a auditoria e registre a contagem retornada antes de ampliar a varredura; a presença das ferramentas não prova que o cargo alcança o histórico.
6. Se qualquer ação não estiver disponível ou a leitura de teste não retornar histórico esperado, pare e informe "capacidade de leitura não validada". Não substitua histórico Discord por sessões locais, Telegram ou outras fontes sem rotulá-las claramente como fontes separadas.

### 3. Mapear e coletar com evidência de cobertura

1. Liste os servidores acessíveis e selecione o servidor autorizado.
2. Liste categorias, canais e threads acessíveis; registre os que foram excluídos por permissão ou escopo.
3. Localize o participante-alvo com busca de membros, validando identidade antes de atribuir mensagens.
4. Busque as mensagens por canal/thread em paginação até atingir o limite temporal ou o histórico disponível. Registre por fonte: identificador, nome, intervalo consultado, contagem lida e resultado da paginação.
5. Mantenha dados brutos em armazenamento privado com acesso restrito; produza um índice de mensagens ou trechos necessários para rastreabilidade, não uma cópia em memória persistente.

### 4. Sintetizar e validar

1. Separe **fatos observados**, **inferências** e **lacunas**.
2. Atribua cada decisão, pendência ou preferência à fonte correspondente (canal/thread e referência de mensagem, quando permitido).
3. Produza uma síntese operacional curta: decisões, projetos/responsáveis, pendências, critérios de decisão, preferências e riscos.
4. Declare cobertura real: canais mapeados, canais lidos, quantidade de mensagens, intervalo temporal, canais inacessíveis e limitações.

### 5. Encerrar ou monitorar corretamente

- Considere a auditoria concluída somente quando houver: mapa de canais acessíveis, identidade validada do participante, cobertura/contagem de mensagens lidas, síntese privada e limitações declaradas.
- Monitores de conclusão devem validar esses artefatos e métricas de cobertura; nunca use apenas o encerramento técnico de uma sessão (`ended_at`) como sinal de sucesso funcional.
- Se a sessão terminar sem coleta confirmada, classifique o resultado como **falha de cobertura**, pause alertas de conclusão e corrija os pré-requisitos antes de reiniciar.

## Checklist de saída

- [ ] Ações de leitura visíveis na própria sessão Discord.
- [ ] Servidor, categorias, canais e threads acessíveis mapeados.
- [ ] Participante-alvo identificado sem ambiguidade.
- [ ] Histórico consultado com paginação e contagem por fonte.
- [ ] Síntese distingue fatos, inferências e lacunas.
- [ ] Artefato privado pesquisável criado sem despejar conteúdo bruto na memória.
- [ ] Cobertura e exclusões declaradas.
- [ ] Nenhuma ação de escrita/administração executada.
