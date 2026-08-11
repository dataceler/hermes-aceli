---
name: joao-dataceler-instagram-carrossel-twitter-editorial
description: Produza carrosséis estilo Twitter no Canva a partir dos templates de João ou Dataceler.
version: 0.1.0
author: Hermes Agent
---

# Carrossel estilo Twitter — João e Dataceler

Use esta skill exclusivamente para posts de Instagram no formato **carrossel estilo Twitter/X** de João Cordeiro ou Dataceler. O fluxo visual é baseado nos templates oficiais existentes no Canva: nunca recrie o design do zero quando o template correto estiver disponível.

Não transfira estas regras para infográficos, Stories, Reels, carrosséis bem produzidos, LinkedIn ou outros formatos.

## Regra central

```text
perfil definido → localizar template oficial → duplicar → editar somente a duplicata → QA → aprovação → salvar
```

- **João:** use o template oficial de João.
- **Dataceler:** use o template oficial da Dataceler.
- Nunca edite, redimensione, renomeie ou sobrescreva o template original.
- Nunca use `generate-design` para substituir o template.
- Toda produção acontece em uma nova duplicata.
- Não publique no Instagram sem autorização explícita separada.

## Entradas

Antes de produzir, confirme ou recupere:

1. perfil de destino: João ou Dataceler;
2. conteúdo-fonte autorizado;
3. quantidade de páginas, se especificada;
4. objetivo editorial e CTA;
5. template oficial correspondente no Canva.

Se o perfil estiver claro, não pergunte novamente. Se o template ainda não estiver identificado de forma inequívoca, pesquise os brand templates do Canva e peça escolha somente quando houver ambiguidade real.

## Localização e duplicação do template

1. Use `search-brand-templates` primeiro, pois o usuário está pedindo um template.
2. Não use query de busca a menos que o usuário dê um título ou tipo explícito; caso contrário, liste os disponíveis e identifique João/Dataceler por nome e miniatura.
3. Quando o template for um Brand Template (`BTM...`), duplique com `create-design-from-brand-template`.
4. Se o usuário confirmar que o “template” é na verdade um design existente (`D...`), localize-o como design e duplique com `copy-design`.
5. Registre os IDs confirmados em `references/canva-template-registry.md` para evitar nova seleção em produções futuras.
6. Verifique a duplicata com `get-design`; confirme ID novo, URL, título, quantidade de páginas e que o ID é diferente do original.

Conclusão: existe uma cópia real e editável; o original permanece intacto.

## Produção na duplicata

1. Desenvolva o roteiro com uma ideia principal por página.
2. Preserve do template:
   - grade;
   - hierarquia;
   - avatar, nome e handle do perfil;
   - tipografia;
   - paleta;
   - margens;
   - elementos recorrentes;
   - lógica de continuidade.
3. Inicie `start-editing-transaction` somente no ID da duplicata.
4. Aplique o conteúdo com `perform-editing-operations`, preferindo `find_and_replace_text` para alterações parciais e respeitando as regras de páginas responsivas.
5. Não invente selos, métricas, fontes, comentários, datas ou afirmações.
6. Se o número de páginas do conteúdo não couber no template duplicado, não mutile texto nem force letras pequenas. Explique a limitação e proponha ajustar o roteiro ou duplicar páginas no Canva manualmente quando a ferramenta não suportar a operação necessária.

## Conteúdo editorial

- O estilo Twitter/X é ritmo editorial, não simulação enganosa de uma postagem real.
- Uma página, uma ideia.
- Use frases curtas, progressão clara e continuidade entre páginas.
- Preserve voz do perfil:
  - João: autoral, direto, ensinável e humano;
  - Dataceler: institucional, executivo e orientado à aplicação empresarial.
- A legenda complementa; não repete página por página.
- Para fatos atuais, use fontes primárias e registre a data da verificação.

## QA e aprovação

1. Leia novamente o conteúdo da duplicata.
2. Verifique todas as páginas disponíveis e suas miniaturas.
3. Confirme:
   - perfil, avatar e handle corretos;
   - ordem e quantidade de páginas;
   - nenhuma referência do template ficou sem substituição;
   - ortografia e fatos;
   - ausência de clipping, overflow e texto pequeno;
   - consistência do arco;
   - original intacto.
4. Mostre as prévias obtidas ao usuário.
5. As mudanças permanecem em rascunho até aprovação explícita.
6. Só chame `commit-editing-transaction` depois de o usuário aprovar claramente.
7. Após o commit, forneça o link direto da duplicata no Canva.
8. Se o usuário rejeitar, corrija na mesma transação quando possível ou cancele com `cancel-editing-transaction`.

## Armadilhas

- Editar o template original.
- Criar do zero quando existe template oficial.
- Usar o template de João na Dataceler ou vice-versa.
- Tratar `generate-design` como duplicação.
- Materializar vários candidatos e espalhar cópias desnecessárias.
- Confirmar alterações sem prévia.
- Declarar salvo antes do commit.
- Publicar sem autorização.
- Transferir este workflow para outros formatos.

## Verificação final

A produção só está concluída quando:

- o template correto foi identificado;
- uma duplicata com ID diferente foi criada;
- somente a duplicata foi editada;
- todas as páginas foram revisadas;
- o usuário aprovou a prévia;
- a transação foi commitada com sucesso;
- o link direto da duplicata foi entregue;
- nada foi publicado automaticamente.
