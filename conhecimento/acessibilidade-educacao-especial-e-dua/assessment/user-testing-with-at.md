---
id: acs.asmt.user-testing-with-at
titulo: Testes com usuários de tecnologia assistiva e com crianças com deficiência
tipo: tecnica
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2024involvingusers, w3c2026wcagem2, hanna1997guidelines, markopoulos2008evaluating, valencia2021ux, peltomaki2025experiences, thompson2020ethical]
relacoes:
  - { tipo: complementa, alvo: acs.asmt.conformance-evaluation }
  - { tipo: relacionado-a, alvo: acs.part.inclusive-and-participatory-design }
  - { tipo: depende-de, alvo: dat.ethics.consent-and-assent-in-research }
  - { tipo: relacionado-a, alvo: psg.consent.child-assent }
  - { tipo: relacionado-a, alvo: acs.at.screen-readers-and-accessibility-apis }
  - { tipo: relacionado-a, alvo: acs.at.alternative-access }
  - { tipo: relacionado-a, alvo: acs.at.aac }
  - { tipo: relacionado-a, alvo: ped.std.single-case-designs }
termos: [teste com usuários, avaliação informal, teste de usabilidade formal, usuário de tecnologia assistiva, nível de experiência com TA, pensar em voz alta, proxy, observação prolongada, adaptação de comunicação, fator de UX para TEA]
---

# Testes com usuários de tecnologia assistiva e com crianças com deficiência

## Definição e terminologia

Teste com usuários, neste domínio, é a observação de pessoas com deficiência usando o produto com a sua própria tecnologia assistiva (TA) e o seu próprio modo de comunicação, para encontrar barreiras de uso. O W3C distingue **avaliações informais**, que "can be very simple" (por exemplo, pedir a um usuário de leitor de tela que encontre um dado numa tabela em rascunho), e **testes de usabilidade formais**, que "follows established protocols to gather quantitative and qualitative data" com usuários representativos [F: w3c2024involvingusers].

O que não é: não é avaliação de conformidade (ver `acs.asmt.conformance-evaluation`) nem estudo de eficácia de aprendizagem (desenhos de caso único ficam em `ped.std.single-case-designs`). Também não é um "teste com uma pessoa cega" que valida o produto para todas as pessoas cegas.

## Problema que resolve

A conformidade não basta: o guia do W3C diz que a avaliação com usuários "identifies usability issues that are not discovered by conformance evaluation alone" e que a conformidade "alone cannot determine if a website is accessible", recomendando combinar as duas [F: w3c2024involvingusers]. Para crianças com deficiência intelectual ou de comunicação, o problema é anterior: os métodos de avaliação foram feitos para adultos típicos. Uma revisão sobre sistemas para pessoas com TEA observou que vários estudos avaliaram usabilidade e UX "using evaluation methods focused on end users without disabilities" e que faltam modelos de UX particularizados [F: valencia2021ux, resumo]; a revisão da UNICEF Innocenti registra que crianças com deficiência tendem a ser excluídas da geração de evidências quando os processos não são adaptados [F: thompson2020ethical].

## Fundamentos e funcionamento

### Recomendações do W3C

O guia "Involving Users in Evaluating Web Accessibility" (EOWG, editora Shawn Lawton Henry; publicado em 2005, revisto em 2021 e com links atualizados em 2024) recomenda [F: w3c2024involvingusers]:

- envolver "a few people with disabilities" e, conforme o público, pessoas idosas; uma variedade de usuários é preferível;
- casar o **nível de experiência com TA** com o público: um sistema interno pode pedir "advanced assistive technology users", um serviço público "novice assistive technology users";
- fazer avaliações informais ao longo do desenvolvimento, mais eficazes do que só um teste formal no fim;
- planejar acessibilidade do local, preparação da TA e remuneração dos participantes (o guia remete a recursos externos);
- não generalizar: resultados de poucas pessoas "cannot be generalized to apply to all people with similar disabilities", e estudos pequenos não têm significância estatística; o relatório deve declarar escopo, método e características dos participantes.

A WCAG-EM 2.0 permite registrar requisitos adicionais de avaliação no escopo, o que abre espaço para incluir testes com usuários no mesmo relatório [F: w3c2026wcagem2, §1.4] [I].

### Crianças como participantes

