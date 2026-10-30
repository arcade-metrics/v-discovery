---
id: acs.relatorio
titulo: Relatório da primeira versão do domínio acessibilidade, educação especial e DUA
tipo: relatorio
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
---

# Relatório: primeira versão do domínio acessibilidade, educação especial e DUA

Data: 2026-10-30. Esta é a primeira versão funcional pedida por `_modelo/metodo-e-qualidade.md`: estrutura, documentos principais fundamentados em fontes verificadas, bibliografia, glossário, mapa e matriz. Todos os documentos estão em `status: rascunho`. A passagem para `revisado` exige o checklist de `_modelo/checklist-revisao.md` por leitor humano.

## Método aplicado

Nove frentes de pesquisa, uma por pasta prevista no brief (`foundations`, `udl`, `standards`, `assistive-tech`, `access-dimensions`, `adaptation`, `participation`, `assessment`, `brazil`). Cada frente seguiu o plano de ids de `_plano-ids.md` e três regras: abrir a fonte antes de citá-la; registrar como lacuna o que não pôde abrir (texto pago, bloqueio de acesso automatizado, só metadados ou resumo); e confirmar, no frontmatter real, todo id de outro domínio usado em relação. As fontes foram consultadas em 2026-10-30; duas chaves reaproveitadas de outro domínio trazem consulta de 2026-10-29.

Cada frente produziu seus documentos e um fragmento de bibliografia e índice em `referencias/fragmentos/acs-<area>.bib` e `acs-<area>-indice.md`. Os fragmentos foram mesclados em `referencias/bibliografia.bib` e `referencias/indice-fontes.md` por `_modelo/mesclar_referencias.py`. Os arquivos de índice do domínio (README, glossário, mapa, matriz e este relatório) foram escritos depois, só a partir dos 35 documentos. A única fonte reaberta nessa etapa foi a Portaria MEC 421/2026 (cópia do sistema MECNormas hospedada pelo IFG), para corrigir `acs.asmt.pei-and-aee-plans` (ver inconsistência 1). O validador `_modelo/validar.py`, rodado sobre a base inteira, confere ids únicos com prefixo correto, alvos de relação existentes (inclusive em outros domínios), chaves de fonte presentes na bibliografia e ausência de menção a produto consumidor. Em 30/10/2026, depois da mesclagem, o validador deu 0 avisos e 0 erros para este domínio; na base inteira, os erros restantes eram todos citações de `gamificacao-e-jogos`, domínio com pesquisa em andamento na mesma data.

## Cobertura

| Área | Documentos | Conteúdo |
|---|---|---|
| foundations | 3 | modelos médico, social, biopsicossocial e de direitos humanos (CDPD, GC4, GC6, CIF); barreira, acessibilidade e adaptação razoável (*ex ante* x *ex nunc*); desenho universal (sete princípios do CUD) e desenho inclusivo |
| udl | 3 | DUA e diretrizes do CAST 3.0 (2024) com as mudanças desde a 2.2; seis revisões e metanálises com reanálise e críticas; DUA x diferenciação x adaptação individual |
| standards | 6 | WCAG 2.2, ISO/IEC 40500:2025 e WCAG 3 (rascunho de 2026); WAI-ARIA 1.2, APG e ARIA 1.3; ISO/IEC 24751 e AfA PNP 3.0; EN 301 549 V4.1.1 e Section 508; GAG, XAG 3.2 e APX; comparação |
| assistive-tech | 4 | definições CAT, LBI, OMS e ISO 9999:2022; Core-AAM e APIs de Android, iOS e Windows, pesquisa WebAIM 2026; varredura, olhar e voz com taxas; CAA, evidência e licenças de seis conjuntos de símbolos |
| access-dimensions | 4 | COGA, linguagem simples (ISO 24495-1, Lei 15.263/2025) e leitura fácil; contraste, reflow, APCA e audiodescrição; legendas, língua de sinais e redundância visual do som; alvos, tempo, gestos e tremor |
| adaptation | 4 | perfis de preferência (PNP, GPII, media features); acomodação x modificação (NCEO, Sireci); adaptação de jogos (GAG, XAG 108 e 117); adaptável x adaptativo x iniciativa mista |
| participation | 3 | desenho inclusivo (IDRC, Microsoft) e design participativo com crianças com deficiência; autodeterminação (agência causal, SDI, SDLMI); participação como construto (fPRC e instrumentos) |
| assessment | 4 | WCAG-EM 2.0, ACT Rules 1.1, limites das ferramentas, VPAT; testes com usuários de TA e com crianças; Index for Inclusion, CHIEF, SIS-C; PAEE, PEI e IEP |
| brazil | 4 | LBI e quadro de obrigatoriedade; PNEEPEI, linha do tempo até o Decreto 12.686/2025 e a Portaria MEC 421/2026; eMAG 3.1 e NBR 17225; Libras |
| raiz | 7 | brief, plano de ids, README, glossário, mapa, matriz comparativa, este relatório |

