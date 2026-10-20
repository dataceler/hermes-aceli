---
name: gmail-label-monitoring
description: "Use when safely monitoring Gmail and applying labels."
version: 1.0.0
author: Dataceler
license: MIT
created_by: agent
metadata:
  hermes:
    tags: [gmail, composio, monitoring, labels]
    related_skills: [composio]
---

# Monitoramento de Gmail com marcadores

## When to Use

Use quando for necessário monitorar uma Inbox e aplicar marcadores existentes conforme regras explicitamente aprovadas.

## Princípios

- Conecte a conta pelo Composio CLI autenticado; confirme leitura antes de agendar escrita.
- Liste os marcadores existentes por API e use IDs, não nomes, para aplicar labels.
- Nunca crie, remova, arquive, marque como lido, responda ou encaminhe mensagens sem autorização específica.
- Defina regras explícitas de classificação com o usuário; não deduza taxonomias por nomes ambíguos.
- Leia somente metadados necessários para classificar: remetente, destinatário, assunto e labels.

## Implementação segura

1. Consulte `GET https://gmail.googleapis.com/gmail/v1/users/me/labels` pelo `composio proxy` e mapeie nome → ID dos labels personalizados.
2. Liste Inbox pelo `GMAIL_FETCH_EMAILS` com `include_payload=false` e `verbose=false`.
3. No primeiro ciclo, grave apenas os IDs atuais em um arquivo de estado modo `600`; não classifique histórico implicitamente.
4. Nos ciclos seguintes, processe somente IDs ainda não vistos.
5. Aplique labels pelo `GMAIL_ADD_LABEL_TO_EMAIL` usando apenas `add_label_ids`.
6. Atualize o estado somente depois de processar o lote; preserve uma janela de IDs recente para deduplicação.
7. Remova artefatos temporários do Composio que contenham metadados após o processamento.

## Agendamento

- Use cron com `no_agent=true` e script determinístico.
- Entregue stdout somente quando houver rotulagem ou falha; saída vazia não gera ruído.
- Mantenha avisos de erro no canal de origem.
- Antes de declarar sucesso, execute uma rodada de baseline, confirme modo `600` do estado e valide que o cron aponta para o script correto.
