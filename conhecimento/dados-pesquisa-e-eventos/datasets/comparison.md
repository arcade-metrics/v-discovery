---
id: dat.ds.comparison
titulo: Comparação de datasets públicos de referência em educação
tipo: comparacao
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [koedinger2010datashop, datashop2026importformat, datashop2026terms, datashop2010kddcuprules, stamper2010kddcup, yu2010feature, heffernan2014assistments, assistments2026interpret, assistments2026terms, choi2020ednet, riiid2020ednetrepo, kuzilek2017oulad, chang2015junyi, datashop2026junyi1198, edudata2026junyi, junyi2020kaggle, settles2018slam, settles2018slamdata, liu2022pykt, xiong2016going]
relacoes:
  - { tipo: relacionado-a, alvo: dat.ds.pslc-datashop }
  - { tipo: relacionado-a, alvo: dat.ds.assistments }
  - { tipo: relacionado-a, alvo: dat.ds.ednet }
  - { tipo: complementa, alvo: adp.kt.comparison }
  - { tipo: complementa, alvo: dat.qual.granularity-and-constructs }
  - { tipo: complementa, alvo: dat.rd.data-documentation }
  - { tipo: relacionado-a, alvo: dat.rd.fair-principles }
  - { tipo: relacionado-a, alvo: lae.dq.bias-and-validity }
  - { tipo: relacionado-a, alvo: psg.deid.reidentification-risk }
  - { tipo: relacionado-a, alvo: psg.deid.anonymization-and-pseudonymization }
termos: [dataset de referência, granularidade de evento, latência de resposta, OULAD, KDD Cup 2010, Junyi Academy, Duolingo SLAM, k-anonimato, CC BY-NC]
---

# Comparação de datasets públicos de referência em educação

## Definição e terminologia

Compara os datasets de interação educacional mais citados como referência: o repositório PSLC DataShop (`dat.ds.pslc-datashop`), o KDD Cup 2010 (hospedado nele), os datasets ASSISTments (`dat.ds.assistments`), EdNet (`dat.ds.ednet`), OULAD, Junyi Academy e Duolingo SLAM 2018. Cada linha foi verificada em fonte aberta nesta sessão. **Granularidade** aqui significa a unidade da linha (ação de interface, transação, passo, resposta a item, resumo diário) e a resolução do tempo associado [I].

## Problema que resolve

Escolher um dataset de referência exige saber, antes de baixar, quem são os alunos, qual o grão, que tempo há, que licença vale e que defeitos são conhecidos. As fontes espalham essas informações em artigos, páginas de ajuda e termos de uso, com contagens que não batem entre si [I].

## Alternativas e comparações

### Quem publica, população e tamanho

| Dataset | Publicador | População | Tamanho | Fonte |
|---|---|---|---|---|
| PSLC DataShop | LearnLab/CMU | varia por dataset (tutores de álgebra, geometria, física, química, línguas, cursos on-line) | 164 datasets, 25 milhões de transações, >111.000 horas-aluno (jun. 2009) | [F: koedinger2010datashop, §I] |
| KDD Cup 2010 | PSLC DataShop, com dados de tutores de álgebra | Algebra 2005: alunos de 13-14 anos | Algebra 2008-09: 8.918.055 passos de treino; Bridge 2008-09: 20.012.499 | [F: datashop2010kddcuprules; liu2022pykt, §3.2; yu2010feature, Table 1] |
| ASSISTments | WPI | ensino fundamental II e médio, matemática, EUA | 2009: 4.217 alunos; 2012: 46.674; 2015: 19.917 | [F: heffernan2014assistments; choi2020ednet, Table 1] |
| EdNet | equipe de pesquisa do serviço, Coreia do Sul | candidatos ao TOEIC; idade não informada | 784.309 alunos, 131.441.538 interações | [F: choi2020ednet, §2] |
| OULAD | Open University, Reino Unido | adultos em ensino a distância, 7 módulos, 2013-2014 | 32.593 alunos, 22 módulo-apresentações, 10.655.280 linhas de clique | [F: kuzilek2017oulad] |
| Junyi 2015 | Academia Sinica com a plataforma, via DataShop | plataforma de matemática de Taiwan derivada do Khan Academy; idade não informada | 247.606 alunos; ~25,9 milhões de logs; 837 exercícios | [F: chang2015junyi; datashop2026junyi1198; edudata2026junyi] |
| Junyi 2020 | fundação sem fins lucrativos de Taiwan, via Kaggle | alunos da plataforma, 2018/08 a 2019/07; série não verificada | 72.630 alunos, 16.217.311 tentativas | [F: junyi2020kaggle] |
| Duolingo SLAM 2018 | Duolingo, via Harvard Dataverse | iniciantes nos primeiros 30 dias, inscritos em nov. 2015; idade não informada | ~6,4 mil aprendizes, >7,1 milhões de palavras | [F: settles2018slam; settles2018slamdata] |

