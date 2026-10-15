---
name: cli-authentication
description: "Use when authenticating a CLI to a third-party service."
version: 1.0.0
author: Aceli
created_by: agent
---

# CLI Authentication

## Purpose

Authenticate command-line clients to third-party services safely, especially on headless servers. Prefer short-lived browser/device flows and verify the saved session with a harmless authenticated read after login.

Use this skill for provider CLIs, cloud dashboards, SaaS tools, SDK command lines, and agent integrations that need a human account authorization.

## Operating principles

1. **Start with the least-privilege path.** Prefer a browser or device authorization flow over copying long-lived API keys.
2. **Never request, repeat, echo, or embed credentials in a command line.** Command-line arguments can leak through process inspection, terminal history, CI logs, and audit trails.
3. **Inspect `--help` before choosing a login mode.** Login behavior and flags differ by CLI version.
4. **Use the CLI's authenticated read command as proof.** A success message alone is not proof that credentials were persisted or remain valid.
5. **Separate account login from application credentials.** A human CLI session, a project API key, and an OAuth connection can be distinct security domains; do not assume one authorizes the others.
6. **Treat a credential shared in chat as exposed.** Continue only when the user explicitly directs its use, avoid reproducing it, and recommend rotation after the immediate task.

## Headless browser-login workflow

1. Run `<tool> login --help` and identify options for non-browser, no-wait, device code, or polling flows.
2. If the CLI supports a no-wait flow, run it to obtain an explicit URL or device code. Do not use a background interactive spinner if it hides the handoff link.
3. Give the user only the official URL/code and tell them to authenticate with the intended organization/account.
4. Start the CLI's poll/completion command in the background when it has a bounded wait. Confirm the process exit status.
5. Run a harmless authenticated read operation, such as listing organizations, current account, or profile metadata.
6. Report the selected organization/account, not tokens, session files, cookies, or raw API responses.

## API-key login workflow

Use only when the CLI explicitly supports a user/API-key login and browser authentication is unavailable or unsuitable.

1. Prefer a protected secret store or environment variable supported natively by the CLI.
2. If no native safe input path exists, store the secret in a root/user-only temporary file (`0700` directory, `0600` file), invoke the CLI without printing the secret, and remove the temporary file with a cleanup trap.
3. Validate with a safe authenticated read.
4. Confirm deletion of the temporary secret file.
5. Recommend rotating a key that was shared through chat or another broad-audience channel.

## Failure diagnosis

- **Login command says success but authenticated read returns 401/unauthorized:** the persisted credential is invalid, revoked, or scoped to a different account. Do not treat login output as final. Re-authenticate with the intended credential path, then rerun the safe read.
- **Installer is blocked by a missing prerequisite:** install only the specific documented prerequisite, retry the official installer, and verify the CLI version before login.
- **A browser URL was not shown by an interactive login:** consult `--help` and choose the CLI's no-wait/device flow rather than guessing URLs.
- **Multiple organizations appear:** retain the selected organization only after verifying it is the requested tenant. Do not switch organizations implicitly.

## Completion checklist

- [ ] CLI version is confirmed.
- [ ] Authentication used an approved account and organization.
- [ ] A safe authenticated read succeeded after login.
- [ ] No token/key was displayed in output or committed to a repository.
- [ ] Any temporary secret file was removed and its deletion verified.
- [ ] The user knows whether the CLI session, project key, and provider OAuth connection are separately configured.

## References

- `references/composio-headless-login.md` — verified Composio CLI headless login and validation pattern.
