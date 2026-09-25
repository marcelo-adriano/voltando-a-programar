# Trilha 3 — Back-end com Docker, SQL e Node.js

> **Objetivo da trilha:** projetar bancos de dados relacionais, escrever SQL com fluência, construir APIs REST seguras e testadas em Node.js e rodar tudo em containers.

**Duração:** 12–16 semanas · **Pré-requisitos:** Trilhas 0 e 1 (Trilha 2 recomendada, para conectar o front ao back)

| Módulo | Tema | Duração |
|--------|------|---------|
| 3.1 | HTTP e REST a fundo | 1 semana |
| 3.2 | Docker: imagens, containers e Dockerfile | 1,5 semana |
| 3.3 | Docker Compose e orquestração local | 1 semana |
| 3.4 | SQL: consultas básicas (MySQL e Workbench) | 1 semana |
| 3.5 | SQL: modelagem de dados e DDL | 1,5 semana |
| 3.6 | SQL: joins, agregações, subconsultas e transações | 1,5 semana |
| 3.7 | SQL: índices, performance e recursos avançados | 1 semana |
| 3.8 | Node.js: fundamentos do runtime | 1 semana |
| 3.9 | Express e arquitetura em camadas | 1,5 semana |
| 3.10 | ORM, migrations e acesso a dados | 1,5 semana |
| 3.11 | Autenticação, autorização e segurança de APIs | 1,5 semana |
| 3.12 | Testes no back-end | 1,5 semana |
| 3.13 | Tópicos extras: NoSQL, cache, filas, tempo real | 1 semana |
| 3.14 | Projetos finais | 2–3 semanas |

