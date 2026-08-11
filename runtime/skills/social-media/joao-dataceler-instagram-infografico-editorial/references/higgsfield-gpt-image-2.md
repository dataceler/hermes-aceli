# Higgsfield GPT Image 2 para infográficos 4:5

Use este fluxo quando João ou a Dataceler pedirem um infográfico gerado pelo Higgsfield CLI, especialmente ao reconstruir uma peça já aprovada.

## Contrato validado

O modelo `gpt_image_2` aceita:

- `prompt` obrigatório;
- referências por `image_references`, expostas pela CLI como `--image`;
- `quality`: `low`, `medium`, `high`;
- `resolution`: `1k`, `2k`, `4k`;
- proporções: `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `3:2`, `2:3`.

Não há 4:5 nativo. Para Instagram, use `3:4`, que exige a menor adaptação.

## Fluxo de reconstrução

1. Use como referência a última peça aprovada, com logos, paletas e texto já conferidos.
2. Inspecione o contrato ao vivo antes da geração:

```bash
higgsfield model get gpt_image_2 --json
```

3. Gere em `3:4`, `high`, `2k`, passando a arte anterior por `--image` e aguardando o resultado final:

```bash
higgsfield generate create gpt_image_2 \
  --image ./referencia.png \
  --aspect_ratio 3:4 \
  --quality high \
  --resolution 2k \
  --wait --json < prompt.txt
```

4. Em image-to-image, descreva a transformação, não reconte toda a imagem. Exija explicitamente:
   - preservação literal de cada palavra;
   - logos e paletas intactos;
   - nenhuma nova alegação;
   - grade e relações informacionais preservadas;
   - conteúdo essencial dentro de margens seguras.
5. Inspecione o PNG bruto inteiro. Modelos de imagem podem reescrever texto mesmo quando a composição parece correta.
6. Se houver poucas alterações textuais, faça no máximo uma correção localizada no próprio GPT Image 2, enumerando as substituições exatas e ordenando preservar todo o restante.
7. Se a correção introduzir novos erros, não continue em ciclos generativos. Volte ao artefato aprovado ou aplique composição determinística autorizada.

## Conversão 3:4 → 4:5 sem corte

Um recorte central de 3:4 para 4:5 remove topo e base e pode cortar badge, título ou rodapé. Prefira extensão horizontal do fundo:

1. Para uma imagem `W × H`, crie canvas com `canvas_width = round(H × 4 / 5)` e a mesma altura.
2. Centralize a imagem original.
3. Preencha as faixas laterais estendendo a primeira e a última coluna de pixels, linha a linha. Isso prolonga fundos escuros e claros sem criar barras visíveis.
4. Redimensione o canvas para `1080 × 1350` com Lanczos.
5. Não estique a arte inteira horizontalmente e não corte conteúdo vertical.

## QA obrigatório

Execute:

```bash
python3 scripts/check_instagram_infographic.py ./final.png --create-thumbnail
```

Depois inspecione:

- PNG final em 1080 × 1350;
- miniatura em 270 × 338;
- cada palavra e acento;
- logos e proporções;
- confinamento cromático das colunas;
- cinco critérios e bloco de decisão;
- artefatos nas faixas laterais;
- clipping, duplicação ou reescrita de fatos.

Só declare fidelidade quando a inspeção visual do resultado final — não apenas do bruto — tiver passado.