### Granularidade, tempo, licença e problemas

| Dataset | Grão da linha | Tempo | Desidentificação | Licença e acesso | Problemas conhecidos |
|---|---|---|---|---|---|
| DataShop | transação (tentativa, dica, resposta do tutor) e rollups aluno-passo e aluno-problema | instante por transação, até milissegundo; duração de passo derivada | `Anon Student Id`; revisão de shareability ligada ao IRB | termos próprios: só pesquisa, sem redistribuição, sem desanonimizar | qualidade e população variam por dataset [I] |
| KDD Cup 2010 | aluno-passo, com `Correct First Attempt`, KC e oportunidade | `Step Start Time`, pode ser nulo | `Anon Student Id` | login no DataShop; citação Stamper et al. | partição teste com rótulos ocultos [F: datashop2010kddcuprules] |
| ASSISTments | aluno × problema | `first_response_time` em ms; `overlap_time` "often computed incorrectly" | ids substituídos; FERPA citada | termos: sem repasse, código e dados devem ser publicados | duplicatas no 2009-2010 (23,6%) [F: xiong2016going] |
| EdNet | resposta (KT1) até ação de interface (KT4) | timestamp Unix em ms por evento; tempos deslocados por valor fixo | um arquivo por id; método não descrito | CC BY-NC 4.0, links públicos | contagens divergentes no artigo; colunas divergentes na documentação |
| OULAD | resumo diário de cliques por material | dia relativo ao início da apresentação | k-anonimato com k = 5 (ARX 3.2.1), ids reatribuídos, idade e IMD generalizados | CC-BY 4.0 | não tem tempo de resposta nem itens [I] |
| Junyi 2015 | tentativa de exercício | `time_done` (timestamp; a documentação de terceiros diz microssegundos) e `time_taken` em segundos | não descrita | projeto público no DataShop; uso comercial vedado | dados extraídos em jan. 2015, artigo usou extração de jul. 2014 [F: edudata2026junyi] |
| Junyi 2020 | tentativa de problema | não verificado | não descrita | CC BY-NC-SA 4.0, versão 9 no Kaggle (atualizada em 13/05/2020) | dicionário de dados não verificado |
| Duolingo SLAM | token da resposta, rotulado certo/errado | `days` desde o início (fracionário) e `time` em segundos por exercício | id anônimo de 8 caracteres B64; países em ISO | CC BY-NC 4.0, versão 4 (13/02/2019) no Dataverse | partição sequencial 80/10/10 por usuário [F: settles2018slam, §2.5] |

Fontes da segunda tabela: [F: datashop2026importformat; datashop2026terms; stamper2010kddcup; assistments2026interpret; assistments2026terms; riiid2020ednetrepo; choi2020ednet; kuzilek2017oulad; edudata2026junyi; junyi2020kaggle; settles2018slam; settles2018slamdata].

### Usos típicos

DataShop e KDD Cup: curvas de aprendizagem, comparação de modelos de KC e previsão de acerto no primeiro intento [F: koedinger2010datashop, §IV; datashop2010kddcuprules]. ASSISTments e EdNet: benchmarks de knowledge tracing [F: liu2022pykt, §3.2; choi2020ednet, §4]. OULAD: previsão de desempenho e evasão combinando demografia e atividade no ambiente virtual [F: kuzilek2017oulad]. Junyi: relações entre exercícios (similaridade, dificuldade, pré-requisito) [F: chang2015junyi] e, na versão 2020, previsão de proficiência, trilhas e abandono [F: junyi2020kaggle]. SLAM: previsão de erro por palavra em aprendizes de segunda língua [F: settles2018slam].

## Vantagens e limitações

Para a pergunta "qual serve de referência para estudo com crianças dos anos iniciais e com tempo de resposta fino", a resposta, nesta revisão, é que **nenhum dataset verificado cobre crianças dos anos iniciais com população declarada** [I]. O que cada um oferece:

- **Como referência de formato**, o DataShop: transação com instante em milissegundo, tipo de resposta do aluno e do sistema, resultado, passo, KC, condição experimental e tipo de evento (avaliativo ou instrucional) [F: datashop2026importformat]. É o modelo mais completo e documentado para desenhar um log próprio [I].
- **Como referência de evento de interface com tempo fino**, EdNet KT4: cada ação (entrar, tocar áudio, eliminar alternativa, selecionar, sair) com timestamp em ms [F: choi2020ednet, Table 5], mas com adultos ou jovens adultos não descritos e tempos deslocados [F: riiid2020ednetrepo].
- **Como população escolar mais jovem com latência**, ASSISTments: ensino fundamental II, `first_response_time` em ms [F: assistments2026interpret], mas com grão de problema e campos de tempo frágeis.
- Junyi 2020 é o candidato mais próximo de crianças, pois a fundação declara atender "all children" [F: junyi2020kaggle], mas série escolar e resolução do tempo não foram verificadas.

