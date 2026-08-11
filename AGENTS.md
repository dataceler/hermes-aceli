# AGENTS.md — contrato de trabalho

## Ordem de leitura

1. `SOUL.md` — identidade e princípios.
2. `USER.md` — preferências operacionais autorizadas.
3. `MAPA.md` — onde cada artefato vive.
4. `docs/security-and-sync.md` — fronteiras de segurança.
5. O contexto do projeto em `projects/<projeto>/` antes de alterar código ou documentação.

## Regras

- Trabalhe em branches para mudanças substanciais; não force-push.
- Antes de commitar, execute `scripts/verify_sanitized_export.py`.
- Não adicione arquivos fora da allowlist de `runtime/`.
- Não copie `.env`, chaves, OAuth, sessões, bancos, caches ou logs.
- Registre decisões e pendências no local temático apropriado, não apenas em conversas.
- O conteúdo de `runtime/` é exportado do Hermes e não deve ser editado manualmente sem motivo documentado.