Totais: 35 documentos conceituais (37 contando brief e plano de ids). 254 relações tipadas no mapa de conceitos: 127 `relacionado-a`, 74 `complementa`, 20 `depende-de`, 12 `avaliado-por`, 11 `parte-de`, 10 `especificado-por`. 218 chaves de fonte distintas no frontmatter dos documentos. Os nove fragmentos têm 220 entradas e 212 chaves distintas (oito chaves estão em dois fragmentos, entre elas `w3c2024wcag22`, `imsglobal2021afapnp` e `gameaccessibility2026fulllist`); as outras seis chaves citadas (`aera2014standards`, `castudl2024`, `peltomaki2025experiences`, `thompson2020ethical`, `who2001icf`, `wilson2026easyread`) já estavam na bibliografia por outros domínios. 505 termos declarados nos campos `termos:`, 465 distintos.

Marcas de afirmação no corpo dos 35 documentos, contadas por script (ocorrências de colchete aberto com a marca, fora do frontmatter; um colchete com duas citações conta uma vez):

| Área | `[F]` | `[I]` | `[H]` |
|---|---|---|---|
| foundations | 105 | 16 | 0 |
| udl | 91 | 26 | 1 |
| standards | 121 | 33 | 1 |
| assistive-tech | 107 | 20 | 1 |
| access-dimensions | 91 | 32 | 3 |
| adaptation | 104 | 45 | 0 |
| participation | 80 | 13 | 0 |
| assessment | 123 | 14 | 1 |
| brazil | 125 | 27 | 3 |
| **Total** | **947** | **226** | **10** |

A contagem inclui a correção de `acs.asmt.pei-and-aee-plans` feita nesta data.

## O que o brief pediu e onde está

| Entregável | Local |
|---|---|
| Estrutura de diretórios | `acessibilidade-educacao-especial-e-dua/` (9 pastas temáticas, mais `_plano-ids.md`) |
| README com escopo, navegação e convenções | `README.md` deste domínio |
| Glossário | `glossario.md` |
| Mapa conceitual | `mapa-conceitos.md` |
| Documentos fundamentados em fontes primárias | as 9 pastas temáticas |
| Bibliografia BibTeX | fragmentos `acs-*.bib` mesclados em `conhecimento/referencias/bibliografia.bib` |
| Matriz comparativa | `matriz-comparativa.md` (dezesseis comparações) |
| Relatório de cobertura e lacunas | este arquivo |

## Normas recentes que mudaram o quadro

Atos e versões publicados entre 2024 e 2026 que os documentos já incorporam:

