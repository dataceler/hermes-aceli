# Hermes → private GitHub backup: implementation contract

## Detection

Before configuring backup, inspect both the shell environment and the message-serving runtime:

```bash
printf 'host_home=%s\n' "${HERMES_HOME:-$HOME/.hermes}"
docker ps --format '{{.Names}} {{.Status}}'
docker inspect -f 'started={{.State.StartedAt}} running={{.State.Running}}' <container>
docker exec <container> sh -lc 'printf "container_home=%s\n" "$HERMES_HOME"'
```

A Docker gateway commonly uses `/opt/data`, while the host CLI defaults to `~/.hermes`. Back up the intended source explicitly; do not assume they are identical.

## Least-privilege key setup

```bash
umask 077
ssh-keygen -t ed25519 -C 'agent-backup@organization' -f ~/.ssh/agent-backup_ed25519 -N ''
chmod 600 ~/.ssh/agent-backup_ed25519
```

Register only `~/.ssh/agent-backup_ed25519.pub` as a Deploy Key in the target repository. For write-backed backups, enable write access there; do not distribute the private key or reuse an existing key.

Repository-local configuration:

```bash
git -C /srv/agent-backup init --initial-branch=main
git -C /srv/agent-backup remote add origin git@github.com:OWNER/REPOSITORY.git
git -C /srv/agent-backup config core.sshCommand 'ssh -i ~/.ssh/agent-backup_ed25519 -o IdentitiesOnly=yes'
git -C /srv/agent-backup ls-remote origin HEAD
```

## Recommended export allowlist

- `memories/MEMORY.md`
- `memories/USER.md`
- `cron/jobs.json`
- text-based skill source (`SKILL.md`, references, templates and scripts) after a secret scan

## Mandatory exclusions

- `.env`, `auth.json`, credential stores, tokens, cookies, OAuth callbacks
- SSH private keys, `.pem`, `.key`, certificates
- `state.db`, `sessions/`, `logs/`, `cache/`
- cron execution/history databases and output directories
- hidden backup snapshots inside skill-curator directories

## Release gate

1. Export to `runtime/`.
2. Generate a non-sensitive manifest: copied count, blocked count and reasons.
3. Scan the repository for forbidden files and high-confidence secret signatures.
4. Inspect staged diff.
5. Commit and push only after all checks pass and the user has approved the publish scope.

## Recurrent backup

A scheduled job may execute export + scanner. Keep `git push` a deliberate, separately approved policy decision unless the user explicitly authorizes automated publication.
