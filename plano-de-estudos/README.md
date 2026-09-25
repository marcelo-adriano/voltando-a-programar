# Plano de Estudos — Voltando a Programar

Este diretório é o **mapa completo** dos estudos. O `README.md` da raiz diz *o que* vou estudar; aqui está *como*, *com quais fontes*, *quais exercícios*, *como me testar* e *quais projetos entregar*.

> **Regra de ouro:** a IA é minha tutora, não minha digitadora. Posso pedir explicações, dicas, revisões e perguntas de fixação. **Não posso** pedir para ela escrever o código de um exercício que ainda não resolvi sozinho.

---

## Índice das trilhas

| # | Trilha | Arquivo | Duração estimada* |
|---|--------|---------|-------------------|
| 0 | Fundamentos: aprender a aprender, terminal, Linux, Git, redes básicas | [00-fundamentos.md](./00-fundamentos.md) | 4–6 semanas |
| 1 | Básico de Desenvolvimento Web (HTML, CSS, JavaScript, testes) | [01-web-basico.md](./01-web-basico.md) | 12–16 semanas |
| 2 | Front-end com TypeScript e React | [02-frontend-react.md](./02-frontend-react.md) | 10–14 semanas |
| 3 | Back-end com Docker, SQL e Node.js | [03-backend-node-sql.md](./03-backend-node-sql.md) | 12–16 semanas |
| 4 | Ciência da Computação com Python | [04-python-ciencia-da-computacao.md](./04-python-ciencia-da-computacao.md) | 14–18 semanas |
| 5 | Arquitetura de Software | [05-arquitetura-de-software.md](./05-arquitetura-de-software.md) | 10–12 semanas |
| 6 | DevOps e SRE | [06-devops.md](./06-devops.md) | 14–18 semanas |
| 7 | Cibersegurança | *(a detalhar — arquivo ainda não criado)* | 14–18 semanas |
| 8 | Certificações Zabbix (repositório futuro) | [08-zabbix.md](./08-zabbix.md) | 10–14 semanas |
| 9 | Certificações Cisco (repositório futuro) | [09-cisco.md](./09-cisco.md) | 16–24 semanas (CCNA) |

\* Estimativas para **10–12 horas por semana**. Com 20 h/semana, divida por quase dois. Com 5 h/semana, multiplique por dois. O importante é a constância, não a velocidade.

**Projetos da Trybe:** a análise dos 40 projetos que entreguei na turma sd-015-a está em [projetos-trybe.md](./projetos-trybe.md). Cada projeto aparece ligado ao módulo do plano que ele cobre, com uma prioridade para refazer (🔴 🟡 🟢). Quando chegar a um módulo, confira se há um projeto da Trybe relacionado a ele.

---

## 1. Como cada trilha está organizada

Todos os arquivos seguem o mesmo formato, para eu saber sempre onde procurar:

```
Trilha
└── Módulo X.Y — Nome (duração)
    ├── Objetivos        → o que eu devo conseguir FAZER ao final
    ├── Conceitos        → checklist do que estudar
    ├── Fontes           → 📘 livro · 🌐 documentação/site · 🎥 vídeo/curso · 🧪 prática interativa · 🇧🇷 em português
    ├── Exercícios       → lista numerada com caixinhas [ ] para marcar
    ├── Autoavaliação    → perguntas que devo responder SEM consultar nada
    └── Projeto          → requisitos + critérios de aceite + desafios extras
```

As caixinhas `- [ ]` funcionam no GitHub: ao editar o arquivo e trocar por `- [x]`, o progresso fica visível.

### Legenda de fontes

| Ícone | Tipo |
|-------|------|
| 📘 | Livro (gratuito quando indicado) |
| 🌐 | Documentação oficial, artigo, site de referência |
| 🎥 | Vídeo, curso, playlist |
| 🧪 | Prática interativa: jogo, laboratório, juiz online, CTF |
| 🇧🇷 | Conteúdo em português |
| 💲 | Pago (sempre existe alternativa gratuita listada) |

---

## 2. Método de estudo

### 2.1 O ciclo semanal

Cada semana segue o ciclo **Estudar → Anotar → Praticar → Testar → Construir → Ensinar**:

