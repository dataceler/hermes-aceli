---
name: dataceler-instagram-production-workflow
description: "Use for Dataceler Instagram carousels. Gate stages."
version: 1.0.0
author: Dataceler
license: MIT
metadata:
  hermes:
    tags: [Instagram, Dataceler, workflow, editorial, QA, orchestration]
    related_skills: [dataceler-instagram-carousel-editorial, grounded-citations, higgsfield-generate, voz-do-joao]
---

# Workflow sequencial de produção Instagram — Dataceler

## When to Use

Use para criar ou revisar carrosséis institucionais da Dataceler quando qualidade depende de pesquisa, decisão editorial, produção visual e QA em fases separadas.

## Princípio

Esta é uma skill **orquestradora**. Carregue somente ela no início. Ela chama uma skill especialista por vez, grava os artefatos em disco e só libera a etapa seguinte após um gate objetivo. Nunca carregue todas as especialistas simultaneamente.

Chrome/Playwright só entra na renderização e QA visual. Higgsfield só entra quando uma ilustração/imagem sintética melhora a compreensão; HTML/CSS determinístico continua obrigatório para texto e composição.

## Estado persistente

Cada post deve usar:

```text
/root/.hermes/artifacts/instagram-dataceler/workflows/<YYYY-MM-DD>-<slug>/
├── workflow.json
├── 01-research.md
├── citation-ledger.json
├── 02-idea.md
├── 03-editorial-brief.md
├── 04-structured-content.md
├── 05-art-direction.md
├── cards.html
├── caption.md
├── slides/
├── contact-sheet.jpg
├── verification.json
└── dataceler-<slug>-ORIGINAIS-SEM-COMPRESSAO.zip
```

`workflow.json` é a fonte de verdade. Para cada fase, registrar `pending|in_progress|passed|blocked`, arquivos de entrada/saída, evidência do gate, causa de bloqueio e timestamp UTC. Ao retomar, ler esse arquivo e iniciar no primeiro estágio que não esteja `passed`.

```json
{"workflow":"instagram-dataceler-v1","publication":"blocked","stages":{"research":{"status":"pending"},"ideation":{"status":"pending"},"editorial":{"status":"pending"},"visual":{"status":"pending"},"caption":{"status":"pending"},"qa":{"status":"pending"},"approval":{"status":"pending"}}}
```

## Etapas

### 1. Pesquisa
**Carregue:** `grounded-citations`.

**Entrada:** tema ou autorização para selecionar tema.

**Produza:** `01-research.md` e `citation-ledger.json`, separando fatos, interpretação e hipóteses.

**Gate:** fonte primária para fatos centrais; relevância empresarial; todas as alegações planejadas sustentadas ou removidas; nenhuma estatística, case ou promessa inventada.

### 2. Ideação
**Carregue:** nenhum especialista adicional; leia somente `01-research.md`.

**Produza:** `02-idea.md` com três ângulos, público, tensão, tese, consequência, risco e CTA possível. Escolha um pelo valor empresarial, especificidade, evidência e potencial de conversa.

**Gate:** não é resumo de notícia; responde o que muda na decisão da empresa; inclui mecanismo, limite e ação reversível; não poderia servir para qualquer empresa de IA.

**Gate de transformação obrigatório:** declarar antes de escrever os slides:
- **Ponto A:** comportamento atual observável, dor e custo operacional do leitor;
- **Ponto B:** nova consciência, decisão ou capacidade que ele terá ao final;
- **ponte:** o mecanismo que conecta A a B;
- **prova de mudança:** uma métrica, comparação, diagnóstico ou decisão concreta que o leitor pode aplicar sem acreditar em promessa genérica.

**Validador de transformação do leitor — obrigatório antes da produção visual**

Preencha e teste este bloco no `03-editorial-brief.md`:

```text
Leitor: [papel e contexto]
Ponto A: [situação atual observável + dor/desejo]
Custo de permanecer em A: [tempo, risco, retrabalho, receita, controle ou oportunidade]
Ponto B: [o que ele passa a enxergar, decidir ou fazer de modo diferente]
Ponte: [mecanismo, diagnóstico ou modelo que torna a mudança possível]
Prova aplicável: [teste, métrica, comparação, checklist ou decisão para amanhã]
Veículo narrativo: [dor | desejo | storytelling | comparação]
```

