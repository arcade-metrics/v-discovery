---
produto: VUOO — Linguagem de produto dos microjogos
slug: vuoo-linguagem
etapa: 00-brief
status: em revisão
atualizado_em: 2026-10-27
---

# Brief: a linguagem dos microjogos do VUOO

> Este brief foi escrito sem entrevista com o dono do produto, que delegou as decisões. As perguntas que a descoberta faria foram respondidas a partir dos documentos-fonte (`00-insumos.md`) e da pesquisa (`pesquisa/`). Passou por duas revisões independentes (`revisao/`). O que é inferência está marcado `[ASSUMIDO]` e consolidado em `99-pendencias.md`.
>
> **Este estudo é insumo**, e não substituto, da consultoria de especificação de produto e da consultoria de design instrucional previstas no orçamento do PIPE, e do co-design com professores (OE6). As decisões de identidade (metáfora, mascote) são **propostas para o 1º ciclo de co-design**.

## Em uma frase

Um sistema de linguagem (visual, verbal, sonora e de jogo) para os microjogos que crianças de 6 a 12 anos usam na escola, que precisa engajar como o Duolingo sem usar as táticas do Duolingo que fazem mal a crianças neurodivergentes, e sem tocar nos estímulos e respostas que o gêmeo digital mede.

## O problema

O problema de design tem três camadas que puxam em direções opostas:

1. **Engajamento.** O gêmeo digital depende de captura contínua (`[IN-27]`). Se a criança não volta, não há trajetória para acompanhar.
2. **Segurança para o público.** As táticas que dão ao Duolingo sua retenção (ofensiva que zera, vidas que acabam, ligas, mascote que cobra, recompensa variável) operam por aversão à perda e comparação social. Crianças com TEA, TDAH e ansiedade associada estão entre as mais sensíveis a imprevisibilidade, punição e sobrecarga sensorial (pesquisa `b`).
3. **Validade de medida.** Cada microjogo também é instrumento. Bônus por velocidade altera tempo de reação; tema, cor e saliência do alvo alteram o estímulo. O PP1 precisa preservar os construtos na migração (r ≥ 0,50) e o PP3 precisa mostrar que a captura se mantém com o Bot adaptativo (r ≥ 0,40) (`[IN-17]`).

**A resposta deste estudo:** a linguagem vive na **moldura** (navegação, Bot, Caminho, Pouso, painel) e nunca entra no **palco de medida**, que é definido pelo protocolo do CIATec. Detalhe em `03-linguagem.md`, seção 11.

## Quem tem o problema

**A criança.** Duas pessoas concretas, na mesma turma de 2º ano de uma escola estadual no interior de SP, que usam um tablet da escola em rodízio, de 10 a 15 minutos, numa sala com 30 colegas e sem fone `[ASSUMIDO]`:

- **Davi, 7 anos.** Sabe de cor o nome de todas as estações da linha de trem da cidade e desenha mapas de trilho com detalhe. Ainda não lê com fluência. É autista; a escola sabe pelo atendimento educacional especializado (AEE), e a plataforma **não sabe o diagnóstico** (ver D-19). Sons altos e repentinos o incomodam. Quando algo dá errado na frente dos colegas, prefere sair da atividade a continuar.
- **Júlia, 7 anos.** Sem condição identificada. Lê bem para a idade, quer ir rápido e se entedia se o jogo for lento.

**A linguagem tem que servir os dois na mesma tela e no mesmo som**, sem que um perceba que algo foi ajustado para o outro (`[IN-04]`).

**O professor.** Professora regente do 2º ano, 25 anos de rede, letramento digital baixo a médio, 30 alunos, 2 com Plano Educacional Individualizado. Usa o VUOO se ele economizar tempo no plano e se ela entender de onde vem cada afirmação (`[IN-21]`, `[IN-22]`). O risco não é só ela desconfiar: é confiar demais e tratar um sinal como laudo.

**O gestor.** Coordenador de educação especial de uma diretoria de ensino. Lê relatórios agregados e presta contas (`[IN-23]`).

**Quem parece público e não é:** clínicos e terapeutas. O produto é educacional, não clínico (`[IN-05]`).

## O que acontece hoje

- **Para a criança:** atividades em papel, jogos educativos genéricos e, nas redes que contrataram, Matific e Elefante Letrado na Sala do Futuro da SEDUC-SP (pesquisa `c`). Nenhum foi desenhado para a turma inteira com atenção a neurodivergência.
- **Para o professor:** o Plano Educacional Individualizado é escrito a partir de observação, laudos externos e formulários, com avaliação pontual. O VUOO quer **complementar** isso com evidência contínua, sem substituir a equipe nem a avaliação.

## Hipóteses

**Regra para todo teste:** nenhuma variante de teste pode conter mecânica que este estudo classifica como não segura (`02-gamificacao.md`). Hipótese que só se testa com um braço inseguro não é testada.

