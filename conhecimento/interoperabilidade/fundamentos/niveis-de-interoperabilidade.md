---
id: iop.fund.niveis-de-interoperabilidade
titulo: Níveis de interoperabilidade (técnica, semântica, organizacional, jurídica)
tipo: conceito
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [ec2026nifo, iso2020ts20748, imsglobal2019lti13]
relacoes:
  - { tipo: complementa, alvo: iop.sem.interoperabilidade-semantica }
  - { tipo: complementa, alvo: iop.fund.conformidade-e-certificacao }
  - { tipo: relacionado-a, alvo: iop.fund.dados-vs-protocolo }
termos: [interoperabilidade técnica, interoperabilidade semântica, interoperabilidade organizacional, interoperabilidade jurídica, camadas de interoperabilidade]
---

# Níveis de interoperabilidade

## Definição e terminologia

Interoperabilidade é a capacidade de dois ou mais sistemas trocarem informação e usarem a informação trocada. A literatura de governo eletrônico decompõe essa capacidade em camadas, porque o sucesso em uma delas não implica sucesso nas outras [I].

O European Interoperability Framework (EIF) organiza a interoperabilidade em quatro camadas — jurídica, organizacional, semântica e técnica — além de uma camada transversal de governança de serviços públicos integrados; o framework é apresentado com 12 princípios subjacentes [F: ec2026nifo].

Neste domínio adotamos a seguinte leitura operacional [I]:

- **Técnica**: os sistemas conseguem se conectar e trocar bytes. Transporte, formato de serialização, autenticação, versionamento de API.
- **Semântica**: os sistemas interpretam da mesma forma o significado do que foi trocado. Vocabulários, modelos de dados, identificadores de conceitos.
- **Organizacional**: os processos, papéis, responsabilidades e acordos de serviço entre as instituições estão alinhados. Quem publica, com que frequência, quem corrige erro, quem responde por qualidade.
- **Jurídica**: há base legal para a troca. Consentimento, finalidade, retenção, responsabilidade pelo tratamento.

O que o conceito **não** é: "interoperabilidade" não é sinônimo de "integração". Integração é a ligação de dois sistemas específicos; interoperabilidade é a propriedade de poder ligar-se a muitos sem acordo bilateral prévio [I].

## Problema que resolve

Uma implementação pode passar em todos os testes de conformidade técnica de um padrão e ainda assim produzir dados inúteis para quem os recebe. Dois LMS podem emitir eventos xAPI válidos com verbos diferentes para a mesma ação, ou com identificadores de atividade que não se referem à mesma coisa. Separar as camadas dá nome a essa falha e indica onde corrigi-la [I].

## Fundamentos e funcionamento

A ordem das camadas é de dependência, não de importância: sem transporte comum não há troca; com transporte comum e sem vocabulário comum há troca sem compreensão; com ambos e sem acordo organizacional há compreensão sem continuidade; e sem base jurídica a troca não pode ocorrer legalmente [I].

Cada camada tem seus próprios instrumentos:

| Camada | Instrumentos típicos | Exemplos neste domínio |
|---|---|---|
| Técnica | protocolo, binding, esquema, autenticação | REST/JSON do OneRoster, JWT do LTI 1.3, JSON-LD do Caliper |
| Semântica | vocabulário controlado, modelo de dados, ontologia | verbos xAPI, perfis Caliper, CASE, CEDS, ESCO |
| Organizacional | acordo de serviço, papéis, governança de identificadores | certificação 1EdTech, calendário do Censo Escolar |
| Jurídica | base legal, consentimento, minimização | LGPD, acordos de compartilhamento |

A ISO/IEC TS 20748-3:2020 trata explicitamente de interoperabilidade de dados de learning analytics, com orientações de mapeamento entre representações, tomando xAPI e Caliper como especificações de referência [F: iso2020ts20748]. O conteúdo normativo do documento não foi consultado, apenas os metadados do catálogo [I].

## Requisitos e pressupostos

- Existe um responsável identificável por cada camada. Em projetos reais, a camada organizacional costuma não ter dono, e é nela que a interoperabilidade falha [H].
- A camada semântica exige identificadores persistentes; sem eles, o mapeamento entre sistemas precisa ser refeito a cada troca [I].

## Vantagens e limitações

Vantagem do modelo em camadas: dá um diagnóstico acionável para falhas de integração e evita que "o padrão não funciona" substitua "não combinamos o vocabulário" [I].

Limitações: as camadas não são estanques. O LTI 1.3, por exemplo, embute decisões semânticas (vocabulário de papéis) dentro de um mecanismo técnico (claims de um JWT) [F: imsglobal2019lti13, §5.3.7] [I]. E a divisão de quatro camadas vem de um contexto de serviços públicos europeus, não de educação; a transposição é analogia, não norma [I].

## Alternativas e comparações

Outros modelos (LISI, níveis de maturidade de interoperabilidade organizacional) existem na literatura de sistemas de informação, mas não foram verificados nesta rodada [H].

## Métricas e métodos de avaliação

- Técnica: suítes de conformidade do mantenedor do padrão (ver `iop.fund.conformidade-e-certificacao`).
- Semântica: proporção de campos que sobrevivem a um ciclo de ida e volta entre dois sistemas sem perda de significado; número de termos que caem em "outro"/extensão [I].
- Organizacional e jurídica: auditoria documental, não teste automatizado [I].

## Relações com outros conceitos

Complementa `iop.sem.interoperabilidade-semantica`, que aprofunda a segunda camada, e `iop.fund.conformidade-e-certificacao`, que trata da verificação da primeira. Relaciona-se a `iop.fund.dados-vs-protocolo`, que classifica os padrões do catálogo por aquilo que eles de fato especificam.

## Lacunas e questões abertas

- O texto do EIF (COM(2017) 134) não foi lido integralmente; as definições de cada camada aqui são leitura operacional `[I]`, e a página consultada só confirma os nomes das camadas e a contagem de princípios [F: ec2026nifo].
- A ISO/IEC TS 20748-3 é paga; seria a referência natural para regras de mapeamento xAPI↔Caliper. Avaliar aquisição.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| ec2026nifo | normativo | 2026-10-29 |
| iso2020ts20748 | normativo (metadados) | 2026-10-29 |
