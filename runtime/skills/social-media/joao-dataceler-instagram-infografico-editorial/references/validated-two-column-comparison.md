# Comparação bilateral validada para Instagram

Este padrão foi validado em uma peça real de 1080 × 1350, com inspeção integral e miniatura de 270 × 338. Use-o para comparar dois produtos, métodos, estratégias ou opções sem declarar um vencedor universal.

## Estrutura comprovada

```text
faixa de contexto
    título dominante
    subtítulo de uma linha
cabeçalhos das duas opções
5 faixas de critérios
    rótulo central do critério
    resposta esquerda
    resposta direita
bloco de decisão
    quando preferir cada opção
rodapé
    autoria à esquerda
    fontes/data à direita
```

Parâmetros que funcionaram em 1080 × 1350:

- margem lateral: 60 px;
- cabeçalho principal: aproximadamente 196 px;
- cabeçalhos das opções: 86 px;
- cinco faixas de aproximadamente 132 px, com 11 px de gutter;
- bloco de decisão: aproximadamente 206 px;
- título: aproximadamente 72 px quando houver dois nomes longos;
- texto das células: aproximadamente 29 px;
- conclusão: aproximadamente 25 px;
- rodapé separado por uma linha fina de destaque.

Esses valores são pontos de partida. Meça o texto renderizado e preserve a margem óptica.

## Orçamento de conteúdo

Cada lado de uma faixa deve caber em até duas linhas curtas. Use frases paralelas e comparáveis.

Bom:

```text
recurso A, recurso B
e recurso C
```

Fraco:

```text
parágrafo explicativo com ressalvas, exemplos e conclusão
```

Se uma célula ultrapassar duas linhas:

1. remova palavras redundantes;
2. troque descrição por rótulos paralelos;
3. reduza o número de critérios;
4. migre para carrossel se a perda de conteúdo for material;
5. diminua a fonte somente como último recurso.

## Comparações de produtos atuais

Antes de redigir:

- consultar documentação oficial de ambos os lados;
- comparar capacidades documentadas, não impressões;
- registrar data de verificação;
- excluir preço, versão ou modelo quando não forem necessários e tiverem alta volatilidade;
- não declarar vencedor sem benchmark comparável;
- distinguir recursos compartilhados de diferenças de fluxo.

Uma conclusão segura é “escolha pelo fluxo” acompanhada de condições objetivas para cada opção.

## Controles de renderização

Implemente verificações mecânicas:

- dimensões finais iguais a 1080 × 1350;
- modo RGB;
- limite explícito de linhas por bloco;
- medição real da largura do título;
- pelo menos 48–60 px de margem lateral;
- metadata do rodapé alinhada pela largura medida, não por coordenada estimada;
- geração de miniatura 270 × 338;
- arquivo final existente antes da entrega.

Overflow guard deve falhar cedo. Quando falhar, corrija a copy ou o layout; não remova o guard.

## Logo e contraste

Ativos de logo podem ter fundo branco embutido, transparência inesperada ou versão branca destinada a fundo escuro.

Antes de inserir:

1. verificar modo RGB/RGBA e transparência;
2. inspecionar contraste contra o fundo final;
3. quando autorizado, converter o símbolo monocromático para a cor institucional necessária;
4. manter proporções com `contain`, nunca esticar;
5. reinspecionar o PNG real.

Um logo presente, mas sem contraste, é um bloqueador visual.

## Comparações co-branded

Uma revisão validada mostrou que uma matriz bilateral neutra pode ficar genérica demais quando compara produtos com identidades amplamente reconhecidas. Nesses casos, aplique co-branding controlado:

1. **Cabeçalhos:** logo real + nome do produto, com cor saturada da respectiva marca.
2. **Células:** tint muito claro derivado da mesma paleta; corpo em texto escuro de alto contraste.
3. **Critérios:** rótulos centrais neutros e idênticos nos dois lados.
4. **Conclusão:** repita a divisão cromática para reforçar “quando escolher cada opção”.
5. **Autoria:** mantenha rodapé e assinatura na identidade do perfil publicador.

Não misture as cores entre colunas. A paleta serve como orientação espacial: o leitor deve identificar imediatamente qual texto pertence a cada produto.

### Aquisição e preparação dos ativos

- Priorize a página oficial do produto, seu CDN ou pacote de marca.
- Se a página oficial do produto usar o símbolo de sua marca-mãe, esse símbolo pode representar o produto quando acompanhado pelo nome explícito; registre a origem.
- Um favicon oficial pode servir como símbolo quando não houver pacote público melhor, desde que permaneça limpo no tamanho final.
- Verifique `RGB/RGBA`, alpha nos cantos, fundo embutido, padding interno e pixel central antes de compor.
- Preserve logos multicoloridos ou com tile próprio como fornecidos; não extraia nem recolora o símbolo se as diretrizes proibirem alteração.
- Use `ImageOps.contain` ou equivalente. Compare por peso óptico: um logo detalhado geralmente precisa de caixa ligeiramente maior que um símbolo simples.
- Inspecione novamente em 1080 × 1350 e 270 × 338; “logo reconhecível em tamanho integral” não garante reconhecimento no feed.

### Proporção cromática recomendada

- cor saturada: cabeçalho e nome da opção na conclusão;
- tint claro: fundo das células e metade correspondente do bloco final;
- neutro: título geral, critérios, bordas, divisórias e rodapé;
- cor da marca publicadora: micro-rótulo, assinatura ou detalhe central — nunca competindo com as marcas comparadas.

Esse sistema preserva reconhecimento de marca sem transformar o infográfico em uma colagem ou sugerir parceria/endosso.

## QA visual comprovado

Inspecione duas versões:

1. **1080 × 1350:** clipping, sobreposição, bordas, eixos, consistência dos cards, contraste e proporção do logo;
2. **270 × 338:** sobrevivência do título, diferenciação das duas colunas, leitura dos critérios e ausência de ruído no rodapé.

Critérios de aprovação:

- título identificável instantaneamente;
- opções claramente separadas;
- rótulos dos critérios reconhecíveis;
- corpo ainda decodificável no feed;
- título e fonte/data com margem direita real;
- símbolo institucional visível;
- nenhuma célula exige zoom para entender a diferença principal.

## Correções que devem virar hábito

- Encurtar a conclusão antes de reduzir fonte.
- Medir a margem direita do título após trocar fonte ou tamanho.
- Alinhar texto de rodapé pela largura calculada.
- Tratar contraste do ativo, não presumir que “logo oficial” já está pronto para qualquer fundo.
- Fazer QA depois da correção; a primeira inspeção não valida a segunda renderização.
