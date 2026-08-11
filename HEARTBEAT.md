# HEARTBEAT — checklist operacional

## Diário

- [ ] Cronjobs críticos tiveram execução e entrega bem-sucedidas.
- [ ] Nenhum backup falhou ou incluiu arquivo fora da allowlist.

## Semanal

- [ ] Executar exportação sanitizada e revisar `reports/audits/`.
- [ ] Revisar pendências em `memory/context/` e `memory/projects/`.
- [ ] Conferir se a Deploy Key continua limitada a este repositório.

## Mensal

- [ ] Revisar acessos GitHub, integrações e revogações necessárias.
- [ ] Aplicar poda de material transitório e verificar crescimento do repositório.
- [ ] Testar restauração seletiva em diretório temporário.

Nenhuma tarefa de heartbeat pode imprimir ou registrar segredos.