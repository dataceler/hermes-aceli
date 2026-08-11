# Local STT persistente em gateway Hermes Docker

## Objetivo

Usar Whisper local para mensagens de voz quando a transcrição deve sobreviver à recriação do contêiner e não depender de uma credencial cloud em tempo de execução.

## Padrão validado

1. Crie um ambiente virtual em um volume persistente, não na camada da imagem.
2. Instale `faster-whisper` nesse ambiente.
3. Armazene o cache do modelo no mesmo volume persistente.
4. Crie um script executável que:
   - recebe o áudio e o caminho de saída como argumentos;
   - define `HF_HOME` para o volume persistente;
   - carrega `WhisperModel` com `device="cpu"` e `compute_type="int8"`;
   - usa `language="pt"`, `vad_filter=True` e `condition_on_previous_text=False`;
   - escreve transcrição UTF-8 em texto simples.
5. Registre o script como um provedor `stt.providers.<nome>` do tipo `command`.
6. Faça o teste via `tools.transcription_tools.transcribe_audio()` **dentro do contêiner** e usando o `HERMES_HOME` efetivo.

## Exemplo de execução do script

```text
/persistent/scripts/transcribe.py {input_path} {output_path} \
  --model {model} --language {language}
```

## Configuração correspondente

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

## Qualidade e desempenho

- `base` é um ponto de partida apropriado para áudios curtos em PT-BR e CPU.
- Teste mensagens reais; fala rápida, ruído e nomes próprios podem exigir `small` ou uma pós-revisão.
- O carregamento por processo é mais simples e persistente, mas acrescenta latência. Se essa latência for inadequada, use um provedor nativo carregado no processo do gateway ou um serviço local persistente.

## Segurança

- Não grave áudio bruto, tokens ou transcrições em logs de debug.
- Não inclua diretórios de cache de modelos, ambientes virtuais ou áudio em backup Git sem uma decisão explícita.
- O provedor de comando executa com as permissões do gateway: trate o script como código operacional confiável.
