# Canva CLI, MCP de designs e OAuth headless

## Finalidade

Use esta referência quando o usuário pedir que Hermes “instale o Canva CLI”, “acesse o Canva” ou crie, edite, procure ou exporte designs no Canva. Não trate instalação do binário como acesso autenticado à conta.

## Escolha correta da integração

Existem três superfícies diferentes:

1. **`@canva/cli`** — CLI oficial para desenvolver e gerenciar aplicativos Canva. Instalação:

   ```bash
   npm install -g @canva/cli@latest
   canva --version
   canva --help
   ```

2. **`canva mcp` / Canva Dev MCP** — assistência para desenvolver apps e integrações Canva. Não é o conector principal para criar e editar designs da conta do usuário.

3. **Canva MCP remoto** — endpoint oficial para design generation/editing, busca, ativos, pastas, exportação e comentários:

   ```text
   https://mcp.canva.com/mcp
   ```

Para operar designs a partir do Hermes, prefira o MCP remoto autenticado por OAuth.

## Procedimento no Hermes

### 1. Verificar o runtime e o pacote

```bash
node --version
npm --version
npm view @canva/cli version engines --json
npm install -g @canva/cli@latest
canva --version
```

Use os requisitos atuais publicados no pacote; não grave uma versão de Node como regra permanente.

### 2. Persistir o MCP antes do OAuth

Em VPS/headless, `hermes mcp add` pode iniciar OAuth durante o probe e terminar sem salvar quando o fluxo interativo não é concluído. Separe configuração e login:

```bash
hermes config set mcp_servers.canva.url https://mcp.canva.com/mcp
hermes config set mcp_servers.canva.auth oauth
hermes config set mcp_servers.canva.connect_timeout 300
hermes config check
hermes mcp list
```

O resultado esperado é `canva` habilitado com transporte HTTPS. Isso prova apenas configuração, não autenticação.

### 3. Executar OAuth interativamente

```bash
hermes mcp login canva
```

Em automação, execute em PTY rastreável. Extraia a URL de autorização e mantenha o processo vivo enquanto o usuário aprova.

Em host remoto, use uma das opções oficiais:

- **paste-back:** o usuário abre a URL, aprova, copia o URL final `http://127.0.0.1:<porta>/callback?code=...&state=...` e o agente o envia ao prompt do processo;
- **túnel SSH:** encaminhar a porta de callback do computador do usuário para o loopback da VPS.

A URL de autorização e o código de callback são efêmeros. Não os salve em memória, skills ou arquivos duráveis.

### 4. Comunicação em Telegram ou outro gateway

- Coloque o link OAuth na mensagem que o usuário realmente receberá; não o deixe somente em progresso de ferramenta ou texto transitório antes de um prompt de esclarecimento.
- Apresente um link rotulado e, se a plataforma puder ocultá-lo, também o URL bruto em uma linha própria.
- Diga que um erro ao abrir `127.0.0.1` é esperado no fluxo paste-back.
- Se não houver redirecionamento, peça o texto exato exibido; não reinicie fluxos repetidamente sem diagnosticar.
- Cada nova tentativa gera porta, `state` e desafio PKCE diferentes; nunca reutilize um link expirado.

### 5. Verificar acesso

Após o OAuth:

```bash
hermes mcp test canva
hermes mcp list
```

Confirme que o arquivo de token existe com modo `0600` sem imprimir seu conteúdo. Inicie uma sessão nova ou use o mecanismo de reload documentado pelo Hermes para expor as ferramentas descobertas.

A primeira validação operacional deve ser de leitura, por exemplo buscar ou listar designs recentes, e deve retornar apenas metadados sanitizados. Só então execute criação ou edição solicitada pelo usuário.

## Escopo e segurança

O Canva MCP pode solicitar permissões de leitura e escrita para designs, ativos, pastas, comentários, templates e marca. Explique o escopo antes da autorização quando ele for materialmente amplo.

- Criar ou editar algo pedido pelo usuário é uma escrita autorizada dentro desse pedido.
- Não excluir, compartilhar, publicar, mover em massa ou alterar ativos de marca sem intenção explícita.
- Não afirmar “Canva conectado” até o OAuth e uma chamada real terem sido verificados.
- Não confundir CLI instalado, MCP configurado, OAuth concluído e acesso operacional validado; são quatro estados distintos.

## Diagnóstico rápido

| Sintoma | Interpretação | Correção |
|---|---|---|
| `canva --version` funciona | CLI instalado | Ainda falta MCP/OAuth para designs |
| MCP aparece habilitado | Configuração persistida | Ainda falta token e chamada real |
| HTTP 401 no probe | Endpoint exige OAuth | Executar `hermes mcp login canva` |
| Callback aponta para loopback da VPS | Fluxo headless normal | Usar paste-back ou túnel SSH |
| `mcp add` termina sem servidor salvo | Probe/OAuth interrompeu o salvamento | Persistir com `hermes config set`, depois fazer login |
| Usuário não encontra o link | Link ficou em saída transitória ou não renderizou | Reenviar em mensagem visível e como URL bruto |

## Fontes oficiais

- Canva MCP: `https://www.canva.dev/docs/mcp/`
- Canva Dev MCP: `https://www.canva.dev/docs/connect/mcp-server/`
- Hermes MCP: `https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/`