- **WCAG-EM 2.0** (Group Note do W3C, 23/07/2026), escrita para a WCAG 2.2, com amostra aleatória de 10% da estruturada e declaração de avaliação (acs.asmt.conformance-evaluation). Junto com ela, o **ACT Rules Format 1.1** virou Recomendação em 05/02/2026, sem retrocompatibilidade plena com a 1.0.
- **EN 301 549 V4.1.1** (2026-09): alinha as cláusulas 9, 10 e 11 à WCAG 2.2 e se destina ao European Accessibility Act; a citação no Jornal Oficial da UE não foi verificada (acs.std.procurement-en-301-549-and-section-508).
- **ISO/IEC 40500:2025** (setembro de 2025): a WCAG 2.2 como norma ISO, substituindo a edição de 2012 (WCAG 2.0); o catálogo indica revisão em curso desde fevereiro de 2026 (acs.std.wcag).
- **Rascunhos do W3C**: WCAG 3 (Working Draft de 10/09/2026, com contraste ainda indefinido), WAI-ARIA 1.3 (04/06/2026), Core-AAM 1.2 (21/10/2026), Media Queries 5 (19/02/2026); "Using ARIA" passou a Discontinued Draft em 24/02/2026.
- **UDL Guidelines 3.0** (30/07/2024): meta de agência do aprendiz, 36 considerações, novas considerações sobre identidade, vieses e práticas excludentes (acs.udl.udl-guidelines).
- **Decreto 12.686/2025**, alterado pelo **Decreto 12.773/2025**, e **Portaria MEC 421/2026** (alterada pela 550/2026): institui a PNEEI e a Reneei, revoga o Decreto 7.611/2011, torna obrigatórios o estudo de caso, o PAEE e o PEI, fixa conteúdo mínimo e revisão anual, veda condicionar matrícula e AEE a laudo e dá três anos para as redes se adaptarem (acs.br.pneepei-and-aee, acs.asmt.pei-and-aee-plans).
- **Lei 15.263/2025** (14/11/2025): Política Nacional de Linguagem Simples para a administração pública, com dezoito técnicas e teste com o público (acs.dim.cognitive-accessibility).
- **Lei 15.249/2025**: CAA de baixa tecnologia no AEE (LBI art. 28, XIX) e eliminação de barreiras para pessoas com necessidades complexas de comunicação (Lei 10.098/2000, art. 17) (acs.br.lbi).
- **ABNT NBR 17225:2025** (lançada em 11/03/2025): 146 itens entre requisitos e recomendações, voluntária (acs.br.emag-and-nbr-17225).
- **Art. 63 da LBI ainda sem regulamento técnico**: o MPF recomendou em 29/08/2025 a regulamentação; a Secretaria de Governo Digital indicou edição até 31/12/2025; nenhum ato foi localizado em 30/10/2026 (acs.br.lbi).

## Fontes que não puderam ser verificadas

Padrão recorrente: normas ISO e ABNT são pagas e foram lidas só por metadados, resumo de catálogo ou amostra (a página da ISO respondeu 403); vários artigos acadêmicos foram lidos só no resumo; algumas páginas de fornecedor não abriram. Cada caso está na seção "Lacunas" do documento e na nota da entrada BibTeX do fragmento. Por área:

- **foundations**: textos integrais de Oliver (2013, só metadados) e de Shakespeare e Watson (2001, só resumo); GC4 em reprodução não oficial e GC6 em versão avançada, numeração a conferir; Comentário Geral nº 2 não lido; manual completo da CIF não consultado; original dos princípios do CUD na NC State não localizado (usada reprodução); transcrição do episódio da CAST sobre Ron Mace não lida.
- **udl**: Meyer, Rose e Gordon (2014) só por metadados e a edição de 2025 não examinada; textos integrais de Capp, King-Sears et al., Almeqdad et al., Boysen e Rao et al. não lidos (números dos resumos); os cinco moderadores de King-Sears et al. não identificados; Bissonnette (2026) é working paper; Griful-Freixenet et al. e Tomlinson (2014) só por resumo ou metadados; Zhang et al. (2024) só metadados.
- **standards**: textos das partes 1 a 4 da ISO/IEC 24751 e da ISO/IEC 40500:2025 não acessados; divergência de rótulo do PNP 3.0 não resolvida; citação da EN 301 549 V4.1.1 no Jornal Oficial não verificada; cláusula 11 da EN lida só nos limites de tempo; lista completa da XAG e padrões APX além de dois não lidos; seção de conformidade do WCAG 3 não lida por inteiro.
- **assistive-tech**: ISO 9999:2022 lida em amostra pública francesa, sem as divisões; Catálogo Nacional de Produtos de TA não respondeu; ata do CAT só em cópia hospedada por um membro; página de CAA da ASHA (403); só o excerto oficial de Beukelman e Light; Koester e Simpson lidos via Nel et al.; documentação Apple de `accessibilityLabel` e afins sem texto legível; valores padrão de varredura não publicados.
- **access-dimensions**: textos da ISO 24495-1 e da NBR ISO 24495-1 não abertos, e status da NBR (vigente e cancelada na mesma página) a confirmar; NBR 16452 (audiodescrição) com o mesmo problema de status; World report on vision e World report on hearing só pela página de publicação; ABNT NBR 15290 não aberta; Smart Touch (Mott et al.) e ISO/TS 9241-411 não abertos.
- **adaptation**: AERA/APA/NCME Standards (2014) não lidos, definições via NCEO; Sireci et al. (2005) só no resumo; Grammenos et al. (2009) só no resumo e Yuan et al. (2011) só metadados; Jameson e Schwarzkopf (2002) não aberto; documentação do UI Options do Fluid não abriu; status final do PNP 3.0 não confirmado.
- **participation**: Frauenberger, Good e Keay-Bright (2011) só no resumo; Druin (2002) só metadados; Imms et al. (2016, 2017), Adair et al. (2018) e os artigos de instrumentos só no resumo do PubMed; teoria da agência causal (2015) e as metanálises de 2001 e 2020 sobre autodeterminação só por metadados.
- **assessment**: Vigo et al. (2013) só no resumo; Hanna et al. (1997) e Markopoulos et al. (2008) só metadados; Thompson et al. (2009) e CHIEF-CP só metadados; edição de 2011 do Index for Inclusion não consultada; texto de Glat, Vianna e Redig sobre PEI não localizado; Portaria MEC 550/2026 não aberta.
- **brazil**: texto integral da NBR 17225 não aberto; Portaria MEC 550/2026 não aberta e a 421/2026 lida na visão "vigente" do MECNormas, sem conferência no DOU; redação vigente do Decreto 12.686 lida pelas notas do Planalto; página do Planalto da LBI com codificação corrompida; Resolução SEDUC-SP 129/2025 e andamento do PDL 30/2025 não verificados; eventual nova resolução do CNE após 2025 não verificada.

## Inconsistências entre documentos, para revisão

Encontradas na leitura dos 35 documentos para este índice. Só a primeira foi corrigida nesta data; as demais ficam para o revisor.

1. **Ato do MEC previsto no art. 7 do Decreto 12.686/2025. Resolvido.** `acs.asmt.pei-and-aee-plans` dizia que o ato não fora localizado e que a norma federal não fixava periodicidade nem conteúdo mínimo; `acs.br.pneepei-and-aee` já citava a Portaria MEC 421/2026. A fonte foi reaberta em 30/10/2026 e os artigos conferidos: art. 7, §§2 a 4 (documento único, revisão anual, vedação de laudo), arts. 10 e 11 (conteúdo mínimo do PAEE e do PEI) e art. 37 (três anos para adequação). O documento passou a citar `mecportaria4212026`, retirou a lacuna, harmonizou periodicidade e conteúdo mínimo e manteve como lacuna a Portaria 550/2026 não aberta.
2. **Ciclo de dependência.** `acs.std.wai-aria` declara `depende-de` `acs.at.screen-readers-and-accessibility-apis`, e este declara `depende-de` `acs.std.wai-aria`. Uma das duas deveria virar `complementa`.
3. **Duas chaves para a mesma página (resolvido em 30/10/2026).** As chaves `gag2026fulllist` e `gag2026timing`, criadas pela frente adaptation, apontavam para as mesmas páginas da Game Accessibility Guidelines que `gameaccessibility2026fulllist` e `gameaccessibility2026timing`. Foram unificadas nestas duas, que ficam com o tipo de fonte `tecnico` do fragmento acs-standards; as entradas redundantes saíram de acs-adaptation.
4. **Rótulo do PNP 3.0.** `acs.std.accessforall-iso-24751` registra a divergência entre "Public Draft 2" (lista da 1EdTech) e "Candidate Final" (página do documento); `acs.adapt.preference-profiles` usa só "Candidate Final" no corpo e na tabela de fontes, com a dúvida apenas na lacuna.
5. **Lacunas remetidas a documento que não as fecha.** `acs.dim.visual` remete braile e linhas braile a `acs.at.screen-readers-and-accessibility-apis`, que não os trata (o brief previa "baixa visão e braile" em assistive-tech). `acs.dim.auditory` remete a ABNT NBR 15290 a `acs.br.libras`, que não a abriu. `acs.found.disability-models` remete o instrumento federal de avaliação biopsicossocial (LBI art. 2, §2) a `acs.br.lbi`, que não verifica sua regulamentação. `acs.adapt.accommodation-vs-modification` remete a correspondência com LBI e AEE a `acs.br.lbi` e `acs.br.pneepei-and-aee`, que não a fazem; a Portaria 421/2026, art. 11, II ("medidas de acessibilidade curricular, didático-pedagógica e avaliativa") é o ponto de partida.
6. **Relações redundantes ou discutíveis.** `acs.asmt.conformance-evaluation` declara `depende-de` e `especificado-por` para o mesmo alvo `acs.std.wcag`. `acs.adapt.preference-profiles` declara `parte-de` `acs.udl.udl-differentiation-and-individualization`, que é documento de comparação; `relacionado-a` parece mais fiel.
7. **Desenho inclusivo definido em dois lugares.** `acs.found.universal-design` (com `idrc2026whatisinclusive`) e `acs.part.inclusive-and-participatory-design` (com `idrc2026inclusiveguide` e `treviranus2018dimensions`) definem o termo. As definições são compatíveis; o glossário aponta o segundo como dono.
8. **Status de normas ABNT.** A NBR ISO 24495-1:2024 (acs.dim.cognitive-accessibility) e a NBR 16452 (acs.dim.visual) aparecem como "Vigente" e "cancelada" na mesma página de catálogo. Não é contradição entre documentos, mas o mesmo ponto pendente em dois deles.

