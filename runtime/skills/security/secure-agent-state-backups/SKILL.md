---
name: secure-agent-state-backups
description: "Use when backing up agent state safely to version control."
version: 0.1.0
author: Aceli
created_by: agent
---

# Secure Agent-State Backups

Use when an AI agent’s memories, skills, schedules, project context, or operational documentation must be versioned to a private Git repository without exposing credentials or replacing the live runtime blindly.

## Outcome

Produce a reviewable, restorable, least-privilege backup repository that holds curated agent state — not a raw copy of the agent home directory.

## Core model

- **Runtime:** the live agent installation and its active configuration.
- **Repository:** a sanitized source of truth for durable knowledge, procedures, cron definitions, documentation and audited snapshots.
- **Restore:** selective and reviewed; never overwrite a production runtime wholesale.

## Procedure

1. **Inspect before writing**
   - Confirm the remote repository exists, its ownership/visibility, default branch, and whether it already contains files.
   - Identify the actual agent home(s). Dockerized gateways can have a different `$HERMES_HOME` from the shell host.
   - Never infer that a host CLI configuration controls the container runtime.

2. **Choose the access boundary**
   - One backup repository: create a dedicated Ed25519 Deploy Key for that repository only.
   - Multiple repositories or organization-wide work: use a private GitHub App with repository-scoped, minimal permissions and short-lived tokens.
   - Never reuse an existing Deploy Key. GitHub associates a deploy key with a single repository.
   - Keep the private key outside Git with restrictive filesystem permissions. Share only the public key for GitHub registration.

3. **Scope Git per repository**
   - Configure the remote and `core.sshCommand` in the repository’s local Git config, using `IdentitiesOnly=yes` and the dedicated key.
   - Do not modify global SSH URL rewriting or make a repository-specific key the default for every GitHub remote.
   - Test read access with `git ls-remote origin HEAD` before relying on the connection.

4. **Build a curated structure**
   - Root contract: identity, agent rules, user-approved context, integration catalog, map, propagation protocol, heartbeat and README.
   - Durable domains: `memory/`, `projects/`, `skills/`, `reports/`, `docs/`, `archive/`, and `scripts/`.
   - Runtime export: isolate under `runtime/` and mark it as generated. Do not edit exported artifacts manually.
   - Document a canonical location for each type of knowledge.

5. **Export only an allowlist**
   - Typical allowlist: durable memory files, selected cron job definitions, and versionable skill source files.
   - Exclude `.env`, `auth.json`, credentials, tokens, cookies, private keys, certificates, state databases, sessions, logs, caches, signed URLs, cron execution databases and job output.
   - Exclude internal backup/cache directories such as hidden curator snapshots from the canonical export.
   - Generate a manifest listing copied and blocked paths, without copying secret values.

6. **Audit before staging**
   - Run a deterministic scanner for forbidden paths and high-confidence secret signatures (private-key blocks, GitHub tokens, API-key assignments).
   - Treat scanner matches conservatively: block and review rather than publish a questionable file.
   - Verify the export has non-zero expected content. A successful scanner alone does not prove the exporter selected the correct source.
   - When exported skills are exact third-party/runtime mirrors, preserve them as vendored content with `.gitattributes` (for example, `runtime/skills/** -whitespace linguist-vendored`). Run whitespace checks strictly on hand-authored control-plane files while the secret scanner still covers the entire repository; never mass-reformat mirrored source just to quiet a diff check.
   - Inspect `git status` and `git diff --cached` before committing.

7. **Commit and publish deliberately**
   - Make commits small and descriptive.
   - Do not use `push --force`, auto-merge or silent publication.
   - First push occurs only after remote access, sanitization and staged diff have all been verified.
   - Scheduled backups should call the export + audit steps first and fail loudly on violations; automatic push needs explicit user approval.

8. **Test restoration**
   - Restore into an isolated temporary directory.
   - Verify individual files/skills/cron definitions before importing into a live agent.
   - Record restoration evidence in an audit report.

## Pitfalls

- A service restarted by a host CLI may not be the Dockerized service receiving messages; inspect the actual container start time and `$HERMES_HOME`.
- Do not copy an example repository’s root files mechanically. Recreate the structure with the current agent’s identity and security boundaries.
- A repository can be private and still be unsafe for unreviewed credentials; private is not a substitute for exclusion and scanning.
- A private Deploy Key with write access is appropriate only for its single intended backup repository, never for broad organization access.

## Verification checklist

- [ ] Remote access succeeds with the dedicated key.
- [ ] Key is repository-scoped and private material is not versioned.
- [ ] Allowlist export creates expected durable artifacts.
- [ ] Forbidden paths and secret patterns are absent from staged content.
- [ ] Generated runtime material is clearly separated from hand-authored documentation.
- [ ] Initial commit and remote state are read back after publication.
- [ ] Selective restore is tested before relying on the backup.

See `references/hermes-github-export.md` for a concise implementation contract for Hermes installations.
