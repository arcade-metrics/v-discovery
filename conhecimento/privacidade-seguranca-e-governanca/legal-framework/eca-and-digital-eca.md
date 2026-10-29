---
id: psg.legal.eca-and-digital-eca
titulo: ECA e Estatuto Digital da Criança e do Adolescente
tipo: conceito
dominio: privacidade-seguranca-e-governanca
status: rascunho
criado: 2026-10-29
atualizado: 2026-10-29
consultado_em: 2026-10-29
fontes: [lei8069eca, lei15211ecadigital, decreto126222025, decreto128802026, brasil2018lgpd]
relacoes:
  - { tipo: parte-de, alvo: psg.legal.comparison }
  - { tipo: complementa, alvo: psg.legal.lgpd-children }
  - { tipo: relacionado-a, alvo: psg.consent.parental-consent }
  - { tipo: relacionado-a, alvo: psg.audit.ripd-dpia }
  - { tipo: relacionado-a, alvo: psg.access.minimization-and-privacy-by-design }
termos: [proteção integral, prioridade absoluta, interesse superior da criança, acesso provável, privacidade por padrão, verificação de idade, supervisão parental, perfilamento, autoridade administrativa autônoma]
---

# ECA e Estatuto Digital da Criança e do Adolescente

## Definição e terminologia

Dois estatutos formam a camada "de direitos da criança" que se sobrepõe à LGPD em qualquer plataforma educacional brasileira. O **ECA** (Lei 8.069/1990) é a lei geral de proteção integral: define criança como "a pessoa até doze anos de idade incompletos" e adolescente como "aquela entre doze e dezoito anos de idade" [F: lei8069eca, art. 2], garante a ambos "todos os direitos fundamentais inerentes à pessoa humana" [F: lei8069eca, art. 3] e impõe à família, à comunidade, à sociedade e ao poder público o dever de assegurá-los "com absoluta prioridade" [F: lei8069eca, art. 4]. O **Estatuto Digital da Criança e do Adolescente**, conhecido como "ECA Digital", é a Lei 15.211, de 17 de setembro de 2025, que "dispõe sobre a proteção de crianças e de adolescentes em ambientes digitais" [F: lei15211ecadigital, ementa]. Esta lei adota os conceitos de criança e adolescente do art. 2 do ECA [F: lei15211ecadigital, art. 2, §1].

Termos próprios do Estatuto Digital: **produto ou serviço de tecnologia da informação** ("produto ou serviço fornecido a distância, por meio eletrônico e provido em virtude de requisição individual") [F: lei15211ecadigital, art. 2]; **acesso provável**; **autoridade administrativa autônoma** ("entidade da administração pública criada por lei, responsável por zelar pela aplicação desta Lei") [F: lei15211ecadigital, art. 2]. O Decreto 12.622, de 17 de setembro de 2025, designa a ANPD como essa autoridade [F: decreto126222025, art. 2].

O que este documento não é: não cobre o ECA como estatuto penal ou de medidas socioeducativas, nem a regulação de redes sociais e jogos comerciais além do que afeta plataformas educacionais.

## Problema que resolve

A LGPD regula o dado; o ECA regula a pessoa em desenvolvimento. Uma plataforma pode estar em conformidade com as bases legais da LGPD e ainda assim violar deveres de proteção integral, por exemplo ao expor a criança a conteúdo inadequado, a perfilamento ou a desenho que induz uso compulsivo. O Estatuto Digital converte esses deveres em obrigações concretas para fornecedores de serviços digitais, com sanções próprias e uma autoridade fiscalizadora, e cria uma regra de alcance ("acesso provável") que captura serviços não dirigidos a menores mas usados por eles [I].

## Fundamentos e funcionamento

### Princípios do ECA aplicáveis a plataformas

- **Interpretação pelo melhor interesse**: o art. 100, parágrafo único, lista como princípios a "proteção integral e prioritária: a interpretação e aplicação de toda e qualquer norma contida nesta Lei" deve considerar a proteção integral (inciso II) e o "interesse superior da criança e do adolescente" (inciso IV) [F: lei8069eca, art. 100, parágrafo único]. [I] É a esse conceito, incorporado também pela Convenção da ONU, que o art. 14 da LGPD remete ao falar em "melhor interesse".
- **Direito à informação e à participação segundo o estágio de desenvolvimento**: a "obrigatoriedade da informação" determina que criança e adolescente, "respeitado seu estágio de desenvolvimento", e seus pais sejam informados de seus direitos e dos motivos de uma intervenção (inciso XI); a "oitiva obrigatória e participação" garante o direito de serem ouvidos e participar das decisões (inciso XII) [F: lei8069eca, art. 100, parágrafo único]. [I] Esses incisos são o fundamento jurídico interno para o assentimento da criança, aprofundado em psg.consent.child-assent.
- **Respeito e dignidade**: "o direito ao respeito consiste na inviolabilidade da integridade física, psíquica e moral" [F: lei8069eca, art. 17]; "é dever de todos prevenir a ocorrência de ameaça ou violação dos direitos da criança e do adolescente" [F: lei8069eca, art. 70].
- **Educação**: o art. 53 assegura o direito à educação e, entre outros, o "direito de ser respeitado por seus educadores" e o "direito de contestar critérios avaliativos" [F: lei8069eca, art. 53, II e III]. [I] O direito de contestar critérios avaliativos é relevante quando a avaliação é mediada por modelo automatizado: dialoga com o direito de "solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado" [F: brasil2018lgpd, art. 20].

