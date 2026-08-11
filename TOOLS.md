# TOOLS — registro de integrações

Este arquivo registra somente a finalidade e o nível de acesso das integrações. Valores de autenticação ficam fora do Git.

| Integração | Finalidade | Acesso permitido |
|---|---|---|
| GitHub | Backup sanitizado e projetos Dataceler | Deploy Key exclusiva por repositório; menor privilégio |
| Google Workspace | Agenda, Drive, Docs e Sheets | Leitura controlada conforme escopo aprovado |
| Hostinger / Coolify | Visibilidade operacional | Leitura controlada |
| Canva / vidIQ | Operação editorial | OAuth e permissões restritas |

Qualquer nova integração exige documentação de propósito, escopo e método de revogação.