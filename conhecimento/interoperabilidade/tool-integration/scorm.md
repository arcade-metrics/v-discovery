---
id: iop.tool.scorm
titulo: SCORM
tipo: padrao
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [scorm2026versions, scorm2026technical, aicc2026cmi5web]
relacoes:
  - { tipo: alternativa-a, alvo: iop.lr.cmi5 }
  - { tipo: alternativa-a, alvo: iop.lr.xapi }
  - { tipo: complementa, alvo: iop.tool.common-cartridge }
termos: [SCO, PIF, imsmanifest.xml, CAM, RTE, SN, sequencing]
---

# SCORM

## Definição e terminologia

SCORM (*Sharable Content Object Reference Model*) é o modelo de referência da ADL para empacotar, lançar e rastrear conteúdo de e-learning dentro de um LMS. Um **SCO** é a unidade lançável e rastreável; um **PIF** (*Package Interchange File*) é o pacote distribuível.

Versões: a linha SCORM 1.2 e a linha SCORM 2004, cuja edição mais recente é a 4th Edition, de março de 2009 [F: scorm2026versions]. As fontes consultadas são do mantenedor de ferramentas SCORM (Rustici Software), não da ADL — o site da ADL não respondeu à consulta [I].

## Problema que resolve

Permitir que um curso produzido por uma ferramenta de autoria rode em qualquer LMS conforme, preservando estrutura, progresso e nota [I].

## Fundamentos e funcionamento

**Content Aggregation Model (empacotamento).** O conteúdo é distribuído como diretório autocontido ou ZIP, chamado Package Interchange File. Um arquivo de manifesto `imsmanifest.xml` na raiz descreve a estrutura do curso, a informação de lançamento de cada SCO e metadados opcionais [F: scorm2026technical].

**Run-Time Environment.** O LMS lança o conteúdo no navegador e executa um SCO por vez. O conteúdo localiza uma API JavaScript fornecida pelo LMS para trocar dados. O modelo de dados é um vocabulário de elementos, com exemplos como status de conclusão, nota, bookmark e tempo total gasto [F: scorm2026technical].

**Sequencing and Navigation.** Regras em XML no manifesto controlam como o aluno navega entre SCOs e como o progresso é consolidado no nível do curso [F: scorm2026technical].

## Requisitos e pressupostos

- O conteúdo roda em navegador, na mesma sessão e em contexto onde a API JavaScript do LMS é alcançável [F: scorm2026technical] [I].
- O LMS mantém o estado entre sessões, já que o modelo prevê bookmark e tempo acumulado [I].

## Vantagens e limitações

Vantagens [I]: ecossistema maduro, suportado por praticamente todo LMS legado; vocabulário fechado, o que dá comparabilidade entre cursos de fornecedores diferentes.

Limitações [I]:
- Exige navegador e API JavaScript local: não cobre aplicação nativa, dispositivo offline, simulador ou atividade física.
- Modelo de dados rígido e orientado a curso; o próprio grupo do cmi5 registra que o modelo SCORM era "complicado demais e com muitos elementos opcionais que não eram usados" [F: aicc2026cmi5web].
- A edição mais recente é de 2009 [F: scorm2026versions]; não há evolução ativa comparável à do xAPI.
- Rastreia dentro do SCO; não registra experiência fora do conteúdo empacotado.

## Alternativas e comparações

cmi5 foi explicitamente pensado para substituir AICC e SCORM com abordagem mais flexível [F: aicc2026cmi5web]. Ver `iop.lr.comparison` para a tabela completa.

| Critério | SCORM | cmi5 |
|---|---|---|
| Lançamento | API JS no navegador | URL com parâmetros + token |
| Transporte de dados | API JS | REST para LRS |
| Fora do navegador | não | sim |
| Conclusão | `cmi.*` | `moveOn` |

## Métricas e métodos de avaliação

Conformidade historicamente verificada por suítes de teste da ADL; estado atual não verificado [H].

## Relações com outros conceitos

Alternativa a `iop.lr.cmi5` e a `iop.lr.xapi` no papel de rastreio de conteúdo. Complementa `iop.tool.common-cartridge`, que resolve o empacotamento de cursos inteiros com vários tipos de recurso.

## Lacunas e questões abertas

- Nomes exatos das funções da API (`Initialize`, `GetValue`, `SetValue`, `Commit`, `Terminate` em SCORM 2004; `LMSInitialize` etc. em 1.2) não foram confirmados em fonte primária; o site da ADL não respondeu e o material consultado não os nomeia.
- Datas das edições 1ª a 3ª do SCORM 2004 e da versão 1.2: não verificadas.
- Situação de manutenção do SCORM sob a ADL hoje: não verificada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| scorm2026versions | tecnico | 2026-10-29 |
| scorm2026technical | tecnico | 2026-10-29 |
| aicc2026cmi5web | secundario | 2026-10-29 |
