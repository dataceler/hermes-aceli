# Monitoramento relativo de outliers em canais do YouTube

Use esta referência quando o objetivo for descobrir vídeos que estejam performando muito acima do histórico do próprio canal, inclusive em canais pequenos. Ela complementa o diagnóstico editorial: o monitor encontra sinais; a análise humana decide se tema, promessa, título, thumbnail ou formato explicam o resultado.

## Modelo de comparação

- Não imponha tamanho mínimo de canal.
- Separe formatos comparáveis. Para a estratégia evergreen da Dataceler, use a aba `/videos` e não misture Shorts ou lives de forma ingênua.
- Analise os 5 uploads long-form mais recentes como candidatos.
- Use até 20 uploads long-form anteriores como linha de base.
- Exija pelo menos 5 observações válidas na linha de base.
- Calcule a média aritmética das visualizações da linha de base.
- Classifique como outlier quando `visualizações do candidato / média da linha de base >= 2`.
- Restrinja alertas a uploads recentes; 14 dias é o padrão inicial.
- Mostre visualizações do candidato, média, tamanho da amostra, múltiplo e data de publicação.

Esse desenho evita que canais grandes dominem o ranking por volume absoluto. O múltiplo é um sinal de interesse relativo, não prova de qualidade ou recomendação editorial.

## Coleta pública sem API paga

Uma rota leve e reproduzível usa `yt-dlp` em virtualenv dedicado:

1. Consulte `https://www.youtube.com/@handle/videos` com `extract_flat` e `playlistend=25`.
2. Leia ID, título, URL e `view_count` dos resultados planos.
3. Calcule o múltiplo antes de fazer consultas detalhadas.
4. Consulte metadados adicionais apenas para candidatos que já ultrapassam o limiar preliminar.

O modo plano traz visualizações rapidamente, mas pode não incluir a data. Quando a extração detalhada exigir confirmação de login, não tente contornar o desafio com credenciais improvisadas. Use uma fonte pública leve:

- página `https://www.youtube.com/watch?v=VIDEO_ID&hl=en&gl=US`;
- cabeçalho `Accept-Language: en-US,en;q=0.9`;
- campo público `publishDate.simpleText`, normalmente em `%b %d, %Y`;
- campo `views.simpleText` para atualizar a contagem, quando presente;
- como alternativa, use o feed oficial do canal para IDs recentes e datas.

Trate o parser de HTML como integração sujeita a mudança. Se o campo desaparecer, falhe de forma observável e revise o extrator; não invente data nem aceite vídeo sem verificar a janela de recência.

## Estado e deduplicação

Persista em JSON, com escrita atômica:

- `alerted_video_ids`: vídeos já enviados;
- `ignored_old_video_ids`: candidatos fortes, mas fora da janela de recência;
- cache de `channel_id`, nome e última coleta bem-sucedida;
- resumo da última execução e falhas recentes.

Regras:

- Marque como alertado somente depois de confirmar o limiar final e a data.
- Não marque um vídeo abaixo do limiar; ele pode cruzá-lo em uma execução futura.
- Use lock de arquivo para impedir duas execuções simultâneas.
- Saída vazia significa “nenhum outlier novo”.
- Falha total deve encerrar com código diferente de zero; falhas parciais devem ser registradas sem fabricar resultados.

## Agendamento silencioso no Hermes

Para um watchdog determinístico, prefira um cron `no_agent=true`:

- o script produz a mensagem final;
- stdout não vazio é entregue literalmente;
- stdout vazio não gera mensagem;
- erro ou código não zero gera alerta operacional;
- use um wrapper `.sh` para executar o Python do virtualenv correto.

Confirme o fuso do host antes de converter a agenda. Em host UTC, `0 12 * * *` corresponde a 9h de Brasília enquanto Brasília estiver em UTC−3. Registre no nome do job o horário humano e o horário técnico.

## Verificação obrigatória

Antes de declarar o monitor pronto:

1. valide número de canais e duplicatas;
2. teste amostras de canais em idiomas e tamanhos diferentes;
3. execute a lista completa com estado temporário;
4. confirme canais bem-sucedidos, falhas e duração;
5. execute novamente com o mesmo estado;
6. exija stdout vazio e zero novos alertas na segunda execução;
7. inicialize o estado definitivo;
8. dispare manualmente o job pelo scheduler;
9. confirme `last_status=ok`, nenhum erro de entrega e próxima execução correta.

## Implantação atual da Dataceler

A implementação operacional usa:

- `~/.hermes/scripts/youtube-outlier-channels.json`;
- `~/.hermes/scripts/youtube-outlier-monitor.py`;
- `~/.hermes/scripts/youtube-outlier-monitor.sh`;
- `~/.hermes/cron/state/youtube-outlier-monitor.json`;
- virtualenv `~/.hermes/cache/venvs/youtube-monitor`.

A lista de canais e o estado são detalhes mutáveis da implantação. O método desta referência deve continuar válido quando a lista mudar.
