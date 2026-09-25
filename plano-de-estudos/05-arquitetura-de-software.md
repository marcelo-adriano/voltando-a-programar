# Trilha 5 — Arquitetura de Software

> **Objetivo da trilha:** pensar como arquiteto: identificar as características que importam em um sistema, avaliar *trade-offs*, escolher estilos arquiteturais, modelar domínios complexos, projetar sistemas distribuídos e documentar decisões.
>
> "Tudo em arquitetura de software é um *trade-off*. Se você acha que encontrou algo que não é, provavelmente ainda não identificou o *trade-off*." — Richards e Ford

**Duração:** 10–12 semanas · **Pré-requisitos:** Trilhas 3 e 4 (você precisa ter construído sistemas para entender por que arquitetura importa)

| Módulo | Tema | Duração |
|--------|------|---------|
| 5.1 | Fundamentos: o que é arquitetura, características e *trade-offs* | 1 semana |
| 5.2 | Design de código: coesão, acoplamento, *clean code* e refatoração | 1,5 semana |
| 5.3 | Documentando arquitetura: C4, ADRs e diagramas | 3 dias |
| 5.4 | Estilos arquiteturais: camadas, hexagonal, *clean*, monolito modular | 1,5 semana |
| 5.5 | Domain-Driven Design (DDD) | 1,5 semana |
| 5.6 | Integração e APIs: REST, GraphQL, gRPC, mensageria | 1 semana |
| 5.7 | Arquiteturas distribuídas: microsserviços e orientação a eventos | 1,5 semana |
| 5.8 | Dados em sistemas distribuídos | 1 semana |
| 5.9 | *System design*: escalabilidade, disponibilidade e desempenho | 1,5 semana |
| 5.10 | Resiliência, observabilidade e qualidade | 1 semana |
| 5.11 | Projetos finais | 2 semanas |

