# Renderização determinística de infográficos textuais

Use este procedimento quando a peça tiver títulos, matrizes, eixos, listas ou outros textos cuja grafia e posição precisem ser exatas. A técnica não substitui direção visual; ela separa criação estética de composição tipográfica verificável.

## Quando escolher

- Infográfico com mais de um bloco textual.
- Matriz 2x2, eixo, escala, fluxo ou comparação posicional.
- Conteúdo em português com acentos que precisam ser preservados.
- Identidade visual com cores e logotipo oficiais.
- Arte que será revisada antes de qualquer publicação.

## Procedimento

1. Salvar fonte, análise e conteúdo estruturado em arquivos separados.
2. Definir dimensão, margens, paleta, tipografia, hierarquia e posições.
3. Manter logotipo e demais ativos dentro da pasta durável do artefato, não apenas em cache temporário.
4. Para todo infográfico de LinkedIn, renderizar obrigatoriamente com Python + Pillow, usando DejaVu Sans e DejaVu Sans Mono. Textos, formas, matrizes, setas, cores e logotipo devem ser posicionados por código.
5. Não usar `image_generate` em infográficos de LinkedIn, salvo quando o usuário solicitar explicitamente um elemento ilustrativo generativo. Mesmo nesse caso, o Pillow deve compor a peça final; tipografia, matriz, rótulos, setas, cores e logotipo continuam determinísticos.
6. Abrir o PNG com `vision_analyze` e pedir uma crítica explícita, não aprovação genérica.
7. Corrigir falhas e renderizar novamente.
8. Verificar formato, dimensões e integridade antes de entregar.

## Estrutura recomendada

```text
infographic/<topic>/
├── source.md
├── analysis.md
├── structured-content.md
├── prompts/infographic.md
├── logo-or-brand-asset.png
├── scripts/render_infographic.py
└── infographic.png
```

## Checklist visual

- Toda palavra está correta e acentuada.
- Nenhum texto está cortado, sobreposto ou pequeno demais para o feed.
- A leitura funciona no sentido esperado sem depender da legenda.
- Setas apontam para a direção conceitualmente correta.
- Rótulos “baixo/alto”, “antes/depois” ou equivalentes correspondem às posições.
- Quadrantes e cores não contradizem o significado.
- Logo mantém proporção e contraste.
- Título domina; explicações e rodapé têm hierarquia inferior.
- A imagem ensina algo que a legenda apenas aprofunda.

## Pitfalls

- Rotacionar texto e seta juntos pode mudar a direção visual da seta; desenhe setas separadamente.
- Confiar apenas na dimensão do arquivo não comprova legibilidade; inspecione a imagem renderizada.
- Usar ativo localizado somente em cache torna o renderizador não reprodutível.
- Uma matriz sem extremos claros pode parecer bonita e ainda comunicar o eixo errado.
- Um infográfico decorativo não satisfaz a exigência visual se não carregar conhecimento.

## Verificação

A peça está pronta somente após `vision_analyze` confirmar ausência de falhas bloqueadoras e uma checagem de arquivo confirmar PNG íntegro nas dimensões definidas.
