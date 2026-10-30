---
id: acs.asmt.conformance-evaluation
titulo: Avaliação de conformidade de acessibilidade
tipo: tecnica
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [w3c2026wcagem2, w3c2026actrulesformat11, w3c2026actrules, vigo2013benchmarking, duran2017tools, webaim2026million, iti2025vpat]
relacoes:
  - { tipo: depende-de, alvo: acs.std.wcag }
  - { tipo: especificado-por, alvo: acs.std.wcag }
  - { tipo: complementa, alvo: acs.asmt.user-testing-with-at }
  - { tipo: relacionado-a, alvo: acs.std.procurement-en-301-549-and-section-508 }
  - { tipo: relacionado-a, alvo: acs.br.emag-and-nbr-17225 }
  - { tipo: relacionado-a, alvo: acs.dim.cognitive-accessibility }
termos: [avaliação de conformidade, WCAG-EM, amostra estruturada, amostra aleatória, processo completo, linha de base de suporte de acessibilidade, declaração de avaliação, ACT Rules, regra atômica, regra composta, cantTell, implementação consistente, ferramenta automática, cobertura, completude, correção, VPAT, ACR]
---

# Avaliação de conformidade de acessibilidade

## Definição e terminologia

Avaliação de conformidade é o procedimento de verificar se um produto digital satisfaz os critérios de sucesso de uma norma de acessibilidade, em geral as WCAG 2.x (ver `acs.std.wcag`), em um nível-alvo (A, AA ou AAA). Três peças a compõem: uma **metodologia** que diz o que examinar e como amostrar (WCAG-EM), um **formato de regra de teste** que diz como verificar cada aspecto de um critério de forma reprodutível (ACT Rules) e um **formato de declaração** que comunica o resultado (por exemplo, o VPAT/ACR).

O que não é: não é teste com usuários (ver `acs.asmt.user-testing-with-at`), não é auditoria de usabilidade e não é a rodada de uma ferramenta automática. A própria metodologia do W3C adverte que "using this methodology alone does not result in being able to make WCAG 2 conformance claims" [F: w3c2026wcagem2].

## Problema que resolve

Sites e aplicativos têm milhares de telas e estados; não dá para testar tudo à mão, e testar só a página inicial esconde barreiras nos fluxos. A avaliação de conformidade dá um caminho reprodutível para decidir o que amostrar, como testar e o que relatar. A escala do problema é grande: a análise automática de um milhão de páginas iniciais feita pela WebAIM em fevereiro de 2026 detectou falhas WCAG 2 em 95,9% delas, com média de 56,1 erros por página; as falhas mais comuns foram texto com baixo contraste (83,9% das páginas), imagens sem texto alternativo (53,1%), campos de formulário sem rótulo (51%), links vazios (46,3%), botões vazios (30,6%) e idioma do documento ausente (13,5%) [F: webaim2026million].

## Fundamentos e funcionamento

### WCAG-EM 2.0

A WCAG Evaluation Methodology 2.0 é uma Group Note do W3C publicada em 23 de julho de 2026 pelo Accessibility Guidelines Working Group, que sucede a WCAG-EM 1.0 de 2014 e é escrita para as WCAG 2.2; como Group Note, tem o endosso do grupo de trabalho e não do W3C como Recomendação [F: w3c2026wcagem2, status]. Ela organiza a avaliação em cinco passos [F: w3c2026wcagem2, §§1 a 5]:

1. **Definir o escopo**: o produto, o nível-alvo (AA é o recomendado em geral), a **linha de base de suporte de acessibilidade** (combinações de navegador e tecnologia assistiva em que o conteúdo deve funcionar) e requisitos adicionais.
2. **Explorar o produto**: telas comuns, funcionalidade essencial, tipos de amostra, tecnologias de que o conteúdo depende.
3. **Selecionar uma amostra representativa**: uma amostra estruturada, uma amostra aleatória e os **processos completos** (fluxos de várias telas, como cadastro ou entrega de uma atividade). A amostra aleatória é "10% of the structured sample set", somada à estruturada; o exemplo do documento é 80 + 8 = 88 amostras [F: w3c2026wcagem2, §3.2].
4. **Avaliar a amostra**: todas as amostras iniciais e todos os processos completos; comparar estruturada e aleatória e, se a aleatória revelar tipos de conteúdo ou falhas novas, voltar à seleção [F: w3c2026wcagem2, §4.3].
5. **Relatar**: documentar cada passo; opcionalmente registrar detalhes, emitir uma **declaração de avaliação**, um escore agregado e relatórios legíveis por máquina [F: w3c2026wcagem2, §5].

