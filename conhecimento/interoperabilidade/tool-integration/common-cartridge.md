---
id: iop.tool.common-cartridge
titulo: Common Cartridge
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2011cc, imsglobal2022qti30]
relacoes:
  - { tipo: complementa, alvo: iop.tool.lti-core }
  - { tipo: complementa, alvo: iop.asmt.qti }
  - { tipo: alternativa-a, alvo: iop.tool.scorm }
  - { tipo: relacionado-a, alvo: iop.md.ieee-lom }
termos: [cartridge, imsmanifest.xml, Thin CC, web link, LTI link, question bank, perfil de conteúdo]
---

# Common Cartridge

## Definição e terminologia

Common Cartridge é o formato do 1EdTech para empacotar e intercambiar conteúdo e avaliações entre plataformas. **Thin CC** é um perfil reduzido, centrado em links (web links e links LTI) em vez de conteúdo embarcado [F: imsglobal2011cc] [I].

Versões e datas, conforme o índice de especificações [F: imsglobal2011cc]:

| Versão | Situação |
|---|---|
| 1.0 | Final Specification (sem data na página) |
| 1.1 | Final, fevereiro de 2011, revisada em maio de 2011 |
| 1.2 | Final, outubro de 2011 |
| 1.3 | Final, julho de 2013 |
| Thin CC | Implementation Guide de maio de 2015, para CC v1.2 e v1.3; substitui o Thin CC v1.3 |

## Problema que resolve

Mover um curso inteiro — materiais, links, bancos de questões, tópicos de discussão — entre plataformas, sem recriar manualmente a estrutura [I].

## Fundamentos e funcionamento

**Manifesto.** A partir da v1.3, o XML descritor de recurso pode ser fornecido inline no `imsmanifest` [F: imsglobal2011cc].

**Tipos de recurso.** A v1.3 acrescentou IWB (lousa interativa), EPUB3 e APIP, e suporta uma lista extensível de tipos [F: imsglobal2011cc].

**Links.** Web links e links LTI fazem parte do Thin CC. A partir da v1.3, links LTI podem carregar metadados LOM completos e padrões curriculares [F: imsglobal2011cc].

**Avaliações.** A v1.2 exigia metadados `cc_profile` para itens QTI; há esquema de item de avaliação QTI listado da v1.0 à v1.3. A v1.3 permite mais de um banco de questões [F: imsglobal2011cc].

**Discussões.** Há um esquema `imsdt` listado da v1.0 à v1.3 [F: imsglobal2011cc].

**Conformidade.** A página não descreve programa de certificação; orientação de conformidade e *test cartridges* vêm pela Common Cartridge Alliance, e há um registro de extensões provisórias [F: imsglobal2011cc].

## Requisitos e pressupostos

- A plataforma de destino implementa os mesmos tipos de recurso; tipos não suportados são ignorados ou falham na importação [I].
- Para links LTI dentro do cartridge, há registro prévio da ferramenta na plataforma de destino, ou o link não lança (ver `iop.tool.lti-core`) [I].

## Vantagens e limitações

Vantagens [I]: transporta estrutura de curso completa, inclusive avaliações e links de ferramenta; o perfil Thin CC reduz drasticamente o tamanho e o acoplamento, por transportar referências em vez de arquivos.

Limitações [I]:
- O conjunto de especificações consultado tem versão mais recente de 2013 (e guia Thin CC de 2015) [F: imsglobal2011cc]; é um padrão estável, não em evolução ativa.
- Lista extensível de tipos de recurso significa que dois cartridges conformes podem não ser intercambiáveis na prática.
- Sem certificação central documentada na página, "compatível com Common Cartridge" é difícil de verificar.

## Alternativas e comparações

| Necessidade | Common Cartridge | SCORM | Deep Linking |
|---|---|---|---|
| Curso completo entre plataformas | sim | parcial (um curso SCORM) | não |
| Rastreio de progresso | não | sim | não |
| Seleção interativa de conteúdo | não | não | sim |
| Avaliações | QTI embarcado | limitado | depende da ferramenta |

## Métricas e métodos de avaliação

Importação de um cartridge de teste em cada plataforma alvo, medindo quantos recursos sobrevivem à importação sem intervenção [I].

## Relações com outros conceitos

Complementa `iop.tool.lti-core` (o cartridge transporta links LTI) e `iop.asmt.qti` (transporta itens de avaliação). O QTI 3.0, por sua vez, perfila o 1EdTech Content Packaging v1.2 e também o IEEE LOM [F: imsglobal2022qti30, §2.4], o que mostra a família de empacotamento compartilhada [I].

## Lacunas e questões abertas

- Existe Common Cartridge 1.4? A página consultada não a menciona [F: imsglobal2011cc]; verificar no portal de padrões do 1EdTech.
- Relação entre Common Cartridge e o Content Packaging 1.2 perfilado pelo QTI 3.0 não foi verificada em detalhe.
- Estado atual da Common Cartridge Alliance: não verificado.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2011cc | normativo | 2026-10-29 |
| imsglobal2022qti30 | normativo | 2026-10-29 |