## Lacunas de conhecimento consolidadas

1. **Regulamentação brasileira pendente.** Ato que regulamente o art. 63 da LBI e defina critério técnico e alcance a aplicativos (acs.br.lbi); ato que torne a NBR 17225 obrigatória ou substitua o eMAG no SISP (acs.br.emag-and-nbr-17225); instrumento federal de avaliação biopsicossocial (acs.found.disability-models, acs.asmt.barriers-and-support-needs); texto da Portaria 550/2026 e conferência da 421 no DOU (acs.br.pneepei-and-aee).
2. **Evidência do DUA.** Nenhum estudo da versão 3.0; nenhuma metanálise que separe efeito para estudantes com e sem deficiência; nenhum estudo brasileiro controlado; o valor da escolha entre múltiplos meios e a base nas redes cerebrais seguem sem teste (acs.udl.udl-evidence).
3. **Critério cognitivo testável.** Não há critério que avalie compreensão de conteúdo por crianças ou por pessoas com deficiência intelectual, nem métrica de nível de leitura validada para o português (acs.std.wcag, acs.dim.cognitive-accessibility).
4. **Crianças com deficiência como população de estudo.** Tamanho de alvo para crianças com deficiência motora ou menores de 7 anos (acs.dim.motor); digitação por olhar e varredura com crianças (acs.at.alternative-access); uso de leitor de tela por crianças (acs.at.screen-readers-and-accessibility-apis); adaptável x adaptativo com crianças com deficiência (acs.adapt.algorithmic-adaptation-and-autonomy); autodeterminação e participação por autorrelato para quem não usa linguagem simbólica (acs.part.self-determination, acs.part.participation-as-construct).
5. **Instrumentos validados no Brasil.** Nenhuma versão brasileira validada verificada de SIS-C, PEM-CY, CAPE/PAC, Picture my Participation ou SDI (acs.asmt.barriers-and-support-needs, acs.part.participation-as-construct, acs.part.self-determination).
6. **Varredura em jogos.** Faltam diretrizes de tempo de ciclo e ordem de varredura em jogo, e valores verificados de janela viável (acs.std.game-accessibility-guidelines, acs.at.alternative-access, acs.adapt.adapting-games-and-activities).
7. **Validade de medidas em atividades lúdicas adaptadas.** Nenhum estudo mede se ajustes de tempo e entrada em jogos educacionais alteram a validade das medidas (acs.adapt.adapting-games-and-activities, acs.adapt.accommodation-vs-modification).
8. **Quem declara o perfil da criança.** Falta orientação publicada sobre quem declara o perfil de preferência de criança com deficiência e como conciliar a voz dela com restrições de avaliação (acs.adapt.preference-profiles).
9. **Recursos em português.** Nenhum conjunto de símbolos de CAA aberto e validado para o português do Brasil; nenhum padrão brasileiro de leitura fácil (acs.at.aac, acs.dim.cognitive-accessibility).
10. **Libras digital.** Equivalência entre intérprete humano e avatar não verificada; dever geral de Libras em conteúdo educacional digital só existe para cursos médios e superiores a distância (acs.br.libras).
11. **Eficácia do PEI e do design participativo.** Não há evidência brasileira sobre efeito do PEI na aprendizagem (acs.asmt.pei-and-aee-plans) nem revisão que meça se o design participativo melhora o produto resultante (acs.part.inclusive-and-participatory-design).
12. **Propostas não validadas.** Limiares de alvo, área ativa e filtro de holdover (acs.dim.motor, `[H]`); regra de preferência declarada como restrição da inferência (acs.adapt.algorithmic-adaptation-and-autonomy); material didático bilíngue digital por extensão do art. 60-B da LDB (acs.br.libras, `[H]`); alcance do art. 63 a plataformas que não sejam "sítio" (acs.br.lbi, `[H]`).

