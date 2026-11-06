# Ficha: Currículo Paulista (referencial estadual de São Paulo)

> Caso de currículo estadual alinhado à BNCC. PDF da etapa EI/EF baixado para leitura em diretório temporário (não versionado no repo): `curriculo_paulista_26_07_2019.pdf`, 526 páginas, SHA-256 `53e60892c40c5d589e222fde60d9d685bcc7870f010da8d86fb495b42f7094a2`. Acesso: 2026-11-05.

```yaml
id: br.sp.curriculo-paulista
name: Currículo Paulista
acronym: CP
jurisdiction: Estado de São Paulo (sistema estadual; adotado por redes municipais em regime de colaboração)
issuing_organization: Secretaria da Educação do Estado de São Paulo (Seduc-SP) e Undime-SP; normas fixadas pelo Conselho Estadual de Educação (CEE-SP)
reference_type: norma estadual (referencial curricular homologado por deliberação do CEE)
domain: [D4, D2]
official_url:
  - https://efape.educacao.sp.gov.br/curriculopaulista/
  - https://efape.educacao.sp.gov.br/curriculopaulista/wp-content/uploads/2022/07/curriculo_paulista_26_07_2019.pdf
  - https://www.ceesp.sp.gov.br/wp-content/uploads/2024/11/2020-00267-delib-186-20-indic-198-20-revogada-parcialmente.pdf (Deliberação CEE 186/2020, EM)
repository_url: not_found
version: "EI/EF: documento de 26/07/2019, homologado em 2019 (Deliberação CEE 169/2019, segundo resultados de busca); EM: Deliberação CEE 186/2020, homologada por resolução de 03/08/2020, parcialmente revogada pela Deliberação CEE 236/2025"
publication_date: 2019 (EI/EF); 2020 (EM)
last_updated: 2025 (revogação parcial da Del. 186/2020; conteúdo não verificado)
legal_status: vigente para a rede estadual (Res. SEDUC 129/2025 art. 2, XII o define como o documento que orienta a organização curricular da rede; Res. SEDUC 84/2024 art. 4 §1 vincula a FGB a ele)
mandatory_scope: rede estadual de SP; municípios que o adotaram por ato próprio (ex.: decretos municipais) [não generalizar]
education_levels: [EI, EF, EM]
geographic_scope: SP
language: pt-BR
license: unknown
technical_formats: [PDF]
api_available: false
data_model_available: false
ontology_available: false
schemas_available: false
implementation_examples: [Res. SEDUC 129/2025 Anexo IV (PEI pede "conteúdos e habilidades do Currículo da Rede Estadual Paulista" por bimestre)]
related_standards: [br.bncc, br.saresp, br.sp.resolucao-seduc-129-2025, br.novo-ensino-medio]
entities: [habilidade com código, objeto de conhecimento, unidade temática, prática de linguagem, campo de atuação, "linguagens" (Arte; equivale a unidade temática), ano]
relationships: [habilidade CP → habilidade BNCC de origem (pelo código), habilidade CP → ano (não bloco)]
vocabularies: [códigos BNCC reanuados, sufixos A/B/C, sufixo "*"; ver terminologia §2]
core_relevance: alta: é o caso real de "currículo derivado" que o Core precisa representar
regional_adapter_relevance: alta (prioridade SP)
limitations: [sem dataset oficial; sem tabela oficial de correspondência CP↔BNCC; significado do "*" não declarado no trecho lido]
open_questions: [Q-CUR-08, Q-CUR-09, Q-CUR-10]
sources: [E-15, E-16, E-17]
access_date: 2026-11-05
research_status: parcial (EI/EF lido no PDF; EM não lido)
```

## Análise técnica: como o CP deriva da BNCC

Levantamento automático dos códigos entre parênteses no PDF EI/EF (extração de texto, conferência visual não feita): **1.945 códigos distintos**, dos quais 1.362 no formato BNCC puro (`EF01LP05`), 451 com sufixo de letra (`EF01LP10A`, `EF01LP10B`, `EF01LP25C`) e 132 com asterisco (`EF01GE12*`, `EF01HI09*`, `EF01EF13*`). Contagem é indicativa [I], não auditada como a da BNCC no vuoo-base v1.1 (`dados/bncc-2018.json`).

| Mecanismo | Evidência no documento | Leitura para dados |
|---|---|---|
| **Mantém a gramática da BNCC** | "A estrutura dos códigos das habilidades do Currículo Paulista mantém a referência da BNCC para que, em caso de necessidade, seja possível observar sua correlação" (Arte, p. impressa 221-222) | o código CP é decodificável pela mesma gramática, mas **não** é o mesmo item da BNCC |
| **Bloco de anos vira ano** | "o código de referência da BNCC (EF15AR01)… o código… no Currículo Paulista (EF01AR01), em que a dezena alterada indica que a habilidade se refere ao 1º ano" (Arte); o mesmo para Educação Física: `EF35EF01` → `EF03EF01` (p. 264) | um item BNCC de bloco gera **vários** itens CP, um por ano: relação 1:n "derivado de" |
| **Desdobramento em partes** | `EF01LP10A` "Nomear as letras do…" e `EF01LP10B` "Recitar as letras do…" (p. ~111) | sufixo A/B/C = partes de uma habilidade BNCC [I, inferido do texto; o documento não define o sufixo no trecho lido] |
| **Habilidades criadas** | Educação Física: "algumas habilidades foram criadas" para a unidade temática Corpo, Movimento e Saúde (p. ~264); História: "algumas habilidades foram criadas com o objetivo de desenvolver aprendizagens sobre o percurso histórico do Estado de São Paulo" (p. ~425) | itens sem item BNCC de origem; o "*" coincide com esses casos [I] |
| **Unidade temática renomeada** | Arte: "aquilo que a BNCC chama de 'unidades temáticas' está nomeado como 'linguagens'" | nível organizador com rótulo local, mesmo tipo |
| **Ordem de apresentação alterada** | LP anos iniciais: habilidades "deslocadas de lugar… não ordenação numérica" | ordem do documento ≠ ordem do código |
| **Habilidades de ano ou articuláveis entre anos** | LP: "Específicas para o Ano" e "Articuláveis entre os Anos" (1,2; 1–5; 3–5; 6,7; 6–9; 8,9) | atributo de abrangência temporal do item |

### Consequências para o Core [I]

1. **Colisão de chave**: `EF01AR01` existe no CP e não existe na BNCC; `EF01LP05` existe nos dois com texto possivelmente diferente. Chave do item = (framework, código), nunca só código.
2. **Associação tipada obrigatória** (`C.CAS`): `derivaDe` (1:n, com subtipo: reanuação, desdobramento, adaptação textual), `criadoLocalmente` (sem origem), `equivalente` só quando texto idêntico verificado.
3. A correspondência CP→BNCC é **calculável pelo código** na maioria dos casos (remover sufixo, voltar ao bloco), mas isso é inferência; precisa de validação contra o texto antes de virar `exata`.
4. O PEI paulista e o SARESP referenciam habilidades do CP, não da BNCC: o alinhamento de avaliação e de plano individual passa pelo currículo estadual.
