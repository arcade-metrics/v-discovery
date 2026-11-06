---
produto: VUOO
slug: vuoo-microjogos
etapa: 02-prd
status: aprovado
atualizado_em: 2026-11-06
---

# PRD: VUOO Microjogos

## 1. Recorte

Os microjogos são um app de micro-atividades de 5 a 15 min por dia, para todos os alunos da turma, do EF ao EM, que funciona offline e se adapta ao aluno.

**Não é:**

- produto só de educação especial;
- ferramenta de diagnóstico;
- jogo de sessão infinita;
- rede social.

## 2. Onde se usa

A Lei 15.100/2025 proíbe o aluno de usar o celular na escola. Ela tem exceções: uso pedagógico orientado pelo professor e uso para acessibilidade, inclusão ou saúde.

- **Casa é o uso principal.** O aluno joga sozinho, de 5 a 15 min por dia, sem o professor precisar cobrar.
- **Sala é opcional**, e só dentro da exceção pedagógica: o professor abre a sessão e conduz a atividade.
- O aluno da educação especial também pode usar em sala pela exceção de acessibilidade, se o PEI dele previr isso.

Assim, o app não depende da escola liberar o celular para funcionar.

## 3. Quem usa

| Quem | O que faz |
|---|---|
| **Aluno** (6 a 17 anos) | Um só tipo de aluno. Joga em casa e, quando o professor abre a sessão, em sala. |
| **Aluno avulso** | Sem escola. Entra numa rede geral; os dados são só dele. |
| **Professor** | Vincula a turma, abre a sessão em sala e ajusta a adaptação de um aluno. |
| **Gestão escolar** | Área simples de cadastro: escolas, turmas, professores, salas, alunos e matrículas. |
| **Responsável** | Dá o consentimento por link. Não usa o app. |

**Educação especial é um metadado do aluno**, não outro usuário. Quando marcado, o fluxo inclui avaliações e documentação específicas (PEI, referência de laudo).

**A adaptação do jogo vem do perfil de apoio, não do metadado.** Qualquer aluno pode ter perfil de apoio, com ou sem laudo. O metadado de educação especial nunca alimenta a adaptação.

A estrutura de cadastro segue os padrões internacionais já estudados. O recorte está em [base/estrutura-escolar.md](base/estrutura-escolar.md).

## 4. Modelo de habilidades

Dois modelos, com papéis diferentes:

- **Funções executivas (Diamond, 2013) são a base.** Organizam o que cada atividade exercita. Valem igual de 6 a 17 anos e independem do conteúdo da série.
  1. Núcleo: controle inibitório (inclui atenção seletiva), memória de trabalho e flexibilidade cognitiva. A flexibilidade depende das outras duas.
  2. Superiores, construídas sobre o núcleo: raciocínio, resolução de problemas e planejamento.