Escolha deliberadamente **um veículo principal** — não use todos por reflexo:
- **dor:** revelar um desperdício, risco ou gargalo que o leitor ainda normaliza;
- **desejo:** mostrar uma capacidade operacional, ganho de controle ou futuro desejável sem promessa vazia;
- **storytelling:** mostrar uma situação, decisão e consequência reconhecíveis antes de apresentar o modelo;
- **comparação:** contrastar “operação atual” com “operação redesenhada” ou uma decisão fraca com uma alternativa melhor.

### Teste de reprovação

O conteúdo falha e volta para ideação se qualquer resposta for “não”:

1. O leitor consegue reconhecer o ponto A sem precisar concordar previamente com a tese?
2. O ponto B descreve uma capacidade ou decisão concreta, e não apenas mais informação?
3. Existe uma ponte causal entre A e B — não apenas uma lista de recomendações?
4. Há um teste ou ação que ele possa aplicar no próximo dia útil?
5. O gancho, os exemplos e o CTA servem ao mesmo deslocamento?
6. Se retirar o tema “IA”, o post ainda revela uma mudança operacional específica? Se não, é provável que seja conteúdo de ferramenta, não transformação.

Registre respostas e evidências no brief. Não renderize enquanto o validador não passar.

## Etapas

### 3. Escrita editorial
**Carregue:** `dataceler-instagram-carousel-editorial`. Carregue `voz-do-joao` apenas quando adaptar ideia/fala autoral de João ao tom institucional.

**Entrada:** pesquisa e ângulo aprovados.

**Produza:** `03-editorial-brief.md` e `04-structured-content.md` com exatamente dez slides. Uma ideia por slide. Diferencie fato, análise Dataceler e hipótese.

**Gate:** progressão ponto A → tensão/custo → mecanismo → ponto B → limite → controle → ação → pergunta; sem slogans vazios; cada slide acrescenta valor; fatos têm fonte; leitura gera critério de decisão.

O slide inicial deve fazer o leitor reconhecer o próprio estado atual. O encerramento deve deixar claro o que ele consegue diagnosticar, decidir ou testar de modo diferente no dia seguinte.

### 4. Direção de arte e produção visual
**Carregue:** `dataceler-instagram-carousel-editorial`. Carregue `higgsfield-generate` apenas para ativo visual necessário.

**Entrada:** brief e roteiro aprovados.

**Produza:** `05-art-direction.md`, `cards.html`, 10 PNGs, `contact-sheet.jpg`.

**Regra:** usar Dataceler Navy HTML, cabeçalho/rodapé fixos, conteúdo verticalmente centralizado. Diagramas devem explicar uma decisão. Higgsfield não renderiza texto de slide.

**Gate:** 10 PNGs RGB 1080×1350; HTML sem overflow; slides densos revisados individualmente e conjunto revisto na contact sheet; identidade Dataceler reconhecível.

### 5. Legenda
**Carregue:** `dataceler-instagram-carousel-editorial`; `voz-do-joao` somente se necessário.

**Entrada:** roteiro congelado, contact sheet e fontes.

**Produza:** `caption.md` que aprofunda mecanismo, consequência, limite, ação e pergunta concreta.

**Gate:** não repete os slides; não usa “hoje” sem data absoluta; tom executivo; sem promessa comercial; fontes coerentes com pesquisa.

### 6. QA e pacote master
**Carregue:** `dataceler-instagram-carousel-editorial` e `grounded-citations`.

**Produza:** `verification.json`, manifesto SHA-256 e ZIP de originais sem compressão.

**Gate:** 10/10 PNGs não vazios, RGB e 1080×1350; overflow zero; ZIP reaberto e íntegro; hashes 10/10 coincidem com masters; fontes verificadas; nenhuma publicação ou rascunho API criado.

### 7. Aprovação humana
Entregue o ZIP master e prévia. Atualize para `awaiting_human_approval`. Aprovação do material não autoriza publicar; publicação exige comando explícito para o post específico.

## Regras de execução

1. Trabalhe em uma fase por vez e atualize o manifest antes/depois.
2. A próxima fase lê arquivos aprovados, não um resumo recontado pelo modelo.
3. Falha bloqueia a fase; preserve artefatos, registre causa/correção e retome dali.
4. Não avance por conveniência nem publique automaticamente.
5. Conclusão válida: QA `passed`, pacote master validado, aprovação humana pendente.
