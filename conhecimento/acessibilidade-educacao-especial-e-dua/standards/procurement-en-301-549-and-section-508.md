---
id: acs.std.procurement-en-301-549-and-section-508
titulo: EN 301 549 e Section 508
tipo: padrao
dominio: acessibilidade-educacao-especial-e-dua
status: rascunho
criado: 2026-10-30
atualizado: 2026-10-30
consultado_em: 2026-10-30
fontes: [etsi2026en301549, etsi2021en301549, accessboard2017section508, w3c2024wcag22]
relacoes:
  - { tipo: parte-de, alvo: acs.std.comparison }
  - { tipo: depende-de, alvo: acs.std.wcag }
  - { tipo: avaliado-por, alvo: acs.asmt.conformance-evaluation }
  - { tipo: relacionado-a, alvo: acs.br.emag-and-nbr-17225 }
  - { tipo: relacionado-a, alvo: iop.fund.conformidade-e-certificacao }
termos: [EN 301 549, norma harmonizada, presunção de conformidade, Section 508, Revised 508 Standards, critério de desempenho funcional, funcionalidade fechada, software não web, incorporação por referência, ICT legada, European Accessibility Act]
---

# EN 301 549 e Section 508

## Definição e terminologia

São as duas principais normas de compra pública e regulação de acessibilidade de TIC fora da web pura.

- **EN 301 549**, "Accessibility requirements for ICT products and services", norma europeia harmonizada mantida por ETSI, CEN e CENELEC. A versão em vigor no repositório da ETSI é a V4.1.1 (2026-09), desenvolvida a partir da V3.2.1 (2021-03) [F: etsi2026en301549, prefácio]. Especifica requisitos de acessibilidade para produtos e serviços de TIC e os procedimentos de teste de cada requisito [F: etsi2026en301549, cl. 1].
- **Section 508 (Revised 508 Standards)**, 36 CFR part 1194, requisitos de escopo e técnicos para TIC sob a Seção 508 nos Estados Unidos, de cumprimento obrigatório pelas agências federais (E101.1); regra final de 18 de janeiro de 2017 [F: accessboard2017section508].

O que não são: não substituem a WCAG; incorporam-na. E não se aplicam diretamente a escolas ou empresas privadas no Brasil; o análogo brasileiro está em `acs.br.emag-and-nbr-17225` [I].

## Problema que resolve

Quem compra ou regula TIC precisa de requisitos que cubram mais que páginas web (software, documentos, hardware, comunicação por voz, terminais fechados) e que permitam teste com resultado conclusivo. A EN 301 549 declara que seus testes são detalhados de modo que "conformance testing can give conclusive results" [F: etsi2026en301549, cl. 1].

## Fundamentos e funcionamento

### Relação com a WCAG

A cláusula 9 (web) da V4.1.1 declara que conformidade com WCAG 2.2 nível AA "is equivalent to conforming with all of clauses 9.1 to 9.4" mais os requisitos de conformidade da cláusula 9.6; a mesma cláusula mapeia WCAG 2.0 e 2.1 para subconjuntos [F: etsi2026en301549, cl. 9.0]. Entre as mudanças da V4.1.1 está o alinhamento das cláusulas 9, 10 (documentos não web) e 11 (software não web) à WCAG 2.2 [F: etsi2026en301549, prefácio]. Na V3.2.1, a equivalência plena era com a WCAG 2.1 AA [F: etsi2021en301549, cl. 9.0]. A V4.1.1 lista os critérios AAA da WCAG 2.2 em 9.5 como informativos, citando o W3C: não se recomenda exigir AAA como política geral [F: etsi2026en301549, cl. 9.0, nota 4]. Webviews dentro de aplicativos seguem a cláusula 11, não a 9 [F: etsi2026en301549, cl. 9.0, nota 3].

A Section 508 incorpora por referência a WCAG 2.0 (Recommendation de 11/12/2008) em 702.10.1: conteúdo eletrônico (E205.4) e software, incluindo interfaces de plataformas e aplicações (E207.2), devem conformar com níveis A e AA da WCAG 2.0, com quatro critérios dispensados para documentos e software não web [F: accessboard2017section508]. ICT existente que cumpria a norma anterior e não foi alterada desde 18 de janeiro de 2018 não precisa ser modificada (E202.2) [F: accessboard2017section508].

### Critérios de desempenho funcional

Ambas têm declarações por capacidade funcional, aplicadas onde os requisitos técnicos não alcançam:

- EN 301 549, 4.2.10 "Usage with limited cognition, language or learning": a TIC "shall provide features and/or presentation that makes it simpler and easier to understand, operate and use"; as notas citam como exemplos velocidade de áudio ajustável, tempos, indicação e sugestão de erro, ordem lógica de foco, saída em áudio do texto, predição de palavras e tarefas em passos fáceis [F: etsi2026en301549, cl. 4.2.10]. A cláusula já existia na V3.2.1 [F: etsi2021en301549].
- Section 508, 302.9 "With Limited Language, Cognitive, and Learning Abilities", com redação equivalente ("simpler and easier"); os critérios do capítulo 3 se aplicam a funções que os capítulos 4 e 5 não cobrem (E204.1) [F: accessboard2017section508].

### Requisitos além da web relevantes para jogos e acesso alternativo

- 5.9 Simultaneous user actions: onde houver modo que exija ações simultâneas, deve haver ao menos um modo que não exija; a nota cita pressionar duas teclas ao mesmo tempo ou tocar com mais de um dedo [F: etsi2026en301549, cl. 5.9].
- Limites de tempo em software não web repetem a estrutura de 2.2.1 da WCAG (desligar, ajustar, estender com 20 s; exceções de tempo real, essencial e 20 horas) [F: etsi2026en301549, cl. 11; w3c2024wcag22, 2.2.1].
- 5.1 Funcionalidade fechada: quando o usuário não pode instalar tecnologia assistiva, a TIC deve ser operável sem ela (5.1.2.2) [F: etsi2026en301549, cl. 5.1]. Um console ou tablet escolar bloqueado pode ser funcionalmente fechado: a norma diz que computadores que não permitem ajustar configurações ou instalar software "are functionally closed" [F: etsi2026en301549, cl. 5.1.1].
- 4.2.11 Privacidade: recursos de acessibilidade devem preservar a privacidade do usuário [F: etsi2026en301549, cl. 4.2.11].

### Efeito jurídico na União Europeia

A V4.1.1 foi preparada sob o pedido de normalização C(2022) 6456 para oferecer um meio voluntário de conformidade com a Diretiva (UE) 2019/882 (European Accessibility Act); uma vez citada no Jornal Oficial, o cumprimento das cláusulas listadas em A.2 confere presunção de conformidade; a V3.2.1 cumpria esse papel para a Diretiva (UE) 2016/2102 (sítios e aplicativos do setor público) [F: etsi2026en301549, prefácio].

## Vantagens e limitações

Vantagens: cobrem software, documentos, hardware e funcionalidade fechada; dão requisitos testáveis para edital [F: etsi2026en301549, cl. 1].

Limitações: os critérios cognitivos são declarações de desempenho funcional, sem teste objetivo equivalente aos critérios técnicos [I]; a Section 508 continua presa à WCAG 2.0, sem os critérios de 2.1 e 2.2 sobre alvo, arraste, reentrada e autenticação [F: accessboard2017section508] [I]; nenhuma das duas trata dificuldade ou mecânica de jogo [I].

## Alternativas e comparações

| Aspecto | EN 301 549 V4.1.1 | EN 301 549 V3.2.1 | Section 508 (2017) |
|---|---|---|---|
| WCAG de referência | 2.2 AA | 2.1 AA | 2.0 A e AA |
| Escopo | web, documentos, software, hardware, voz | idem | idem |
| Cognição | 4.2.10 (funcional) | 4.2.10 | 302.9 (funcional) |
| Efeito | presunção de conformidade (Diretiva 2019/882) após citação no JO | Diretiva 2016/2102 | obrigatória para agências federais dos EUA |

## Exemplo técnico independente de domínio

```
checklist_de_compra(produto):
    tipo = classificar(produto)    # web | software não web | documento | hardware | fechado
    se tipo == web: exigir WCAG 2.2 AA + 9.6
    se tipo == software não web: exigir cl. 11 (inclui webviews)
    se fechado: exigir 5.1 (operável sem TA do usuário)
    sempre: 5.9 (sem ações simultâneas obrigatórias); 4.2.10 (declaração e evidência de teste)
```

## Relações com outros conceitos

Depende de `acs.std.wcag`. É avaliada por `acs.asmt.conformance-evaluation`. Relaciona-se com `acs.br.emag-and-nbr-17225` (requisitos brasileiros) e com `iop.fund.conformidade-e-certificacao` (conformidade versus certificação).

## Lacunas e questões abertas

- Não foi verificado se a V4.1.1 já foi citada no Jornal Oficial da UE; até isso ocorrer, a presunção de conformidade sob a Diretiva 2019/882 não vale para ela.
- Não foi verificada revisão da Section 508 para WCAG 2.1 ou 2.2.
- O texto da cláusula 11 foi lido só nos trechos de limites de tempo.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| etsi2026en301549 | normativo | 2026-10-30 |
| etsi2021en301549 | normativo | 2026-10-30 |
| accessboard2017section508 | normativo | 2026-10-30 |
| w3c2024wcag22 | normativo | 2026-10-30 |
