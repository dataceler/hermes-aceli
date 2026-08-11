---
name: third-party-api-integrations
description: Securely connect, validate, and operationalize third-party REST APIs and remote MCP servers in Hermes without leaking credentials or causing unintended writes.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [api, integrations, authentication, secrets, mcp, validation]
---

# Third-Party API Integrations

Use this skill when a user asks to connect Hermes to an external SaaS, infrastructure provider, REST API, or remote MCP server using an API key or token.

## Core principles

- Treat every supplied credential as a secret. Never repeat it in chat, logs, summaries, memory, or diagnostic output.
- Store secrets in `$HERMES_HOME/.env` (normally `~/.hermes/.env`) and enforce mode `600` on POSIX systems.
- Store stable non-secret endpoints separately, such as `SERVICE_BASE_URL`, preferably using HTTPS.
- Never send Bearer/API tokens over plain HTTP across a network. If discovery finds only HTTP, locate or request the HTTPS domain before authenticating.
- Use official documentation to determine base URLs, authentication headers, scopes, rate limits, and endpoints. Do not guess.
- Validate with an authenticated, read-only endpoint before declaring success.
- Return only minimal probe metadata: HTTP status, authentication result, resource count, and permission summary. Do not print customer data, meeting content, IPs, secrets, or full API responses unless requested.
- Do not claim a native Hermes integration exists merely because direct REST access works. State whether access is native tool, MCP, skill/script, or direct API.

## Workflow

1. **Discover support**
   - Check installed skills/plugins and Hermes docs for a native integration.
   - Check the provider's official API/MCP documentation.
   - Identify required inputs: token, base URL, team/workspace, scopes, and API version.

2. **Assess credential risk**
   - Determine whether the token is read-only, scoped, team-bound, or equivalent to full account permissions.
   - Prefer least-privilege tokens (`read` rather than `write`, `deploy`, `root`, or account-wide access).
   - If the token was pasted into chat, do not echo it; mention rotation only when chat export/sharing is a realistic risk.

3. **Resolve the endpoint safely**
   - Prefer a provider-owned HTTPS API endpoint.
   - For self-hosted services, inspect existing config and authorized infrastructure inventory to locate the instance.
   - Probe public health endpoints without authentication first.
   - If only `http://host:port` exists, do not transmit the token. Ask for an HTTPS domain or establish an explicitly authorized secure tunnel.

4. **Persist configuration**
   - Update one named variable in `.env` without overwriting unrelated lines.
   - Normalize base URLs by removing a trailing slash.
   - Apply mode `600` and verify only presence, never the value.
   - Avoid putting tokens directly in shell history or process arguments when a safer file-based flow is available.

5. **Validate read-only access**
   - Use `GET` against identity, teams, account, inventory, notes, or status endpoints.
   - Parse the response in-process and print only sanitized metadata.
   - Handle HTTP errors without dumping response headers or bodies that may contain sensitive context.
   - Retry transient/WAF failures once with the same documented headers that worked previously; capture the retry pattern, not the transient error.

6. **Operationalize**
   - If a native Hermes tool exists, verify Hermes recognizes it and document restart/reset requirements.
   - If the provider offers MCP, prefer the official remote MCP for first-class tools when it can consume secrets securely.
   - Do not duplicate secrets into `config.yaml` merely to populate MCP headers. Confirm environment interpolation support or use a secure wrapper/secret facility.
   - If only direct REST is available, state that future access will use authenticated API calls or offer to add a reusable provider reference/script.

7. **Verify and report**
   - Confirm file permission, HTTPS/TLS, endpoint, HTTP status, and read-only behavior.
   - Clearly state what was not changed.
   - Explain write/deploy/destructive permissions and require explicit user intent before using them.

## Common pitfalls

- **API key without a base URL:** common for self-hosted services. A token alone is insufficient; discover or request the instance URL.
- **Health success is not authentication success:** validate both public health/TLS and one authenticated read-only endpoint.
- **Resource list success does not imply least privilege:** some provider tokens inherit all owner permissions even when tested with `GET`.
- **MCP availability does not mean MCP is enabled:** self-hosted services may require a dashboard toggle and a token with specific permissions.
- **Restart requirements differ:** direct terminal/API use may work immediately, while gateway-native tools and MCP discovery usually require a gateway restart or fresh session.
- **Secret duplication:** `.env` plus literal YAML headers creates two secret copies. Avoid unless the system has no secure indirection and the user accepts the trade-off.
- **Enabled API is not authorized access:** for OAuth providers such as Google, project-level API enablement, credential project ownership, and token scopes are separate gates. Existing tokens do not gain newly enabled services automatically.
- **Multi-service checks can be shallow:** a generic live check may exercise only one endpoint. Validate each important service individually, using real read-only calls and sanitized output.
- **Helper CLI drift:** inspect the installed helper's `--help` before using optional flags from prose documentation; capture the supported invocation rather than repeatedly retrying an obsolete flag.
- **CLI installation mistaken for account access:** distinguish binary availability, integration configuration, authentication, and a verified API/MCP call. Do not declare a SaaS connected after only installing its CLI.
- **Headless OAuth hidden from the user:** persist remote MCP configuration before login, run OAuth in a tracked interactive process, and place the authorization URL in the user-visible message itself. For loopback callbacks on a remote host, use documented paste-back or an SSH tunnel; never retain transient authorization URLs or codes.

## Provider and operational references

- Granola API: `references/granola.md`
- Hostinger API: `references/hostinger.md`
- Coolify API and MCP: `references/coolify.md`
- Google OAuth gates, YouTube read-only, and efficient channel analysis: `references/google-oauth-youtube.md`
- Canva CLI vs design MCP, headless OAuth, and verified account access: `references/canva.md`
- Higgsfield CLI, headless loopback OAuth, billing-workspace selection, companion skills, and no-cost readiness checks: `references/higgsfield.md`
- vidIQ remote MCP, headless OAuth, least-privilege tool selection, credit-aware verification: `references/vidiq.md`
- Municipal NFS-e SOAP integration with ICP-Brasil A1/A3 certificates, XML signatures, homologation and fiscal confirmation gates: `references/nfse-soap-certificate-integration.md`
- Safe cross-platform bot avatar/name synchronization and destination-CDN verification: `references/bot-profile-media-sync.md`

Load the relevant reference before configuring or operating that provider or workflow.