A declaração de avaliação só pode ser publicada quando todos os requisitos não opcionais foram cumpridos, todas as amostras avaliadas atendem ao alvo e o responsável se compromete a mantê-la correta; há forma prevista para conformidade parcial [F: w3c2026wcagem2, §5.3]. Sobre ferramentas, o texto diz: "While most accessibility checks are not fully automatable, evaluation tools can significantly assist evaluators" [F: w3c2026wcagem2].

### ACT Rules

O ACT Rules Format 1.1 é Recomendação do W3C desde 5 de fevereiro de 2026 e não é totalmente retrocompatível com a 1.0 [F: w3c2026actrulesformat11, status]. Uma regra ACT é "a plain language description of how to test a specific type of content for a specific aspect of an accessibility requirement", serve a testes automáticos e manuais, e pode ser **atômica** (uma condição) ou **composta** (combina resultados de regras atômicas) [F: w3c2026actrulesformat11]. Cada regra traz identificador, mapeamento para requisitos, aplicabilidade, expectativas, pressupostos, suporte de acessibilidade e exemplos. Os resultados possíveis são `passed`, `failed`, `inapplicable`, `cantTell` (por exemplo, aplicabilidade automatizada mas expectativa a julgar manualmente) e `untested` [F: w3c2026actrulesformat11]. Uma ferramenta é **consistente** com uma regra quando não contradiz seus exemplos, não deixa resultados `untested`, reprova ao menos um exemplo de falha e mapeia os requisitos da mesma forma [F: w3c2026actrulesformat11]. O formato admite que os exemplos "do not guarantee that implementations will never produce incorrect results".

O repositório de regras é mantido pelo ACT Rules Community Group com a ACT Task Force do AG WG; uma regra passa de proposta a aprovada depois que ao menos uma ferramenta ou metodologia a implementa integralmente; muitos critérios das WCAG 2.2 ainda aparecem com "No ACT Rules available for this criterion yet", e as regras são informativas, não necessárias para declarar conformidade [F: w3c2026actrules].

### Limites das ferramentas automáticas

Dois estudos independentes convergem. Vigo, Brown e Conway testaram seis ferramentas contra as WCAG 2.0: a cobertura chega no máximo a metade dos critérios de sucesso, a completude (proporção de violações reais detectadas) fica entre cerca de 14% e 38%, e as ferramentas mais completas erram mais, com correção de cerca de 66% a 71% [F: vigo2013benchmarking, resumo]. O serviço digital do governo britânico montou uma página com 143 falhas em 19 categorias e testou dez ferramentas: a melhor encontrou 41% (contando os avisos para inspeção manual), todas juntas encontraram 71%, e 29% das barreiras não foram encontradas por nenhuma; a conclusão é que as ferramentas "cannot be relied on, by themselves, to check the accessibility of a website" [F: duran2017tools]. A própria WebAIM avisa que "Absence of detected errors does not indicate that a page is accessible or conformant" [F: webaim2026million].

### Declaração: VPAT e ACR

O VPAT (Voluntary Product Accessibility Template) é um modelo gratuito do Information Technology Industry Council (ITI), na versão 2.5Rev de abril de 2025, com edições 508 (Section 508 revisada), EU (EN 301 549), WCAG (WCAG 2.2) e INT (as três); preenchido com resultados de teste, chama-se ACR (Accessibility Conformance Report); cada critério recebe "supports; partially supports; does not support; or not applicable", e o ITI não revisa, aprova nem certifica VPATs ou ACRs [F: iti2025vpat]. É, portanto, autodeclaração do fornecedor.

## Requisitos e pressupostos

- Versão da norma e nível-alvo fixados antes de começar [F: w3c2026wcagem2, §1.2].
- Linha de base de suporte de acessibilidade explícita; sem ela, "funciona com leitor de tela" não é verificável [F: w3c2026wcagem2, §1.3].
- Avaliador com competência manual: a maioria das verificações não é automatizável [F: w3c2026wcagem2].
- Em produto com muito conteúdo gerado ou dinâmico (atividades, jogos), os processos completos precisam incluir os fluxos interativos, não só páginas estáticas [I].

## Vantagens e limitações

