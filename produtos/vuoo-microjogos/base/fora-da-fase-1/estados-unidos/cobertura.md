# Cobertura por domínio — Estados Unidos

Classificação conforme §6.4 do [briefing](../../padroes-README.md): **C** completa, **P** parcial, **I** indireta, **A** ausente, **NV** não verificada. Sem notas de qualidade. Base: fichas e [modelo-de-dados.md](modelo-de-dados.md). Classificações são julgamento desta pesquisa [I] sobre o escopo documentado.

| Referência | D1 Org. acadêmica | D2 Aprendizagem | D3 Aprendiz | D4 Currículo | D5 Avaliação | D6 Experiência | D7 Inclusão | D8 Interop./Gov. |
|---|---|---|---|---|---|---|---|---|
| Ed-Fi DS 6.1 | C | P (LearningStandard) | P (histórico, programas) | P | C (Assessment, Grade) | A (Intervention apenas) | P (SpecialEducation, IEP early access, Accommodation) | C (API, descritores, extensões) |
| CEDS 14 | C | NV | P | NV | P | NV | NV | P (vocabulário; sem API) |
| OneRoster 1.2 | P (sem calendário de dias, sem programas) | A | I (demographics) | A | P (Gradebook) | I (Resources) | A | C |
| Edu-API 1.0 | P (ensino superior; catálogo/oferta) | I (LearningObjectiveSet) | A | I | A | A | A | C (OAuth, escopo de privacidade) |
| CASE 1.1 | A | C | A | C | I (CFRubric NV) | A | A | P |
| Caliper 1.2 | I (group, membership) | A | I | A | P (eventos de avaliação) | C | A | P |
| QTI 3.0 | A | I (alinhamento) | A | A | C | P | P (PNP) | P |
| CLR 2.0 / OB 3.0 | A | I (Alignment) | C | A | P (Result, rubrica) | A | A | C (VC) |
| LTI 1.3 / Advantage | I (context, NRPS) | A | A | A | P (AGS) | P | A | C |
| Common Cartridge | A | A | A | I | P (QTI) | P | A | P |
| CCSS | A | C | A | C | A | A | A | P (identificadores, XML) |
| NGSS | A | C | A | C | P (assessment boundary) | A | A | A (sem formato máquina localizado) |
| FERPA | A | A | P (direitos sobre o registro) | A | A | A | A | C |
| COPPA | A | A | A | A | A | A | A | P (consentimento, retenção) |
| Leis estaduais (SOPIPA e outras) | A | A | A | A | A | A | A | P |

## Leitura

- **D1** fica bem coberto pela soma Ed-Fi + OneRoster + Edu-API; as três divergem em *onde* põem a vigência e o papel, o que é exatamente o teste do Core.
- **D2/D4**: CASE é o transporte; CCSS e NGSS são o conteúdo. NGSS sem formato legível por máquina localizado é a maior lacuna prática.
- **D6** só tem Caliper (e LTI como canal). Nenhum padrão americano modela percurso adaptativo ou jogo; Ed-Fi Path é sobre trajetória de pós-secundário/carreira [I: inferido do nome dos modelos; não lido].
- **D7**: a cobertura americana é organizada por **programa legal** (IDEA/IEP, Section 504 — este não verificado), não por barreira/funcionalidade; QTI PNP é a exceção orientada a necessidade.
- **D8**: forte em transporte e em lei federal; a variação estadual é a parte menos documentada.
