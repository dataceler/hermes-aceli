---
name: dataceler-youtube-evergreen-editorial
description: Planeje vídeos profundos de IA com estratégia evergreen.
version: 0.1.0
author: Hermes
metadata:
  hermes:
    tags: [YouTube, Evergreen, IA, Estratégia, Dataceler]
---

# Dataceler YouTube Evergreen Editorial

Planeja vídeos de IA profundos, acessíveis e úteis para empresários e pessoas não técnicas, combinando demanda evergreen com oportunidades atuais. Não persegue tendências sem aderência editorial, não copia criadores de referência e não transforma resultados pessoais em promessas; depende de pesquisa verificável, posicionamento claro e embalagem honesta.

## When to Use

- “Crie uma pauta para o YouTube da Dataceler.”
- “Transforme este tópico de IA em um vídeo profundo.”
- “Quais assuntos evergreen devemos gravar?”
- “Pesquise temas de IA em alta para o canal.”
- “Crie título, thumbnail, roteiro e plano de distribuição.”
- “Avalie se esta pauta serve para empresários e público não técnico.”
- “Monte um calendário que equilibre evergreen e tendências.”

## Prerequisites

- Nenhuma variável de ambiente é obrigatória para planejamento editorial.
- Acesso a `web_search` e `web_extract` para pesquisa e verificação de fontes.
- Acesso a `browser_navigate` e `vision_analyze` quando for necessário avaliar páginas ou thumbnails.
- Tema, objetivo empresarial e restrições do vídeo; se ausentes, assumir educação sobre IA para empresários e pessoas não técnicas.
- Para analisar desempenho privado do canal, OAuth do YouTube com escopo somente leitura; não é necessário para criar pautas.
- Ler `references/source-analysis.md` ao revisar a estratégia-base ou explicar a origem dos princípios.

## How to Run

1. Carregue esta skill com `skill_view`.
2. Use `web_search` para mapear demanda evergreen e sinais atuais.
3. Use `web_extract` para verificar fontes primárias e dados citáveis.
4. Use `vision_analyze` para revisar a embalagem visual quando houver thumbnail.
5. Entregue o pacote editorial no chat ou salve-o com `write_file` para aprovação.
6. Não publique nem agende vídeos sem autorização explícita.

## Quick Reference

- `web_search`: perguntas recorrentes, tendências, notícias e concorrentes.
- `web_extract`: documentação, estudos, anúncios e fontes primárias.
- `browser_navigate`: páginas dinâmicas e interfaces do YouTube.
- `vision_analyze`: thumbnail, contraste, legibilidade e recorte.
- `write_file`: briefing, roteiro, descrição e plano de distribuição.
- `execute_code`: cálculo de pontuação editorial e comparação de métricas.
- `references/source-analysis.md`: seis vídeos de referência e limites da coleta.

## Procedure

1. **Defina a decisão que o vídeo melhora.**
   - Escreva uma pergunta central que o público realmente faria.
   - Identifique quem decide: dono, gestor, profissional de TI ou pessoa não técnica aprendendo IA.
   - Defina o resultado útil: compreender, comparar, evitar um risco, escolher ou implementar.
   - Conclua somente quando a pauta puder ser resumida em: “Depois deste vídeo, a pessoa conseguirá ___.”

2. **Classifique a oportunidade.**
   - `Evergreen`: responde a uma dúvida duradoura e continua útil após o ciclo de notícias.
   - `Tendência`: parte de um evento, ferramenta, lançamento ou mudança recente.
   - `Híbrida`: usa a tendência como entrada e entrega um princípio duradouro.
   - Priorize um portfólio majoritariamente evergreen. Aceite tendência somente quando houver aderência à IA, ao negócio e ao público da Dataceler.

3. **Pesquise em duas camadas.**
   - Camada evergreen: perguntas recorrentes, conceitos, erros, critérios de decisão e aplicações.
   - Camada atual: lançamentos, mudanças regulatórias, novos recursos, buscas emergentes e discussões recentes.
   - Use `web_search` para descoberta e `web_extract` para confirmar a fonte.
   - Toda afirmação atual, estatística ou capacidade de produto precisa de fonte verificável e data de referência.

4. **Pontue as pautas.**
   - Atribua de 0 a 3 para: longevidade, demanda atual, relevância empresarial, utilidade prática, diferenciação, força das fontes e viabilidade de produção.
   - Use `execute_code` para somar quando houver várias pautas.
   - Não escolha apenas pela maior busca. Elimine temas que exigem superficialidade, promessa enganosa ou experiência que a Dataceler não possui.

5. **Encaixe em um pilar editorial.**
   - Fundamentos de IA para negócios.
   - Aplicações práticas e automação.
   - Critérios de decisão, riscos e governança.
   - Ferramentas explicadas para pessoas não técnicas.
   - Análises de casos reais e verificáveis.
   - Tendências traduzidas em consequências duradouras.
   - Se a pauta não couber em um pilar, explique por que ela merece abrir um novo antes de avançar.