| Etapa | O que fazer | % do tempo |
|-------|-------------|-----------|
| **Estudar** | Ler a fonte principal ou assistir às aulas do módulo. Uma fonte principal por vez; as outras são consulta. | 25% |
| **Anotar** | Escrever com as próprias palavras em `anotacoes/` (ver estrutura abaixo). Criar cartões no Anki. | 10% |
| **Praticar** | Fazer os exercícios do módulo **sem IA e sem copiar**. Travou 30 min? Pedir uma **dica** (não a solução). | 35% |
| **Testar** | Responder a autoavaliação de cabeça. Errou? Volte ao conceito. | 10% |
| **Construir** | Avançar no projeto do módulo. | 15% |
| **Ensinar** | Escrever um "TIL" (Today I Learned) ou explicar o conceito em voz alta (técnica Feynman). | 5% |

### 2.2 Técnicas que funcionam (com base em pesquisa sobre aprendizagem)

1. **Recuperação ativa (active recall):** fechar o material e tentar lembrar. Reler é a técnica **menos** eficaz.
2. **Repetição espaçada:** usar o [Anki](https://apps.ankiweb.net/) todo dia (10–15 min). Um cartão por conceito, pergunta curta, resposta curta.
3. **Intercalação:** misturar tipos de exercício (ex.: não fazer 20 exercícios de `map` seguidos; alternar `map`, `filter`, `reduce`).
4. **Técnica Feynman:** explicar o conceito como se fosse para uma criança. Onde a explicação trava é onde está a lacuna.
5. **Pomodoro:** 25 min de foco + 5 min de pausa. Celular em outro cômodo.
6. **Dificuldade desejável:** se o exercício está fácil demais, você não está aprendendo. O desconforto é o sinal de que o cérebro está trabalhando.
7. **Projetos acima de tutoriais:** o "inferno dos tutoriais" é assistir a tudo e não conseguir fazer nada sozinho. Para cada hora de tutorial, pelo menos uma hora de construção própria.

**Fontes sobre como aprender:**
- 🎥🇧🇷 [Aprendendo a Aprender — Barbara Oakley e Terrence Sejnowski (Coursera, gratuito para auditar)](https://www.coursera.org/learn/aprender)
- 📘 *Fixe o Conhecimento* (Make It Stick) — Brown, Roediger e McDaniel
- 📘 *Ultralearning* — Scott Young
- 📘 *Trabalho Focado* (Deep Work) — Cal Newport
- 📘 *The Programmer's Brain* — Felienne Hermans (como o cérebro lê e aprende código)

### 2.3 Como usar IA sem atrapalhar o aprendizado

A IA vai escrever muito código no seu trabalho futuro. Por isso mesmo você precisa entender o que ela escreve, para revisar, corrigir e decidir. Use estes prompts:

| Situação | Prompt |
|----------|--------|
| Entender um conceito | "Explique **closures** em JavaScript para um iniciante, com uma analogia. Depois me faça 5 perguntas para ver se entendi. Não mostre as respostas até eu responder." |
| Travado num exercício | "Estou fazendo este exercício: [enunciado]. Meu código: [código]. **Não me dê a solução.** Me dê só uma dica sobre onde está o problema." |
| Revisão de código | "Revise meu código como um desenvolvedor sênior. Aponte problemas de legibilidade, bugs e boas práticas, **mas não reescreva** o código. Eu vou corrigir." |
| Gerar exercícios | "Crie 10 exercícios progressivos sobre `Array.prototype.reduce`, do mais fácil ao mais difícil, sem soluções." |
| Simular prova | "Faça um simulado de 20 questões de múltipla escolha sobre VLANs e trunking no nível CCNA. Uma questão por vez. Corrija e explique após cada resposta." |
| Entrevista técnica | "Simule uma entrevista técnica para desenvolvedor júnior back-end Node.js. Faça uma pergunta de cada vez e avalie minha resposta." |
| Verificar entendimento | "Vou explicar o que é o event loop. Corrija os erros conceituais da minha explicação: [explicação]." |

**Proibido durante o aprendizado:** "Resolva este exercício", "Faça este projeto", autocompletar de código com IA (desligue o Copilot ou similar nos exercícios; pode ligar de novo nos projetos depois que dominar o módulo).

### 2.4 Rotina sugerida (10–12 h/semana)

| Dia | Atividade | Tempo |
|-----|-----------|-------|
| Seg | Estudo do conteúdo novo + Anki | 1h30 |
| Ter | Exercícios | 1h30 |
| Qua | Estudo + exercícios | 1h30 |
| Qui | Exercícios + autoavaliação | 1h30 |
| Sex | Descanso ou revisão leve (Anki) | 0–30 min |
| Sáb | Projeto do módulo | 3h |
| Dom | Revisão da semana + TIL + planejamento da próxima + Anki | 1h |

---

## 3. Cronograma e trilhas paralelas

Estudar tudo em sequência levaria mais de 2 anos antes de chegar em DevOps e Cisco. Como você já trabalha com serviços de TI (redes, NAS, proxy), a sugestão é **duas trilhas em paralelo**:

- **Trilha principal (≈ 70% do tempo): Desenvolvimento**, a sequência 1 → 2 → 3 → 4 → 5.
- **Trilha secundária (≈ 30% do tempo): Infraestrutura**, a sequência 0 (Linux/redes) → 9 (CCNA) → 8 (Zabbix) → 6 (DevOps) → 7 (Segurança).

A trilha de infraestrutura rende retorno rápido no seu negócio (Marcelo IT Services) e a de desenvolvimento cria a base para automação, DevOps e AppSec.

### Visão em semestres (≈ 12 h/semana)

| Período | Trilha principal (dev) | Trilha secundária (infra) | Marco |
|---------|------------------------|---------------------------|-------|
| Mês 1 | 0 — Fundamentos (tempo integral) | — | Linux, Git e terminal fluentes |
| Meses 2–4 | 1 — HTML, CSS, JavaScript | Redes básicas (0.5) + início CCNA (9.1–9.3) | Site Marcelo IT no ar |
| Meses 5–7 | 1 — JavaScript avançado, testes | CCNA (9.4–9.8) | Lista de tarefas com testes |
| Meses 8–10 | 2 — TypeScript e React | CCNA (9.9–9.12) + simulados | **Prova CCNA** |
| Meses 11–13 | 3 — Docker, SQL | 8 — Zabbix (8.1–8.6) | API da loja virtual (início) |
| Meses 14–16 | 3 — Node.js, autenticação, testes | 8 — Zabbix (8.7–8.12) | **Prova Zabbix ZCU/ZCS** |
| Meses 17–20 | 4 — Python e Ciência da Computação | 6 — DevOps (6.1–6.6) | Pipeline CI/CD do projeto integrador |
| Meses 21–23 | 5 — Arquitetura de Software | 6 — DevOps (6.7–6.13) | Deploy em nuvem com IaC |
| Meses 24–27 | 7 — Cibersegurança (AppSec em foco) | 7 — Cibersegurança (redes/blue team) | **Prova Security+ ou equivalente** |
| Depois | CCNP / CKA / ZCP / OSCP… | | Especialização |

> Esse cronograma é um ponto de partida, não um contrato. Revise-o todo mês (seção 6).

---

## 4. Projeto Integrador: **Marcelo IT Services**

Para não ficar só em projetos soltos, um projeto **cresce junto com os estudos**: o sistema da sua empresa de serviços de TI. O `homepage.html` da raiz é a semente.

| Trilha | Evolução do projeto |
|--------|---------------------|
| 1 — Web básico | Site institucional responsivo e acessível (HTML/CSS). Formulário de contato com validação e consulta de CEP (ViaCEP) em JavaScript. Catálogo de serviços filtrável. |
| 2 — React | Reescrever o site como SPA em React + TypeScript. Área de **orçamento online**: o cliente escolhe serviços e vê o valor estimado. Agenda de visitas técnicas. |
| 3 — Back-end | API REST em Node.js + MySQL: clientes, serviços, orçamentos, **ordens de serviço (OS)**, agendamentos. Login com JWT para o técnico. Tudo em Docker Compose. |
| 4 — Python | Scripts de automação para o dia a dia: inventário de máquinas de clientes, relatório de backup, checagem de sites. Módulo de relatórios em Python (FastAPI). |
| 5 — Arquitetura | Refatorar para arquitetura hexagonal, escrever ADRs e diagramas C4. Serviço de notificações orientado a eventos (e-mail/WhatsApp quando a OS muda de status). |
| 6 — DevOps | CI/CD com GitHub Actions, infraestrutura como código (Terraform), deploy em nuvem ou VPS, Kubernetes (k3s), observabilidade (Prometheus/Grafana). |
| 7 — Segurança | Modelagem de ameaças, pipeline DevSecOps (SAST, SCA, DAST), hardening do servidor, relatório de segurança. |
| 8 — Zabbix | Monitorar a própria infra do sistema **e** oferecer "monitoramento gerenciado" como novo serviço para clientes. |
| 9 — Cisco | Projetar a rede de um cliente fictício (pequena empresa) e documentar no portfólio. |

Ao final, você terá um portfólio real e um produto que pode usar no seu negócio.

---

## 5. Estrutura de repositórios e pastas

### 5.1 Este repositório (`voltando-a-programar`)

Sugestão de organização conforme os estudos avançam (crie as pastas quando chegar em cada trilha):

```
voltando-a-programar/
├── README.md
├── plano-de-estudos/            ← você está aqui
├── anotacoes/                   ← resumos com suas palavras, um arquivo por módulo
│   ├── 01-web-basico/
│   │   ├── 1.2-html-semantico.md
│   │   └── ...
│   └── til/                     ← "Today I Learned", um arquivo por dia/tema
├── 00-fundamentos/
│   ├── exercicios/
│   └── projetos/
├── 01-web-basico/
│   ├── exercicios/
│   │   ├── 1.3-css/
│   │   │   ├── ex01-box-model/
│   │   │   └── ...
│   └── projetos/
│       ├── marcelo-it-site/
│       └── lista-de-tarefas/
├── 02-frontend-react/
├── 03-backend-node-sql/
├── 04-python-cc/
├── 05-arquitetura/
├── 06-devops/
├── 07-ciberseguranca/
└── projeto-integrador/          ← o sistema Marcelo IT Services evoluindo
```

> Projetos grandes (o projeto integrador, a API da loja) podem virar **repositórios próprios** quando crescerem, para parecerem produtos no portfólio.

### 5.2 Repositórios futuros

| Repositório | Conteúdo | Quando criar |
|-------------|----------|--------------|
| `certificacoes-zabbix` | Laboratórios, templates, scripts de API, anotações por objetivo do ZCU/ZCS/ZCP/ZCE, simulados | Ao iniciar a trilha 8 |
| `certificacoes-cisco` | Topologias do Packet Tracer/GNS3/CML, configs, laboratórios por tópico do blueprint, flashcards, scripts de automação | Ao iniciar a trilha 9 |
| `homelab` | Documentação e IaC do seu laboratório caseiro (Proxmox, VMs, rede) | Trilha 6 |

### 5.3 Fluxo Git para os estudos

Você já usa branches e PRs (`planejamento`, `iniciando-o-html`). Continue assim, porque isso também é treino:

1. Uma **issue** por módulo (ex.: "Módulo 1.3 — CSS fundamentos"), com a checklist de exercícios. As das trilhas 0 e 1 já existem: [issues com a etiqueta `trilha-0`](https://github.com/marcelo-adriano/voltando-a-programar/issues?q=label%3Atrilha-0) e [`trilha-1`](https://github.com/marcelo-adriano/voltando-a-programar/issues?q=label%3Atrilha-1), agrupadas nos marcos [Trilha 0](https://github.com/marcelo-adriano/voltando-a-programar/milestone/1) e [Trilha 1](https://github.com/marcelo-adriano/voltando-a-programar/milestone/2).
2. Um **GitHub Project** (quadro Kanban) com colunas `A fazer / Estudando / Revisão / Feito`: o [quadro Voltando a Programar](https://github.com/users/marcelo-adriano/projects/1).
3. Uma **branch** por módulo: `modulo/1.3-css`.
4. Commits pequenos seguindo [Conventional Commits](https://www.conventionalcommits.org/pt-br/): `feat(css): exercício 04 de flexbox`.
5. **PR** ao terminar o módulo. Descreva o que aprendeu e o que teve dificuldade (isso vira diário de bordo).

---

## 6. Acompanhamento e revisões

- **Diário:** ao fim de cada sessão, 3 linhas em `anotacoes/til/`: o que estudei, o que entendi, o que ficou confuso.
- **Revisão semanal (domingo):** marcar caixinhas, atualizar o Kanban, planejar a próxima semana.
- **Revisão mensal:** reler a autoavaliação dos módulos anteriores. Se não souber responder, revisar. Ajustar o cronograma.
- **Revisão de trilha:** ao terminar uma trilha, escrever um artigo (LinkedIn, dev.to, blog próprio) resumindo o que aprendeu e mostrando o projeto.
- **Critério de "módulo concluído":** (1) todos os exercícios obrigatórios feitos, (2) autoavaliação respondida sem consulta com pelo menos 80% de acerto, (3) projeto atende aos critérios de aceite.

---

## 7. Recursos gerais (valem para várias trilhas)

### Roteiros e currículos
- 🌐 [roadmap.sh](https://roadmap.sh/): roteiros visuais para Frontend, Backend, DevOps, Cyber Security, Software Architect, Python, SQL, Docker, Kubernetes e outros. Use para conferir se não esqueceu nenhum tópico.
- 🌐 [The Odin Project](https://www.theodinproject.com/): currículo gratuito e completo de desenvolvimento web, muito baseado em projetos.
- 🌐 [freeCodeCamp](https://www.freecodecamp.org/): certificações gratuitas (Responsive Web Design, JavaScript, Back End, Python, Relational Database…).
- 🌐 [OSSU — Open Source Society University](https://github.com/ossu/computer-science): currículo de Ciência da Computação equivalente a uma graduação, só com materiais gratuitos.
- 🌐 [Teach Yourself Computer Science](https://teachyourselfcs.com/): os 9 assuntos de CC que todo engenheiro deveria estudar, com o melhor livro e o melhor curso de cada.
- 🎥 [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu/): terminal, Git, editores, scripts, depuração.

### Canais e cursos em português 🇧🇷
- 🎥🇧🇷 [Curso em Vídeo (Gustavo Guanabara)](https://www.cursoemvideo.com/): HTML5/CSS3, JavaScript, Python, Git/GitHub, Algoritmos, Redes. Gratuito e muito didático para a base.
- 🎥🇧🇷 [Rocketseat](https://www.rocketseat.com.br/): conteúdo gratuito no YouTube sobre JS, React, Node; formações pagas 💲.
- 🎥🇧🇷 [LINUXtips (Jeferson Fernando)](https://www.youtube.com/@LINUXtips): Linux, Docker, Kubernetes, DevOps.
- 🎥🇧🇷 [Full Cycle](https://www.youtube.com/@FullCycle): arquitetura, DDD, microsserviços, Kubernetes (curso completo pago 💲).
- 🎥🇧🇷 [Filipe Deschamps](https://www.youtube.com/@FilipeDeschamps): curso.dev e conteúdo sobre carreira e desenvolvimento web.
- 🎥🇧🇷 [Fabio Akita](https://www.youtube.com/@Akitando): fundamentos de computação, Linux, redes, carreira (vídeos longos e densos).
- 🎥🇧🇷 [Mente Binária](https://www.mentebinaria.com.br/): computação de baixo nível, engenharia reversa, segurança (gratuito).

### Prática contínua
- 🧪 [Exercism](https://exercism.org/): exercícios com mentoria humana gratuita (JS, TS, Python, Bash, SQL…).
- 🧪 [Codewars](https://www.codewars.com/): desafios curtos ("katas") por nível.
- 🧪🇧🇷 [Beecrowd](https://judge.beecrowd.com/) (antigo URI Online Judge): juiz online brasileiro, problemas em português.
- 🧪 [LeetCode](https://leetcode.com/) e [NeetCode](https://neetcode.io/roadmap): algoritmos e estruturas de dados.
- 🧪 [Frontend Mentor](https://www.frontendmentor.io/): desafios de front-end com design pronto.

### Inglês técnico
Boa parte das melhores fontes está em inglês. Estratégia:
- Documentação: use o tradutor do navegador no começo, mas **leia o original ao lado**.
- Vídeos: legenda em inglês (não em português) para treinar o ouvido.
- Monte um glossário no Anki com termos técnicos (*deploy*, *rollback*, *throughput*, *latency*...).
- 🎥 [BBC Learning English](https://www.bbc.co.uk/learningenglish) e 🧪 [Duolingo](https://www.duolingo.com/) (15 min/dia) para a base.

---

## 8. Mapa de certificações sugerido

```
                         ┌─────────────────────────── Infraestrutura / Redes ──────────────────────────┐
                         │  CCNA 200-301 ──► CCNA Automation ──► CCNP Enterprise (ENCOR + ENARSI)        │
                         │                   (antigo DevNet)                                            │
                         │  Zabbix ZCU ──► ZCS ──► ZCP ──► ZCE                                          │
                         └──────────────────────────────────────────────────────────────────────────────┘
                         ┌─────────────────────────── DevOps / Cloud ──────────────────────────────────┐
                         │  LFCS ou LPIC-1 ──► AWS Cloud Practitioner ──► AWS SAA                       │
                         │                 └─► Terraform Associate ──► CKAD / CKA                       │
                         └──────────────────────────────────────────────────────────────────────────────┘
                         ┌─────────────────────────── Segurança ───────────────────────────────────────┐
                         │  ISC2 CC ──► CompTIA Security+ ──► CCNA Cybersecurity / CySA+ / BTL1          │
                         │                                └─► eJPT ──► OSCP                             │
                         └──────────────────────────────────────────────────────────────────────────────┘
```

Detalhes de cada certificação (conteúdo, custo aproximado, preparação) estão nas trilhas 6, 7, 8 e 9. Programas e versões de provas mudam; **sempre confira o site oficial** antes de marcar a prova.