| # | Hipótese | Como saberíamos que é falsa | Onde roda | Confiança |
|---|----------|------------------------------|-----------|-----------|
| HIP-1 | Uma coleção entregue em marcos fixos, sem contador e sem anúncio, aumenta o retorno sem aumentar pulos e pausas. | Turmas com coleção não têm mais dias de voo por criança que turmas sem coleção, ou têm mais pulos. | A/B de configuração entre turmas do PP5 (vuoo F5.2) ou A/B/n do CIATec (≥ 500 por grupo) | média |
| HIP-2 | No treino, acrescentar a descrição verbal da ação pelo Bot ao retorno de competência do alvo aumenta a conclusão sem aumentar pulos. | A conclusão não muda, ou os pulos aumentam, na variante com descrição verbal. | A/B/n do CIATec ("2 tipos de feedback", `03` §5) | média |
| HIP-3 | O Céu da turma (meta coletiva sem prazo e sem falta) é percebido como justo e não gera culpa entre colegas. | Em observação de sala, alguma criança é apontada como culpada pela constelação. **Critério de parada: o Céu sai.** | Piloto do PP5, com observação estruturada; grupos focais de estudantes do CIATec (PT2) | baixa |
| HIP-4 | As expressões do Bot (com boca de luz) são compreendidas sem mediação adulta. | Menos de 80% das crianças do 1º ano identificam a expressão pretendida. | Grupos focais e estudo de usabilidade do CIATec (PT2, 200 estudantes), ou sub-estudo com emenda ao CEP | média |
| HIP-5 | O Modo suave, oferecido a todos sem marcação, é usado por quem precisa e não vira marcador social. | O modo é usado quase só por crianças com Plano Educacional Individualizado, ou quase ninguém o encontra. | Piloto do PP5, só na base de pesquisa, com consentimento específico (D-19) | média |
| HIP-6 | Uma identidade visual calma não perde para a estética saturada de jogos comerciais aos olhos das crianças sem condição identificada. | Em teste de preferência, essas crianças acham as telas "de bebê" ou "chatas". | Grupos focais do CIATec (PT2) ou sub-estudo com emenda ao CEP | baixa |

**Sobre o PP3:** o A/B do PP3 compara **Bot adaptativo × Bot não adaptativo**, os dois com a mesma linguagem (vuoo PP3, F3.3). **Esta linguagem não altera esse desenho.** A variante "Bot não adaptativo" está especificada em `03` §4.

**Prazos éticos:** todo teste com crianças precisa de protocolo no CEP submetido com pelo menos dois meses de antecedência (vuoo, ética). O co-design do PIPE (F3.4) é com **adultos** (15 a 20 professores e coordenadores). As hipóteses com crianças rodam onde a tabela indica.

**Hipótese mais frágil:** HIP-6, com HIP-3 logo atrás. Se crianças sem condição identificada acharem a linguagem calma sem graça, a promessa de "turma inteira" cai e o VUOO vira "o app das crianças com laudo" (`[IN-02]`, `[IN-04]`). Por isso a linguagem tem **intensidades sobre os mesmos tokens** (Modo suave; celebração quieta, padrão ou festa) e a HIP-6 é a primeira a ser levada ao CIATec.

## Proposta de valor

- **Criança:** "eu sei o que vai acontecer, posso errar sem problema, e ninguém fica sabendo como eu fui."
- **Professora:** "em 2 minutos eu sei o que mudou na minha turma, de onde veio essa informação e o que posso fazer."
- **Gestor:** "consigo mostrar acompanhamento individualizado sem expor nenhuma criança."

## Não-objetivos

- **Não é a identidade do CIATec.** Esta linguagem é do produto VUOO; o CIATec aparece como chancela científica e decide seus próprios jogos e experimentos.
- **Não define os jogos.** Os jogos saem do co-design (OE6), da consultoria de design instrucional e do protocolo do CIATec. Aqui ficam a gramática, as regras de composição e exemplos.
- **Não toca o palco de medida.** Estímulos, tempos, tamanhos e número de tentativas são do protocolo do CIATec.
- **Não monetiza a criança.** Não há loja, moeda, anúncio nem recompensa paga.

## Riscos

| Risco | Tipo | Impacto | O que reduziria |
|-------|------|---------|-----------------|
| Linguagem calma demais perde as crianças sem condição identificada (HIP-6) | usuário | alto | Intensidades sobre os mesmos tokens; HIP-6 levada cedo ao CIATec |
| Linguagem contamina a medida | científico | alto | Palco de medida travado pelo protocolo; configurações registradas por sessão como covariáveis |
| Afeto do Bot vira contingente ao desempenho, ou vínculo vira dependência | usuário/legal | alto | Expressões não contingentes; regras de vínculo (`03` §4) |
| Pressão social muda de lugar (Céu, coleção, dias de voo) | usuário/legal | alto | Nada na tela da criança tem estado de "faltou"; critério de parada do Céu |
| Professor lê o painel como diagnóstico | usuário/legal | alto | Duas camadas no cartão, rodapé de limite, encaminhamento, contestação (D-17) |
| Dado de Plano Educacional Individualizado vira rótulo | legal | alto | D-19: dado sensível, acesso restrito, RIPD |
| Câmera (Wemoga Eye) sem aviso | legal | alto | Componente "Câmera ligada" e assentimento (`03` §11) |
| Aparelhos compartilhados e fracos, sala barulhenta, sem fone | técnico | médio | Áudio redundante com o visual; offline; senha-figura |
| Jogos do CIATec presos ao SaaS pago | governança | médio | D-18 |

## Pontas soltas

Todas em `99-pendencias.md`.