- **BNCC é o mapeamento.** Cada atividade aponta para uma ou mais habilidades da BNCC: competências gerais → área → componente → unidade temática → objeto de conhecimento → habilidade (código, ex. EF01LP02).
- **Fonte da BNCC:** a base canônica única, compartilhada com o VUOO Elo, no repositório [vuoo-base](https://github.com/arcade-metrics/v-base), **release v1.1**: versão final (EI, EF e EM) do MEC e BNCC Computação (`dados/bncc-2018.json`, `dados/bncc-computacao-2022.json`), com identificador estável por item (`bncc-2018/EF01LP02`, `bncc-computacao-2022/EF01CO01`) e o código oficial como atributo. Os microjogos consomem a versão relacional; o Elo, a versão RDF.

**Ligação:** cada habilidade da BNCC aponta para as funções executivas que ela exige (relação N:N, guardada como dado). A ligação é **curadoria rotulada**, com autor e data, nunca norma.

**Regra da dupla camada:** numa tarefa que observa função executiva, o conteúdo da BNCC **nunca decide a resposta certa**. Ele pode aparecer como "roupa" (a figura tocada é um bolo, mas o que manda tocar é o sinal). Senão, quem ainda não domina o conteúdo erra a função executiva por causa do conteúdo. O conteúdo da BNCC decide a resposta só na parte curricular da atividade. Anatomia e ficha-modelo de referência em `base/precedente-linguagem/04-microjogos.md`.

**Promessa do produto:** prática e observação das funções executivas, não melhora cognitiva. A evidência de transferência do treino para fora da tarefa é fraca.

## 5. Fluxo do aluno

1. **Primeiro acesso, com internet:** o responsável autoriza pelo link e o aluno vincula o aparelho por código ou QR, sem e-mail nem senha.
2. **Estilo:** fica nas configurações do aluno. Não é um passo do primeiro acesso.
3. **Tela inicial:** no estilo do Duolingo, com uma trilha de etapas (ver seção 6).
4. **Sessão:** no estilo do Duolingo, com começo e fim.
5. **Fim da sessão:** o aluno vê o resumo e pode continuar jogando.
   - **Trilha:** até 2 sessões por dia.
   - **Jogos livres:** depois da trilha, até 30 min por dia. Ao chegar a 30 min, um alerta gentil sugere parar; o aluno pode continuar.
   - "Parar" e "Continuar" têm sempre o mesmo peso visual.
6. **Sincronização:** sempre que houver rede, o app atualiza os dados nos dois sentidos.

## 6. Mecânicas (estilo Duolingo)

**Entra:**

- **trilha visual de etapas**, como no Duolingo: etapas feitas, a próxima em destaque e as **futuras visíveis**. As futuras aparecem neutras, sem cadeado ameaçador;
- meta do dia;
- **ofensiva compassiva** (ver abaixo);
- **celebração de participação** no fim da lição: descreve o que o aluno fez, nunca conta acertos;
- mascote;
- feedback imediato de acerto e erro. O mascote nunca reage ao erro com tristeza; nenhuma reação dele depende de acerto ou erro.

**Pausar e pular** são sempre permitidos, sem perda, e contam como dado de autorregulação, nunca como falha.

**Não entra:**

- **vidas**: punem o erro e travam quem mais precisa praticar;
- **ofensiva que zera**: nada se perde por ausência;
- **ligas com ranking público**: expõem o aluno da educação especial diante da turma.

**Ofensiva compassiva.** A ofensiva é importante, mas nunca pune a ausência:

- **Meta semanal:** "3 de 5 dias nesta semana". Recomeça toda semana, sem perder nada.
- **Casas dos dias:** os dias que faltam continuam aparecendo, mas **neutros**: sem cor de alerta, sem "faltam", sem nada que evidencie perda. O aluno pode **voltar e fazer** a atividade de um dia que passou, e ela conta para a meta da semana.
- **Ofensiva de semanas:** conta as semanas em que a meta foi cumprida. Uma semana sem meta **pausa** a contagem, nunca a zera.
- **Dias jogados:** o total só cresce.
- A tela mostra só o que o aluno fez, nunca o que faltou. Sem mensagem de cobrança ("senti sua falta", "não perca sua ofensiva").

## 7. Medida

**O que se captura:** toques, arrastos e sensores inerciais (acelerômetro e giroscópio), além das respostas. Sem visão computacional. Tudo é normalizado no aparelho, até 100 Hz. Detalhes em [base/captura-de-interacao.md](base/captura-de-interacao.md).

Dois tipos de uso:

1. **Registro do jogo, sempre ligado:** acertos, tempo, tentativas, desistências e a interação física, em toda atividade. Serve para adaptar a dificuldade e para o professor ver o progresso. Não é avaliação.
2. **Avaliação, em momentos marcados:** atividades curtas de funções executivas e de BNCC, no início e periodicamente. Para o aluno com o metadado de educação especial, alimentam o PEI.
   - Durante a avaliação, estilo e mecânicas não mudam os estímulos: sem mascote ajudando, sem dica, com tamanhos e tempos iguais para todos. Só as acomodações de acesso continuam valendo.
   - O aluno é avisado de que é um momento diferente.

## 8. Adaptação e estilo (v0.0.0)

- **Parametrizado desde o início:** nenhuma tela usa valor fixo. Presets novos entram depois sem refazer telas.
- **Tudo fica nas configurações do jogador.** Não há controle de estilo dentro do jogo.
- **3 estilos de base:** Calmo, Moderado e Vibrante. **Moderado é sempre o padrão.**
- **5 complementos:** Alto contraste, Ouvir instruções, Toque fácil (alvos maiores, tocar em vez de arrastar), Tempo livre (sem limite) e Sem som.
- **Valores iniciais** vêm das configurações do celular (menos movimento, fonte maior, contraste) e do perfil de apoio do aluno.
- **O professor pode travar** um ajuste; o aluno vê o cadeado.
- **Na avaliação** só valem os complementos de acesso (seção 7).

**Depois da v0.0.0:** bases Mínimo, Foco e Máximo, Libras, leitor de tela, acionador e varredura, presets próprios do aluno, ajuste por IA.

O estudo completo, com todos os eixos e presets, está em [base/parametrizacao-estilo.md](base/parametrizacao-estilo.md).

## 9. Offline e aparelho

- **Primeiro acesso exige rede.** Depois, o app funciona todo sem rede.
- **No aparelho:** a trilha da semana e um conjunto de jogos livres.
- **Sincroniza sempre que houver rede.** Séries brutas de sensores sobem só por Wi-Fi.
- **Login sem rede vale 30 dias**, depois pede conexão. `[ASSUMIDO]`
- **Aparelho mínimo:** Android 8+, iOS 15+, 2 GB de RAM. `[ASSUMIDO]`
- **Tamanho:** app instalado até 150 MB; atualização semanal até 20 MB. `[ASSUMIDO]`

Os números são revistos depois dos testes de peso.

## 10. O que os dados entregam

- **Professor**, numa visão simples na área de gestão, por aluno e por turma:
  - uso (dias e minutos);
  - progresso na trilha;
  - desempenho por função executiva e por habilidade da BNCC;
  - resultado das avaliações;
  - "sincronizado em …". Quem jogou sem rede aparece como **"aguardando sincronização"**, nunca como "não jogou".
- **PEI:** resultados das avaliações do aluno com o metadado de educação especial.
- **Outros sistemas:** exportação dos eventos em xAPI e Caliper.
- **Nunca aparece:** ranking entre alunos, comparação nominal com colegas, dados brutos de sensores.

## 11. Métricas

**Métrica-norte:** porcentagem de alunos que jogam 3 ou mais dias por semana, sem o professor cobrar.

- Limiar na turma piloto: pelo menos 50% depois da 3ª semana. `[A CONFIRMAR]`
- Abaixo disso, o produto não se sustenta. É a primeira coisa a testar.

**Secundárias:**

- sessões concluídas sobre sessões iniciadas;
- retorno em 7 e em 30 dias;
- **inclusão:** alunos com perfil de apoio concluem as atividades na mesma proporção que o resto da turma, com diferença menor que 10 pontos. `[A CONFIRMAR]`

**Guarda-corpos** (não podem piorar):

- tempo diário em jogos livres acima de 30 min, sinal de uso compulsivo (seção 5);
- abandono logo depois de um erro;
- perda de eventos na sincronização acima de 1%;
- travamentos do app.

## 12. Requisitos

### Funcionais

| Id | Requisito | Seção |
|---|---|---|
| RF-01 | O responsável autoriza o uso por um link que já o autentica, antes de qualquer coleta de dado do aluno. | 3, 5 |
| RF-02 | O aluno vincula o aparelho por código ou QR, sem e-mail nem senha. | 5 |
| RF-03 | O aluno avulso usa o app sem escola, numa rede geral, sem compartilhar dados com ninguém. | 3 |
| RF-04 | O aluno avulso pode levar o histórico ao entrar numa escola, com aprovação dele ou do responsável. | 3 |
| RF-05 | A gestão cadastra escolas, turmas, professores, salas, alunos e matrículas. | 3 |
| RF-06 | O aluno tem um metadado de educação especial que habilita avaliações e documentação específicas (PEI, referência de laudo). | 3 |
| RF-07 | Qualquer aluno pode ter perfil de apoio, que define os valores iniciais da adaptação. | 3, 8 |
| RF-08 | A referência de laudo guarda só metadados e referência externa; o arquivo nunca é armazenado. | 3 |
| RF-09 | Cada atividade aponta para uma ou mais funções executivas e habilidades da BNCC. | 4 |
| RF-10 | A tela inicial mostra a trilha de etapas e a meta do dia. | 5, 6 |
| RF-11 | A sessão tem começo e fim; ao terminar, o aluno vê o resumo e pode seguir para jogos livres. | 5 |
| RF-12 | O app tem meta semanal com casas neutras e dias recuperáveis, ofensiva de semanas que pausa e nunca zera, celebração de participação, mascote e feedback imediato. | 6 |
| RF-12a | A trilha mostra etapas feitas, a próxima em destaque e as futuras, neutras. | 6 |
| RF-12b | Até 2 sessões de trilha por dia; depois, jogos livres com alerta gentil aos 30 min. | 5 |
| RF-12c | Pausar e pular sempre permitidos, sem perda, registrados como autorregulação. | 6 |
| RF-13 | O app não tem vidas nem ranking público. | 6 |
| RF-14 | O professor abre uma sessão em sala e conduz a atividade. | 2, 3 |
| RF-15 | O app registra respostas, acertos, tempo, tentativas, desistências, toques, arrastos e sensores inerciais em toda atividade. | 7 |
| RF-16 | A dificuldade se adapta ao desempenho registrado. | 7 |
| RF-17 | A avaliação acontece em momentos marcados, avisa o aluno e mantém os estímulos iguais para todos, valendo só as acomodações de acesso. | 7 |
| RF-18 | O aluno escolhe, nas configurações, 1 de 3 estilos de base e os complementos que quiser. | 8 |
| RF-19 | Os valores iniciais do estilo vêm das configurações do celular e do perfil de apoio. | 8 |
| RF-20 | O professor trava um ajuste de estilo; o aluno vê o cadeado. | 8 |
| RF-21 | O professor vê, por aluno e por turma: uso, progresso, desempenho por função executiva e BNCC, avaliações e data da última sincronização. | 10 |
| RF-22 | Os resultados de avaliação do aluno com metadado de educação especial ficam disponíveis para o PEI. | 10 |
| RF-23 | Os eventos podem ser exportados em xAPI e Caliper. | 10 |

### Não funcionais

| Id | Requisito | Seção |
|---|---|---|
| RNF-01 | O aluno começa com app em Flutter (Android e iOS), *mobile first* (D-34); o build web do mesmo código vem depois (D-36). Área web para professor e gestão. | 1, 3 |
| RNF-02 | Depois do primeiro acesso, o app funciona todo sem rede: trilha da semana e jogos livres ficam no aparelho. | 9 |
| RNF-03 | Estímulo, resposta e feedback acontecem no aparelho, em até um quadro, sem rede. | 7 |
| RNF-04 | Sincronização sempre que houver rede, em lote, sem duplicar e sem perder eventos (perda abaixo de 1%). | 9, 11 |
| RNF-05 | Séries brutas de sensores sobem só por Wi-Fi. | 9 |
| RNF-06 | Toque e sensores normalizados no aparelho, até 100 Hz, por uma única implementação versionada para Android e iOS. | 7 |
| RNF-07 | Login sem rede vale 30 dias. `[ASSUMIDO]` | 9 |
| RNF-08 | Roda em Android 8+, iOS 15+ e 2 GB de RAM. `[ASSUMIDO]` | 9 |
| RNF-09 | App instalado até 150 MB; atualização semanal até 20 MB. `[ASSUMIDO]` | 9 |
| RNF-10 | Nenhuma tela usa valor visual fixo: tudo vem de parâmetros. | 8 |
| RNF-11 | A fila local no aparelho guarda só o UUID do aluno, nunca nome nem CPF. | 7 |
| RNF-12 | Metadado de educação especial e referência de laudo são dado sensível, com acesso isolado, e nunca alimentam a adaptação. | 3 |
| RNF-13 | Nenhum SDK de terceiros envia dados do app para fora. | 7 |
| RNF-14 | Toda tela do professor mostra a data da última sincronização do aluno. | 10 |

## 13. Riscos

| Risco | Impacto | O que reduz |
|---|---|---|
| O aluno não volta por conta própria (métrica-norte abaixo do limiar). | alto | Turma piloto cedo, medindo retorno semanal antes de produzir muito conteúdo. |
| A Lei 15.100/2025 limita o uso em sala. | médio | Casa como uso principal; sala só pela exceção pedagógica ou de acessibilidade (seção 2). |
| Vazamento de dado sensível de menor (deficiência, laudo). | alto | Acesso isolado, laudo só como referência, UUID no aparelho, sem SDK de terceiros. |
| O app falha em aparelhos baratos ou com pouco espaço. | médio | Limites de tamanho, testes de peso, normalização com perfil do aparelho. |
| Custo de produzir atividades para EF e EM. | alto | Funções executivas como base, que vale para todas as idades; BNCC como mapeamento. |
| A adaptação vira rótulo e expõe o aluno. | médio | Adaptação pelo perfil de apoio, nunca pelo metadado; sem ranking. |
| Prometer melhora cognitiva sem evidência. | médio | Promessa limitada a prática e observação (seção 4). |
| A estética calma parece "de bebê" para alunos sem condição identificada, e o app vira "o app dos alunos com laudo". | alto | Moderado como padrão; estética por idade; testar cedo com alunos sem perfil de apoio. |
| O professor confia demais e trata um sinal do app como laudo. | médio | Sinais sempre com origem e limite; sem diagnóstico; linguagem de observação, nunca de condição. |

## 14. Pontas soltas

| # | Item | Marca |
|---|---|---|
| P-01 | Limiar da métrica-norte: 50% com 3+ dias por semana depois da 3ª semana. | `[A CONFIRMAR]` |
| P-02 | Limiar de inclusão: diferença menor que 10 pontos na conclusão. | `[A CONFIRMAR]` |
| P-03 | Limites diários: 2 sessões de trilha e 30 min de jogos livres. | decidido em 05/11/2026; revisar após o piloto |
| P-04 | Validade do login sem rede (30 dias). | `[ASSUMIDO]` |
| P-05 | Aparelho mínimo (Android 8+, iOS 15+, 2 GB). | `[ASSUMIDO]` |
| P-06 | Tamanho do app (150 MB) e da atualização semanal (20 MB). | `[ASSUMIDO]` |
| P-07 | Quais habilidades da BNCC e funções executivas entram primeiro, e a tabela de ligação entre elas. | `[A CONFIRMAR]` |
| P-08 | Protocolo das avaliações: quais tarefas, frequência e quem define. | `[A CONFIRMAR]` |
| P-09 | Lista de medidas calculadas no aparelho e fração de amostra bruta. | `[A CONFIRMAR]` |
| P-11 | Identidade visual: paleta, tipografia, mascote. É a A-12 de [decisoes.md](decisoes.md); acompanhar lá. | `[A CONFIRMAR]` |
| P-12 | Pagamento: a escola ou rede paga pelos microjogos? Preço e risco de a escola não ver valor. Validar com 3 a 5 escolas. | deixado para depois |
| P-13 | Situação de uso hoje (brief §2): confirmar com professores regentes e do AEE. | `[A CONFIRMAR]` |
