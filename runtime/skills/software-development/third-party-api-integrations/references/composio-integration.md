# Composio — safe Platform integration and first-call proof

Use this reference when a user provides a Composio key, asks to integrate Composio into an agent/application, or asks for an MCP connection to Composio.

## Route before configuring

Composio has two distinct products. Do not mix their credentials or setup:

- `ak_...` project keys indicate **Composio Platform**: an application/agent uses sessions for its own users.
- `ck_...` keys indicate **Composio For You**: a personal agent connects the user's own apps.

For Platform work, inspect the real repository before changing code. Identify the language, dependency manager, current agent/tool loop, stable user or tenant identifier, and secret-loading mechanism. If no codebase is available at the stated working directory, ask for the repository path and the first target integration; do not fabricate a demo app or placeholder identity.

## Current Platform model

- Use the current `composio` SDK. `composio-core` is legacy and does not support the current Sessions flow.
- A Platform key belongs in the codebase's existing secret mechanism as `COMPOSIO_API_KEY`; never print it, put it in source, URLs, logs, or `config.yaml`.
- The runtime unit is a session bound to the application's stable user ID. Reuse a persisted session ID in multi-turn flows instead of creating a new session per request.
- A generic session exposes discovery and connection-management meta tools. Do **not** register that broad session as a Hermes MCP by default: it can surface access to many third-party apps.

## Least-privilege first integration

1. Ask or discover the exact target toolkit; never invent a toolkit or tool slug.
2. Prefer one read-only action for the first proof (for example, a small account/profile/list query), not a write, send, publish, delete, or financial action.
3. If the target account is not connected, use the Connect Link returned by Composio. Do not create a separate OAuth flow or ask for provider passwords/tokens in chat.
4. For a fixed, narrow agent, configure a direct-tools session with an explicit allowlist only after discovering the provider's exact tool identifiers. Keep connection management enabled if the user must authorize an account through the agent.
5. Only configure a hosted session MCP after its tools and account scope are deliberately constrained. Store its URL/headers as secrets; do not duplicate them in source control.

## What counts as working

SDK installation, key presence, session creation, tool search, schema retrieval, and a Connect Link do **not** prove an integration works. Declare success only when a safe, provider-backed, read-only tool call returns a real result from the user's connected account and yields a non-empty Composio log/request ID. Report only minimal result metadata and the log ID; never show raw provider data unless requested.

## Canonical sources

Before using version-sensitive code or option names, consult:

- https://docs.composio.dev/docs/quickstart.md
- https://docs.composio.dev/docs/sessions-via-mcp.md
- https://docs.composio.dev/docs/configuring-sessions.md
- https://docs.composio.dev/docs/providers.md