6. **Formule a tese.**
   - Use a estrutura: contexto → mecanismo → consequência → decisão.
   - Diga o que costuma ser mal compreendido, por que acontece e o que o público deve fazer.
   - Evite “IA vai mudar tudo”. Prefira uma tese testável e delimitada.
   - Conclua com uma frase que possa ser defendida por evidência, exemplo ou demonstração.

7. **Crie título e thumbnail antes do roteiro.**
   - Título: problema ou resultado específico, tensão honesta e linguagem que o público usa.
   - Thumbnail: uma única ideia visual, contraste forte, poucas palavras e prova ou transformação reconhecível.
   - Título e thumbnail devem se complementar, não repetir a mesma frase.
   - Números só entram quando forem verdadeiros, contextualizados e verificáveis.
   - Não copie rosto, cenário, tipografia ou identidade de criadores usados como referência.

8. **Estruture conteúdo profundo.**
   - Gancho: apresente a pergunta e a promessa real nos primeiros momentos.
   - Contexto: explique por que isso importa para a operação ou decisão.
   - Modelo mental: forneça uma estrutura simples para entender o tema.
   - Mecanismo: mostre como e por que funciona.
   - Evidência: use fonte, demonstração ou caso real identificado.
   - Aplicação: dê passos, critérios ou perguntas práticas.
   - Limites: diga quando a recomendação não se aplica e quais riscos existem.
   - Síntese: retome a decisão que a pessoa agora consegue tomar.

9. **Traduza sem empobrecer.**
   - Defina termos técnicos no primeiro uso.
   - Use exemplos de vendas, atendimento, finanças, operações e gestão.
   - Separe claramente o que uma ferramenta faz, o que exige integração e o que permanece humano.
   - Remova jargão que não melhora a decisão, mas preserve mecanismos, riscos e critérios.

10. **Planeje produção viável.**
    - Use o ciclo: capturar ideias → pesquisar → priorizar → roteirizar → gravar → editar → revisar → agendar → medir.
    - Prefira um canal mínimo viável consistente a uma produção sofisticada que não se sustenta.
    - Defina previamente demonstrações, telas, gráficos e fontes necessárias.
    - Não grave enquanto houver afirmação importante sem fonte ou exemplo.

11. **Converta tendência em ativo duradouro.**
    - Abra com o acontecimento atual.
    - Explique a mudança concreta.
    - Extraia o princípio que continuará válido.
    - Entregue um framework ou critério de decisão reutilizável.
    - Se o vídeo perder toda a utilidade quando a notícia sair do ciclo, reescreva como híbrido ou descarte.

12. **Prepare o pacote editorial.**
    - Tese e público.
    - Classificação: evergreen, tendência ou híbrido.
    - Três títulos com justificativa curta.
    - Conceito de thumbnail com texto exato.
    - Roteiro por blocos e duração estimada.
    - Fontes e afirmações que dependem delas.
    - Descrição, capítulos e CTA para comentários.
    - Derivações opcionais para Instagram e LinkedIn, sem enfraquecer o vídeo principal.

13. **Defina sucesso além de visualizações.**
    - Impressões e taxa de clique medem embalagem.
    - Retenção e tempo assistido medem entrega da promessa.
    - Comentários qualificados medem compreensão e relevância.
    - Leads, reuniões ou oportunidades medem impacto empresarial quando aplicável.
    - Visualizações de longo prazo medem força evergreen.
    - Não atribua causalidade a uma única métrica ou vídeo.

14. **Revise antes da aprovação.**
    - Confirme que a promessa do título é entregue.
    - Confirme que uma pessoa não técnica entende sem perder profundidade.
    - Confirme que tendências têm uma camada duradoura.
    - Confirme que claims, números e exemplos são verificáveis.
    - Confirme que CTA, descrição e thumbnail não contradizem a tese.

## Pitfalls

- **Confundir tendência com estratégia.** Use a tendência como distribuição; preserve uma lição evergreen.
- **Imitar “gurus”.** Extraia processos das referências, nunca personalidade, promessas ou identidade visual.
- **Prometer resultados de terceiros.** Casos pessoais são evidência anedótica, não garantia para a Dataceler.
- **Produzir vídeo longo e raso.** Duração não substitui mecanismo, evidência, aplicação e limites.
- **Falar só com especialistas.** Traduza termos e conecte cada conceito a uma decisão empresarial.
- **Criar lista genérica de ferramentas.** Compare usos, requisitos, riscos e critérios de escolha.
- **Usar números sem contexto.** Informe fonte, período, base e limitação.
- **Tratar thumbnail como decoração.** Ela deve comunicar uma tensão ou transformação específica.
- **Assumir transcrição inexistente.** Se o YouTube indicar `caption: false`, use somente metadados, descrição e visual, declarando a limitação.
- **Publicar sem aprovação.** Entregue o pacote para revisão; publicação exige autorização separada.

## Verification

Use `read_file` no pacote final e confirme, em uma única revisão, a presença de: público, decisão, classificação editorial, tese, títulos, thumbnail, roteiro profundo, fontes, aplicação, limites, CTA e métricas; rejeite a entrega se qualquer afirmação atual não tiver fonte ou se a promessa de embalagem não aparecer no roteiro.