### Fontes principais da trilha
- 🎥 [Full Stack Open](https://fullstackopen.com/en/): partes 3 (Node/Express), 4 (testes, autenticação), 12 (containers) e 13 (bancos relacionais).
- 🌐 [Node.js — Learn](https://nodejs.org/en/learn) e [documentação da API](https://nodejs.org/docs/latest/api/)
- 🌐 [Docker Docs](https://docs.docker.com/) — *Get started*
- 🌐 [MySQL 8 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/)
- 📘 *Node.js Design Patterns* — Mario Casciaro e Luciano Mammino
- 🌐 [Node.js Best Practices — Yoni Goldberg](https://github.com/goldbergyoni/nodebestpractices) (tradução 🇧🇷 disponível no repositório)
- 📘 *Designing Data-Intensive Applications* — Martin Kleppmann (leitura de fundo; aprofundado na trilha 5)

---

## Módulo 3.1 — HTTP e REST a fundo (1 semana)

### Conceitos
- [ ] Anatomia da requisição e da resposta: linha inicial, cabeçalhos, corpo
- [ ] Métodos: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`; métodos seguros e **idempotentes**
- [ ] Códigos de status: 2xx, 3xx, 4xx, 5xx; os 20 mais usados e quando usar cada um (200, 201, 204, 301, 304, 400, 401, 403, 404, 409, 422, 429, 500, 502, 503)
- [ ] Cabeçalhos importantes: `Content-Type`, `Accept`, `Authorization`, `Cache-Control`, `ETag`, `Location`, `Set-Cookie`, CORS (`Access-Control-*`)
- [ ] HTTP/1.1, HTTP/2 e HTTP/3 (visão geral)
- [ ] Estilo **REST**: recursos, representações, restrições (cliente-servidor, sem estado, cache, interface uniforme), modelo de maturidade de Richardson
- [ ] Design de URLs: substantivos, plural, hierarquia (`/clientes/42/ordens`), filtros, ordenação e paginação por query string
- [ ] Formato de erro padronizado (RFC 9457 — *Problem Details*)
- [ ] Versionamento de API
- [ ] Documentação com **OpenAPI** (Swagger)
- [ ] Ferramentas: `curl`, HTTPie, Insomnia/Postman/Bruno, extensão REST Client do VS Code

### Fontes
- 🌐 [MDN — HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP) 🇧🇷: *Visão geral*, *Mensagens*, *Métodos*, *Status*, *Cabeçalhos*, *CORS*, *Cache*.
- 🌐 [Microsoft — RESTful web API design](https://learn.microsoft.com/pt-br/azure/architecture/best-practices/api-design) 🇧🇷
- 🌐 [Martin Fowler — Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)
- 🌐 [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/): guia de estilo usado em empresa real.
- 🌐 [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) · [Swagger Editor](https://editor.swagger.io/)
- 🌐 [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457)
- 📘 *HTTP: The Definitive Guide* — Gourley e Totty (clássico, para consulta)

### Exercícios
- [ ] **E3.1.1** Use `curl -v` com `GET`, `POST` (JSON), `PUT` e `DELETE` contra o `httpbin.org` e explique cada linha da saída.
- [ ] **E3.1.2** Para cada status da lista acima, escreva um cenário real da API Marcelo IT em que ele seria usado.
- [ ] **E3.1.3** Classifique `GET`, `POST`, `PUT`, `PATCH` e `DELETE` como seguros e/ou idempotentes e justifique.
- [ ] **E3.1.4** Projete (só no papel/markdown) as rotas da API da **loja virtual**: produtos, categorias, clientes, pedidos, itens do pedido, com filtros e paginação.
- [ ] **E3.1.5** Escreva a especificação **OpenAPI** dessas rotas no Swagger Editor.
- [ ] **E3.1.6** Analise a documentação de uma API pública famosa (GitHub, Stripe) e liste 5 boas práticas que ela segue.

### Autoavaliação
1. Qual a diferença entre `PUT` e `PATCH`?
2. O que significa ser idempotente? Por que isso importa para novas tentativas de requisição?
3. Quando usar 401 e quando usar 403? E 400 x 422?
4. O que significa dizer que o REST é "sem estado" (*stateless*)?
5. O que é CORS e em que lado ele é configurado?

---

## Módulo 3.2 — Docker: imagens, containers e Dockerfile (1,5 semana)

### Conceitos
- [ ] O problema que containers resolvem ("na minha máquina funciona")
- [ ] Container x máquina virtual; *namespaces* e *cgroups* (visão geral)
- [ ] **Instalação e configuração**: Docker Engine no Linux, Docker Desktop, usuário no grupo `docker` (e o risco disso)
- [ ] Imagem x container; registros (Docker Hub); tags; `latest` e por que evitar em produção
- [ ] Comandos: `run` (`-d`, `-p`, `-e`, `-v`, `--name`, `--rm`, `-it`), `ps`, `logs`, `exec`, `stop`, `rm`, `images`, `pull`, `push`, `inspect`, `system prune`
- [ ] **Dockerfile**: `FROM`, `WORKDIR`, `COPY`, `ADD`, `RUN`, `ENV`, `ARG`, `EXPOSE`, `USER`, `HEALTHCHECK`, `CMD`, `ENTRYPOINT`
- [ ] **RUN x CMD x ENTRYPOINT**: momento de execução (build x runtime), forma *exec* x forma *shell*, combinação de `ENTRYPOINT` + `CMD`, sobrescrita na linha de comando, sinais e PID 1
- [ ] Camadas e cache de build; ordem das instruções; `.dockerignore`
- [ ] **Multi-stage builds**
- [ ] Imagens pequenas: `alpine`, `slim`, *distroless*
- [ ] Volumes: *named volumes* x *bind mounts* x `tmpfs`; persistência de dados
- [ ] Redes: `bridge`, `host`, `none`; redes definidas pelo usuário e DNS interno
- [ ] Boas práticas de segurança: usuário não-root, sem segredos na imagem, varredura de vulnerabilidades (`docker scout`, Trivy)

### Fontes
- 🌐 [Docker Docs — Get started](https://docs.docker.com/get-started/) e [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- 🌐 [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/)
- 🌐 [Dockerfile reference — Understand how CMD and ENTRYPOINT interact](https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact)
- 🧪 [Play with Docker](https://labs.play-with-docker.com/): laboratório no navegador.
- 📘 *Docker Deep Dive* — Nigel Poulton
- 🎥🇧🇷 [LINUXtips — Descomplicando o Docker](https://www.youtube.com/@LINUXtips) (vídeos e livro gratuito do Jeferson Fernando)
- 🎥 Full Stack Open — parte 12 (Containers).
- 🌐 [Node.js Docker best practices (Snyk)](https://snyk.io/blog/10-best-practices-to-containerize-nodejs-web-applications-with-docker/)

### Exercícios
- [ ] **E3.2.1** Rode `nginx` expondo a porta 8080 e sirva o `homepage.html` com *bind mount*.
- [ ] **E3.2.2** Rode um MySQL em container com volume nomeado. Apague o container, crie outro com o mesmo volume e confirme que os dados continuam.
- [ ] **E3.2.3** Entre num container com `exec -it` e investigue: processos, usuário, sistema de arquivos, rede.
- [ ] **E3.2.4** Escreva um Dockerfile para uma API "olá mundo" em Node.js. Construa, rode e veja as camadas com `docker history`.
- [ ] **E3.2.5** Mude a ordem das instruções (copiar `package.json` antes do código) e compare o tempo de rebuild ao alterar só o código.
- [ ] **E3.2.6** **RUN x CMD x ENTRYPOINT**: crie 4 imagens (só `CMD`, só `ENTRYPOINT`, os dois juntos, forma shell x exec) e documente o comportamento de `docker run imagem` e `docker run imagem argumento` em cada caso.
- [ ] **E3.2.7** Mostre que um container com `CMD` em forma *shell* não recebe `SIGTERM` corretamente (demora 10s para parar) e corrija.
- [ ] **E3.2.8** Converta a imagem para *multi-stage* (build com TypeScript + imagem final só com o JS compilado) e compare o tamanho.
- [ ] **E3.2.9** Faça a imagem rodar com usuário não-root e adicione `HEALTHCHECK`.
- [ ] **E3.2.10** Rode o Trivy na sua imagem e corrija as vulnerabilidades mais graves trocando a imagem base.
- [ ] **E3.2.11** Crie uma rede, suba dois containers nela e faça um se comunicar com o outro pelo nome.
- [ ] **E3.2.12** Publique uma imagem sua no Docker Hub ou no GitHub Container Registry com tag de versão.

### Autoavaliação
1. Qual a diferença entre imagem e container?
2. Explique RUN, CMD e ENTRYPOINT: quando cada um executa e como interagem.
3. Por que a forma *exec* (`["node", "app.js"]`) é preferível à forma *shell*?
4. Por que a ordem das instruções no Dockerfile afeta o tempo de build?
5. Qual a diferença entre volume nomeado e *bind mount*?
6. Por que não colocar segredos em `ENV` ou `ARG` no Dockerfile?
7. Container é uma forma de segurança? Até que ponto?

---

## Módulo 3.3 — Docker Compose e orquestração local (1 semana)

### Conceitos
- [ ] `compose.yaml`: `services`, `image` x `build`, `ports`, `environment`, `env_file`, `volumes`, `networks`, `depends_on` (com `condition: service_healthy`), `restart`, `healthcheck`, `profiles`
- [ ] Comandos: `up -d`, `down` (e `down -v`), `ps`, `logs -f`, `exec`, `build`, `watch`
- [ ] Variáveis e arquivo `.env`
- [ ] Ambiente de desenvolvimento com *hot reload* (bind mount ou `develop.watch`)
- [ ] Vários arquivos compose (`compose.override.yaml`) para dev e produção
- [ ] Inicialização do banco com scripts (`/docker-entrypoint-initdb.d`)
- [ ] Introdução ao que é orquestração em produção (Kubernetes, Swarm), vista na trilha 6

### Fontes
- 🌐 [Docker Compose — docs](https://docs.docker.com/compose/) e [Compose file reference](https://docs.docker.com/reference/compose-file/)
- 🌐 [Awesome Compose](https://github.com/docker/awesome-compose): exemplos oficiais de stacks.

### Exercícios
- [ ] **E3.3.1** Compose com MySQL + Adminer (ou phpMyAdmin) e volume persistente.
- [ ] **E3.3.2** Compose com API Node + MySQL, onde a API só sobe quando o banco estiver saudável.
- [ ] **E3.3.3** Script SQL de inicialização que cria as tabelas e insere dados de exemplo ao subir o banco pela primeira vez.
- [ ] **E3.3.4** *Hot reload* da API em desenvolvimento dentro do container.
- [ ] **E3.3.5** Stack completa: front (Vite) + API + MySQL + Nginx como proxy reverso na frente de tudo.
- [ ] **E3.3.6** Separe configurações de dev e produção com `compose.override.yaml`.

### Autoavaliação
1. O `depends_on` sozinho garante que o banco está pronto para receber conexões? Como resolver?
2. O que `docker compose down -v` apaga?
3. Como os serviços de um Compose se encontram na rede?

---

## Módulo 3.4 — SQL: consultas básicas (MySQL e Workbench) (1 semana)

### Conceitos
- [ ] Banco de dados relacional: tabelas, linhas, colunas, chave primária, chave estrangeira
- [ ] SGBDs: MySQL, PostgreSQL, SQLite, SQL Server; diferenças de dialeto
- [ ] **MySQL em Docker** e **MySQL Workbench** (conexão, editor de consultas, diagrama EER, engenharia reversa)
- [ ] Categorias de comandos: DQL, DML, DDL, DCL, TCL
- [ ] **`SELECT`**: colunas, `*` (e por que evitar), apelidos (`AS`)
- [ ] **`CONCAT`**, `CONCAT_WS`, funções de string (`UPPER`, `LOWER`, `LENGTH`, `SUBSTRING`, `REPLACE`, `TRIM`)
- [ ] **`DISTINCT`**
- [ ] **`COUNT`** (`COUNT(*)` x `COUNT(coluna)` x `COUNT(DISTINCT coluna)`)
- [ ] **`ORDER BY`** (`ASC`/`DESC`, várias colunas)
- [ ] **`LIMIT`** e `OFFSET` (paginação)
- [ ] **Filtros com `WHERE`**: operadores de comparação (`=`, `<>`, `<`, `>`, `<=`, `>=`), **`AND`**, **`OR`**, `NOT`, precedência e parênteses
- [ ] `BETWEEN`, `IN`, `LIKE` (`%`, `_`), `IS NULL` / `IS NOT NULL` (e por que `= NULL` não funciona)
- [ ] Funções numéricas (`ROUND`, `CEIL`, `FLOOR`, `ABS`) e de data (`NOW`, `CURDATE`, `DATE_FORMAT`, `DATEDIFF`, `YEAR`, `MONTH`)
- [ ] `CASE WHEN`
- [ ] `IFNULL` / `COALESCE`
- [ ] Ordem lógica de execução de uma consulta (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT)

### Fontes
- 🧪 [SQLBolt](https://sqlbolt.com/): lições interativas curtas (**faça todas**).
- 🧪 [SQLZoo](https://sqlzoo.net/): tutoriais e exercícios.
- 🧪 [SQL Murder Mystery](https://mystery.knightlab.com/): resolva um crime com SQL.
- 🧪 [Select Star SQL](https://selectstarsql.com/): livro interativo.
- 🌐 [MySQL — Tutorial oficial](https://dev.mysql.com/doc/refman/8.4/en/tutorial.html)
- 🌐 [Banco de dados de exemplo Sakila (MySQL)](https://dev.mysql.com/doc/sakila/en/): locadora de filmes, ótimo para praticar.
- 🌐 [MySQL Workbench — manual](https://dev.mysql.com/doc/workbench/en/)
- 🎥🇧🇷 [Curso de Banco de Dados MySQL — Curso em Vídeo](https://www.cursoemvideo.com/)
- 📘 *Aprendendo SQL* (Learning SQL) — Alan Beaulieu
- 🧪 [HackerRank — SQL](https://www.hackerrank.com/domains/sql) (nível Basic e Easy)

### Exercícios
- [ ] **E3.4.1** Complete o SQLBolt inteiro.
- [ ] **E3.4.2** Suba o MySQL em Docker, conecte o Workbench e importe o banco **Sakila**.
- [ ] **E3.4.3** Sakila — 30 consultas, por exemplo:
  - [ ] Os 10 filmes mais longos, com título e duração.
  - [ ] Clientes cujo sobrenome começa com "S", em ordem alfabética.
  - [ ] Nome completo dos atores em uma coluna só (`CONCAT`).
  - [ ] Quantas classificações indicativas (`rating`) distintas existem.
  - [ ] Filmes com aluguel entre 2.99 e 4.99 **e** duração maior que 120 minutos.
  - [ ] Filmes da classificação `PG` **ou** `G`, que não sejam da década de 1990.
  - [ ] Pagamentos da segunda página (registros 11 a 20), do maior para o menor.
  - [ ] Clientes inativos ou sem e-mail.
  - [ ] Categoria "curto/médio/longo" para cada filme com `CASE`.
- [ ] **E3.4.4** Resolva o SQL Murder Mystery.
- [ ] **E3.4.5** 20 exercícios Basic/Easy do HackerRank SQL.
- [ ] **E3.4.6** Escreva a ordem lógica de execução de 5 consultas suas e explique por que não dá para usar um apelido do `SELECT` no `WHERE`.

### Autoavaliação
1. Qual a diferença entre `COUNT(*)` e `COUNT(coluna)`?
2. Por que `WHERE coluna = NULL` não retorna nada?
3. Qual a precedência entre `AND` e `OR`? Dê um exemplo de bug causado por ela.
4. O que o `DISTINCT` faz com várias colunas?
5. Por que paginação com `OFFSET` fica lenta em tabelas grandes?

---

## Módulo 3.5 — SQL: modelagem de dados e DDL (1,5 semana)

### Conceitos
- [ ] Levantamento de requisitos → modelo conceitual → lógico → físico
- [ ] **Modelo Entidade-Relacionamento**: entidades, atributos, relacionamentos, cardinalidade (1:1, 1:N, N:N), notação pé-de-galinha
- [ ] Tabela associativa para N:N
- [ ] **Normalização**: 1FN, 2FN, 3FN (e FNBC como curiosidade); anomalias de inserção, atualização e exclusão; quando desnormalizar
- [ ] Chaves: primária, estrangeira, candidata, natural x substituta (*surrogate*), composta; `AUTO_INCREMENT` x UUID
- [ ] **DDL**: `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE`, `DROP`, `TRUNCATE`
- [ ] Tipos de dados no MySQL: `INT`, `BIGINT`, `DECIMAL` (dinheiro!), `VARCHAR` x `TEXT`, `CHAR`, `DATE`, `DATETIME` x `TIMESTAMP`, `BOOLEAN`, `ENUM`, `JSON`
- [ ] **Restrições**: `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `PRIMARY KEY`, `FOREIGN KEY` com `ON DELETE`/`ON UPDATE` (`CASCADE`, `RESTRICT`, `SET NULL`)
- [ ] **DML**: `INSERT` (vários registros), `UPDATE` e `DELETE` (sempre com `WHERE`!), `INSERT ... ON DUPLICATE KEY UPDATE`
- [ ] *Charset* e *collation* (`utf8mb4`)
- [ ] Engenharia direta e reversa no Workbench
- [ ] Dados de exemplo (*seeds*)

### Fontes
- 📘 *Projeto de Banco de Dados* — Carlos Alberto Heuser 🇧🇷 (clássico brasileiro sobre modelagem)
- 📘 *Sistemas de Banco de Dados* — Elmasri e Navathe (referência acadêmica)
- 🌐 [MySQL — Data Types](https://dev.mysql.com/doc/refman/8.4/en/data-types.html)
- 🌐 [MySQL — FOREIGN KEY Constraints](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)
- 🌐 [dbdiagram.io](https://dbdiagram.io/) ou [drawSQL](https://drawsql.app/): diagramas a partir de código.
- 🎥🇧🇷 Curso em Vídeo — Banco de Dados MySQL (aulas de modelagem).
- 📘 *SQL Antipatterns* — Bill Karwin (o que **não** fazer)

### Exercícios
- [ ] **E3.5.1** Normalize até a 3FN uma planilha de vendas desnormalizada (crie uma com 15 colunas repetitivas) e documente cada etapa.
- [ ] **E3.5.2** Modele no papel e depois no Workbench o banco da **loja virtual**: clientes, endereços, categorias, produtos, estoque, pedidos, itens do pedido, pagamentos, avaliações.
- [ ] **E3.5.3** Escreva o script DDL completo com todas as restrições e chaves estrangeiras.
- [ ] **E3.5.4** Script de *seed* com pelo menos 20 clientes, 50 produtos e 100 pedidos.
- [ ] **E3.5.5** Teste as regras `ON DELETE CASCADE` x `RESTRICT` x `SET NULL`, apagando um cliente com pedidos em cada configuração.
- [ ] **E3.5.6** Mostre com exemplo por que dinheiro deve ser `DECIMAL` e não `FLOAT`.
- [ ] **E3.5.7** Modele o banco do **Marcelo IT Services**: clientes (PF/PJ), endereços, equipamentos do cliente, técnicos, serviços, orçamentos, ordens de serviço, itens da OS, agendamentos, histórico de status.
- [ ] **E3.5.8** Leia 5 capítulos do *SQL Antipatterns* e encontre (ou provoque) cada antipadrão no seu modelo.

### Autoavaliação
1. Explique 1FN, 2FN e 3FN com um exemplo.
2. Como representar um relacionamento N:N em tabelas?
3. Chave natural (CPF) ou substituta (id)? Prós e contras.
4. Quando desnormalizar é uma boa ideia?
5. Qual a diferença entre `DELETE`, `TRUNCATE` e `DROP`?

### Projeto 3.5 — Banco de dados da loja virtual (projeto do README)
**Entregáveis:** diagrama ER (imagem + arquivo do Workbench), script DDL, script de seed, documento explicando as decisões de modelagem (tipos, chaves, normalização, regras de exclusão). Tudo subindo automaticamente com Docker Compose.

---

## Módulo 3.6 — SQL: joins, agregações, subconsultas e transações (1,5 semana)

### Conceitos
- [ ] **JOINs**: `INNER`, `LEFT`, `RIGHT`, `CROSS`, *self join*; `FULL OUTER` (e como simular no MySQL); `ON` x `USING`
- [ ] Armadilhas: linhas duplicadas, filtro no `WHERE` que transforma `LEFT JOIN` em `INNER`
- [ ] **Agregações**: `SUM`, `AVG`, `MIN`, `MAX`, `COUNT`; `GROUP BY`; **`HAVING`** x `WHERE`
- [ ] `GROUP_CONCAT`; `WITH ROLLUP`
- [ ] **Subconsultas**: no `WHERE` (`IN`, `EXISTS`), no `FROM` (tabela derivada), no `SELECT` (escalar), correlacionadas
- [ ] **CTEs** (`WITH`) e CTEs recursivas
- [ ] **Funções de janela**: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM() OVER (PARTITION BY ... ORDER BY ...)`
- [ ] `UNION` x `UNION ALL`
- [ ] **Views**
- [ ] **Transações**: `START TRANSACTION`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`; propriedades **ACID**
- [ ] Níveis de isolamento e anomalias (leitura suja, leitura não repetível, leitura fantasma); *locks*; *deadlocks*
- [ ] *Stored procedures*, *functions* e *triggers* (saber que existem, quando usar e quando evitar)
- [ ] Usuários e permissões (`CREATE USER`, `GRANT`, `REVOKE`), princípio do menor privilégio

### Fontes
- 🧪 SQLBolt (lições de JOIN e agregação) · SQLZoo (*SELECT within SELECT*, *SUM and COUNT*, *JOIN*, *More JOIN*)
- 🧪 [PostgreSQL Exercises](https://pgexercises.com/): excelentes exercícios de joins, agregação e recursão (em Postgres; quase tudo funciona no MySQL).
- 🧪 [LeetCode — SQL 50](https://leetcode.com/studyplan/top-sql-50/)
- 🌐 [Visual explanation of SQL joins (diagramas)](https://joins.spathon.com/)
- 🌐 [Mode — SQL Tutorial (Intermediate e Advanced)](https://mode.com/sql-tutorial/)
- 🌐 [MySQL — Window Functions](https://dev.mysql.com/doc/refman/8.4/en/window-functions.html) e [Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html)
- 🎥 Full Stack Open — parte 13 (em PostgreSQL + Sequelize).

### Exercícios
- [ ] **E3.6.1** Sakila — 25 consultas com JOIN, por exemplo:
  - [ ] Filmes e suas categorias.
  - [ ] Clientes que **nunca** alugaram (com `LEFT JOIN ... IS NULL` e com `NOT EXISTS`).
  - [ ] Faturamento por loja e por mês.
  - [ ] Os 5 atores com mais filmes.
  - [ ] Categorias com mais de 60 filmes (`HAVING`).
  - [ ] Para cada cliente, o valor do aluguel mais caro que ele fez (subconsulta correlacionada **e** função de janela).
  - [ ] Ranking dos 3 filmes mais alugados **por categoria** (`ROW_NUMBER` + `PARTITION BY`).
  - [ ] Crescimento do faturamento mês a mês (`LAG`).
- [ ] **E3.6.2** Loja virtual — 20 relatórios: produtos mais vendidos, clientes com maior gasto, ticket médio por mês, produtos sem venda, estoque abaixo do mínimo, pedidos com valor acima da média, taxa de recompra.
- [ ] **E3.6.3** Todos os exercícios de *Joins*, *Aggregation* e *Recursive* do PostgreSQL Exercises.
- [ ] **E3.6.4** 30 problemas do LeetCode SQL 50.
- [ ] **E3.6.5** CTE recursiva: árvore de categorias (categoria → subcategoria → …) com o caminho completo.
- [ ] **E3.6.6** Transação de **finalizar pedido**: baixar estoque, criar pedido e itens, registrar pagamento. Force um erro no meio e confirme o `ROLLBACK`.
- [ ] **E3.6.7** Abra dois terminais e reproduza: leitura não repetível em `READ COMMITTED`, e um *deadlock*. Explique o que aconteceu.
- [ ] **E3.6.8** Crie uma view `vw_resumo_pedidos` e um usuário que só tem permissão de `SELECT` nessa view.
- [ ] **E3.6.9** Crie um *trigger* que grava o histórico de mudança de status de uma OS. Depois escreva prós e contras de fazer isso no banco ou na aplicação.

### Autoavaliação
1. Qual a diferença entre `WHERE` e `HAVING`?
2. Por que um `LEFT JOIN` pode "virar" `INNER JOIN` sem você perceber?
3. Quando usar subconsulta, CTE ou JOIN?
4. O que é uma função de janela e o que ela faz que o `GROUP BY` não faz?
5. Explique cada letra do ACID.
6. O que é um *deadlock* e como o banco resolve?

---

## Módulo 3.7 — SQL: índices, performance e recursos avançados (1 semana)

### Conceitos
- [ ] Como o banco guarda os dados: páginas, árvore B+ (B+tree), índice clusterizado (InnoDB) x secundário
- [ ] **Índices**: quando criar, índices compostos e ordem das colunas (prefixo mais à esquerda), índice de cobertura, índice único
- [ ] Custo dos índices (escrita, espaço)
- [ ] **`EXPLAIN`** e `EXPLAIN ANALYZE`: tipos de acesso (`ALL`, `index`, `range`, `ref`, `eq_ref`, `const`), `rows`, `Extra`
- [ ] Consultas que não usam índice (função na coluna, `LIKE '%x'`, conversão de tipo)
- [ ] Problema N+1 (visto de novo no ORM)
- [ ] Paginação por cursor (*keyset*) x `OFFSET`
- [ ] Backup e restauração (`mysqldump`), replicação (visão geral)
- [ ] PostgreSQL: principais diferenças em relação ao MySQL (vale conhecer os dois)

### Fontes
- 🌐 [Use The Index, Luke!](https://use-the-index-luke.com/pt): guia gratuito sobre índices e performance SQL (tem versão 🇧🇷 parcial).
- 🌐 [MySQL — Optimization](https://dev.mysql.com/doc/refman/8.4/en/optimization.html) e [EXPLAIN Output Format](https://dev.mysql.com/doc/refman/8.4/en/explain-output.html)
- 📘 *High Performance MySQL* — Silvia Botros e Jeremy Tinley (4ª ed.)
- 🌐 [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)

### Exercícios
- [ ] **E3.7.1** Gere uma tabela de pedidos com **1 milhão** de linhas (script ou procedure). Meça uma consulta por cliente e data sem índice e com índice.
- [ ] **E3.7.2** Crie um índice composto `(cliente_id, data)` e mostre com `EXPLAIN` quais consultas o usam e quais não.
- [ ] **E3.7.3** Encontre 5 consultas que "quebram" o índice e reescreva-as.
- [ ] **E3.7.4** Compare paginação por `OFFSET` e por cursor na página 50.000.
- [ ] **E3.7.5** Faça backup com `mysqldump`, apague o banco e restaure. Automatize com o script de backup da trilha 0.
- [ ] **E3.7.6** Rode o banco da loja também em PostgreSQL e anote as diferenças de sintaxe encontradas.

### Autoavaliação
1. Por que um índice acelera a leitura e atrasa a escrita?
2. Em um índice `(a, b, c)`, uma consulta filtrando só por `b` usa o índice? Por quê?
3. O que significa `type: ALL` no `EXPLAIN`?
4. O que é um índice de cobertura?

---

## Módulo 3.8 — Node.js: fundamentos do runtime (1 semana)

### Conceitos
- [ ] O que é o Node.js: V8 + libuv; *single thread* com I/O não bloqueante; event loop do Node (fases: timers, poll, check…); *thread pool*
- [ ] Módulos: CommonJS (`require`) x ES Modules (`import`); `"type": "module"`
- [ ] Módulos nativos: `fs/promises`, `path`, `os`, `events` (`EventEmitter`), `http`, `crypto`, `url`, `child_process`, `worker_threads`
- [ ] `process`: `argv`, `env`, `exit`, `on('SIGTERM')`; *graceful shutdown*
- [ ] **Streams**: readable, writable, transform, `pipeline`; *backpressure*
- [ ] `Buffer`
- [ ] Criar um servidor HTTP **sem framework** (`http.createServer`)
- [ ] Variáveis de ambiente e configuração (`.env`, `node --env-file`)
- [ ] Executar TypeScript no Node (`tsx`, compilação com `tsc`, suporte nativo a *type stripping* nas versões recentes)
- [ ] Depuração do Node no VS Code; `node --watch`
- [ ] Test runner nativo (`node:test`)
- [ ] Logs estruturados (Pino)

### Fontes
- 🌐 [Node.js — Learn](https://nodejs.org/en/learn): *Getting Started*, *Asynchronous Work* (event loop, `EventEmitter`), *Manipulating Files*, *Command Line*.
- 🌐 [Node.js — The Node.js Event Loop](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- 📘 *Node.js Design Patterns*: capítulos 1 a 6.
- 🎥 Full Stack Open — parte 3.
- 🧪 [NodeSchool — learnyounode](https://github.com/workshopper/learnyounode) (workshop no terminal; antigo, mas ainda útil).

### Exercícios
- [ ] **E3.8.1** CLI em Node que recebe uma pasta (`process.argv`) e lista os arquivos com tamanho, usando `fs/promises`.
- [ ] **E3.8.2** Leia um CSV de 500 MB com **streams**, sem estourar a memória, e calcule o total de uma coluna. Compare o uso de memória com `readFile`.
- [ ] **E3.8.3** Servidor HTTP puro com rotas `GET /servicos`, `GET /servicos/:id`, `POST /servicos` (lendo o corpo da requisição na mão) e 404.
- [ ] **E3.8.4** `EventEmitter` para eventos de OS (`os:criada`, `os:concluida`) com dois ouvintes (log e "e-mail").
- [ ] **E3.8.5** *Graceful shutdown*: ao receber `SIGTERM`, parar de aceitar conexões e terminar as requisições em andamento.
- [ ] **E3.8.6** Mostre uma operação síncrona pesada bloqueando o servidor e resolva com `worker_threads`.
- [ ] **E3.8.7** Gere hash SHA-256 de arquivos com `crypto` e verifique integridade (ligue com o script de backup).
- [ ] **E3.8.8** Escreva testes com `node:test` para o E3.8.1.

### Autoavaliação
1. Se o Node é *single-threaded*, como ele atende milhares de conexões?
2. O que bloqueia o event loop? Dê 3 exemplos.
3. Qual a diferença entre `process.nextTick` e `setImmediate`?
4. O que é *backpressure* em streams?
5. CommonJS x ES Modules: diferenças práticas.

---

## Módulo 3.9 — Express e arquitetura em camadas (1,5 semana)

### Conceitos
- [ ] Express: `app`, rotas, `req` (`params`, `query`, `body`, `headers`), `res` (`status`, `json`, `send`), `Router`
- [ ] **Middlewares**: o que são, a ordem importa, `next()`, middlewares de terceiros (`cors`, `helmet`, `morgan`/`pino-http`, `express.json`), middleware de erro (4 argumentos)
- [ ] Tratamento centralizado de erros; erros de domínio x erros HTTP; async errors (Express 5 trata Promises rejeitadas)
- [ ] **Validação** de entrada com Zod (ou Joi) em middleware
- [ ] **Arquitetura em camadas — Model, Service, Controller (MSC)**: responsabilidade de cada camada, fluxo da requisição, injeção de dependências simples
- [ ] Estrutura de pastas por camada x por funcionalidade (*feature*)
- [ ] Configuração por ambiente
- [ ] Documentação da API com Swagger UI a partir do OpenAPI
- [ ] Alternativas: Fastify, NestJS, Hono (visão geral)

### Fontes
- 🌐 [Express — Guia](https://expressjs.com/pt-br/) 🇧🇷: *Roteamento*, *Escrevendo middlewares*, *Usando middlewares*, *Tratamento de erros*, *Boas práticas de produção: segurança e performance*.
- 🌐 Node.js Best Practices: seções *Project Architecture* e *Error Handling*.
- 🎥 Full Stack Open — partes 3 e 4.
- 🌐 [Fastify](https://fastify.dev/) · [NestJS](https://docs.nestjs.com/)

### Exercícios
- [ ] **E3.9.1** Reescreva o servidor HTTP puro do módulo 3.8 com Express. Compare.
- [ ] **E3.9.2** Middleware de log que mede o tempo de cada requisição.
- [ ] **E3.9.3** Middleware de validação genérico: `validar(schemaZod)` para `body`, `params` e `query`.
- [ ] **E3.9.4** Middleware de erro que converte `NaoEncontradoError`, `ValidacaoError` e `ConflitoError` em 404, 422 e 409 no formato *Problem Details*.
- [ ] **E3.9.5** CRUD de serviços em memória em **camadas**: `routes → controller → service → model`. O controller não deve conhecer o banco; o model não deve conhecer HTTP.
- [ ] **E3.9.6** Regra de negócio no service: não permitir excluir um serviço que esteja em alguma OS aberta.
- [ ] **E3.9.7** Paginação, filtros e ordenação por query string (`?page=2&limit=20&sort=-preco&categoria=redes`).
- [ ] **E3.9.8** Swagger UI servindo a documentação em `/docs`.
- [ ] **E3.9.9** Configure `helmet`, `cors` (liberando só a origem do seu front) e limite de tamanho do corpo.

### Autoavaliação
1. O que é um middleware e por que a ordem de registro importa?
2. Qual a responsabilidade de cada camada no MSC? Onde fica a regra de negócio?
3. Por que o controller não deve acessar o banco diretamente?
4. Como o Express identifica um middleware de erro?

---

## Módulo 3.10 — ORM, migrations e acesso a dados (1,5 semana)

### Conceitos
- [ ] Acesso ao banco em três níveis: driver puro (`mysql2`) → *query builder* (Knex) → **ORM** (Sequelize, Prisma, Drizzle, TypeORM)
- [ ] **SQL injection** e consultas parametrizadas (*prepared statements*)
- [ ] *Pool* de conexões
- [ ] ORM: modelos, tipos, validações, **associações** (`hasOne`, `hasMany`, `belongsTo`, `belongsToMany`), *eager loading* x *lazy loading*
- [ ] **Migrations** e **seeders**: versionamento do esquema do banco
- [ ] Transações pelo ORM
- [ ] Problema **N+1** e como detectar (logs de SQL)
- [ ] Quando o ORM atrapalha e é melhor escrever SQL
- [ ] Padrão Repository (preparação para a trilha 5)

### Fontes
- 🌐 [mysql2 — docs](https://sidorares.github.io/node-mysql2/docs)
- 🌐 [Sequelize — docs](https://sequelize.org/docs/v6/): *Core Concepts*, *Associations*, *Migrations*, *Transactions*.
- 🌐 [Prisma — docs](https://www.prisma.io/docs): *Getting started*, *Prisma schema*, *Relations*, *Migrate*.
- 🌐 [Drizzle ORM — docs](https://orm.drizzle.team/docs/overview)
- 🌐 [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- 🎥 Full Stack Open — parte 13 (Sequelize, migrations, associações).

### Exercícios
- [ ] **E3.10.1** Conecte a API de serviços ao MySQL com `mysql2` e SQL puro parametrizado.
- [ ] **E3.10.2** Demonstre um **SQL injection** em uma rota vulnerável (concatenando string) e corrija com parâmetros.
- [ ] **E3.10.3** Migre o acesso a dados para um ORM (Sequelize **ou** Prisma) com migrations e seeders.
- [ ] **E3.10.4** Modele as associações da loja: cliente 1:N pedidos, pedido N:N produtos (via itens), produto N:1 categoria.
- [ ] **E3.10.5** Rota `GET /pedidos` que traz cliente e itens: mostre o problema **N+1** no log de SQL e corrija com *eager loading*.
- [ ] **E3.10.6** Transação no ORM para criar pedido + itens + baixa de estoque.
- [ ] **E3.10.7** Crie uma migration que adiciona uma coluna com valor padrão e outra que a remove (*rollback*).
- [ ] **E3.10.8** Escreva um relatório complexo (função de janela) com SQL puro dentro do projeto que usa ORM.
- [ ] **E3.10.9** Crie uma interface `ProdutoRepository` e duas implementações: uma com ORM e uma em memória (para testes).

### Autoavaliação
1. O que é SQL injection e como consultas parametrizadas o evitam?
2. O que é o problema N+1?
3. Por que usar migrations em vez de alterar o banco à mão?
4. Quando é melhor não usar ORM?
5. O que é um *pool* de conexões e por que usá-lo?

---

## Módulo 3.11 — Autenticação, autorização e segurança de APIs (1,5 semana)

### Conceitos
- [ ] Autenticação (quem é você) x autorização (o que pode fazer)
- [ ] **Senhas**: nunca guardar em texto puro; *hash* com sal usando **bcrypt** ou **argon2**; por que não MD5/SHA-256 puro
- [ ] Sessões com cookie x **tokens JWT**: vantagens e desvantagens
- [ ] **JWT**: estrutura (header, payload, assinatura), assinatura HS256 x RS256, `exp`, `iat`, `sub`; o payload **não é criptografado**
- [ ] *Access token* de curta duração + *refresh token*; revogação; onde guardar no front (cookie `HttpOnly` x memória)
- [ ] Middleware de autenticação e de autorização por papel (RBAC: cliente, técnico, admin)
- [ ] Autorização por recurso (um cliente só vê as próprias OS) e a falha **IDOR/BOLA**
- [ ] OAuth 2.0 e OpenID Connect (visão geral: "Entrar com Google")
- [ ] **OWASP API Security Top 10**
- [ ] Proteções: *rate limiting*, `helmet`, CORS restritivo, validação de entrada, limite de tamanho de payload, mensagens de erro sem detalhes internos, logs sem dados sensíveis
- [ ] Segredos: `.env` fora do Git, gerenciadores de segredos
- [ ] LGPD: dados pessoais, minimização, consentimento, direito de exclusão
- [ ] Recuperação de senha segura (token de uso único com validade)

### Fontes
- 🌐 [jwt.io — Introduction](https://jwt.io/introduction)
- 🌐 [OWASP — Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- 🌐 [OWASP — Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) e [JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) (exemplos em Java, mas os conceitos valem para qualquer linguagem)
- 🌐 [OWASP API Security Top 10](https://owasp.org/API-Security/)
- 🌐 [Express — Boas práticas de segurança](https://expressjs.com/pt-br/advanced/best-practice-security.html) 🇧🇷
- 🌐 [OAuth 2.0 simplificado — Aaron Parecki](https://aaronparecki.com/oauth-2-simplified/)
- 🌐 [Guia LGPD — gov.br](https://www.gov.br/anpd/pt-br) 🇧🇷
- 🎥 Full Stack Open — parte 4 (autenticação com token).

### Exercícios
- [ ] **E3.11.1** Cadastro de usuário com senha em **bcrypt**. Mostre no banco que é impossível ver a senha.
- [ ] **E3.11.2** Meça o tempo de `bcrypt` com custo 10, 12 e 14 e explique o que o custo significa.
- [ ] **E3.11.3** Login que retorna um JWT; decodifique o token no jwt.io e veja que o payload é legível.
- [ ] **E3.11.4** Middleware `autenticar` (valida o token) e `autorizar('admin', 'tecnico')`.
- [ ] **E3.11.5** Demonstre uma falha **IDOR** (cliente A lê a OS do cliente B trocando o id na URL) e corrija.
- [ ] **E3.11.6** *Refresh token* em cookie `HttpOnly`, `Secure`, `SameSite=Strict`, com rotação e logout que o revoga.
- [ ] **E3.11.7** *Rate limiting* no login (5 tentativas por minuto por IP) e resposta 429.
- [ ] **E3.11.8** Fluxo de "esqueci minha senha" com token de uso único, validade de 30 minutos, armazenado em hash.
- [ ] **E3.11.9** Revise sua API com o OWASP API Security Top 10 e escreva, para cada item, se ela está protegida e como.
- [ ] **E3.11.10** Garanta que nenhum log grava senha, token ou CPF completo.

### Autoavaliação
1. Por que usar bcrypt/argon2 em vez de SHA-256 para senhas?
2. O conteúdo de um JWT é secreto? O que garante a assinatura?
3. Como invalidar um JWT antes de ele expirar?
4. O que é IDOR (ou BOLA)? Por que é a falha número 1 do OWASP API Top 10?
5. Onde guardar o token no front-end, e quais os riscos de cada opção?
6. Qual a diferença entre autenticação e autorização?

---

## Módulo 3.12 — Testes no back-end (1,5 semana)

### Conceitos
- [ ] Testes unitários do *service* com dublês do *model*/repositório (*stubs*, *mocks*, *spies*)
- [ ] Ferramentas: **Vitest** ou **Jest**; ecossistema clássico **Mocha + Chai + Sinon** (muito usado em cursos e empresas; vale conhecer)
- [ ] Testes de integração da API com **Supertest** (requisição HTTP real contra o app)
- [ ] Banco de teste: banco separado em Docker, **Testcontainers**, limpeza entre testes, *fixtures* e *factories*
- [ ] Testes de contrato com o schema OpenAPI (visão geral)
- [ ] Cobertura
- [ ] TDD no back-end
- [ ] Testes de carga (visão geral): **k6** ou autocannon

### Fontes
- 🌐 [Supertest](https://github.com/ladjs/supertest)
- 🌐 [Mocha](https://mochajs.org/) · [Chai](https://www.chaijs.com/) · [Sinon](https://sinonjs.org/)
- 🌐 [Testcontainers for Node.js](https://node.testcontainers.org/)
- 🌐 [JavaScript Testing Best Practices — Yoni Goldberg](https://github.com/goldbergyoni/javascript-testing-best-practices): seção de back-end.
- 🌐 [Node.js testing best practices (goldbergyoni)](https://github.com/goldbergyoni/nodejs-testing-best-practices)
- 🌐 [k6 — docs](https://grafana.com/docs/k6/latest/)
- 🎥 Full Stack Open — parte 4 (testando o back-end).

### Exercícios
- [ ] **E3.12.1** Testes unitários de todos os *services* da API de serviços com o repositório em memória (sem banco).
- [ ] **E3.12.2** Os mesmos testes com *stubs* do Sinon (ou `vi.fn()`), para praticar as duas abordagens.
- [ ] **E3.12.3** Testes de integração com Supertest para todas as rotas: sucesso, validação (422), não encontrado (404), não autorizado (401/403).
- [ ] **E3.12.4** Suba um MySQL de teste com Testcontainers e rode as migrations antes dos testes.
- [ ] **E3.12.5** *Factory* de dados de teste (ex.: `criarCliente({ tipo: 'PJ' })`).
- [ ] **E3.12.6** Teste do fluxo de autenticação completo: cadastro → login → acesso a rota protegida → refresh → logout.
- [ ] **E3.12.7** Implemente uma funcionalidade nova com TDD (ex.: cupom de desconto no pedido).
- [ ] **E3.12.8** Teste de carga com k6 na rota de listagem e descubra quantas requisições por segundo ela aguenta. Adicione um índice e compare.

### Autoavaliação
1. Qual a diferença entre um teste unitário do *service* e um teste de integração da rota?
2. Por que não usar o banco de desenvolvimento nos testes?
3. O que é uma *factory* de testes?
4. Quando um mock deixa o teste sem valor?

---

## Módulo 3.13 — Tópicos extras: NoSQL, cache, filas, tempo real (1 semana)

### Conceitos
- [ ] NoSQL: documentos (**MongoDB**), chave-valor (**Redis**), colunar, grafos; quando usar cada um
- [ ] MongoDB: coleções, documentos, consultas, agregações, Mongoose
- [ ] **Cache** com Redis: *cache-aside*, TTL, invalidação ("há só duas coisas difíceis em computação…")
- [ ] **Filas e trabalhos em segundo plano**: BullMQ (Redis) ou RabbitMQ; envio de e-mail assíncrono
- [ ] Tempo real: WebSocket (Socket.IO) e Server-Sent Events
- [ ] Upload de arquivos (Multer) e armazenamento (disco x S3/MinIO)
- [ ] Envio de e-mail (Nodemailer + Mailpit para testes locais)
- [ ] GraphQL (visão geral; aprofundado na trilha 5)

### Fontes
- 🌐 [MongoDB University](https://learn.mongodb.com/) (cursos gratuitos)
- 🌐 [Redis — docs](https://redis.io/docs/latest/) e [Redis University](https://university.redis.io/)
- 🌐 [BullMQ — docs](https://docs.bullmq.io/)
- 🌐 [Socket.IO — docs](https://socket.io/docs/v4/)
- 🌐 [MinIO](https://min.io/docs/minio/container/index.html)
- 🌐 [Mailpit](https://mailpit.axllent.org/)

### Exercícios
- [ ] **E3.13.1** Cache com Redis na listagem de serviços (TTL de 5 min, invalidação ao alterar um serviço). Meça a diferença com k6.
- [ ] **E3.13.2** Fila com BullMQ: ao concluir uma OS, enfileirar o envio de e-mail ao cliente (capturado no Mailpit).
- [ ] **E3.13.3** Painel do técnico recebendo em tempo real (WebSocket ou SSE) quando uma nova OS é criada.
- [ ] **E3.13.4** Upload de fotos do equipamento na OS, guardadas no MinIO (compatível com S3).
- [ ] **E3.13.5** Modele o catálogo de produtos da loja em MongoDB e compare com o modelo relacional.

---

## Módulo 3.14 — Projetos finais (2–3 semanas)

### Projeto A — API da loja virtual (projeto do README)
**Requisitos funcionais:**
- Cadastro e login de clientes (bcrypt + JWT com refresh token); papel admin.
- CRUD de categorias e produtos (só admin), com upload de imagem.
- Catálogo público com busca, filtros, ordenação e paginação.
- Carrinho e **finalização de pedido em transação** (estoque, pedido, itens, pagamento simulado).
- Cliente vê só os próprios pedidos; admin vê todos e muda o status.
- Relatórios para o admin: vendas por período, produtos mais vendidos, clientes que mais compram.
- E-mail de confirmação de pedido por fila.

**Requisitos técnicos:**
- Node.js + TypeScript + Express, arquitetura em camadas (routes → controllers → services → repositories/models).
- MySQL com migrations e seeders via ORM; pelo menos um relatório em SQL puro com função de janela.
- Validação com Zod; erros no formato *Problem Details*.
- Segurança: `helmet`, CORS restritivo, *rate limiting*, sem IDOR, checklist do OWASP API Top 10 documentado.
- Testes: unitários dos *services* (≥ 80% de cobertura) e de integração com Supertest + Testcontainers.
- Documentação OpenAPI com Swagger UI.
- Tudo sobe com um único `docker compose up` (API, MySQL, Redis, Mailpit, Adminer).
- Dockerfile *multi-stage*, usuário não-root, `HEALTHCHECK`.
- CI no GitHub Actions: lint, testes, build da imagem.
- README com diagrama ER, arquitetura, como rodar e decisões tomadas.

### Projeto B — API do Marcelo IT Services
Back-end do projeto integrador, ligado à SPA da trilha 2 (trocar o MSW pela API real):
- Clientes PF/PJ, endereços e equipamentos.
- Catálogo de serviços e orçamentos (converter um orçamento aprovado em OS).
- Ordens de serviço com histórico de status, fotos, técnico responsável, peças usadas.
- Agenda de visitas (evitar conflito de horário do técnico, sem visitas em feriados).
- Papéis: cliente, técnico, admin.
- Notificações por e-mail em fila; painel em tempo real.

### Mini-projetos extras (escolha pelo menos 2)
- [ ] Encurtador de URLs com estatísticas de cliques (Redis)
- [ ] API de blog com comentários aninhados (CTE recursiva)
- [ ] Chat em tempo real com salas (Socket.IO)
- [ ] Clone simplificado de uma API de pagamentos com idempotência (`Idempotency-Key`)
- [ ] Desafios de back-end de processos seletivos (ex.: repositórios públicos de "backend challenges" no GitHub)

---

## ✅ Checklist de conclusão da Trilha 3
- [ ] SQLBolt, SQL Murder Mystery e PostgreSQL Exercises (Joins/Aggregation) completos
- [ ] 30+ problemas do LeetCode SQL 50
- [ ] Banco da loja modelado, normalizado e documentado
- [ ] API da loja completa, testada, documentada e em Docker Compose
- [ ] API Marcelo IT ligada à SPA
- [ ] Autoavaliações com ≥ 80% de acerto
- [ ] Artigo/post resumindo a trilha