## Respostas às perguntas abertas do brief

| Pergunta do brief | Resposta desta versão | Id |
|---|---|---|
| Que parte do DUA tem evidência experimental sobre aprendizagem e que parte é prescrição de desenho ainda sem teste? | Há evidência de que pacotes "baseados em DUA" podem melhorar desempenho (g = 0,43 na metanálise com controle) e engajamento, mas com poucos estudos longos, presenciais e com população regular; na reanálise, só dois passaram, sem transferência para teste padronizado. Técnicas isoladas citadas pelo CAST têm apoio próprio. O valor da escolha entre múltiplos meios, a base nas redes cerebrais e as considerações novas da 3.0 não foram testados. As considerações funcionam como prescrições de desenho. | acs.udl.udl-evidence, acs.udl.udl-guidelines |
| Onde a conformidade com WCAG deixa de garantir acesso, sobretudo para barreiras cognitivas, e o que preenche essa lacuna? | O próprio W3C admite que a WCAG não cobre toda necessidade cognitiva; os critérios de leitura ficam em AAA e os novos critérios A/AA tratam só ajuda, reentrada e autenticação. As exceções de "essencial" e "tempo real" deixam de fora a mecânica de jogo, e o reflow isenta jogos. Preenchem: COGA, linguagem simples e leitura fácil; perfis de preferência; diretrizes de jogos; e testes com usuários de TA, porque ferramentas automáticas acham de 14% a 38% das violações. | acs.std.wcag, acs.dim.cognitive-accessibility, acs.std.comparison, acs.asmt.user-testing-with-at, acs.asmt.conformance-evaluation |
| Como representar preferências e necessidades de acesso de forma portável entre sistemas, e quem deve declarar esse perfil? | Por perfil funcional, não diagnóstico: o PNP da AccessForAll / ISO/IEC 24751, com conjuntos de ativação, de opção e de proibição, e perfis por contexto; as media features do sistema cobrem só preferências gerais. A especificação não diz quem declara. Recomendação dos documentos: registrar quem declarou cada valor, deixar a pessoa alterar o que não for restrição de avaliação e ouvir a criança. O perfil é dado que pode revelar deficiência e pede minimização. | acs.adapt.preference-profiles, acs.std.accessforall-iso-24751 |
| Quando adaptar automaticamente ajuda e quando retira da pessoa a escolha sobre como aprender? | Ajuda quando compensa barreira de acesso estável e mensurável, a pessoa vê e desfaz a mudança, ou a inferência substitui um formulário inacessível e vira preferência editável. Retira a escolha quando reduz a habilidade-alvo sem aviso (modificação silenciosa) ou quando a pessoa queria o desafio. A preferência declarada deve limitar a inferência, e a sugestão deve ser confirmada. A evidência vem de adultos em tarefas de menu. | acs.adapt.algorithmic-adaptation-and-autonomy, acs.adapt.accommodation-vs-modification, acs.part.self-determination |
| Que mecânicas e tempos de jogo são barreiras para acionadores, varredura ou rastreamento ocular, e como compensar sem descaracterizar a atividade? | Barreiras: janela de reação curta, segurar, repetir rápido, ações simultâneas, sequências a memorizar, gesto de trajetória, alvo pequeno ou móvel e câmera contínua; na varredura, cada escolha custa vários ciclos; no olhar, o toque de Midas. Compensação: ajuste de velocidade, pausa ativa, alternar em vez de segurar, esquema de controle simplificado, atraso pós-aceitação, pular trecho fora da mecânica central e dificuldade por mecânica. Para não descaracterizar, decide-se contra o construto da atividade e o dado carrega a condição de jogo. Faltam diretrizes de tempo para varredura em jogo. | acs.std.game-accessibility-guidelines, acs.at.alternative-access, acs.adapt.adapting-games-and-activities |
| Como avaliar barreiras e necessidades de suporte sem reduzir a pessoa a um diagnóstico? | Medindo o descompasso entre pessoa e ambiente e os apoios que o fecham, com potencialidades: Index for Inclusion para a escola, CHIEF e PEM-CY para o ambiente, SIS-C para a intensidade de suporte; separando attendance e involvement; priorizando autorrelato acessível e tratando o proxy como outra perspectiva. A CDPD e o Decreto 12.686/2025 vedam condicionar apoio a laudo; o estudo de caso usa as mesmas categorias. Faltam versões brasileiras validadas. | acs.asmt.barriers-and-support-needs, acs.part.participation-as-construct, acs.found.disability-models, acs.asmt.pei-and-aee-plans |
| Quais requisitos legais e normativos brasileiros são obrigatórios para plataformas educacionais digitais, e quais são apenas recomendados? | Obrigatórios: acessibilidade de sítios de empresas com sede ou representação no país (LBI art. 63, sem regulamento técnico); recursos de acessibilidade e TA sem cobrança na escola, inclusive privada (art. 28, §1); eMAG para o SISP; janela de Libras e legenda em cursos médios e superiores a distância; AEE, estudo de caso, PAEE e PEI sem laudo para as redes. Recomendados: NBR 17225, eMAG fora do SISP, Libras em vídeo no eMAG, linguagem simples fora do setor público. | acs.br.lbi, acs.br.emag-and-nbr-17225, acs.br.libras, acs.br.pneepei-and-aee |

