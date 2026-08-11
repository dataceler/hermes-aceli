---
name: dataceler-instagram-stories-editorial
description: Planeje Stories para João e Dataceler.
version: 0.1.0
author: Hermes
metadata:
  hermes:
    tags: [Instagram, Stories, Dataceler, João, Editorial]
    related_skills: [dataceler-instagram-carousel-editorial]
---

# Stories de João e Dataceler

Planeja sequências de Instagram Stories para o perfil pessoal de João Cordeiro e para o perfil institucional da Dataceler. Não cria carrosséis, não trata Stories como simples reposts e não publica automaticamente; usa ferramentas Hermes sem dependência obrigatória de ambiente.

Leia `references/strategy-v1.md` para os papéis dos perfis, horários e benchmark operacional. Copie `templates/weekly-calendar.md` ao montar uma nova semana.

## When to Use

- “Crie o calendário de Stories desta semana.”
- “O que João e Dataceler devem postar hoje?”
- “Planeje Stories para leads mornos.”
- “Transforme este bastidor em duas narrativas diferentes.”
- “Revise alcance, retenção, respostas e DMs dos Stories.”
- “Ajuste os horários ou o benchmark do calendário.”
- “Crie uma sequência pessoal para João.”
- “Crie uma sequência institucional para a Dataceler.”

## Prerequisites

- Nenhuma variável de ambiente, instalação ou credencial é obrigatória.
- Identificar o período do calendário e confirmar a data atual com `terminal` quando houver termos relativos como “hoje”.
- Conhecer os acontecimentos reais que podem aparecer como bastidores; usar placeholders quando eles ainda não forem conhecidos.
- Ter autorização para qualquer informação de cliente, equipe, familiar ou terceiro.
- Para revisar resultados, obter visualizações por quadro, respostas, interações e DMs após 24 horas.
- Carregar `dataceler-instagram-carousel-editorial` apenas se houver carrossel relacionado; não transferir regras visuais de carrossel automaticamente para Stories.

## How to Run

1. Carregue esta skill com `skill_view`.
2. Leia `references/strategy-v1.md` e `templates/weekly-calendar.md` com `skill_view`.
3. Confirme datas e dias da semana por meio do `terminal`; não calcule mentalmente datas relativas.
4. Crie o calendário real com `write_file`, separando João e Dataceler em cada dia.
5. Use `patch` para aplicar correções de horário, CTA ou conteúdo sem reescrever material aprovado.
6. Verifique o arquivo final com `read_file` e uma checagem mecânica via `terminal` ou `execute_code`.
7. Entregue o calendário para aprovação; não publique.

## Quick Reference

- Audiência: seguidores atuais e leads mornos.
- João: confiança, proximidade, vida pessoal e visão de fundador.
- Dataceler: autoridade, método, prova e avanço comercial.
- Arco: presença → relevância → prova → conversa.
- João: começar às 11h, horário de Brasília.
- Dataceler: começar às 16h, horário de Brasília.
- CTA leve: enquete, reação, quiz.
- CTA média: caixa, resposta, palavra-chave.
- CTA alta: diagnóstico, reunião, proposta.
- Medição: primeiro quadro, menor alcance, último quadro, interações e DMs.
- Escrita: `write_file`.
- Correção: `patch`.
- Verificação: `read_file` + `execute_code` ou `terminal`.
- Estratégia: `references/strategy-v1.md`.
- Modelo semanal: `templates/weekly-calendar.md`.

## Procedure

1. **Defina o papel de cada perfil.**
   - João responde “por que confiar em mim?”.
   - Dataceler responde “por que esta empresa consegue resolver?”.
   - Não publique a mesma sequência nos dois perfis.
   - Para um mesmo acontecimento, João mostra dilema e aprendizado; Dataceler mostra método, critério e capacidade.

2. **Confirme datas e horários.**
   - Use `terminal` para confirmar data, dia da semana e fuso de Brasília.
   - Fixe o início de João às 11h e da Dataceler às 16h.
   - Quando houver narrativa ao longo do dia, publique o primeiro quadro no horário definido e a conclusão depois.
   - Não substitua esses horários por janelas genéricas sem nova orientação do usuário.

