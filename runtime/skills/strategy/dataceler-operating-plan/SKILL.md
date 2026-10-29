---
name: dataceler-operating-plan
description: "Use when planning Dataceler sales, products and growth."
version: 0.1.0
author: João Cordeiro, Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Dataceler, Strategy, Sales, Product, Operations]
    related_skills: []
---

# Plano operacional Dataceler — 90 dias a 3 anos

## When to Use

Use ao priorizar produto, vertical, capacidade, contratação, canal comercial, conteúdo, preço ou metas da Dataceler.

Use este plano como fonte de verdade para decisões de produto, vendas, contratação, conteúdo e capacidade da Dataceler. Carregue `references/plano-90d-3a.md` quando a decisão depender de detalhes, metas ou tabelas completas. O plano detalhado prevalece sobre documentos estratégicos anteriores em caso de conflito.

## Tese e foco

- Construir **funcionários digitais**: IA que executa jobs operacionais com processo, limites, integração e métrica; não vender chatbot genérico nem horas isoladas.
- Cluster fixo de entrada: **imobiliárias → construtoras → incorporadoras**. Arquitetura e gerenciadoras são adjacentes de construtoras. Não abrir outros segmentos antes dos gatilhos formais de revisão.
- Vender e construir em paralelo, mas cada projeto deve passar no filtro: PI da Dataceler, recorrência, ao menos 60% reaproveitável, aderência ao cluster, capacidade disponível e canal oficial.
- Serviços podem consumir até 60% da capacidade nos seis primeiros meses; 40% no ano 1 e 30% no ano 2, desde que todo projeto deposite componentes no motor.

## Metas e marcos

| Horizonte | Clientes | MRR | ARR | Marco |
|---|---:|---:|---:|---|
| Jan/2027 (90 dias) | 3 fundadores | R$ 9 mil | R$ 110 mil | motor v1 e três provas reais |
| Abr/2027 (6 meses) | 9 | R$ 30 mil | R$ 360 mil | 5 agentes; remarketing elegível |
| Out/2027 (ano 1) | 25 | R$ 95 mil | R$ 1,2 mi | 8 agentes; onboarding de 2 dias |
| Out/2028 (ano 2) | 70 | R$ 290 mil | R$ 3,5 mi | canal e onboarding sem código |
| Out/2029 (ano 3) | 150 | R$ 450 mil | ~R$ 5,4 mi | ~US$ 1 mi ARR |

Meta intermediária: 15 clientes pagantes em julho de 2027. Não antecipar a tese de US$ 1 mi ARR: exige canal, time e onboarding, não apenas dois sócios em venda consultiva.

## Produtos de entrada e sequência

1. **Imobiliárias:** Carteira e Gestor na KZA; depois Anunciante. ICP: já investe em portais/anúncios pagos, carteira própria e imóveis parados.
2. **Construtoras:** Memória de Obra; depois Medição, Compras e Chamados/Pós-venda. Dor: pendências e decisões perdidas em grupos, medição e conferência manual.
3. **Incorporadoras / compra de terreno:** Garimpeiro. Começar por 30 dias de operação manual com a construtora fundadora; refatorar somente se houver oportunidades aceitas e piloto pago.

Um agente entra no catálogo apenas após dois clientes com o mesmo código, segundo cérebro documentado, 200 itens rotulados com precisão >=90%, onboarding <=1 semana e página/vídeo publicados.

## 90 dias: ordem de execução

- Semanas 1–8: entregar aos três fundadores, construir motor multi-tenant, KZA Fase 2, PoC Memória de Obra, Garimpeiro manual, material comercial e rede/contatos-ponte. Não fazer prospecção fria.
- Semanas 9–13: iniciar 20 contas novas por semana com gancho pesquisado; diagnósticos, pilotos pagos e vídeo/prova reais.
- Capacidade total estimada: 700 horas. Não aceitar quarta implantação antes da semana 9; fila de espera é preferível a customização sem capacidade.

## Go-to-market

- Produto da venda: diagnóstico remoto de 90 minutos com decisor e operador, amostra real, job atual e métrica combinada. Presencial apenas na implantação quando o job exigir, sobretudo construtoras/incorporadoras.
- Processo comercial: contato → diagnóstico → proposta em 48h → piloto pago de 30 dias → aceite por métrica → contrato de 12 meses → expansão.
- Canal inicial: rede pessoal, contatos-ponte e indicação; conteúdo founder-led apoia a prova desde o início. Prospecção fria começa apenas com vídeo real e caso em andamento.
- Não usar ligação fria como primeiro toque, automação de envio em massa em WhatsApp, SDR terceirizado, captação paga fria, feira ou expansão geográfica precoce.
- Tráfego pago: apenas remarketing ao atingir MRR >= R$30 mil; ampliar somente se custo por reunião ficar abaixo da prospecção.

## Mensagem e conteúdo

- Dataceler: vitrine de agentes, provas, demonstrações e preços; perfil pessoal: opinião, bastidor e aprendizado.
- Conteúdo vende o processo e a evidência: demos de 60–90 s, antes/depois, critérios, indicadores e limites. Nunca prometer resultado sem caso/métrica.
- CTA padrão: diagnóstico de um gargalo concreto, não pedido genérico de compra.

## Motor e controles

Construir: multi-tenant, segundo cérebro versionado por cliente, decisão barata com fallback, evals, custo por tenant, fila de exceções, memória operacional, conectores oficiais e painel de métrica. Dados e canais de clientes somente por integração oficial; WhatsApp apenas API oficial.

## Pessoas e gatilhos

- Primeiro hire: analista de operação no mês 4–5, quando houver seis clientes ou quatro diagnósticos/mês, desde que caixa >=3 meses.
- SDR próprio no mês 7–9 somente se: dois agentes de catálogo com onboarding <=1 semana, funil confirmado por três meses e MRR >= R$40 mil. Diagnóstico e fechamento continuam com sócio.
- Engenheiro/FDE no mês 9–12 quando houver 15 clientes e sócio técnico estiver >50% em implantação.

## Métricas semanais

1. Contas novas abordadas e respostas.
2. Diagnósticos marcados.
3. Pilotos e métrica combinada.
4. MRR e percentual recorrente.
5. Horas de serviço versus produto e custo de IA por tenant.

## Guardrails de decisão

- Rever cluster apenas no mês 6 se houver menos de nove clientes e menos de três construtoras em piloto, ou churn >5% por dois meses.
- Capital no mês 12 somente com payback <4 meses, churn <2,5%, 25+ clientes, dois agentes self-service e receita de serviços <=40%.
- Refatorar Garimpeiro somente após 30 dias manuais com >=3 oportunidades aceitas e piloto pago.
- Escalar serviços que não melhoram motor, catálogo ou evidência é proibido.

## Verificação

Antes de recomendar iniciativa, contratação, preço, canal ou nova vertical: compare com metas, capacidade, filtros e gatilhos deste plano. Diferencie premissa dos sócios, estimativa a validar e evidência real da Dataceler.