---
id: rtm.case.figma-multiplayer
titulo: "Figma multiplayer: servidor autoritativo por documento com last-writer-wins por propriedade"
tipo: estudo-de-caso
dominio: realtime-multiplayer
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
ano_do_sistema: 2016
fontes: [wallace2019figma]
relacoes:
  - { tipo: relacionado-a, alvo: rtm.arch.authoritative-server }
  - { tipo: relacionado-a, alvo: rtm.proto.websocket }
  - { tipo: relacionado-a, alvo: rtm.sync.crdt }
  - { tipo: relacionado-a, alvo: rtm.sync.operational-transformation }
  - { tipo: relacionado-a, alvo: rtm.sync.state-replication }
  - { tipo: relacionado-a, alvo: rtm.pred.client-side-prediction }
  - { tipo: relacionado-a, alvo: rtm.rel.reconnection }
  - { tipo: relacionado-a, alvo: rtm.mp.rooms-and-matches }
  - { tipo: relacionado-a, alvo: rtm.mp.presence }
termos: [last-writer-wins, fractional indexing, multiplayer undo, offline edits, per-document server process]
---

# Figma multiplayer: servidor autoritativo por documento com last-writer-wins por propriedade

## Contexto e gênero de interação

Figma é um editor de design vetorial no navegador com edição colaborativa simultânea. A fonte é o artigo "How Figma's multiplayer technology works", de Evan Wallace, cofundador da Figma, publicado no blog da empresa em 16 de outubro de 2019 [F: wallace2019figma]. O autor afirma que a Figma foi a primeira ferramenta de design com edição colaborativa ao vivo e que começou a construir o sistema "quatro anos antes" do texto (cerca de 2015); uma nota relacionada no site data o lançamento público da edição multiplayer em 28 de setembro de 2016 [F: wallace2019figma].

O gênero é colaboração sem jogo rápido: não há adversários, o "tempo real" exigido é o da resposta local imediata e da convergência de todos os participantes para o mesmo documento [I].

## Restrições de projeto

Reportado pelo autor [F: wallace2019figma]:

- clientes são páginas web; conexão por WebSocket a um cluster de servidores;
- edição offline por tempo arbitrário, com reaplicação ao reconectar;
- velocidade de entrega como prioridade de startup: OT foi julgado complexo demais para implementar corretamente;
- o produto não é um editor de texto; edições concorrentes no mesmo texto não precisam de merge fino.

O artigo não informa número de colaboradores por documento, latências ou banda [F: wallace2019figma].

## Arquitetura escolhida

Cliente/servidor com um processo de servidor por documento multiplayer; todos que editam o documento conectam-se a esse processo. Ao abrir, o cliente baixa uma cópia do arquivo; mudanças fluem nos dois sentidos pelo WebSocket. Só o documento usa o sistema multiplayer; comentários, usuários, times e projetos ficam em Postgres com outro mecanismo, porque têm compromissos diferentes de desempenho, disponibilidade offline e segurança [F: wallace2019figma].

Reconexão: ao voltar, o cliente baixa uma cópia fresca, reaplica as edições offline por cima e retoma a sincronização em nova conexão; o autor diz que isso mantém a lógica de conexão simples e concentra a dificuldade nas atualizações a documentos já conectados [F: wallace2019figma].

O time construiu primeiro um playground web que simulava três clientes e um servidor, para testar cenários offline e de banda limitada antes de tocar no código real [F: wallace2019figma].

## Técnicas usadas

### Por que não OT nem CRDT "puro"

OT (usado pelo Google Docs) foi rejeitado por complexidade e "explosão combinatória" de estados, e por ser desnecessário fora de edição de texto. CRDTs serviram de inspiração, mas não foram adotados integralmente: CRDTs visam sistemas descentralizados sem autoridade central, e como o servidor da Figma é essa autoridade, o overhead que CRDTs exigem pôde ser descartado [F: wallace2019figma].

### Last-writer-wins por propriedade

O servidor guarda o último valor que qualquer cliente enviou para cada propriedade de cada objeto. Mudanças em propriedades diferentes do mesmo objeto não conflitam; mudanças na mesma propriedade de objetos diferentes também não. Em conflito real (mesma propriedade, mesmo objeto), vence o último valor recebido pelo servidor; como o servidor define a ordem, não há timestamps. Mudanças são atômicas no nível do valor da propriedade: duas edições simultâneas no mesmo texto resultam em um valor inteiro, não em merge [F: wallace2019figma].

