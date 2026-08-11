# Higgsfield CLI — configuração segura e validação

Use este fluxo quando o usuário pedir geração de imagens, infográficos ou vídeos pelo Higgsfield CLI em uma máquina remota/headless.

## Instalação

```bash
npm i -g @higgsfield/cli
higgsfield --version
higgsfield auth login --help
```

Não presuma o nome do binário nem os subcomandos antes de verificar a versão instalada.

## OAuth headless com callback loopback

1. Inicie `higgsfield auth login --no-color` em processo interativo rastreado e mantenha-o aberto.
2. Entregue ao usuário a URL de autorização impressa pela própria CLI.
3. O callback padrão aponta para `http://localhost:8765/callback`. Em um VPS, há duas rotas válidas:
   - criar no computador do usuário um túnel `ssh -N -L 8765:127.0.0.1:8765 <vps>` antes de abrir a URL; ou
   - se o usuário enviar a URL completa do callback, encaminhá-la uma única vez ao listener local `127.0.0.1:8765` enquanto o processo ainda estiver aguardando.
4. Nunca repetir, salvar em arquivos, memória ou resumos o `code`, `state`, token ou URL completa do callback. Trate-os como credenciais efêmeras.
5. Confirme no processo original a mensagem de autenticação concluída e `exit 0`.
6. Verifique a existência do token sem imprimi-lo: `higgsfield auth token >/dev/null`.

Se o processo expirar ou encerrar, inicie um novo login. Não reutilize callback antigo.

## Workspace de cobrança

Autenticação não significa geração pronta. `higgsfield account status` pode falhar com `No workspace selected` mesmo quando `model list` funciona.

```bash
higgsfield workspace list --json
higgsfield workspace status --json
higgsfield account status --json
```

- Exatamente um workspace: selecione-o automaticamente com `higgsfield workspace set <id>`.
- Mais de um workspace: peça ao usuário para escolher, pois isso define onde os créditos serão consumidos.
- Não exponha IDs, e-mail, saldo detalhado ou resposta completa quando bastar informar status autenticado, plano/saldo presente e quantidade de recursos.

## Companion skills

Instalação não interativa para o conjunto oficial:

```bash
npx skills add higgsfield-ai/skills --yes --global
```

A execução sem `--yes --global` pode parar na interface de seleção sem instalar nada. O instalador também pode reportar falhas para agentes não suportados (por exemplo, PromptScript) embora a instalação e os symlinks do Hermes tenham sido concluídos. Verifique o destino específico, não apenas o resumo agregado:

- diretórios em `~/.agents/skills/higgsfield-*`;
- symlinks correspondentes em `~/.hermes/skills/higgsfield-*`;
- reconhecimento pela listagem de skills do Hermes.

Skills externas executam com permissões do agente. Carregue e revise a skill relevante antes de cada classe de geração, especialmente quando o scanner do instalador sinalizar risco.

## Verificação sem consumir créditos

Não gere mídia paga apenas para provar instalação. Valide, em ordem:

1. `higgsfield --version`;
2. token disponível sem imprimir;
3. workspace selecionado;
4. `higgsfield account status --json` com sucesso;
5. `higgsfield model list --image --json` e `--video --json`;
6. contrato do modelo pretendido, por exemplo `higgsfield model get gpt_image_2 --json`.

Uma geração real só é necessária quando o usuário pediu um artefato ou autorizou explicitamente o consumo.

## Critério de pronto

Declare a integração pronta somente quando CLI instalada, OAuth concluído, workspace selecionado, conta autenticada, companion skills reconhecidas e ao menos um contrato de modelo validado. Diferencie claramente CLI/skills de MCP; instalar a CLI não configura um servidor MCP.