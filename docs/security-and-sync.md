# Segurança e sincronização

## Escopo permitido para exportação

- `memories/MEMORY.md`
- `memories/USER.md`
- `cron/jobs.json`
- conteúdo de `skills/` que passe pelo verificador sanitário

## Exclusões obrigatórias

`.env`, `auth.json`, chaves, certificados, tokens, cookies, callbacks, `state.db`, `sessions/`, `logs/`, `cache/`, bancos de execução de cron e saídas de cron.

## Regras Git

- Deploy Key exclusiva e limitada ao repositório `dataceler/hermes-aceli`.
- `core.sshCommand` local ao repositório, sem alterar o SSH global.
- Nenhum `push` sem exportação e verificação bem-sucedidas.
- Nenhum `push --force`, reescrita de histórico ou alteração de permissões por automação.
- Commits devem referenciar a natureza da mudança, não dados sensíveis.

## Incidente

Se um segredo for detectado após commit: interromper sync, revogar o segredo, removê-lo do histórico com procedimento aprovado e registrar a causa sem reproduzir o valor.