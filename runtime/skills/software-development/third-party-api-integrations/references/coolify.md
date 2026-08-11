# Coolify API and MCP

Official docs: `https://coolify.io/docs/`

## Required inputs

A Coolify token alone is insufficient. Obtain both:

- HTTPS instance URL, e.g. `https://coolify.example.com`
- API token containing the full `<id>|<secret>` form

Recommended variables:

- `COOLIFY_BASE_URL`
- `COOLIFY_API_TOKEN`

Normalize the base URL without a trailing slash.

## Connection and validation

- Public health endpoint: `GET /api/health` (outside `/api/v1`)
- API base: `<base>/api/v1`
- Authentication: `Authorization: Bearer <token>`
- Safe authenticated probe: `GET /api/v1/teams`

Validate in this order:

1. DNS/TLS and `GET /api/health` without the token.
2. Authenticated `GET /api/v1/teams`.
3. Return only HTTP status and number of visible teams.

A self-hosted instance may be discoverable at `http://host:8000`, but never transmit a Bearer token there over the public network. Check for an HTTPS dashboard domain or establish an explicitly authorized secure tunnel first.

## Permissions

Coolify tokens are team-bound. Current permission classes include:

- `read`: resources and inventory;
- `read:sensitive`: secrets, private keys, environment variables, logs, and other sensitive fields;
- `write`: create/update/delete;
- `deploy`: deployment actions;
- `root`: bypasses permission checks and has full API control.

Prefer `read` for assistant browsing. Extra permissions add risk and do not help the official read-oriented MCP tools.

## Official MCP

- Endpoint: `<base>/mcp`
- Transport: Streamable HTTP
- Header: `Authorization: Bearer <token>`
- API access and MCP server must both be enabled in Coolify settings.
- MCP tools are scoped to the token's team.

For Hermes native MCP, ensure the client can reference the token securely. Do not duplicate a token from `.env` as a literal `Authorization` header in `config.yaml` unless secure interpolation/secret injection is confirmed or the user accepts the duplicate-secret trade-off. Direct REST remains valid when MCP cannot consume the secret safely.

## Write safety

Require explicit intent before deploys, restarts, resource creation/update/deletion, API enable/disable, or MCP enable/disable. Enabling API or MCP programmatically may require `root` permission and should not be used merely as a connection test.
