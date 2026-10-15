# Composio CLI: headless login and validation

## Scope

This reference covers the Composio CLI authentication pattern verified on Linux with CLI `0.4.3`. It does not configure a Composio Platform project key, a provider connection, or tool execution permissions.

## Safe browser handoff

```bash
composio login --no-wait
```

The command prints an official dashboard URL containing a short-lived CLI login key, then exits. Give that URL to the authorized human to complete login.

Start completion after the human handoff:

```bash
composio login --poll
```

The poll command uses the cached pending login key and completes once the browser authorization succeeds.

## Verify persisted session

Do not trust the login spinner or success banner alone. Run a harmless organization read:

```bash
composio orgs list
```

A successful response confirms that the CLI can use the stored user session. A `401 UserApiKey_Unauthorized` means the persisted session is invalid or revoked and must be replaced before performing CLI operations.

## Organization handling

The CLI can select the first available organization automatically. Confirm the selected organization is the intended tenant before using any organization-scoped command. To change only after explicit confirmation:

```bash
composio orgs switch --org-id <organization-id>
```

## Important boundaries

- CLI user login is distinct from a Platform `ak_...` project key used by an application SDK.
- A Gmail/provider connection may be active while a project API key still lacks session creation or tool-execution permission.
- Never paste a `uak_...` key into a shell command or store it in a repository. If an authorized user provides one for a recovery flow, keep it out of output and delete any temporary protected file immediately after use.