## Próximos passos sugeridos

1. **Revisão humana** dos 35 documentos com o checklist, começando pelos que dependem de metadados, resumo ou cópia não oficial: acs.std.accessforall-iso-24751, acs.udl.udl-evidence, acs.part.participation-as-construct, acs.br.pneepei-and-aee e acs.br.emag-and-nbr-17225.
2. **Resolver as inconsistências 2 a 8** acima: desfazer o ciclo ARIA x leitores de tela, unificar as chaves da Game Accessibility Guidelines, alinhar o rótulo do PNP 3.0, fechar ou reatribuir as lacunas órfãs (braile, NBR 15290, instrumento biopsicossocial, correspondência acomodação x AEE) e revisar as relações redundantes.
3. **Segunda rodada de fontes** com acesso institucional: normas ISO (24751, 9999, 40500, 24495-1) e ABNT (17225, 16452, 15290); DOU da Portaria 421/2026 e texto da 550/2026; textos integrais de King-Sears et al., Capp e Boysen.
4. **Acompanhar mudanças com data**: regulamentação do art. 63 da LBI; citação da EN 301 549 V4.1.1 no Jornal Oficial; próximos rascunhos do WCAG 3 (algoritmo de contraste); WAI-ARIA 1.3; revisão da ISO/IEC 40500; nova resolução do CNE sobre AEE.
5. **Fechar a fronteira com `fundamentos-pedagogicos`**: confirmar que `ped.incl.udl-in-practice`, `ped.incl.assistive-technology-in-teaching` e `ped.incl.evidence-based-practices-by-population` citam os ids `acs.*` em vez de redefinir DUA, TA e marco legal, para que cada fato tenha um dono.
6. **Conversão para grafo.** Com ids, relações tipadas e termos no frontmatter, um script pode gerar SKOS a partir dos arquivos, junto com `grafo-conhecimento-educacional`, como já recomendado nos relatórios dos domínios em primeira versão.