O que **nenhum** deles oferece, pelo verificado [I]:
1. população dos anos iniciais (cerca de 6 a 10 anos) declarada e descrita;
2. eventos cognitivo-motores (trajetória de ponteiro ou toque, tempo de reação medido a partir do início do estímulo);
3. metadados de relógio e dispositivo (fonte do tempo, sincronização, latência de entrada) que permitam confiar em milissegundos;
4. indicadores de deficiência ou necessidade educacional específica em crianças (OULAD tem `disability`, mas para adultos [F: kuzilek2017oulad]);
5. documentação de consentimento e assentimento de crianças, ou datasheet no sentido de `dat.rd.data-documentation`;
6. dados em português ou de contexto brasileiro.

## Métricas e métodos de avaliação

Critérios usados nesta comparação, aplicáveis a novos candidatos [I]: população declarada (idade, nível, país); grão da linha; resolução e semântica do tempo; campos de resposta do sistema (feedback, dica); presença de KC; método de desidentificação descrito; licença; versionamento; defeitos conhecidos documentados. A reprodutibilidade de resultados depende de versão e pré-processamento: o AUC do DKT no ASSISTments2009 varia de 0,73 a 0,821 entre artigos [F: liu2022pykt, §3.3].

## Exemplo técnico independente de domínio

```
ficha_de_candidato:
  populacao: {idade: "6-10", nivel: anos iniciais, pais: ?}   # exigido
  grao: acao_de_interface | transacao | resposta | resumo_diario
  tempo: {resolucao_ms: 1, origem: estimulo_on|evento_ui, relogio: monotonic?}
  feedback_do_sistema: sim|nao ; kc: sim|nao
  desidentificacao: {metodo: descrito|nao, k: ?, deslocamento_tempo: ?}
  licenca: CC-BY | CC-BY-NC | termos_proprios ; versao: ?
  defeitos_conhecidos: [..]
aceitar se populacao e tempo atendem; senão usar só como referência de formato
```

## Relações com outros conceitos

Resume `dat.ds.pslc-datashop`, `dat.ds.assistments` e `dat.ds.ednet`. Complementa `adp.kt.comparison`, que compara modelos sobre esses dados, e `dat.qual.granularity-and-constructs`, que discute o grão mínimo. A falta de datasheets liga-se a `dat.rd.data-documentation` e a licenças não comerciais a `dat.rd.fair-principles`. Vieses de população em `lae.dq.bias-and-validity`; k-anonimato do OULAD e deslocamento de tempo do EdNet em `psg.deid.anonymization-and-pseudonymization` e `psg.deid.reidentification-risk`.

## Lacunas e questões abertas

- Série escolar, faixa etária e resolução de tempo do Junyi 2020 não verificadas (a página do Kaggle não renderiza sem JavaScript; só a API de metadados foi lida).
- Número de alunos do KDD Cup 2010 e da competição ASSISTments 2017 não verificados em fonte primária.
- Não foi feita busca sistemática por datasets com crianças pequenas (por exemplo, leitura inicial ou jogos educativos); outros podem existir no próprio DataShop.
- As contagens variam entre fontes (Junyi 2015: 25.925.922 logs em Choi et al. e 25.925.992 linhas na documentação de terceiros) [F: choi2020ednet, Table 1; edudata2026junyi].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| koedinger2010datashop | academico | 2026-10-30 |
| datashop2026importformat | fornecedor | 2026-10-30 |
| datashop2026terms | fornecedor | 2026-10-30 |
| datashop2010kddcuprules | fornecedor | 2026-10-30 |
| stamper2010kddcup | fornecedor | 2026-10-30 |
| yu2010feature | academico | 2026-10-30 |
| heffernan2014assistments | academico | 2026-10-30 |
| assistments2026interpret | fornecedor | 2026-10-30 |
| assistments2026terms | fornecedor | 2026-10-30 |
| choi2020ednet | academico | 2026-10-30 |
| riiid2020ednetrepo | fornecedor | 2026-10-30 |
| kuzilek2017oulad | academico | 2026-10-30 |
| chang2015junyi | academico | 2026-10-30 |
| datashop2026junyi1198 | fornecedor | 2026-10-30 |
| edudata2026junyi | secundario | 2026-10-30 |
| junyi2020kaggle | fornecedor | 2026-10-30 |
| settles2018slam | academico | 2026-10-30 |
| settles2018slamdata | fornecedor | 2026-10-30 |
| liu2022pykt | academico | 2026-10-30 |
| xiong2016going | academico | 2026-10-30 |
