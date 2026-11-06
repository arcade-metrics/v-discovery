---
produto: VUOO
slug: vuoo-microjogos
etapa: 03-mvp
status: aprovado
atualizado_em: 2026-11-06
---

# MVP: VUOO Microjogos

## 1. O que o MVP prova

**A estrutura funciona de ponta a ponta:** o aluno entra, joga, e o professor vê o resultado, lido a partir de grafos de conhecimento.

O foco é a **infraestrutura e a arquitetura em camadas**, não o conteúdo nem o engajamento. O teste da métrica-norte (PRD, seção 11) fica para depois do MVP.

## 2. Linha de corte

### Entra

**Estrutura escolar completa, em duas camadas:**

- **camada agnóstica:** organização, pessoas, papéis, períodos letivos, etapas (anos e séries), componentes curriculares, turmas, matrículas;
- **camada Brasil:** vocabulários, códigos e regras nacionais (Censo/INEP, BNCC), como dado sobre a camada agnóstica.

**Acesso, simples mas com a rotina completa** (dentro da LGPD; métodos mais rígidos entram depois):

- cadastro do professor;
- login do professor com e-mail e senha, e recuperação de senha;
- login simplificado do aluno, entrando numa escola ou rede;
- rede, escola, turma e professor globais para o aluno sem escola;
- autorização do responsável antes de qualquer coleta.

**Atividades:**

- estrutura agnóstica para guardar atividades;
- **manifesto por atividade**, que determina como ela é executada;
- **motor de atividades**, que lê o manifesto e roda a atividade no app;
- catálogo de atividades curadas (o conteúdo é definido em paralelo, ver seção 3).

**Entrega para o usuário:**

- área do professor: só os cadastros e a visão de resultado;
- app do aluno: só entrar, jogar e mandar o resultado;
- resultado para o professor, a partir de grafos de conhecimento (funções executivas e BNCC).

### Fica para depois

- métodos de autenticação mais rígidos;
- avaliações em momentos marcados e PEI;
- estilos e complementos além do mínimo para o motor funcionar parametrizado;
- mecânicas do estilo Duolingo além da trilha simples;
- exportação xAPI e Caliper;
- teste de engajamento com turma real.

## 3. Conteúdo

- O MVP precisa da **estrutura** para guardar e executar atividades, não do catálogo pronto.
- **Em paralelo**, separamos as atividades: entre **700 e 2.000** para o início.
- O formato do manifesto e a curadoria serão discutidos à parte. `[A CONFIRMAR]`

## 4. Ordem de construção

1. **Infraestrutura e arquitetura em camadas** (agnóstica e Brasil).
2. Estrutura escolar e acesso.
3. Estrutura de atividades, manifesto e motor.
4. Resultado para o professor pelos grafos de conhecimento.
5. Escola de demonstração e dashboard.

## 5. Critérios de aceite

A entrega precisa ser muito simples:

- [ ] O professor se cadastra, entra, recupera a senha e cadastra escola, turma e alunos.
- [ ] O aluno entra pelo login simplificado, numa escola ou na rede global.
- [ ] O aluno abre uma atividade, o motor a executa a partir do manifesto, e o resultado é registrado.
- [ ] O professor vê o resultado do aluno, ligado a funções executivas e habilidades da BNCC.
- [ ] Trocar a camada Brasil não exige mudar a camada agnóstica.

## 6. Demonstração

- **Escola de demonstração (mockup):** uma escola com dados de 1 ano letivo de alunos.
- **Tela de demonstração** das atividades do aluno.
- **Dashboard** que agrupa os resultados.

## 7. LGPD mínima (para não desmontar depois)

O foco é fazer o login funcionar. Mas estas bases entram já, porque mudá-las depois exige refazer o banco:

1. **Pessoa com UUID interno.** CPF e outros documentos são uma lista de identificadores, não a chave.
2. **Papel × organização × vigência** desde o início, com isolamento por rede (tenant).
3. **Consentimento do responsável registrado** antes de qualquer coleta, com a base legal por operação.
4. **Campos sensíveis marcados e separados:** metadado de educação especial e referência de laudo ficam numa tabela isolada.
5. **Concessão de acesso** da escola aos dados do aluno, como tabela própria, mesmo que no MVP seja sempre automática pela matrícula.
6. **Registro de acesso:** quem viu ou mudou o quê, só por acréscimo.
7. **Senha com hash forte;** recuperação por token de uso único, com validade curta; tudo em HTTPS.
8. **Escola de demonstração só com dados sintéticos.**
9. **Nenhum SDK de terceiros** enviando dados para fora.

**Fica para depois:** textos jurídicos, revogação em camadas, exportação pelo titular, prazos de retenção, autenticação forte, residência dos dados no Brasil.

## 8. Pontas soltas

| # | Item | Situação |
|---|---|---|
| M-01 | Formato do manifesto de atividade. | Em paralelo. Partir da anatomia em 9 fases e da ficha-modelo de `base/precedente-linguagem/04-microjogos.md`, adaptadas (sem bloco de medida do projeto). |
| M-02 | Curadoria e catálogo (700 a 2.000 atividades). | Em paralelo. Ponto de partida: Sinal Aberto (go/no-go), Luzes em Ordem (Corsi), Mudou a Regra (DCCS), Trilho (Torre de Londres). |
| M-03 | Grafo de conhecimento (atividade, função executiva, BNCC). | No MVP, tabelas relacionais. O modelo deve permitir gerar o grafo depois. A BNCC vem do vuoo-base v1.1 (versão relacional, com a BNCC Computação), com os mesmos identificadores do VUOO Elo (`bncc-2018/<CODIGO>`, `bncc-computacao-2022/<CODIGO>`). |
| M-04 | Camada agnóstica e camada Brasil completas. | Em `base/camada-agnostica/` e `base/camada-brasil/`. |
| M-05 | LGPD na rotina de acesso. | Mínimo definido na seção 7. |