3. **Escolha um objetivo por sequência.**
   - Presença: aumentar familiaridade.
   - Relevância: conectar a uma dor ou desejo.
   - Prova: mostrar raciocínio, método ou resultado autorizado.
   - Conversa: gerar resposta de baixa ou média fricção.
   - Conversão: convidar um lead contextualizado para avançar.
   - Uma sequência não precisa cumprir todos os objetivos simultaneamente.

4. **Planeje João como perfil pessoal.**
   - Misture vida real, rotina, decisões, aprendizado, opinião e trabalho.
   - Vida pessoal deve revelar humanidade ou contexto, não virar exposição compulsória.
   - Nem todo momento pessoal precisa terminar em IA, Dataceler ou venda.
   - Use fatos reais; quando faltarem, deixe `[placeholder]` em vez de inventar.

5. **Planeje Dataceler como perfil institucional.**
   - Priorize IA aplicada, diagnóstico, método, demonstração, prova autorizada, FAQ e oferta.
   - Faça uma ideia avançar por quadro: problema → mecanismo → aplicação → limite → próximo passo.
   - Não invente clientes, cases, métricas ou resultados.
   - Prefira silêncio planejado a conteúdo institucional sem valor.

6. **Construa uma sequência curta.**
   - Quadro 1: contexto ou gancho reconhecível.
   - Quadro 2: tensão, problema ou decisão.
   - Quadro 3: explicação, percepção ou método.
   - Quadro 4: exemplo, consequência ou aprendizado.
   - Quadro 5: CTA coerente, quando necessário.
   - Use menos quadros quando a ideia já estiver completa.

7. **Aplique a escada de CTA.**
   - Comece com enquete, reação ou pergunta simples.
   - Avance para caixa, DM ou palavra-chave depois de contexto e prova.
   - Use diagnóstico, reunião ou proposta apenas quando a sequência qualificou o problema.
   - Não faça pedido comercial forte todos os dias.

8. **Proteja privacidade e confiança.**
   - Não publique localização sensível em tempo real.
   - Não mostre telas, mensagens, calendário, proposta, credencial ou dado confidencial.
   - Não exponha cliente, equipe, familiar ou terceiro sem consentimento.
   - Não trate vulnerabilidade como obrigação editorial.

9. **Crie o calendário em arquivo.**
   - Copie a estrutura de `templates/weekly-calendar.md`.
   - Para cada dia e perfil, preencha objetivo, horário, quadros, formato, CTA e campos de medição.
   - Marque explicitamente pausas planejadas.
   - Preserve placeholders para acontecimentos ainda não confirmados.

10. **Meça após 24 horas.**
    - Registre visualizações do primeiro, menor e último quadro.
    - Registre respostas, votos, reações, cliques e DMs qualificadas.
    - Trate benchmark como piso operacional, não como prova isolada de qualidade.
    - Se o primeiro quadro atinge o benchmark e o último não, revise continuidade ou quantidade.
    - Se nenhum quadro atinge, teste abertura, horário ou intervalo — uma variável por vez.

11. **Feche a semana com aprendizado.**
    - Identifique sequências com melhor conclusão e resposta.
    - Registre dúvidas e linguagem do público.
    - Escolha apenas um ajuste controlado para a próxima semana.
    - Atualize a referência somente quando o usuário tornar uma decisão durável.

## Pitfalls

- Tratar seguidores atuais como público completamente frio.
- Fazer João parecer um canal corporativo disfarçado.
- Transformar vida pessoal em conteúdo comercial forçado.
- Usar Dataceler como catálogo de serviços.
- Repostar a mesma sequência nos dois perfis.
- Inventar rotina, acontecimentos, cases ou resultados.
- Trocar 11h e 16h por horários “ótimos” não comprovados.
- Avaliar apenas a visualização do primeiro Story.
- Considerar o benchmark temporário uma meta permanente.
- Aumentar volume para compensar baixa qualidade.
- Alterar tema, horário, abertura e CTA simultaneamente.
- Levar aprendizados de Stories para a skill de carrosséis sem validação.
- Publicar automaticamente ou assumir que aprovação editorial autoriza postagem.

## Verification

Use `read_file` no calendário final e confirme em uma única revisão que cada dia contém perfis separados, horários corretos, objetivo, quadros, CTA ou pausa intencional e campos de medição; que João pode mostrar vida pessoal sem exposição forçada; que Dataceler mantém voz institucional; e que nenhuma informação foi inventada ou publicada.