Vantagens: método reprodutível e comparável entre avaliadores; regras ACT reduzem divergência entre ferramentas; o ACR dá linguagem comum para compras públicas (ver `acs.std.procurement-en-301-549-and-section-508`). Limitações: conformidade com WCAG não garante uso efetivo por todas as pessoas, sobretudo nas barreiras cognitivas pouco cobertas por critérios testáveis (ver `acs.dim.cognitive-accessibility`) [I]; ferramentas automáticas cobrem fração pequena e erram [F: vigo2013benchmarking; duran2017tools]; o VPAT não tem verificação independente [F: iti2025vpat]; a amostragem pode perder telas raras mas críticas [I].

## Alternativas e comparações

| Método | O que entrega | Cobertura | Custo | Limite principal |
|---|---|---|---|---|
| Varredura automática | Lista de falhas detectáveis | Parcial; 14% a 38% das violações reais em um estudo [F: vigo2013benchmarking] | Baixo | Falsos negativos e positivos |
| Revisão especialista com WCAG-EM | Avaliação por critério em amostra representativa | Todos os critérios no nível-alvo [F: w3c2026wcagem2] | Médio a alto | Depende da competência do avaliador |
| Teste com usuários de TA | Barreiras reais de uso | Não mapeia critérios exaustivamente | Alto | Não generalizável a partir de poucos usuários (ver `acs.asmt.user-testing-with-at`) |
| Autodeclaração (VPAT/ACR) | Documento de conformidade | A do teste que a fundamenta | Variável | Sem certificação [F: iti2025vpat] |

## Métricas e métodos de avaliação

Proporção de critérios atendidos por amostra e por processo; número de falhas por critério; escore agregado, que a WCAG-EM trata como opcional [F: w3c2026wcagem2, §5.4]; para ferramentas: cobertura, completude e correção [F: vigo2013benchmarking]; para regras: consistência da implementação com a regra ACT [F: w3c2026actrulesformat11].

## Exemplo técnico independente de domínio

```
avaliacao(produto, alvo="WCAG 2.2 AA"):
    escopo = definir(produto, alvo, baseline=[(navegador_A, leitor_de_tela_X), (sistema_B, ampliador_Y)])
    estruturada = telas_comuns + funcionalidade_essencial + um_de_cada_tipo(atividade, video, formulario)
    aleatoria = sortear(produto.telas, n = ceil(0.10 * len(estruturada)))
    processos = [login -> escolher_atividade -> responder -> ver_feedback]
    para cada amostra em estruturada + aleatoria + processos:
        auto = rodar_regras_ACT(amostra)            # passed | failed | cantTell
        manual = revisar(amostra, criterios_nao_automatizaveis + cantTell)
    se aleatoria revelou falha nova: ampliar(estruturada); repetir
    relatorio(por_criterio, por_processo, baseline, data, versao)
```

## Relações com outros conceitos

Depende de `acs.std.wcag` e é especificada por ela. Complementa `acs.asmt.user-testing-with-at`, que encontra o que critérios não capturam. Relaciona-se com `acs.std.procurement-en-301-549-and-section-508` (o ACR é o artefato de compra), com `acs.br.emag-and-nbr-17225` (requisitos brasileiros a avaliar) e com `acs.dim.cognitive-accessibility` (onde a conformidade é mais fraca).

## Lacunas e questões abertas

- Não foi verificado se a WCAG-EM 2.0 trata de aplicativos nativos e jogos com o mesmo detalhe que de páginas web; o texto fala em "digital product", mas a aplicação a mecânicas de jogo não foi analisada.
- Não há estudo aberto recente, equivalente ao de 2013, sobre completude de ferramentas atuais baseadas em ACT; o texto integral de Vigo et al. não foi lido, só o resumo.
- Não foi localizado procedimento brasileiro oficial de declaração de conformidade equivalente ao ACR.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| w3c2026wcagem2 | normativo (W3C Group Note) | 2026-10-30 |
| w3c2026actrulesformat11 | normativo (W3C Recommendation) | 2026-10-30 |
| w3c2026actrules | normativo (repositório W3C WAI) | 2026-10-30 |
| vigo2013benchmarking | academico (resumo no repositório institucional) | 2026-10-30 |
| duran2017tools | tecnico (blog do serviço digital do governo britânico) | 2026-10-30 |
| webaim2026million | tecnico | 2026-10-30 |
| iti2025vpat | tecnico (associação setorial) | 2026-10-30 |
