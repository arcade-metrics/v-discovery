# Questões abertas: currículo, avaliação e inclusão

> Ambiguidades, lacunas de verificação, conflitos e decisões pendentes. Cada item diz o que falta e como fechar. Data: 2026-11-05.

## Currículo

| Id | Questão | Tipo | Como fechar |
|---|---|---|---|
| Q-CUR-01 | **Resolvida em 06/11/2026:** versão final (2018), no repositório **vuoo-base** (`fontes/bncc/`, https://github.com/arcade-metrics/v-base): fonte oficial `BNCC_EI_EF_110518_versaofinal_site.pdf` (versão final, EI, EF e EM) e cópia de trabalho `BNCC_reparado.pdf`. Pergunta original: Qual edição da BNCC usar como texto canônico de EI/EF: 2017 (transcrita em [bncc/](bncc/README.md)) ou 2018 (bncc-dados)? Diferem em 9 textos de habilidade e 8 objetos com o mesmo código. | decisão | decidir; o modelo suporta as duas como `EdicaoDoTexto` com `equivalente` só onde o texto é idêntico |
| Q-CUR-02 | Os 2 códigos impressos duas vezes (EF05LP25, EF04LP27): qual registro um sistema externo quer dizer quando envia só o código? | ambiguidade da fonte | regra de desambiguação no adaptador (pela edição 2018, que corrigiu?) [conferir em bncc-dados] |
| Q-CUR-03 | O portal da BNCC versiona o documento? Licença explícita? | lacuna | consultar MEC; até lá `license: unknown` |
| Q-CUR-04 | Res. CNE/CEB 2/2025 (citada por redes como exigência de informar se o referencial contempla Computação) e prazo de implementação da Res. 1/2022: não abertos | lacuna | abrir os textos no portal do CNE |
| Q-CUR-05 | **Candidato a entidade do Core**: `AdocaoCurricular` (organização × edição curricular × programa × coorte). Nenhuma entidade de `_convencoes.md` §4 cobre "regime curricular por coorte" (DCNEM 2024 arts. 39 e 42) | candidato a entidade do Core | discutir com a síntese do Core; alternativa: atributo de C.ENR |
| Q-CUR-06 | Competências e "capacidades" dos IFAs (Res. CNE/CEB 4/2025, Anexo) não têm código: quem cunha o id? Redes estaduais vão codificar (como fez a Portaria MEC 1.432/2018 para os itinerários de 2018, cujos códigos não foram verificados)? | lacuna | acompanhar MEC/Consed; cunhar ids provisórios com mapa de substituição (regra bncc-dados) |
| Q-CUR-07 | DCN gerais (Res. CNE/CEB 4/2010), DCNEI (Res. 5/2009) e DCN do EF de 9 anos (Res. 7/2010): texto oficial não aberto; alterações posteriores não verificadas | lacuna de verificação | baixar do portal do CNE (gov.br/mec/cne) |
| Q-CUR-08 | Significado oficial do sufixo `*` e das letras `A/B/C` no Currículo Paulista: inferido, não lido em definição explícita | lacuna | procurar nota metodológica no documento (introdução) ou no portal Efape |
| Q-CUR-09 | Currículo Paulista EM: códigos próprios (FGB e itinerários)? A Del. CEE 186/2020 foi parcialmente revogada pela 236/2025: o que mudou? | lacuna | ler o volume EM e a Del. 236/2025 |
| Q-CUR-10 | Existe tabela oficial de correspondência Currículo Paulista ↔ BNCC (ou dataset)? Hoje a correspondência é calculada pelo código | lacuna | consultar Efape/Seduc-SP; senão, validar por comparação de texto (como em bncc/99-verificacao) |

## Avaliação

| Id | Questão | Tipo | Como fechar |
|---|---|---|---|
| Q-AVA-01 | Microdados do Saeb: estrutura (dicionário), nível de agregação, identificadores de escola e de aluno | lacuna | inspecionar microdados do Inep (frente de organização pode ter o dicionário do Censo) |
| Q-AVA-02 | Escalas de LP e MT do 5º e 9º anos **alinhadas à BNCC**: publicadas? Mesma métrica da escala 2001 (comparabilidade de série histórica)? | lacuna | página "Matrizes e escalas" do Inep e notas técnicas do Saeb 2025 |
| Q-AVA-03 | O Inep publica correspondência entre itens/habilidades da matriz Saeb-BNCC e códigos da BNCC? (0 ocorrências na matriz de Linguagens) | lacuna | documentos de referência do Saeb; sem isso, alinhamento só por curadoria |
| Q-AVA-04 | Matrizes do Saeb/Enem para o EM alinhadas à DCNEM 2024 (prazo do Inep 20/12/2025; Saeb até 2027): publicadas? | lacuna temporal | acompanhar Inep |
| Q-AVA-05 | SARESP vigente: matriz (Currículo Paulista?), cortes de MT, cortes atuais de LP, séries avaliadas, ato normativo anual | lacuna (site oficial deu 403) | acessar educacao.sp.gov.br manualmente ou pedir à Seduc-SP |
| Q-AVA-06 | Prova Paulista (avaliação bimestral da rede, citada por imprensa) e Idesp: estrutura e relação com SARESP | lacuna | idem |
| Q-AVA-07 | Ato que fixa o padrão de 743 pontos (Pesquisa Alfabetiza Brasil, Inep 2023): texto oficial | lacuna de verificação | publicação do Inep |

## Inclusão

| Id | Questão | Tipo | Como fechar |
|---|---|---|---|
| Q-INC-01 | **Candidato a entidade do Core**: `EstudoDeCaso` (avaliação de barreiras, contexto, potencialidades e demandas) entre C.SUP e C.PLN | candidato a entidade do Core | decidir se é entidade própria ou primeira seção de C.PLN |
| Q-INC-02 | Formato do plano: a Port. MEC 421 dá conteúdo mínimo e admite documento único; SP tem formulário próprio anterior a ela (prazo de adequação até 2029). O adaptador SP deve exportar no formato SP e validar contra o mínimo federal? | decisão | confirmar com a Seduc-SP se os anexos da Res. 129 serão revistos |
| Q-INC-03 | A categoria do Censo/CMDEB (deficiência, TEA, AH/SD) é obrigatória em coleta oficial: como mantê-la fora do modelo pedagógico e da personalização sem perder a obrigação de reportar? | conflito de desenho | política de acesso por papel + base legal do art. 11 II; coordenar com a frente de organização |
| Q-INC-04 | Estudantes com dislexia/TDAH (Lei 14.254) sem elegibilidade à educação especial: o PEI da Port. 421 se aplica a eles? A lei não prevê plano; SP restringe o PEI aos elegíveis (art. 14 §3) | lacuna normativa | registrar apoio sem plano formal; acompanhar regulamentação |
| Q-INC-05 | O Observatório da Educação Especial Inclusiva (Port. 421 art. 24) e a Reneei vão coletar dados individuais das redes? | lacuna temporal | acompanhar Secadi/MEC |
| Q-INC-06 | Res. CNE/CEB 4/2009 (AEE) foi substituída após o Decreto 12.686/2025? (pendência herdada de acs.br.pneepei-and-aee) | lacuna | portal do CNE |
| Q-INC-07 | **Conflito**: Res. SEDUC-SP 129/2025 exige laudo para especialidade do professor e para abrir sala de recursos (arts. 9 e 18) e cobra a busca do laudo após um ano; a Port. MEC 421/2026 (posterior) veda condicionar AEE a laudo. Qual prevalece na rede estadual e como o adaptador registra? | conflito normativo | não resolver no dado: laudo como documento opcional com efeitos administrativos locais; pedir posição jurídica |
| Q-INC-08 | Andamento do PDL 30/2025 (ALESP), que pretende sustar a Res. SEDUC 129/2025 | lacuna temporal | consultar ALESP |

## Dados e privacidade

| Id | Questão | Tipo | Como fechar |
|---|---|---|---|
| Q-DAD-01 | Papéis LGPD: escola/rede como controladora e VUOO como operadora, ou controladoria conjunta para o modelo do aprendiz? (pendência também em psg.legal.lgpd-children) | decisão jurídica | guia da ANPD sobre agentes de tratamento |
| Q-DAD-02 | Prazo de guarda de registros escolares e de documentos de AEE: há norma federal ou estadual (SP) de temporalidade? A LGPD só autoriza conservar por obrigação legal (art. 16 I) | lacuna | tabela de temporalidade de documentos da Seduc-SP / Conarq |
| Q-DAD-03 | Localização de dados: nenhuma exigência encontrada na LGPD; há exigência em contratos públicos de SP ou em norma de TIC estadual? | lacuna | editais e normas de TIC do Governo de SP |
| Q-DAD-04 | Barreiras e acomodações ("ledor", "tempo adicional") são dado sensível por revelarem condição de saúde (art. 11 §1)? Proposta: tratar como sensíveis | interpretação | posição jurídica |
| Q-DAD-05 | ECA Digital em serviço contratado pela escola: supervisão parental e consentimento para download (art. 12 §2) se aplicam a app escolar? (pendência de psg.legal.eca-and-digital-eca) | lacuna | atos da ANPD sobre o ECA Digital |