Mudanças locais aplicam-se imediatamente; mudanças do servidor que conflitam com mudanças locais ainda não confirmadas são descartadas no cliente, para evitar que um valor antigo sobrescreva o novo por um instante (flicker) [F: wallace2019figma].

### Criação e remoção de objetos

Criar e apagar são ações explícitas; escrever em um ID não atribuído não cria objeto. IDs são gerados no cliente incluindo um identificador por cliente, o que permite criação offline. Apagar remove todos os dados do servidor; a cópia fica só no buffer de undo do cliente que apagou, para que documentos longevos não cresçam [F: wallace2019figma].

### Árvore e reparentamento

Cada filho guarda um link ao pai como propriedade; o objeto nunca tem mais de um pai e sua identidade é preservada. Movimentos concorrentes podem formar ciclos (A sob B e B sob A); o servidor rejeita a atualização que forma ciclo, mas um cliente pode recebê-la antes de saber da rejeição; nesse caso o cliente remove temporariamente os objetos da árvore até a rejeição chegar, e eles somem brevemente, o que o autor reconhece como imperfeito mas raro. A ordem entre irmãos usa fractional indexing (posição como fração entre 0 e 1; inserir entre dois é tomar o ponto médio); link ao pai e posição são uma única propriedade, atualizada atomicamente [F: wallace2019figma].

### Undo multiplayer

Princípio adotado: desfazer vários passos, copiar algo e refazer até o presente deve deixar o documento inalterado. Um undo modifica o histórico de redo naquele momento, e um redo modifica o histórico de undo, para que refazer não sobrescreva mudanças posteriores de outros [F: wallace2019figma].

## Resultados e números reportados

O artigo não apresenta métricas (latência, banda, escala, taxa de conflitos). As únicas datas são 2015 (início) e 2016 (lançamento) [F: wallace2019figma]. Resultado qualitativo declarado: o sistema funciona em produção e o autor julgou "menos assustador que o esperado" construir multiplayer para um editor visual [F: wallace2019figma].

## Lições documentadas pelo autor

- A pesquisa em CRDT é útil mesmo em sistemas centralizados [F: wallace2019figma].
- Pesquisa e prototipagem antecipadas compensaram [F: wallace2019figma].
- Separar o documento (sincronizado por propriedade) de metadados (banco relacional) por terem requisitos distintos [F: wallace2019figma].

## O que é opinião e o que é fato

- Fato: arquitetura, regras de conflito, tratamento de árvore, undo, offline, conforme descrito pelo autor [F: wallace2019figma].
- Opinião do autor: que OT é "complexo demais" e que CRDTs completos têm overhead desnecessário quando há servidor; são juízos de engenharia da equipe, não comparações medidas [F: wallace2019figma] [I].
- Interpretação deste documento: o esquema é um registro LWW por propriedade com ordenação pelo servidor, que converge trivialmente; a dificuldade real está nas invariantes estruturais (árvore sem ciclos, ordem de irmãos), e é aí que os autores aceitam anomalias visíveis mas raras [I].

## Limites do estudo

- Texto de blog de 2019 sobre um sistema iniciado em 2015; não há dados de escala nem descrição de como o processo por documento é distribuído ou tolera falhas [I].
- As conclusões dependem do domínio (documentos de design com propriedades independentes); não se transferem a texto colaborativo, como o próprio autor nota [F: wallace2019figma].

## Relações com outros conceitos

Instância de `rtm.arch.authoritative-server` por documento sobre `rtm.proto.websocket`, com resolução LWW por propriedade: uma alternativa pragmática a `rtm.sync.crdt` e `rtm.sync.operational-transformation` quando há autoridade central. A aplicação local imediata com descarte de atualizações conflitantes não confirmadas é uma forma de `rtm.pred.client-side-prediction` em colaboração. O processo por documento corresponde a `rtm.mp.rooms-and-matches`; a reconexão por download e reaplicação, a `rtm.rel.reconnection`.

## Lacunas e questões abertas

- Como o processo por documento escala e se recupera de falha: não descrito [H].
- Presença (cursores de outros usuários) não é tratada no artigo, embora seja parte visível do produto [I].

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| wallace2019figma | tecnico (blog de engenharia do fornecedor, autor do sistema) | 2026-10-29 |
