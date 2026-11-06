# Ficha curta: variação estadual (padrões de dados e privacidade estudantil)

```yaml
id: us.state-variation
name: Variação estadual — obrigatoriedade de padrões de dados e leis estaduais de privacidade estudantil
acronym: n/a
jurisdiction: estados dos EUA
issuing_organization: legislativos e agências estaduais de educação (SEAs)
reference_type: leis estaduais; especificações estaduais de coleta
domain: [D8, D1]
official_url: varia por estado
version: n/a
legal_status: misto
mandatory_scope: por estado
sources: [E29, E30, E31, E32, E33, E34, E35, E36, E37, E40]
access_date: 2026-11-05
research_status: parcial — amostra de estados; nenhum levantamento exaustivo
```

## 1. Quem é obrigado a quê: padrões de dados

| Padrão | Evidência de obrigatoriedade | Fonte |
|---|---|---|
| Ed-Fi | Nenhum mandato federal. O playbook da Ed-Fi para SEAs trata a adoção como escolha e não lista estados [E36]. A Ed-Fi afirma adoção por "over half of states" (alegação do fornecedor, trecho) [E40]. | E36, E40 |
| Ed-Fi — Texas | TEDS (Texas Education Data Standards) "based on the national Ed-Fi" core, usado para carregar dados no TSDS; PEIMS é a coleta estadual obrigatória submetida pelo TSDS PEIMS; Unique ID gera identificadores para alunos e staff | E33 (trecho) |
| Ed-Fi — Carolina do Sul, Vermont, Wisconsin, Maine | Coleta estadual via API Ed-Fi descrita nas páginas estaduais (SC, VT) ou por fornecedores (ME, WI) | E34, E35 (trecho) |
| OneRoster | Nenhum ato estadual que o exija foi localizado. O 1EdTech publica guia de compras com item-modelo de RFP ("especificar o método de troca OneRoster: CSV ou REST") | E37 (trecho) |
| SIF | Ao menos um RFP estadual (Iowa) pediu solução SIF estadual (trecho de busca) | trecho |
| CEDS | Voluntário | `iop.ros.ceds` |

Conclusão [I]: nos EUA, a obrigatoriedade de formato vem da **especificação de coleta de cada SEA** (frequentemente Ed-Fi com extensões e descritores estaduais), enquanto OneRoster/LTI são exigências de mercado (contratos e RFPs distritais). Não declarar obrigatoriedade sem o ato do estado específico.

## 2. Leis estaduais de privacidade estudantil

**SOPIPA (Califórnia), Bus. & Prof. Code §22584 e seguintes** [E30, E31 — fontes secundárias; texto oficial em leginfo.legislature.ca.gov não lido]:

- Aplica-se ao *operador* que sabe que seu serviço é usado principalmente para fins escolares K-12 e foi desenhado e comercializado para isso; **não depende de contrato** com a escola.
- Proíbe: publicidade direcionada com base em dados do serviço; construir perfil do aluno exceto para fins escolares K-12; vender informação do aluno; divulgar fora das exceções.
- Exige: segurança razoável; exclusão a pedido da escola/rede.
- Vigente desde 2016-01-01; alcança operadores fora da Califórnia que coletam dados de alunos californianos; emendada em 2024 (Stats. 2024, ch. 935; conteúdo não lido).

**Outros estados** (fontes secundárias, contagens divergentes e datadas) [E32]: Student Privacy Compass cita 38 estados com 91 leis desde 2013 (sem data); outra contagem cita 21 estados com leis no modelo SOPIPA. Não foi feito levantamento estado a estado.

## 3. Implicações para o Core [I]

1. Política de dados é **por contrato e por estado**: o adaptador EUA precisa de uma entidade de acordo de compartilhamento (data privacy agreement) vinculada à C.ORG contratante, com finalidades permitidas e prazo de exclusão.
2. Proibição de perfilamento fora de "fins escolares" e de publicidade → finalidade (`purpose`) obrigatória em C.CNS e em todo uso de C.EVT para modelagem do aluno.
3. Exclusão a pedido da organização → operação de expurgo por organização/aluno com registro.
