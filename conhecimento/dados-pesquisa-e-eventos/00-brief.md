---
id: dat.brief
titulo: Brief do domínio dados de pesquisa e eventos
tipo: relatorio
dominio: dados-pesquisa-e-eventos
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
---

# Brief: dados de pesquisa e eventos

Segue o modelo, o método e o checklist de `_modelo/`. Este arquivo contém só o que é específico do domínio.

## Escopo

Como capturar, estruturar, governar e compartilhar dados gerados por interação com software educacional, com foco em pesquisa. Inclui: telemetria e esquemas de evento (game analytics, event sourcing, OpenTelemetry como referência de instrumentação); qualidade e granularidade de eventos; gestão de dados de pesquisa (princípios FAIR, planos de gestão de dados, repositórios); ética em pesquisa com menores (CEP/CONEP, consentimento e assentimento como exigência de pesquisa); datasets públicos de referência em educação (PSLC DataShop, ASSISTments, EdNet) e sua documentação (datasheets).

Fora do escopo: LGPD, consentimento como gestão de permissões, anonimização e privacidade diferencial (ficam em `privacidade-seguranca-e-governanca`, citados aqui quando o dado vira dataset de pesquisa); modelos preditivos (ficam em `aprendizagem-adaptativa`), formatos padronizados de troca (ficam em `interoperabilidade`, mas o mapeamento evento para xAPI é documentado aqui).

## Estrutura sugerida

- `events/`: modelos de evento, telemetria de jogos, event sourcing, instrumentação.
- `quality/`: granularidade, relógios e ordenação, perda e deduplicação.
- `research-data/`: FAIR, planos de gestão de dados, repositórios, versionamento de datasets.
- `research-ethics/`: CEP/CONEP, consentimento e assentimento em protocolo de pesquisa.
- `datasets/`: datasets públicos de referência e documentação.

## Fontes prioritárias (a verificar na pesquisa, sem URL ou DOI até verificação)

1. Drachen, Seif El-Nasr e Canossa, "Game Analytics" (livro).
2. Wilkinson et al., 2016, princípios FAIR; diretrizes de plano de gestão de dados de agências de fomento (incluindo FAPESP).
3. Lei 13.709/2018 (LGPD), Estatuto da Criança e do Adolescente, Resoluções CNS 466/2012 e 510/2016.
4. Sweeney, k-anonimato; Dwork, privacidade diferencial.
5. Gebru et al., Datasheets for Datasets.
6. Documentação de PSLC DataShop, ASSISTments, EdNet.
7. OpenTelemetry, especificação de sinais e semântica de eventos.

## Perguntas abertas

- Qual a granularidade mínima de evento que preserva construtos cognitivo-motores?
- Como conciliar FAIR com proteção de dados de menores?
- Que esquema de evento permite mapeamento sem perda para xAPI?
- Quais requisitos específicos a FAPESP impõe a planos de gestão de dados?
