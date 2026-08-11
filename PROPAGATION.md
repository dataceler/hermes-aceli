# PROPAGATION — ciclo de continuidade

## 1. Captura

Decisões, pendências, preferências e procedimentos relevantes nascem no Hermes e são registrados no destino canônico.

## 2. Curadoria

Somente conhecimento durável entra em memória ou documentação. Conversa bruta, logs e material efêmero ficam fora.

## 3. Exportação sanitizada

`scripts/export_hermes_state.py` copia exclusivamente uma allowlist do runtime e gera um manifesto. Arquivos com indicadores de segredo são bloqueados.

## 4. Verificação

`scripts/verify_sanitized_export.py` deve passar antes de qualquer commit. Falha bloqueia publicação.

## 5. Commit e sync

Commits devem ser pequenos, descritivos e revisáveis. `push` é explícito; nunca há `push --force` nem sincronização silenciosa.

## 6. Poda

Diários, snapshots e material transitório passam por retenção. Conteúdo histórico vai para `archive/` ou é removido conforme política documentada.

## Restauração

A restauração é seletiva: recuperar um arquivo, skill ou definição de cron após inspeção. Nunca restaurar o diretório Hermes inteiro sobre um runtime em produção.
