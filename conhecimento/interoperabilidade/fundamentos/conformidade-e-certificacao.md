---
id: iop.fund.conformidade-e-certificacao
titulo: Conformidade, certificação e o que elas garantem
tipo: conceito
dominio: interoperabilidade
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [imsglobal2020caliper, imsglobal2022qti30, imsglobal2022oneroster, edtech2026lti, imsglobal2011cc, edfi2026datastandard]
relacoes:
  - { tipo: complementa, alvo: iop.fund.niveis-de-interoperabilidade }
  - { tipo: relacionado-a, alvo: iop.catalogo }
termos: [conformidade, certificação, RFC 2119, MUST, SHOULD, suíte de certificação, normativo, informativo]
---

# Conformidade e certificação

## Definição e terminologia

**Conformidade** é a propriedade de uma implementação satisfazer os requisitos normativos de uma especificação. **Certificação** é o reconhecimento, por um terceiro, de que uma implementação passou em um conjunto de testes definido por esse terceiro. Não são a mesma coisa: certificação é um subconjunto verificável da conformidade, e normalmente mais estrito em alguns pontos e mais frouxo em outros [I].

O Caliper 1.2 é explícito: tudo que não está em seção marcada como não normativa é normativo; as palavras-chave seguem a RFC 2119; uma implementação que falha em um requisito MUST/REQUIRED/SHALL "is considered nonconformant"; SHOULD indica boa prática [F: imsglobal2020caliper, §1.3]. A especificação também registra que o guia de conformidade e certificação define os requisitos para Sensors e pode impor restrições normativas mais estritas que a própria especificação, para categorias específicas de implementação [F: imsglobal2020caliper, §1.4.1].

## Problema que resolve

Uma declaração de "suportamos o padrão X" não é verificável. Conformidade dá o critério; certificação dá a evidência de terceiro. Em compras públicas, a segunda é o que pode ser exigida em edital [I].

## Fundamentos e funcionamento

**Documentos de conformidade separados.** Nos padrões 1EdTech, o guia de conformidade é um documento do conjunto, distinto da especificação: o QTI 3.0 lista QTI-CERT-30 no seu documentation set [F: imsglobal2022qti30, §2.4]; o OneRoster 1.2 lista um Implementation Guide e um Conformance and Certification Guide [F: imsglobal2022oneroster].

**Suítes de teste.** A página do padrão LTI aponta para o guia de certificação do LTI Advantage, uma FAQ, a suíte de diagnóstico e certificação em `build.1edtech.org` (com login) e uma suíte legada; também sugere requisitos de LTI Advantage para RFPs institucionais [F: edtech2026lti].

**Conformidade sem certificação central.** O Common Cartridge é o contraexemplo: a página de especificações não descreve programa de certificação próprio, e a orientação de conformidade e os *test cartridges* vêm pela Common Cartridge Alliance [F: imsglobal2011cc].

**Normativo versus não normativo dentro do mesmo padrão.** No Ed-Fi, o Unifying Data Model é explicitamente não normativo, enquanto as páginas de Best Practices e as API Guidelines são normativas; as diretrizes de extensão são não normativas [F: edfi2026datastandard]. Ler o modelo como se fosse a norma leva a conclusões erradas sobre o que é obrigatório [I].

## Requisitos e pressupostos

- A especificação distingue claramente requisitos de recomendações (RFC 2119 ou equivalente).
- Existe suíte executável e acessível. Quando a suíte exige associação à organização mantenedora, a certificação deixa de ser critério neutro e passa a ter custo de entrada [I]. Não foi possível verificar nesta rodada se a certificação 1EdTech exige associação — a página de programa consultada retornou 404.

## Vantagens e limitações

Vantagem: certificação reduz o custo de avaliação de fornecedor e cria linha de base comparável.

Limitações [I]:
- Certificação cobre a camada técnica. Dois produtos certificados no mesmo padrão podem continuar semanticamente incompatíveis (ver `iop.fund.niveis-de-interoperabilidade`).
- Certificação é por versão e por papel (plataforma ou ferramenta); dizer "certificado em LTI" sem dizer em qual serviço e versão não informa.
- Certificação tem validade temporal e pode se referir a uma versão antiga do produto.

## Alternativas e comparações

| Instrumento | Quem verifica | O que garante |
|---|---|---|
| Autodeclaração de conformidade | o próprio fornecedor | nada verificável |
| Suíte de teste pública executada pelo comprador | o comprador | comportamento observado, na versão testada |
| Certificação pelo mantenedor | terceiro | aprovação em um conjunto fixo de casos |
| Piloto com dados reais | as duas partes | interoperabilidade semântica e operacional |

## Métricas e métodos de avaliação

Para avaliação própria, independentemente de certificação [I]: percentual de casos da suíte pública que passam; número de campos obrigatórios do padrão ausentes nas mensagens reais; taxa de rejeição do consumidor em produção.

## Relações com outros conceitos

Complementa `iop.fund.niveis-de-interoperabilidade`: certificação endereça a camada técnica e parte da semântica, e nada das camadas organizacional e jurídica.

## Lacunas e questões abertas

- Páginas de programa de certificação do 1EdTech (`/program/certification`, `/program/trusted-apps`) retornaram 404 na consulta; o vínculo entre certificação e associação permanece não verificado.
- Não foi verificado se xAPI (IEEE 9274.1.1) tem programa de conformidade equivalente ao do antigo LRS Test Suite da ADL.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| imsglobal2020caliper | normativo | 2026-10-29 |
| imsglobal2022qti30 | normativo | 2026-10-29 |
| imsglobal2022oneroster | normativo | 2026-10-29 |
| edtech2026lti | fornecedor | 2026-10-29 |
| imsglobal2011cc | normativo | 2026-10-29 |
| edfi2026datastandard | fornecedor | 2026-10-29 |