A literatura de interação criança-computador tem guias próprios. Hanna, Risden e Alexander publicaram em 1997 diretrizes para teste de usabilidade com crianças na revista interactions [F: hanna1997guidelines, metadados], e Markopoulos, Read, MacFarlane e Höysniemi sistematizaram métodos em livro de 2008 (Evaluating Children's Interactive Products) [F: markopoulos2008evaluating, metadados]. O conteúdo das duas obras não foi lido nesta sessão; a adaptação de protocolos de "pensar em voz alta" à idade, frequentemente atribuída a elas, fica como não verificada.

### Crianças com deficiência intelectual

A revisão sistemática de Peltomäki et al. (41 estudos) catalogou 27 subcategorias de adaptação para ouvir crianças com deficiência intelectual moderada a profunda: figuras, símbolos gráficos, faces emocionais, Talking Mats, sinais-chave, fotografias, dispositivos geradores de fala; muitas vezes com apoio da equipe escolar. Entrevistas e questionários com adaptações simples servem a crianças que falam; para crianças "with non-symbolic communication and severe or profound intellectual disabilities", os autores apontam tarefas e observação prolongada [F: peltomaki2025experiences, resumo e resultados]. A UNICEF acrescenta que o dissentimento pode ser não verbal (passividade, silêncio, choro) e deve encerrar a sessão [F: thompson2020ethical, seção 3.2.1].

### Crianças autistas

Valencia, Rusu e Botella propõem nove fatores de UX para pessoas com TEA, derivados das características e necessidades dessa população e de diretrizes de estudos anteriores, como base "to adapt and/or create UX evaluation instruments and methods" [F: valencia2021ux, resumo]. Trata-se de proposta teórica, não de instrumento validado.

## Requisitos e pressupostos

- Participantes usando a própria TA, configurada como no dia a dia; testar com TA desconhecida mede o desconhecimento, não o produto [I, coerente com w3c2024involvingusers].
- Consentimento do responsável e assentimento da criança, com materiais acessíveis (ver `psg.consent.child-assent` e `dat.ethics.consent-and-assent-in-research`).
- Avaliação prévia do modo de comunicação e de quem medeia (professor, profissional de AEE, familiar) [F: peltomaki2025experiences].
- Tarefas definidas antes; para crianças, sessões curtas e ambiente familiar [H].

## Vantagens e limitações

Vantagens: encontra barreiras que critérios não capturam, inclusive de compreensão e de esforço; gera exemplos concretos que orientam a equipe [F: w3c2024involvingusers]. Limitações: poucos participantes, sem generalização [F: w3c2024involvingusers]; risco de usar adultos (pais, terapeutas) como **proxy** e perder a perspectiva da criança [I]; métodos verbais excluem crianças sem fala [F: peltomaki2025experiences]; custo e logística de recrutamento.

## Alternativas e comparações

| Formato | Quando usar | Força | Fraqueza |
|---|---|---|---|
| Informal pontual com usuário de TA | Durante o desenvolvimento, dúvida específica | Rápido, barato [F: w3c2024involvingusers] | Sem protocolo, achado anedótico |
| Usabilidade formal com tarefas | Antes de lançar fluxos críticos | Dados comparáveis | Exige protocolo e amostra planejada |
| Observação prolongada em contexto | Crianças sem comunicação simbólica | Inclui quem não responde a perguntas [F: peltomaki2025experiences] | Lento; interpretação do observador |
| Relato de proxy (pais, professores) | Complemento | Acessível | Não substitui a voz da criança [I] |
| Co-design | Exploração inicial | Participação real (ver `acs.part.inclusive-and-participatory-design`) | Não mede desempenho |

## Métricas e métodos de avaliação

Conclusão de tarefa, tempo, erros e pedidos de ajuda; número e gravidade das barreiras encontradas, ligadas ao critério WCAG quando houver; para crianças com comunicação limitada, registros de observação (envolvimento, sinais de desconforto) e escolhas feitas com apoios visuais [F: peltomaki2025experiences]. Questionários padronizados de usabilidade feitos para adultos típicos devem ser adaptados antes do uso [F: valencia2021ux].

## Exemplo técnico independente de domínio

```
plano_teste(fluxo):
    perfis = [leitor_de_tela(experiente), leitor_de_tela(iniciante), acionador+varredura,
              ampliador, crianca_DI_fala, crianca_sem_fala_simbolica, crianca_TEA]
    para cada participante p:
        pre: consentimento(responsavel) e assentimento(p, material_acessivel(p))
        ambiente: TA_de_p, configuracao_de_p, mediador_conhecido_se_necessario
        tarefas = adaptar(fluxo.tarefas, p.modo_comunicacao)    # simbolos, demonstracao
        coletar(conclusao, tempo, ajudas, barreiras, sinais_de_dissentimento)
        se dissentimento: parar e registrar
    relatorio: barreiras x criterio WCAG x perfil, sem generalizar por deficiência
```

## Relações com outros conceitos

Complementa `acs.asmt.conformance-evaluation`. Depende de `dat.ethics.consent-and-assent-in-research` e se relaciona com `psg.consent.child-assent` para a ética. Relaciona-se com `acs.part.inclusive-and-participatory-design` (participação desde o desenho), com `acs.at.screen-readers-and-accessibility-apis`, `acs.at.alternative-access` e `acs.at.aac` (as TAs envolvidas) e com `ped.std.single-case-designs` quando o objetivo passa a ser medir efeito.

## Lacunas e questões abertas

- Os guias clássicos de teste com crianças (Hanna et al., 1997; Markopoulos et al., 2008) foram verificados só por metadados.
- Não foi localizada revisão aberta específica sobre métodos de teste de usabilidade com crianças com deficiência intelectual; a melhor evidência aberta vem de pesquisa sobre ouvir essas crianças em geral.
- Uma revisão de 2024 sobre métodos de avaliação de usabilidade para pessoas com TEA foi encontrada em busca, mas o DOI indicado não resolveu; não foi citada.
- Não há consenso sobre número mínimo de participantes por perfil de TA.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2024involvingusers | normativo (orientação W3C WAI, não normativa) | 2026-10-30 |
| w3c2026wcagem2 | normativo (W3C Group Note) | 2026-10-30 |
| hanna1997guidelines | academico [metadados] | 2026-10-30 |
| markopoulos2008evaluating | academico [metadados] | 2026-10-30 |
| valencia2021ux | academico (resumo via Crossref) | 2026-10-30 |
| peltomaki2025experiences | academico | 2026-10-29 |
| thompson2020ethical | tecnico | 2026-10-29 |
