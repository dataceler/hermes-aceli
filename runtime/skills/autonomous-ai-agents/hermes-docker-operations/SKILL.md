---
name: hermes-docker-operations
description: Use when operating Hermes in Docker with persistent config.
version: 0.1.0
author: Hermes Agent
created_by: agent
---

# Hermes Docker Operations

Use this skill when configuring, debugging, or extending a Hermes Agent gateway that runs in Docker. It prevents a common operational failure: changing a host-side Hermes profile while the active messaging gateway reads a different `HERMES_HOME` inside its container.

## Scope

Use for:

- Telegram, Discord, or other gateway behavior running in Docker;
- persistent configuration, skills, cron settings, or local providers;
- installing a local dependency used by the gateway;
- validating a feature from the same runtime that serves channel traffic.

Do not use for a plain non-container Hermes installation.

## Core rule: discover the effective runtime first

Before changing configuration, identify all of the following from the running container:

1. container name or ID;
2. gateway process and Python executable;
3. `HERMES_HOME` inside the process environment;
4. resolved config path via `hermes config path` inside the container;
5. persistent mounts via `docker inspect`.

Never assume the host CLI's `~/.hermes/config.yaml` is the configuration used by the messaging gateway. A host installation and a Docker installation may coexist with different homes, credentials, jobs, and channel state.

## Configuration procedure

1. Inspect the effective container runtime first.
2. Use the **container's** Hermes executable and `hermes config set` for non-secret settings.
3. Keep secrets in the container profile's `.env` or another approved secret store; do not put them in `config.yaml`, scripts, Git, or chat messages.
4. Re-read the relevant YAML section from the effective config path.
5. Restart the gateway only from a shell that is external to the gateway process when a reload is needed.
6. Validate the feature using the actual in-container implementation, not a similarly named host-side executable.

## Persistent local services and providers

For a dependency that the gateway needs at runtime:

1. Do not install it only into an ephemeral container layer if the image can be recreated.
2. Install its virtual environment, model cache, scripts, and other durable assets in a bind-mounted or named persistent volume.
3. Reference the in-container volume path in Hermes configuration.
4. Use a Hermes command-type provider when an external program accepts an input file and returns/writes a deterministic output.
5. Set explicit language/model/timeouts for speech or media providers; avoid relying on defaults that may be English-centric.

## STT command-provider pattern

For local speech-to-text where the gateway's built-in Python environment cannot retain the dependency:

```yaml
stt:
  enabled: true
  echo_transcripts: true
  provider: local-asr
  language: pt
  providers:
    local-asr:
      type: command
      command: "/persistent/scripts/transcribe.py {input_path} {output_path} --model {model} --language {language}"
      format: txt
      language: pt
      model: base
      timeout: 300
```

Requirements for the command script:

- read only the supplied `{input_path}`;
- write UTF-8 plaintext to `{output_path}`;
- write no credentials or raw audio to logs;
- keep model/cache paths within persistent storage;
- exit non-zero with concise errors when transcription fails.

See `references/persistent-local-stt.md` for the validated implementation pattern.

## Verification checklist

Before declaring success:

- [ ] the dependency imports from its persistent runtime;
- [ ] the model/cache is available in persistent storage;
- [ ] the configured command provider returns a transcript through `transcribe_audio()` inside the gateway container;
- [ ] the effective `config.yaml` contains the intended provider;
- [ ] a short inbound channel voice message has been tested after the gateway reload, when possible;
- [ ] no API tokens, private keys, signed URLs, or chat/session databases were copied into the persistent script or artifact.

## Pitfalls

- **Host/container profile mismatch:** a successful `hermes config set` on the host does not prove the Docker gateway changed.
- **Ephemeral installation:** a package installed in the running image can disappear after recreation.
- **False validation:** invoking a host-side transcription library does not verify the channel gateway's route.
- **Cloud fallback assumptions:** a configured cloud provider may be unavailable at runtime; local STT is a resilient fallback when privacy and predictable operating cost matter.
- **Overclaiming success:** internal dispatcher validation is strong but a live inbound voice note is the final end-to-end proof.
