# Hermes Aceli — fonte de verdade operacional

Repositório privado e sanitizado da Aceli, copiloto executivo e operacional da Dataceler.

## Finalidade

- preservar memória durável, skills, crons e documentação operacional;
- permitir revisão humana e restauração controlada;
- compartilhar contexto de trabalho entre Hermes na VPS e Claude Code quando necessário;
- manter uma trilha auditável de mudanças.

Este repositório **não é** uma cópia integral de `~/.hermes` e não substitui o runtime. Ele recebe somente artefatos permitidos pela política de exportação.

## Princípios

1. Uma fonte de verdade por assunto.
2. Nada relevante fica apenas no chat: decisões, pendências e procedimentos entram em artefatos revisáveis.
3. Nenhum segredo é versionado: credenciais, OAuth, chaves privadas, sessões, bancos, logs e URLs assinadas são proibidos.
4. Sincronização é explícita, auditada e reversível; nunca faz `push --force`.
5. O runtime continua sendo a configuração ativa da VPS; este repositório é o backup sanitizado e a base documental.

Veja [MAPA.md](MAPA.md) para a navegação e [docs/security-and-sync.md](docs/security-and-sync.md) para o contrato de segurança.
