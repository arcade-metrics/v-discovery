# Regras de negócio do VUOO (reservado)

Registro das regras de negócio da plataforma, uma por arquivo, com código estável `RN-nn`. Pasta criada em 29/10/2026 e deixada vazia de propósito: as regras serão escritas depois que a base de conhecimento dos domínios de privacidade, dados e eventos, e acessibilidade estiver em primeira versão, e discutidas antes de fechar.

## Formato previsto (a confirmar na primeira regra)

```yaml
---
id: RN-01
titulo:
status: proposta | aceita | substituída
origem: [IN-17]            # insumos que a originam
decisao: [D-20]            # decisões de produto que a fixaram
embasamento: [gam.instr.evidence-centered-design]   # ids de conhecimento/
substitui:                 # RN anterior, se houver
atualizado_em: AAAA-MM-DD
---
```

Corpo: enunciado da regra em uma frase verificável; o que ela protege; como se testa que está sendo cumprida; exceções; custo de voltar atrás.

## Candidatas já identificadas

Decisões marcadas *invariante* em `../../vuoo-linguagem/05-decisoes.md`: palco de medida e moldura (D-20), separação entre base de pesquisa e base operacional (IN-04, D-19), perfis de acesso (IN-21 a IN-23), PEI como dado sensível (D-19), sinal de atenção com confirmação (D-16, D-17, IN-35), limite diário (D-14), governança dos jogos do CIATec (D-18), canal de voz por fone (D-21).