### O Estatuto Digital (Lei 15.211/2025)

**Alcance.** A lei "aplica-se a todo produto ou serviço de tecnologia da informação direcionado a crianças e a adolescentes no País" e também aos de acesso provável, caracterizado por "suficiente probabilidade de uso e atratividade" por menores, "considerável facilidade ao acesso e utilização" ou "significativo grau de risco à privacidade, à segurança ou ao desenvolvimento biopsicossocial" [F: lei15211ecadigital, art. 1 e parágrafo único]. Ficam de fora apenas "as funcionalidades essenciais" de infraestrutura, como protocolos e padrões técnicos abertos [F: lei15211ecadigital, art. 2, §2]. A lei não contém exclusão para serviços educacionais; as palavras "educacional" e "escola" não aparecem no texto, e "educação" surge apenas como fundamento ("promoção da educação digital") e como medida de conscientização [F: lei15211ecadigital, art. 4, VIII; art. 6, §2; art. 17, §4, VII]. [I] Uma plataforma educacional voltada a alunos é, portanto, serviço "direcionado a crianças e a adolescentes" e está integralmente sujeita à lei.

**Deveres de desenho.** Os produtos devem "garantir a proteção prioritária desses usuários" e "ter como parâmetro o seu melhor interesse" [F: lei15211ecadigital, art. 3]. O fornecedor deve "garantir, por padrão, a configuração no modelo mais protetivo disponível em relação à privacidade"; o produto "deverá, por padrão, operar com o grau mais elevado de proteção da privacidade e dos dados pessoais" [F: lei15211ecadigital, art. 7, caput e §1]. O art. 8 exige "realizar gerenciamento de riscos de seus recursos, funcionalidades e sistemas" e "desenvolver desde a concepção e adotar por padrão configurações que evitem o uso compulsivo" [F: lei15211ecadigital, art. 8]. [I] Esses dispositivos são a positivação, em lei brasileira, de privacy by design e by default, tratados em psg.access.minimization-and-privacy-by-design.

**Dados e perfilamento.** "É vedada a utilização de técnicas de perfilamento para direcionamento de publicidade comercial a crianças e a adolescentes" [F: lei15211ecadigital, art. 22]; "é vedada a criação de perfis comportamentais de usuários crianças e adolescentes" para fins publicitários [F: lei15211ecadigital, art. 26]. O art. 16 obriga a disponibilizar a pais, responsáveis, crianças e adolescentes informação "sobre os riscos e as medidas de segurança adotadas para esse público", e o parágrafo único trata do tratamento de dados de menores que vá além do estritamente necessário, caso em que o controlador deve mapear riscos e elaborar relatório de impacto [F: lei15211ecadigital, art. 16]. Os relatórios semestrais de transparência exigidos de fornecedores com mais de um milhão de usuários menores devem incluir "os aprimoramentos técnicos para aferir consentimento parental conforme o disposto no § 1º do art. 14" da LGPD [F: lei15211ecadigital, art. 31, VI]. [I] O perfilamento pedagógico (modelo de aluno para adaptação do ensino) não é o perfilamento publicitário vedado; permanece, porém, sujeito ao melhor interesse e aos deveres de desenho.

**Verificação de idade e supervisão parental.** Para conteúdo impróprio, a verificação deve ocorrer "a cada acesso do usuário", "vedada a autodeclaração" [F: lei15211ecadigital, art. 9, §1]; lojas de aplicativos e sistemas operacionais devem adotar "medidas proporcionais, auditáveis e tecnicamente seguras" para estimar a idade [F: lei15211ecadigital, art. 12, I], e dados usados para verificação só podem servir a esse fim [F: lei15211ecadigital, art. 13]. O download de aplicativos por menores exige "consentimento livre e informado dos pais ou responsáveis legais", "vedada a presunção de autorização" [F: lei15211ecadigital, art. 12, §2]. Os fornecedores devem oferecer ferramentas de supervisão parental com configurações padrão de alta proteção [F: lei15211ecadigital, cap. V]. O Decreto 12.880, de 18 de março de 2026, regulamenta a lei, estabelece princípios para métodos de aferição de idade (minimização de dados, proibição de reter imagem ou cópia de documento de identidade) e atribui à ANPD a definição de padrões e certificação dessas soluções e das etapas de implementação [F: decreto128802026, art. 24, 30 e 49].