### Fontes principais da trilha
- 📘 *Fundamentos da Arquitetura de Software* (Fundamentals of Software Architecture) — Mark Richards e Neal Ford. **Livro guia da trilha.**
- 📘 *Software Architecture: The Hard Parts* — Ford, Richards, Sadalage e Dehghani
- 📘 *Designing Data-Intensive Applications* — Martin Kleppmann. **O livro mais importante sobre sistemas de dados.**
- 📘 *A Philosophy of Software Design* — John Ousterhout
- 📘 *Arquitetura Limpa* — Robert C. Martin
- 📘 [*Software Engineering at Google* (gratuito)](https://abseil.io/resources/swe-book)
- 🌐 [martinfowler.com](https://martinfowler.com/): artigos de referência sobre arquitetura, refatoração, microsserviços e padrões.
- 🌐 [microservices.io — Chris Richardson](https://microservices.io/): catálogo de padrões de microsserviços.
- 🌐 [roadmap.sh — Software Architect](https://roadmap.sh/software-architect) e [System Design](https://roadmap.sh/system-design)
- 🎥🇧🇷 [Full Cycle](https://www.youtube.com/@FullCycle) e [Rodrigo Branas](https://www.youtube.com/@RodrigoBranas): arquitetura, Clean Architecture, DDD.
- 🎥 [ByteByteGo — Alex Xu (YouTube)](https://www.youtube.com/@ByteByteGo)

---

## Módulo 5.1 — Fundamentos: o que é arquitetura, características e *trade-offs* (1 semana)

### Conceitos
- [ ] O que é arquitetura de software (estrutura, características, decisões, princípios de design)
- [ ] Papel do arquiteto; arquitetura x design
- [ ] **Características arquiteturais** ("-idades"): disponibilidade, escalabilidade, elasticidade, desempenho, confiabilidade, segurança, manutenibilidade, testabilidade, implantabilidade, observabilidade, custo
- [ ] Identificar características a partir de requisitos e do domínio; características explícitas x implícitas
- [ ] Medir e governar características: *fitness functions*
- [ ] **Quantum arquitetural** e acoplamento
- [ ] Pensamento arquitetural: *trade-offs*, amplitude técnica, "a primeira lei da arquitetura de software"
- [ ] Lei de Conway e *Inverse Conway Maneuver*
- [ ] Arquitetura evolutiva

### Fontes
- 📘 *Fundamentos da Arquitetura de Software*: capítulos 1 a 7.
- 📘 *Building Evolutionary Architectures* — Ford, Parsons, Kua e Sadalage (2ª ed.)
- 🌐 [Martin Fowler — Software Architecture Guide](https://martinfowler.com/architecture/)
- 🌐 [Martin Fowler — Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html)
- 🌐 [ISO/IEC 25010 — atributos de qualidade de software (visão geral)](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010)

### Exercícios
- [ ] **E5.1.1** Para 3 sistemas conhecidos (um e-commerce na Black Friday, um sistema bancário, o site da Marcelo IT), liste as 5 características mais importantes e justifique.
- [ ] **E5.1.2** Faça 2 **katas de arquitetura** (há listas públicas de katas, como as do livro *Fundamentos da Arquitetura de Software* e as [Architectural Katas](https://www.architecturalkatas.com/)): leia os requisitos e identifique as características arquiteturais.
- [ ] **E5.1.3** Escreva uma *fitness function* automatizada: um teste que falha se a camada de domínio importar algo da camada de infraestrutura (em Python com `import-linter`; em TS com `dependency-cruiser`).
- [ ] **E5.1.4** Analise um projeto seu e escreva: quais características ele privilegia e quais sacrifica.

### Autoavaliação
1. Qual a diferença entre um requisito funcional e uma característica arquitetural?
2. Por que não dá para maximizar todas as características ao mesmo tempo?
3. O que é uma *fitness function*?
4. O que diz a Lei de Conway?

---

## Módulo 5.2 — Design de código: coesão, acoplamento, *clean code* e refatoração (1,5 semana)

### Conceitos
- [ ] **Complexidade** como inimiga principal (Ousterhout): dependências e obscuridade
- [ ] **Módulos profundos** x rasos; esconder informação
- [ ] **Coesão** (tipos) e **acoplamento** (tipos); conascência
- [ ] Nomes, funções pequenas, comentários úteis, tratamento de erros, formatação
- [ ] *Code smells*: método longo, classe grande, obsessão por primitivos, lista de parâmetros longa, inveja de funcionalidade, cirurgia com rifle, código duplicado, comentários que explicam código ruim
- [ ] **Refatoração**: definição, refatorações do catálogo (extrair função, renomear, mover método, substituir condicional por polimorfismo, introduzir objeto de parâmetro…), sempre com testes
- [ ] Trabalhando com código legado: pontos de extensão (*seams*), testes de caracterização
- [ ] Dívida técnica: tipos (quadrante de Fowler) e como negociar com o negócio
- [ ] Code review: o que olhar, como comentar

### Fontes
- 📘 *Refatoração* (Refactoring, 2ª ed.) — Martin Fowler 🇧🇷 (exemplos em JavaScript). **Fonte principal.**
- 📘 *A Philosophy of Software Design* — John Ousterhout
- 📘 *Código Limpo* — Robert C. Martin
- 📘 *Trabalho Eficaz com Código Legado* (Working Effectively with Legacy Code) — Michael Feathers
- 🌐🇧🇷 [Refactoring.Guru — Refatoração e code smells](https://refactoring.guru/pt-br/refactoring)
- 🌐 [Catálogo de refatorações — Martin Fowler](https://refactoring.com/catalog/)
- 🌐 [Martin Fowler — Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html)
- 🌐 [Google — Code Review Developer Guide](https://google.github.io/eng-practices/review/)
- 🧪 [Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) e outros katas de Emily Bache

### Exercícios
- [ ] **E5.2.1** Faça o exemplo do capítulo 1 do *Refatoração* acompanhando passo a passo, com testes.
- [ ] **E5.2.2** Gilded Rose Kata: escreva testes de caracterização primeiro, depois refatore, depois adicione a funcionalidade nova.
- [ ] **E5.2.3** Mais 2 katas de refatoração de Emily Bache (ex.: *Tennis*, *Theatrical Players*, *Trip Service*).
- [ ] **E5.2.4** Encontre 10 *code smells* nos seus projetos das trilhas 1 a 4 e refatore 5 deles.
- [ ] **E5.2.5** Revise um PR de um colega ou de um projeto aberto seguindo o guia de code review do Google.
- [ ] **E5.2.6** Escreva um registro de dívida técnica do projeto integrador (item, impacto, custo, prioridade).

### Autoavaliação
1. O que é um módulo "profundo"?
2. Refatorar sem testes é refatorar?
3. O que é um teste de caracterização?
4. Dê 5 *code smells* e a refatoração que corrige cada um.

---

## Módulo 5.3 — Documentando arquitetura: C4, ADRs e diagramas (3 dias)

### Conceitos
- [ ] **Modelo C4**: Contexto, Contêineres, Componentes, Código
- [ ] **ADR** (*Architecture Decision Record*): contexto, decisão, status, consequências
- [ ] Diagramas como código: **Mermaid**, PlantUML, Structurizr
- [ ] UML útil: diagrama de sequência, de classes, de estados, de implantação
- [ ] RFCs / *design docs*
- [ ] arc42 (modelo de documentação)

### Fontes
- 🌐 [c4model.com](https://c4model.com/)
- 🌐 [ADR — GitHub organization](https://adr.github.io/) e [modelo de Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- 🌐 [Mermaid — docs](https://mermaid.js.org/) (o GitHub renderiza Mermaid em arquivos `.md`)
- 🌐 [arc42](https://arc42.org/)
- 🌐 [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)

### Exercícios
- [ ] **E5.3.1** Diagramas C4 níveis 1, 2 e 3 do sistema Marcelo IT Services em Mermaid, no repositório.
- [ ] **E5.3.2** Escreva 5 ADRs para decisões já tomadas no projeto integrador (ex.: "MySQL em vez de MongoDB", "JWT com refresh token em cookie", "monolito modular em vez de microsserviços").
- [ ] **E5.3.3** Diagrama de sequência do fluxo "cliente aprova orçamento → OS criada → técnico notificado".
- [ ] **E5.3.4** Diagrama de estados da OS.
- [ ] **E5.3.5** Escreva um *design doc* de 2 páginas para uma funcionalidade nova (ex.: portal do cliente).

---

## Módulo 5.4 — Estilos arquiteturais: camadas, hexagonal, *clean*, monolito modular (1,5 semana)

### Conceitos
- [ ] **Arquitetura em camadas** (revisão da trilha 3/4): prós, contras, "sinkhole anti-pattern"
- [ ] **Arquitetura Hexagonal** (*Ports and Adapters*) — Alistair Cockburn: portas de entrada e de saída, adaptadores primários e secundários
- [ ] **Clean Architecture**: entidades, casos de uso, adaptadores de interface, *frameworks & drivers*; a regra da dependência
- [ ] **Onion Architecture**
- [ ] Comparação: o que as três têm em comum (o domínio no centro, independente de infraestrutura)
- [ ] **Monolito modular**: módulos com fronteiras claras, comunicação por interfaces, banco compartilhado x esquemas separados
- [ ] **Microkernel** (plugins)
- [ ] **Pipeline** (*pipes and filters*)
- [ ] **Arquitetura baseada em serviços** (*service-based*): meio-termo entre monolito e microsserviços
- [ ] **Vertical Slice Architecture**
- [ ] Como escolher: tamanho do time, domínio, características exigidas

### Fontes
- 📘 *Fundamentos da Arquitetura de Software*: capítulos 9 a 17 (um capítulo por estilo).
- 🌐 [Alistair Cockburn — Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- 🌐 [Robert C. Martin — The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- 📘 *Arquitetura Limpa*: partes V e VI.
- 📘 *Architecture Patterns with Python* (cosmicpython.com): parte I inteira.
- 🌐 [Kamil Grzybek — Modular Monolith Primer](https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer)
- 🌐 [Shopify Engineering — Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)
- 🎥🇧🇷 Rodrigo Branas — vídeos sobre Clean Architecture e Hexagonal.

### Exercícios
- [ ] **E5.4.1** Desenhe a mesma funcionalidade ("agendar visita técnica") nas arquiteturas em camadas, hexagonal e *clean*. Compare as dependências.
- [ ] **E5.4.2** Refatore a API da loja (trilha 3) para **hexagonal**: domínio sem nenhuma importação de Express ou ORM; portas `PedidoRepository`, `GatewayPagamento`, `Notificador`; adaptadores HTTP, MySQL, em memória.
- [ ] **E5.4.3** Prove o desacoplamento: rode os casos de uso com adaptadores em memória nos testes, e troque o adaptador HTTP por um de CLI sem tocar no domínio.
- [ ] **E5.4.4** Organize o projeto integrador como **monolito modular** (módulos: clientes, catálogo, orçamentos, ordens, agenda, notificações) e crie uma *fitness function* que impede um módulo de acessar o banco de outro.
- [ ] **E5.4.5** Implemente um mini-sistema de plugins (microkernel): relatórios que podem ser adicionados sem alterar o núcleo.
- [ ] **E5.4.6** Escreva uma ADR justificando o estilo escolhido para o projeto integrador.

### Autoavaliação
1. Qual problema a arquitetura hexagonal resolve?
2. O que são portas e adaptadores? Dê exemplos de cada tipo.
3. Qual é a "regra da dependência" da Clean Architecture?
4. Por que um monolito modular costuma ser um bom ponto de partida?
5. Quando uma arquitetura em camadas simples é suficiente?

---

## Módulo 5.5 — Domain-Driven Design (DDD) (1,5 semana)

### Conceitos
**DDD estratégico**
- [ ] Domínio, subdomínios (*core*, de suporte, genérico)
- [ ] **Linguagem ubíqua**
- [ ] **Contextos delimitados** (*bounded contexts*) e **mapa de contextos** (relacionamentos: parceria, cliente-fornecedor, conformista, camada anticorrupção, *open host service*, *shared kernel*)
- [ ] **Event Storming** (descoberta colaborativa do domínio)

**DDD tático**
- [ ] **Entidades** x **objetos de valor** (*value objects*)
- [ ] **Agregados** e raiz do agregado; regras de consistência; tamanho dos agregados
- [ ] **Repositórios** (um por agregado)
- [ ] **Serviços de domínio** x serviços de aplicação
- [ ] **Eventos de domínio**
- [ ] Fábricas
- [ ] Modelo anêmico x modelo rico

### Fontes
- 📘 *Aprendendo Domain-Driven Design* (Learning DDD) — Vlad Khononov: **o mais acessível para começar**.
- 📘 *Domain-Driven Design Distilled* — Vaughn Vernon (curto e direto)
- 📘 *Domain-Driven Design* — Eric Evans (o "livro azul", original e denso)
- 📘 *Implementando Domain-Driven Design* — Vaughn Vernon (o "livro vermelho", prático)
- 🌐 [DDD Crew (GitHub)](https://github.com/ddd-crew): modelos de *bounded context canvas*, *context mapping*, *Event Storming*.
- 🌐 [Martin Fowler — Bounded Context](https://martinfowler.com/bliki/BoundedContext.html), [Value Object](https://martinfowler.com/bliki/ValueObject.html), [Anemic Domain Model](https://martinfowler.com/bliki/AnemicDomainModel.html)
- 🌐 [Alberto Brandolini — Event Storming](https://www.eventstorming.com/)
- 🎥🇧🇷 Full Cycle e Rodrigo Branas — conteúdos sobre DDD.

### Exercícios
- [ ] **E5.5.1** Faça um *Event Storming* (sozinho ou com alguém, com post-its ou no [Miro](https://miro.com/)/Excalidraw) do negócio Marcelo IT: do primeiro contato do cliente até o pagamento.
- [ ] **E5.5.2** Identifique os subdomínios (qual é o *core*?) e os contextos delimitados; desenhe o mapa de contextos.
- [ ] **E5.5.3** Monte um glossário da linguagem ubíqua (o que é "OS", "orçamento", "visita", "chamado"…) e ajuste o código para usar esses termos.
- [ ] **E5.5.4** Implemente objetos de valor: `Dinheiro`, `Cpf`, `Cnpj`, `Email`, `Endereco`, `PeriodoDeAtendimento`, imutáveis e autovalidados.
- [ ] **E5.5.5** Modele o agregado `OrdemDeServico` (raiz) com itens e histórico, garantindo as invariantes (não adicionar item a OS concluída; total sempre consistente).
- [ ] **E5.5.6** Publique eventos de domínio (`OrdemConcluida`, `OrcamentoAprovado`) e trate-os em outro módulo.
- [ ] **E5.5.7** Crie uma **camada anticorrupção** para integrar com uma API externa "feia" (ex.: um ERP fictício com nomes em inglês e formatos estranhos).
- [ ] **E5.5.8** Transforme um modelo anêmico (classes só com getters/setters e toda a lógica nos services) em um modelo rico.

### Autoavaliação
1. O que é um contexto delimitado? Por que "Cliente" pode significar coisas diferentes em contextos diferentes?
2. Qual a diferença entre entidade e objeto de valor?
3. Por que os agregados devem ser pequenos?
4. O que é uma camada anticorrupção?
5. Quando DDD **não** vale a pena?

---

## Módulo 5.6 — Integração e APIs: REST, GraphQL, gRPC, mensageria (1 semana)

### Conceitos
- [ ] Comunicação **síncrona** x **assíncrona**
- [ ] REST (revisão), versionamento, paginação, idempotência (`Idempotency-Key`), HATEOAS
- [ ] **GraphQL**: schema, queries, mutations, resolvers, problema N+1 e DataLoader; quando usar
- [ ] **gRPC** e Protocol Buffers: contratos, streaming; quando usar
- [ ] **Webhooks**: assinatura (HMAC), novas tentativas, idempotência
- [ ] **Mensageria**: filas x tópicos (*pub/sub*); **RabbitMQ** (exchanges, filas, *bindings*, ack, DLQ) e **Kafka** (tópicos, partições, *consumer groups*, *offsets*, retenção)
- [ ] Garantias de entrega: no máximo uma vez, pelo menos uma vez, exatamente uma vez (e por que é difícil)
- [ ] Consumidores idempotentes
- [ ] **API Gateway** e **BFF** (*Backend for Frontend*)
- [ ] *Contract testing* (Pact)
- [ ] AsyncAPI

### Fontes
- 📘 *Enterprise Integration Patterns* — Gregor Hohpe e Bobby Woolf · 🌐 [enterpriseintegrationpatterns.com](https://www.enterpriseintegrationpatterns.com/)
- 🌐 [GraphQL — Learn](https://graphql.org/learn/)
- 🌐 [gRPC — Introduction](https://grpc.io/docs/what-is-grpc/introduction/)
- 🌐 [RabbitMQ — Tutorials](https://www.rabbitmq.com/tutorials) (os 6 tutoriais em Python ou JavaScript)
- 🌐 [Apache Kafka — Introduction](https://kafka.apache.org/intro) e [Confluent Developer — cursos gratuitos](https://developer.confluent.io/courses/)
- 🌐 [Pact — docs](https://docs.pact.io/)
- 🌐 [Stripe — Idempotent requests](https://docs.stripe.com/api/idempotent_requests) (exemplo real de API bem desenhada)

### Exercícios
- [ ] **E5.6.1** Faça os 6 tutoriais do RabbitMQ.
- [ ] **E5.6.2** Implemente `Idempotency-Key` na rota de criação de pedido da API da loja.
- [ ] **E5.6.3** Endpoint de webhook que recebe notificações de "pagamento aprovado" com validação de assinatura HMAC e tratamento de duplicatas.
- [ ] **E5.6.4** Exponha o catálogo da loja também em GraphQL e resolva o N+1 com DataLoader.
- [ ] **E5.6.5** Serviço gRPC simples (ex.: cálculo de frete) chamado pela API.
- [ ] **E5.6.6** Suba um Kafka (ou Redpanda) no Docker, produza eventos de pedidos e consuma com dois *consumer groups* diferentes.
- [ ] **E5.6.7** Fila com DLQ: mensagens que falham 3 vezes vão para a fila de "mortas" e geram alerta.
- [ ] **E5.6.8** Tabela comparativa: REST x GraphQL x gRPC x mensageria (quando usar cada um).

### Autoavaliação
1. Quando preferir comunicação assíncrona?
2. Por que "exatamente uma vez" é tão difícil? Como consumidores idempotentes ajudam?
3. Qual a diferença entre uma fila e um tópico?
4. Quais problemas o GraphQL resolve e quais cria?

---

## Módulo 5.7 — Arquiteturas distribuídas: microsserviços e orientação a eventos (1,5 semana)

### Conceitos
- [ ] **As falácias da computação distribuída**
- [ ] **Microsserviços**: definição, características, *database per service*, autonomia de times; custos (complexidade operacional, consistência, testes, observabilidade)
- [ ] Monolito distribuído (o pior dos mundos)
- [ ] Como decompor: por capacidade de negócio, por subdomínio (DDD), granularidade (desintegradores e integradores)
- [ ] Migração de monolito: **Strangler Fig**, *branch by abstraction*
- [ ] **Arquitetura orientada a eventos (EDA)**: topologias *broker* x *mediator*; notificação de evento x transferência de estado por evento
- [ ] **Sagas**: coreografia x orquestração; transações compensatórias
- [ ] **Transactional Outbox** e *Change Data Capture* (CDC)
- [ ] **CQRS** e **Event Sourcing**: o que são, quando valem a pena (raramente)
- [ ] *Service mesh* (visão geral)
- [ ] Serverless (visão geral)

### Fontes
- 📘 *Criando Microsserviços* (Building Microservices, 2ª ed.) — Sam Newman
- 📘 *Monolith to Microservices* — Sam Newman
- 📘 *Microservices Patterns* — Chris Richardson · 🌐 [microservices.io](https://microservices.io/patterns/)
- 📘 *Software Architecture: The Hard Parts* (decomposição, granularidade, sagas)
- 🌐 [Martin Fowler — Microservices](https://martinfowler.com/articles/microservices.html) e [Microservice Premium](https://martinfowler.com/bliki/MicroservicePremium.html)
- 🌐 [Martin Fowler — Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html)
- 🌐 [Martin Fowler — What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html)
- 🌐 [Martin Fowler — CQRS](https://martinfowler.com/bliki/CQRS.html) e [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)
- 🌐 [Fallacies of distributed computing (Wikipédia)](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)

### Exercícios
- [ ] **E5.7.1** Liste as 8 falácias e, para cada uma, um problema real que ela causaria no projeto integrador se fosse dividido em microsserviços.
- [ ] **E5.7.2** Extraia o módulo de **notificações** do monolito modular para um serviço separado que consome eventos do RabbitMQ (Strangler Fig).
- [ ] **E5.7.3** Implemente o **Transactional Outbox**: ao concluir a OS, grave o evento na tabela `outbox` na mesma transação; um processo publica os eventos pendentes.
- [ ] **E5.7.4** **Saga** de pedido na loja (reservar estoque → cobrar → confirmar), com compensações quando o pagamento falha. Faça uma versão coreografada e uma orquestrada.
- [ ] **E5.7.5** CQRS simples: modelo de escrita normalizado e modelo de leitura desnormalizado (atualizado por eventos) para o painel de relatórios.
- [ ] **E5.7.6** Event Sourcing de uma conta bancária (eventos `Depositado`, `Sacado`), reconstruindo o saldo e criando *snapshots*.
- [ ] **E5.7.7** Escreva uma ADR: "por que o projeto integrador **não** usa microsserviços (ainda)", com os critérios que mudariam essa decisão.

### Autoavaliação
1. Quais são os principais custos dos microsserviços?
2. O que é um "monolito distribuído"?
3. Qual a diferença entre saga coreografada e orquestrada?
4. Que problema o Transactional Outbox resolve?
5. Quando CQRS e Event Sourcing valem a pena?

---

## Módulo 5.8 — Dados em sistemas distribuídos (1 semana)

### Conceitos
- [ ] Modelos de dados: relacional, documento, grafo, colunar, séries temporais; persistência poliglota
- [ ] Mecanismos de armazenamento: B-tree x LSM-tree
- [ ] **Replicação**: líder-seguidor, multi-líder, sem líder; replicação síncrona x assíncrona; atraso de replicação
- [ ] **Particionamento** (*sharding*): por faixa x por hash; *hot spots*; rebalanceamento
- [ ] **Teorema CAP** e **PACELC**; consistência forte x eventual
- [ ] Transações distribuídas; *two-phase commit* e por que evitar
- [ ] Consenso (Raft, só a ideia)
- [ ] Relógios e ordenação de eventos
- [ ] Processamento em lote x em fluxo (*batch* x *stream*)

### Fontes
- 📘 *Designing Data-Intensive Applications*: partes I e II (capítulos 1 a 9). **Fonte principal.**
- 🌐 [The Raft Consensus Algorithm (visualização)](https://raft.github.io/)
- 🌐 [Jepsen](https://jepsen.io/analyses): análises de consistência de bancos reais (leitura avançada).

### Exercícios
- [ ] **E5.8.1** Configure replicação primário-réplica do MySQL em Docker Compose. Grave no primário, leia na réplica e observe o atraso.
- [ ] **E5.8.2** Simule o problema "ler a própria escrita" (usuário salva e não vê a alteração porque leu da réplica) e implemente uma solução.
- [ ] **E5.8.3** Implemente particionamento por hash de clientes em 3 "bancos" (SQLite) e mostre o problema do rebalanceamento ao adicionar um quarto; depois implemente *consistent hashing*.
- [ ] **E5.8.4** Para 5 sistemas (banco, rede social, carrinho de compras, estoque, contador de visualizações), escolha entre consistência forte ou eventual e justifique.
- [ ] **E5.8.5** Resumo de 1 página de cada capítulo lido do DDIA.

### Autoavaliação
1. O que o teorema CAP realmente diz (e o que ele não diz)?
2. Qual a diferença entre replicação e particionamento?
3. O que é consistência eventual? Dê um exemplo aceitável e um inaceitável.
4. Por que *two-phase commit* é evitado em microsserviços?

---

## Módulo 5.9 — *System design*: escalabilidade, disponibilidade e desempenho (1,5 semana)

### Conceitos
- [ ] Escalabilidade vertical x horizontal; serviços sem estado
- [ ] **Balanceadores de carga** (camada 4 x 7, algoritmos, *health checks*)
- [ ] **Cache** em todas as camadas: navegador, CDN, proxy reverso, aplicação, banco; estratégias (*cache-aside*, *write-through*, *write-behind*); invalidação; *thundering herd*
- [ ] **CDN**
- [ ] Filas para desacoplar e absorver picos
- [ ] **Rate limiting** (token bucket, leaky bucket, janela deslizante)
- [ ] Disponibilidade: "noves" (99,9% = ~8,7 h fora do ar por ano), redundância, *failover*, multi-região
- [ ] Latência x throughput; percentis (p50, p95, p99)
- [ ] Estimativas de "guardanapo" (*back-of-the-envelope*)
- [ ] Busca (Elasticsearch/OpenSearch), armazenamento de objetos (S3), IDs distribuídos
- [ ] Roteiro de uma entrevista de *system design*: requisitos → estimativas → API → modelo de dados → desenho de alto nível → aprofundamento → gargalos

### Fontes
- 🌐 [The System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer) 🇧🇷 (tem tradução): **fonte principal gratuita**.
- 📘 *System Design Interview — An Insider's Guide* (volumes 1 e 2) — Alex Xu
- 🌐 [ByteByteGo — blog e newsletter](https://blog.bytebytego.com/)
- 🌐 [High Scalability](https://highscalability.com/): estudos de caso de arquiteturas reais.
- 🌐 Blogs de engenharia: [Netflix](https://netflixtechblog.com/), [Uber](https://www.uber.com/blog/engineering/), [Discord](https://discord.com/category/engineering), [Nubank](https://building.nubank.com/) 🇧🇷, [Mercado Livre](https://medium.com/mercadolibre-tech) 🇧🇷, [iFood](https://medium.com/ifood-tech) 🇧🇷
- 🌐 [AWS Well-Architected Framework](https://docs.aws.amazon.com/pt_br/wellarchitected/latest/framework/welcome.html) 🇧🇷

### Exercícios
- [ ] **E5.9.1** Estimativas: quantos servidores, quanto armazenamento e quanta banda para um sistema com 1 milhão de usuários ativos por dia enviando 10 fotos cada?
- [ ] **E5.9.2** Faça por escrito (com diagrama) o *system design* de: encurtador de URL, sistema de notificações, feed de rede social, chat, *rate limiter*, sistema de reservas.
- [ ] **E5.9.3** Coloque 3 réplicas da API atrás de um Nginx como balanceador em Docker Compose e derrube uma durante um teste de carga com k6.
- [ ] **E5.9.4** Implemente um *rate limiter* com *token bucket* em Redis.
- [ ] **E5.9.5** Meça p50, p95 e p99 da API da loja com k6, identifique o gargalo e corrija.
- [ ] **E5.9.6** Leia 5 estudos de caso de blogs de engenharia e resuma: problema, solução, *trade-offs*.
- [ ] **E5.9.7** Simule 3 entrevistas de *system design* com a IA como entrevistadora (veja o prompt no README do plano).

### Autoavaliação
1. Por que serviços sem estado escalam horizontalmente com mais facilidade?
2. Qual a diferença entre latência e throughput?
3. Por que olhar o p99 e não só a média?
4. Quanto tempo fora do ar por mês permite um SLA de 99,9%?
5. O que é *thundering herd* e como mitigar?

---

## Módulo 5.10 — Resiliência, observabilidade e qualidade (1 semana)

### Conceitos
- [ ] **Padrões de estabilidade**: *timeout*, *retry* com *backoff* exponencial e *jitter*, **circuit breaker**, *bulkhead*, *fallback*, degradação graciosa, *load shedding*
- [ ] Antipadrões de estabilidade: reações em cadeia, falhas em cascata, integração sem timeout
- [ ] **Observabilidade**: logs estruturados, métricas (RED e USE), *traces* distribuídos; **OpenTelemetry**; IDs de correlação
- [ ] Engenharia do caos (Chaos Engineering)
- [ ] Estratégia de testes em sistemas distribuídos: pirâmide, testes de contrato, testes E2E com moderação, testes em produção (*feature flags*, *canary*)
- [ ] **The Twelve-Factor App**
- [ ] Segurança como característica arquitetural (ponte com a trilha 7): *zero trust*, defesa em profundidade, menor privilégio

### Fontes
- 📘 *Release It!* (2ª ed.) — Michael Nygard: **o livro sobre sistemas que sobrevivem à produção**.
- 🌐 [The Twelve-Factor App](https://12factor.net/pt_br/) 🇧🇷
- 🌐 [Martin Fowler — Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html)
- 🌐 [AWS Builders' Library — Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- 🌐 [OpenTelemetry — docs](https://opentelemetry.io/docs/)
- 🌐 [Principles of Chaos Engineering](https://principlesofchaos.org/)
- 📘 *Observability Engineering* — Majors, Fong-Jones e Miranda

### Exercícios
- [ ] **E5.10.1** Implemente um *circuit breaker* do zero (estados fechado, aberto, semiaberto) com testes.
- [ ] **E5.10.2** Na integração com a API de CEP (ou com o serviço de notificações), adicione timeout, *retry* com *backoff* + *jitter* e *circuit breaker*; simule a queda do serviço e mostre a degradação graciosa.
- [ ] **E5.10.3** Instrumente a API com OpenTelemetry e veja um *trace* passando por API → fila → serviço de notificações no Jaeger.
- [ ] **E5.10.4** Revise o projeto integrador contra os 12 fatores e corrija o que estiver fora.
- [ ] **E5.10.5** Experimento de caos: derrube o Redis, o RabbitMQ e o banco (um de cada vez) e documente o comportamento do sistema e as melhorias necessárias.

### Autoavaliação
1. Por que *retries* sem *backoff* podem derrubar um sistema?
2. Explique os 3 estados de um *circuit breaker*.
3. Quais são os 3 pilares da observabilidade?
4. Cite 5 dos 12 fatores e o motivo de cada um.

---

## Módulo 5.11 — Projetos finais (2 semanas)

### Projeto A — Marcelo IT Services com arquitetura documentada
- Monolito modular com arquitetura hexagonal em cada módulo e DDD tático no módulo de Ordens de Serviço.
- Serviço de notificações extraído, orientado a eventos (RabbitMQ), com Outbox e consumidor idempotente.
- Resiliência nas integrações externas (CEP, feriados, e-mail).
- Observabilidade com OpenTelemetry.
- *Fitness functions* no CI (regras de dependência entre camadas e módulos).
- Documentação: C4 (níveis 1–3), 10+ ADRs, mapa de contextos, glossário da linguagem ubíqua, diagramas de sequência e de estados.

### Projeto B — Portfólio de *system design*
Um diretório `05-arquitetura/system-design/` com 6 desenhos completos (requisitos, estimativas, API, modelo de dados, diagrama, gargalos e *trade-offs*), escritos como se fossem para uma entrevista.

### Projeto C — Kata de arquitetura completo
Escolha um kata e produza: características arquiteturais priorizadas, estilo escolhido com justificativa, C4, ADRs e riscos.

---

## ✅ Checklist de conclusão da Trilha 5
- [ ] *Fundamentos da Arquitetura de Software* lido
- [ ] *Designing Data-Intensive Applications*: partes I e II lidas, com resumos
- [ ] Gilded Rose + 2 katas de refatoração
- [ ] Projeto integrador refatorado para hexagonal + monolito modular
- [ ] 10+ ADRs e diagramas C4 no repositório
- [ ] 6 *system designs* documentados
- [ ] Autoavaliações com ≥ 80% de acerto
- [ ] Artigo/post sobre uma decisão arquitetural que você tomou e seus *trade-offs*
