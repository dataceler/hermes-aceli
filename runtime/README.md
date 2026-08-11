# runtime/ — exportação sanitizada

Esta pasta é preenchida por `scripts/export_hermes_state.py` a partir de um Hermes selecionado.

Conteúdo permitido:

- `memories/` — memória durável sanitizada;
- `cron/jobs.json` — definição de cronjobs sem bases de execução;
- `skills/` — procedimentos versionáveis que tenham passado no scanner;
- `manifest.json` — relatório de origem, arquivos copiados e arquivos bloqueados.

Não editar arquivos exportados diretamente. Corrija a fonte ou registre uma decisão em `memory/`/`projects/`, então exporte novamente.