**Fiscalização e sanções.** A ANPD "ficará responsável por fiscalizar o cumprimento desta Lei em todo o território nacional" [F: lei15211ecadigital, art. 34; F: decreto126222025, art. 2]. Sanções: "advertência, com prazo para adoção de medidas corretivas de até 30 (trinta) dias"; "multa simples, de até 10% (dez por cento) do faturamento do grupo econômico no Brasil"; "suspensão temporária das atividades"; "proibição de exercício das atividades" [F: lei15211ecadigital, art. 35]. A página do Planalto indica que advertência e multa são aplicadas pela autoridade administrativa e as duas últimas pelo Judiciário, e que o fundo de destino das multas é o Fundo Nacional para a Criança e o Adolescente [F: lei15211ecadigital, art. 35, §5 e cap. XV].

**Vigência.** Na redação atual, "esta Lei entra em vigor em 17 de março de 2026" (art. 41-A, incluído pela Lei 15.352/2026, que substituiu a regra anterior de seis meses após a publicação) [F: lei15211ecadigital, art. 41-A].

## Requisitos e pressupostos

- Determinar se o serviço é "direcionado" ou de "acesso provável"; para plataforma escolar a resposta é afirmativa pela própria finalidade [I].
- Configuração padrão mais protetiva, gerenciamento de riscos desde a concepção e ausência de mecanismos de uso compulsivo: obrigações legais, não recomendações [F: lei15211ecadigital, art. 7 e 8].
- Nenhuma publicidade comportamental a menores, mesmo em modelo freemium [F: lei15211ecadigital, art. 22 e 26].
- Relatório de impacto quando o tratamento de dados de menores exceder o estritamente necessário [F: lei15211ecadigital, art. 16, parágrafo único]; ver psg.audit.ripd-dpia.
- Informação sobre riscos e medidas de segurança acessível a pais e às próprias crianças [F: lei15211ecadigital, art. 16].

## Vantagens e limitações

O Estatuto Digital resolve uma ambiguidade da LGPD ao fixar deveres de desenho e ao nomear uma autoridade (ANPD) única para dados e para proteção digital de menores, evitando conflito de competências [I]. Suas limitações para o contexto educacional: a lei foi escrita pensando em redes sociais, lojas de aplicativos e jogos; não há regra específica para o caso em que a escola, e não os pais, contrata o serviço, nem para a relação entre consentimento parental (LGPD art. 14, §1) e "consentimento para download" (art. 12, §2) [I]. A regulamentação por decreto é recente e a certificação de soluções de aferição de idade ainda depende de atos da ANPD [F: decreto128802026, art. 49].

## Exemplo técnico independente de domínio

```
# Trecho de política de configuração padrão para serviço de acesso provável por menores
perfil_padrao_menor:
  privacidade: maxima                    # Lei 15.211, art. 7
  geolocalizacao: desligada
  publicidade_comportamental: proibida   # art. 22 e 26
  notificacoes_engajamento: desligadas   # art. 8 (uso compulsivo)
  dados_verificacao_idade: {uso: "somente aferir idade", retencao_documento: nunca}   # art. 13; Decreto 12.880, art. 24
  supervisao_parental: {disponivel: sim, padrao: alta_protecao}                        # cap. V
  informacao_riscos: {publico: [responsavel, crianca], formato: acessivel}             # art. 16
```

## Relações com outros conceitos

Parte de psg.legal.comparison; complementa psg.legal.lgpd-children, que trata das bases legais e do art. 14 da LGPD referidos pelo Estatuto Digital. O consentimento exigido para download e o consentimento do art. 14 são confrontados em psg.consent.parental-consent. O relatório de impacto do art. 16 é tratado em psg.audit.ripd-dpia. Os deveres de desenho remetem a psg.access.minimization-and-privacy-by-design.

## Lacunas e questões abertas

- O texto da Lei 15.211/2025 foi lido na página do Planalto, que alerta não substituir a publicação no DOU e apresenta codificação de caracteres corrompida; citações tiveram acentos restaurados. Os vetos (arts. 7, §3; 35, §3; 36; 41) e as inclusões posteriores (36-A, 41-A) foram vistos apenas nas notas da página.
- As MPs 1.317/2025 e 1.319/2025 e a Lei 15.352/2026, que alteraram a vigência e dispositivos conexos, não foram abertas; a informação vem das notas de redação do Planalto.
- O Decreto 12.880/2026 foi lido parcialmente (aferição de idade, supervisão parental, sanções); a Política Nacional que ele institui não foi examinada.
- Falta posição da ANPD sobre como o Estatuto Digital se aplica a plataformas contratadas por escolas públicas e sobre a interação com a Política Nacional de Educação Digital (Lei 14.533/2023, não consultada).
- Os arts. 74 a 80 do ECA (classificação indicativa de diversões e espetáculos) foram localizados só pelo cabeçalho de seção; sua aplicação a jogos educacionais não foi examinada.

## Fontes

| Chave | Tipo | Consultado em |
|---|---|---|
| lei8069eca | normativo | 2026-10-29 |
| lei15211ecadigital | normativo | 2026-10-29 |
| decreto126222025 | normativo | 2026-10-29 |
| decreto128802026 | normativo | 2026-10-29 |
| brasil2018lgpd | normativo | 2026-10-29 |
