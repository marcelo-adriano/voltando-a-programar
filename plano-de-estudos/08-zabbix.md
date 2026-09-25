# Trilha 8 — Certificações Zabbix (plano para o repositório `certificacoes-zabbix`)

> **Objetivo da trilha:** dominar o Zabbix para monitorar infraestrutura, redes, aplicações e serviços, e conquistar as certificações oficiais. Além da certificação, isso pode virar um **novo serviço** da Marcelo IT: *monitoramento gerenciado* para clientes.

**Duração:** 10–14 semanas (até o nível ZCS) · **Pré-requisitos:** Trilha 0 (Linux, redes), módulo 3.2 (Docker). Ajudam: SQL (trilha 3), Python (trilha 4), redes Cisco (trilha 9), módulo 6.11 (observabilidade).

---

## 1. As certificações oficiais

As certificações Zabbix estão atreladas a **treinamentos oficiais** (dados pela Zabbix ou por parceiros autorizados). O exame é feito ao fim do treinamento. Os níveis são:

| Nível | Nome | Foco | Duração do treinamento | Pré-requisito |
|-------|------|------|------------------------|---------------|
| 1 | **ZCU** — Zabbix Certified User | Usar a interface: visualizar, filtrar e interpretar dados e problemas; conceitos básicos | 1 dia (online) | Nenhum |
| 2 | **ZCS** — Zabbix Certified Specialist | Instalar, configurar e manter o Zabbix do zero; coletar métricas por vários métodos; detectar problemas; notificar | 5 dias | Nenhum (ZCU recomendado) |
| 3 | **ZCP** — Zabbix Certified Professional | Automatizar e escalar em infraestrutura distribuída: proxies, descoberta automática (LLD, *network discovery*, autorregistro), técnicas avançadas | 3 dias | ZCS |
| 4 | **ZCE** — Zabbix Certified Expert | Alta disponibilidade, segurança da instalação, otimização de desempenho, processos internos, integração via API | 5 dias | ZCP |

Há também exames de **upgrade** para atualizar a certificação para a versão LTS nova sem refazer o curso inteiro.

**Sobre versões:** as certificações seguem as versões **LTS** do Zabbix. A 7.0 LTS é a base estável atual; a **8.0 LTS** estava em fase beta em meados de 2026 e já existem treinamentos oficiais para ela. Quando for se inscrever, escolha a LTS mais recente disponível.

> Preços, datas, turmas em português e parceiros no Brasil: consulte sempre o [site oficial de treinamentos](https://www.zabbix.com/training) antes de planejar o investimento.

**Fontes oficiais sobre as certificações:**
- 🌐 [Zabbix — Training](https://www.zabbix.com/training)
- 🌐 [Zabbix Certified User — exame](https://www.zabbix.com/exam_zcu)
- 🌐 [Zabbix Certified Specialist (ZCS)](https://www.zabbix.com/training_specialist)
- 🌐 [Zabbix Certified Professional (ZCP)](https://www.zabbix.com/training_professional)
- 🌐 [Zabbix — Life Cycle and Release Policy](https://www.zabbix.com/life_cycle_and_release_policy) (datas de suporte de cada versão)
- 🌐 [Zabbix — Roadmap](https://www.zabbix.com/roadmap)

### Estratégia sugerida
1. Estude por conta própria seguindo os módulos abaixo (**8.1 a 8.8 cobrem o conteúdo do ZCU e do ZCS**).
2. Faça o **ZCU** (curto e barato) para validar a base.
3. Faça o treinamento **ZCS** já com bastante prática. Você vai aproveitar muito mais o curso.
4. Monte a oferta de monitoramento para clientes.
5. Depois de alguns meses operando, siga para **ZCP** (módulos 8.9 a 8.11) e **ZCE** (módulos 8.12 a 8.14).

---

## 2. Estrutura do repositório `certificacoes-zabbix`

```
certificacoes-zabbix/
├── README.md                 ← progresso, certificações obtidas, índice
├── laboratorio/
│   ├── compose.yaml          ← Zabbix server + frontend + banco + agentes de teste
│   ├── terraform/            ← VMs do laboratório no Proxmox (opcional)
│   └── ansible/              ← instalação de agentes nos hosts
├── anotacoes/
│   ├── zcu/                  ← um arquivo por tópico
│   ├── zcs/
│   ├── zcp/
│   └── zce/
├── templates/                ← templates próprios exportados (YAML)
├── scripts/
│   ├── api/                  ← scripts Python usando a API (zabbix_utils)
│   ├── externos/             ← external checks e UserParameters
│   └── media-types/          ← webhooks de notificação (Telegram, WhatsApp…)
├── dashboards/
├── exercicios/               ← um diretório por módulo, com o passo a passo
└── simulados/                ← perguntas de revisão por tema
```

---

## 3. Fontes principais da trilha

- 🌐 [Documentação oficial do Zabbix](https://www.zabbix.com/documentation/current/pt/manual) 🇧🇷 (parte do manual tem tradução). **Fonte principal**: leia o manual da versão que você vai certificar.
- 📘 [*Zabbix 7 IT Infrastructure Monitoring Cookbook* (3ª ed.) — Nathan Liefting e Brian van Baekel (Packt)](https://www.packtpub.com/en-us/product/zabbix-7-it-infrastructure-monitoring-cookbook-9781801078320) e o [repositório de código do livro](https://github.com/PacktPublishing/Zabbix-7-IT-Infrastructure-Monitoring-Cookbook).
- 🌐 [Zabbix Blog](https://blog.zabbix.com/): artigos técnicos oficiais.
- 🎥 [Canal oficial do Zabbix no YouTube](https://www.youtube.com/@ZabbixCompany): webinars, *Zabbix Summit*, tutoriais.
- 🌐 [Zabbix Integrations](https://www.zabbix.com/integrations): templates e integrações oficiais.
- 🌐 [Zabbix Community Templates (GitHub)](https://github.com/zabbix/community-templates)
- 🌐 [Fórum oficial do Zabbix](https://www.zabbix.com/forum/)
- 🌐 [zabbix_utils — biblioteca Python oficial para a API](https://github.com/zabbix/python-zabbix-utils)
- 🎥🇧🇷 Comunidade Zabbix no Brasil: procure pelos eventos *Zabbix Conference Latam/Brasil* no YouTube e por grupos da comunidade brasileira.

---

## 4. Laboratório

Monte o laboratório antes do módulo 8.2. Sugestão (no homelab da trilha 6 ou em Docker):

| Máquina | Papel |
|---------|-------|
| `zbx-server` | Zabbix server + frontend + banco (PostgreSQL ou MySQL) |
| `zbx-proxy` | Zabbix proxy (a partir do módulo 8.9) |
| `linux-01`, `linux-02` | Hosts Linux com agente 2 (um com Nginx + MySQL, outro com Docker) |
| `win-01` | Host Windows com agente (VM de avaliação do Windows Server) |
| Roteador/switch | Equipamento de rede via SNMP: um roteador doméstico real, um MikroTik CHR, ou roteadores Cisco no GNS3/CML (trilha 9) |
| Impressora / NAS | Se tiver em casa: ótimo para SNMP real |

---

## Módulo 8.1 — Fundamentos de monitoramento e arquitetura do Zabbix (1 semana)

### Conceitos
- [ ] Por que monitorar; monitoramento reativo x proativo; disponibilidade, desempenho, capacidade
- [ ] Métricas, eventos, problemas, alertas; o que é um bom alerta
- [ ] Coleta **passiva** (o servidor pergunta) x **ativa** (o agente envia)
- [ ] **Arquitetura**: Zabbix server, banco de dados, frontend web (PHP), agente (agent e **agent 2**), proxy, Java gateway, web service (relatórios)
- [ ] Fluxo de dados: item → histórico/tendências → trigger → evento → problema → ação → notificação
- [ ] Objetos principais: *host*, *host group*, *template*, *item*, *trigger*, *graph*, *dashboard*, *action*, *media type*, *user*, *user group*, *user role*
- [ ] Histórico x tendências (*trends*); retenção
- [ ] Zabbix x Prometheus x Nagios x outras ferramentas: pontos fortes de cada um

### Fontes
- 🌐 Manual: *Introduction*, *Zabbix concepts* e *Definitions*.
- 🌐 Manual: *What's new* da versão que você vai estudar.
- 📘 *Zabbix 7 Cookbook*: capítulo 1.

### Exercícios
- [ ] **E8.1.1** Desenhe a arquitetura do Zabbix com todos os componentes e o fluxo de dados (Mermaid).
- [ ] **E8.1.2** Escreva o glossário dos objetos do Zabbix com suas palavras.
- [ ] **E8.1.3** Liste 20 coisas que você monitoraria em um cliente pequeno (servidor, NAS, link de internet, impressora, backup, certificado do site…) e o método de coleta de cada uma.

### Autoavaliação
1. Qual a diferença entre um item passivo e um ativo?
2. Qual a diferença entre histórico e tendência?
3. Qual a diferença entre evento e problema?
4. Para que serve o Zabbix proxy?

---

## Módulo 8.2 — Instalação e configuração inicial (1 semana)

### Conceitos
- [ ] Requisitos de hardware e dimensionamento inicial
- [ ] Instalação por **pacotes oficiais** (repositório Zabbix para Debian/Ubuntu/RHEL) — o método cobrado nos treinamentos
- [ ] Instalação com **Docker/Docker Compose** (imagens oficiais)
- [ ] Banco de dados: PostgreSQL (com TimescaleDB opcional) ou MySQL/MariaDB; criação do esquema
- [ ] Servidor web: Nginx ou Apache; PHP
- [ ] Arquivos de configuração: `zabbix_server.conf`, `zabbix_agentd.conf` / `zabbix_agent2.conf`; parâmetros principais
- [ ] Serviços systemd e logs
- [ ] Primeiro acesso ao frontend; troca da senha do Admin
- [ ] Fuso horário e idioma (português)

### Fontes
- 🌐 [Zabbix — Download and install](https://www.zabbix.com/download): gera os comandos para sua distribuição.
- 🌐 Manual: *Installation* (requisitos, pacotes, containers, *upgrade*).
- 🌐 [Zabbix Docker — repositório oficial](https://github.com/zabbix/zabbix-docker)
- 📘 *Zabbix 7 Cookbook*: capítulo 1 (instalação).

### Exercícios
- [ ] **E8.2.1** Instale o Zabbix server por **pacotes** em uma VM Debian/Ubuntu com PostgreSQL e Nginx, seguindo o manual.
- [ ] **E8.2.2** Instale o mesmo ambiente com **Docker Compose** e compare os dois métodos.
- [ ] **E8.2.3** Instale o agente 2 em dois hosts Linux (à mão e depois com o playbook Ansible do módulo 6.7).
- [ ] **E8.2.4** Instale o agente no Windows.
- [ ] **E8.2.5** Aumente o nível de log do server, provoque um erro (ex.: senha errada do banco) e diagnostique pelo log.
- [ ] **E8.2.6** Documente todo o passo a passo em `laboratorio/README.md` para conseguir recriar o ambiente.

### Autoavaliação
1. Quais componentes precisam estar funcionando para o frontend mostrar dados?
2. Qual a diferença entre o agente clássico e o agente 2?
3. Onde ficam os logs do server e do agente?

---

## Módulo 8.3 — Interface, hosts, grupos e visualização de problemas (ZCU) (1 semana)

### Conceitos
- [ ] Navegação no frontend: *Dashboards*, *Monitoring* (*Problems*, *Hosts*, *Latest data*, *Maps*, *Discovery*), *Services*, *Inventory*, *Reports*, *Data collection*, *Alerts*, *Users*, *Administration*
- [ ] Filtros, tags, severidades, reconhecimento (*acknowledge*) e comentários em problemas; supressão; manutenção
- [ ] *Latest data* e gráficos *ad hoc*
- [ ] Hosts: interfaces (agente, SNMP, IPMI, JMX), grupos, tags, macros, inventário
- [ ] Aplicar templates oficiais (ex.: *Linux by Zabbix agent*, *Windows by Zabbix agent*)
- [ ] Usuários, grupos de usuários, papéis (*user roles*) e permissões por grupo de hosts
- [ ] Relatórios básicos: disponibilidade, *top 100 triggers*

### Fontes
- 🌐 Manual: *Quickstart* (login, novo usuário, novo host, novo item, novo trigger, notificações, template).
- 🌐 Manual: *Web interface* (descrição de cada menu).
- 🌐 [ZCU — página do treinamento/exame](https://www.zabbix.com/exam_zcu)

### Exercícios
- [ ] **E8.3.1** Faça o *Quickstart* do manual inteiro.
- [ ] **E8.3.2** Cadastre todos os hosts do laboratório com grupos (`Linux`, `Windows`, `Rede`, `Clientes/Empresa-X`) e tags (`ambiente`, `cliente`, `servico`).
- [ ] **E8.3.3** Aplique os templates oficiais e explore o *Latest data* de cada host.
- [ ] **E8.3.4** Provoque problemas (pare um serviço, encha o disco, derrube a rede de um host) e pratique: filtrar, reconhecer, comentar, mudar severidade, fechar manualmente.
- [ ] **E8.3.5** Crie um período de manutenção e mostre que os alertas são suprimidos.
- [ ] **E8.3.6** Crie um usuário "cliente" que só enxerga os hosts do grupo da própria empresa, em modo somente leitura.
- [ ] **E8.3.7** Escreva 30 perguntas de revisão sobre a interface (para o simulado do ZCU).

### Autoavaliação
1. Como ver só os problemas de severidade Alta ou maior de um grupo de hosts?
2. O que acontece com um problema quando você o reconhece? E quando o fecha manualmente?
3. Como as permissões funcionam: por usuário ou por grupo de usuários? Sobre hosts ou sobre grupos de hosts?

---

## Módulo 8.4 — Itens e métodos de coleta (1,5 semana)

### Conceitos
- [ ] Anatomia de um item: nome, tipo, chave (*key*), tipo de informação, unidades, intervalo de atualização (incluindo intervalos personalizados), histórico, tendências
- [ ] **Tipos de item**:
  - [ ] Zabbix agent (passivo) e Zabbix agent (ativo)
  - [ ] **Simple checks** (`icmpping`, `net.tcp.service`)
  - [ ] **SNMP agent** (v1, v2c, v3), OIDs, MIBs, `snmpwalk`
  - [ ] **HTTP agent** (APIs REST e páginas)
  - [ ] **Dependent items** (um item "mestre" alimenta vários)
  - [ ] **Calculated** e **aggregate**
  - [ ] **External checks** e **UserParameter** (métricas personalizadas no agente)
  - [ ] **Zabbix trapper** e `zabbix_sender`
  - [ ] **Internal** (métricas do próprio Zabbix)
  - [ ] **Script** (JavaScript)
  - [ ] **Database monitor** (ODBC), **JMX**, **IPMI**, **SSH/Telnet agent**
  - [ ] Plugins do agente 2 (Docker, MySQL, PostgreSQL, Redis…)
- [ ] Itens de log (`log[]`, `logrt[]`, `eventlog[]` no Windows)
- [ ] Unidades e multiplicadores; itens de texto x numéricos

### Fontes
- 🌐 Manual: *Configuration → Items* e *Item types* (uma página por tipo).
- 🌐 Manual: *Zabbix agent item keys* e *Zabbix agent 2 plugins*.
- 🌐 [Net-SNMP — tutoriais](http://www.net-snmp.org/wiki/index.php/Tutorials)
- 📘 *Zabbix 7 Cookbook*: capítulo sobre tipos de monitoramento.

### Exercícios
- [ ] **E8.4.1** Crie à mão (sem template) itens de CPU, memória, disco, rede e processos para um host Linux, via agente passivo e ativo. Compare no *Latest data*.
- [ ] **E8.4.2** Monitore disponibilidade com `icmpping`, `icmppingsec` e `icmppingloss` do gateway e de um DNS público.
- [ ] **E8.4.3** `snmpwalk` em um equipamento de rede, encontre os OIDs de interfaces e crie itens SNMP de tráfego e status. Repita com **SNMPv3** (autenticação e criptografia).
- [ ] **E8.4.4** Item HTTP agent que consulta a API do projeto integrador (`/health`) e outro que lê um JSON grande como item mestre.
- [ ] **E8.4.5** *Dependent items* extraindo vários valores do JSON do item mestre.
- [ ] **E8.4.6** *UserParameter* que retorna a idade (em horas) do último backup feito pelo script da trilha 0.
- [ ] **E8.4.7** Script que envia a quantidade de OS abertas via `zabbix_sender` para um item *trapper*.
- [ ] **E8.4.8** Item calculado: percentual de disco livre a partir de dois itens.
- [ ] **E8.4.9** Monitore um log de aplicação procurando a palavra `ERROR`.
- [ ] **E8.4.10** Monitore o MySQL e o Docker com os plugins do agente 2.
- [ ] **E8.4.11** Monitore a data de expiração do certificado HTTPS do site.
- [ ] **E8.4.12** *Database monitor* (ODBC) executando uma consulta SQL de negócio.

### Autoavaliação
1. Quando usar agente ativo em vez de passivo?
2. O que é um *dependent item* e por que ele economiza recursos?
3. Qual a diferença entre SNMPv2c e SNMPv3?
4. Qual a diferença entre *UserParameter* e *external check*?
5. Quando usar *trapper*?

---

## Módulo 8.5 — Pré-processamento (1 semana)

### Conceitos
- [ ] O que é e onde acontece o pré-processamento
- [ ] Transformações: multiplicador, **mudança por segundo** (*change per second*), diferença simples, *trim*, **expressão regular**, **JSONPath**, **XML XPath**, CSV para JSON, Prometheus *pattern*, **JavaScript**
- [ ] Validação: faixa, regex, **descartar inalterados** (*discard unchanged*, com *heartbeat*)
- [ ] Tratamento de erro personalizado (*custom on fail*)
- [ ] Testar o pré-processamento na interface

### Fontes
- 🌐 Manual: *Item value preprocessing* e *JavaScript preprocessing*.
- 🌐 [JSONPath — referência (Zabbix)](https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality)

### Exercícios
- [ ] **E8.5.1** Converta um contador de bytes de interface SNMP em bits por segundo (*change per second* + multiplicador).
- [ ] **E8.5.2** Use JSONPath para extrair campos do JSON da API.
- [ ] **E8.5.3** Use regex para extrair a versão de um programa a partir de um texto.
- [ ] **E8.5.4** Pré-processamento em JavaScript que converte um status textual (`"ok"`, `"degradado"`, `"fora"`) em números.
- [ ] **E8.5.5** *Discard unchanged with heartbeat* em um item que raramente muda e compare o volume de dados gravados.
- [ ] **E8.5.6** Leia métricas no formato Prometheus (`/metrics` da API da trilha 6) com o pré-processamento *Prometheus pattern*.

---

## Módulo 8.6 — Triggers, expressões e dependências (1,5 semana)

### Conceitos
- [ ] Anatomia de um trigger: nome (com macros), severidade, **expressão**, expressão de recuperação, modo de geração de eventos (único/múltiplo), fechamento manual, tags
- [ ] Sintaxe das expressões: `last()`, `avg()`, `min()`, `max()`, `count()`, `nodata()`, `change()`, `find()`, `trendavg()`, funções de tempo, operadores
- [ ] **Histerese** (evitar "pisca-pisca")
- [ ] **Dependências de triggers** (se o roteador cai, não alertar sobre todos os hosts atrás dele)
- [ ] Previsão: `timeleft()` e `forecast()`
- [ ] Correlação de eventos (global e por trigger)
- [ ] Boas práticas: alertar sobre o que exige ação; severidades coerentes; nomes claros

### Fontes
- 🌐 Manual: *Triggers*, *Trigger expression*, *Trigger dependency*, *Supported functions*.
- 🌐 Manual: *Event correlation*.
- 📘 *Zabbix 7 Cookbook*: capítulo sobre triggers avançados.

### Exercícios
- [ ] **E8.6.1** Trigger de CPU alta **sustentada** (média de 5 min > 90%) em vez de valor instantâneo.
- [ ] **E8.6.2** Trigger com histerese: alerta de disco acima de 90%, recupera só abaixo de 85%.
- [ ] **E8.6.3** Trigger `nodata()` para detectar que o agente parou de enviar dados.
- [ ] **E8.6.4** Trigger de previsão: "o disco vai encher em menos de 7 dias" (`timeleft`).
- [ ] **E8.6.5** Trigger de backup atrasado (idade > 26 horas) usando o *UserParameter* do módulo 8.4.
- [ ] **E8.6.6** Trigger de certificado expirando em 15 dias.
- [ ] **E8.6.7** Dependências: hosts do laboratório dependem do "roteador"; derrube o roteador e mostre que só um alerta é gerado.
- [ ] **E8.6.8** Trigger que detecta mudança de versão de um software (`change()`).
- [ ] **E8.6.9** Revise todos os triggers criados e ajuste nomes e severidades seguindo uma política escrita por você.

### Autoavaliação
1. Qual a diferença entre `last()` e `avg(,5m)` em um trigger de CPU?
2. O que é histerese e como implementá-la?
3. Para que servem as dependências entre triggers?
4. O que faz o `nodata()`?

---

## Módulo 8.7 — Eventos, ações e notificações (1 semana)

### Conceitos
- [ ] Tipos de evento: trigger, descoberta, autorregistro, internos
- [ ] **Ações**: condições, operações (enviar mensagem, executar comando remoto), **escalonamento** por etapas, operações de recuperação e de atualização
- [ ] **Tipos de mídia** (*media types*): e-mail, SMS, **webhooks** (Telegram, Slack, Microsoft Teams, WhatsApp via API, sistemas de chamados); scripts
- [ ] Mídias por usuário; horários de atuação; severidades por mídia
- [ ] Macros em mensagens (`{HOST.NAME}`, `{EVENT.SEVERITY}`, `{ITEM.LASTVALUE}`…)
- [ ] **Comandos remotos** (reiniciar um serviço automaticamente) e seus riscos
- [ ] Integração com sistemas de chamados (ex.: GLPI, Jira, *Service desk*)

### Fontes
- 🌐 Manual: *Events*, *Actions*, *Media types*, *Macros*.
- 🌐 [Zabbix Integrations — Webhooks](https://www.zabbix.com/integrations?cat=notifications_alerting)

### Exercícios
- [ ] **E8.7.1** Configure notificação por e-mail (use o Mailpit em laboratório) e por **Telegram** (webhook oficial).
- [ ] **E8.7.2** Ação com escalonamento: 1ª mensagem ao técnico imediatamente; se não reconhecido em 15 min, mensagem ao responsável; em 30 min, para você.
- [ ] **E8.7.3** Mensagens personalizadas com macros, em português, contendo tudo que o técnico precisa para agir.
- [ ] **E8.7.4** Comando remoto que reinicia o Nginx quando ele cai (com limites, para não entrar em laço).
- [ ] **E8.7.5** Webhook próprio (JavaScript) que abre uma OS no sistema Marcelo IT (API da trilha 3) quando surge um problema de severidade Alta em um cliente.
- [ ] **E8.7.6** Mídia com horário de atuação: problemas de severidade baixa só notificam em horário comercial.

### Autoavaliação
1. Qual a diferença entre ação e tipo de mídia?
2. Como funciona o escalonamento em uma ação?
3. Quais os riscos dos comandos remotos e como reduzi-los?

---

## Módulo 8.8 — Templates, macros, visualização e monitoramento web (1,5 semana)

### Conceitos
- [ ] **Templates**: criar, vincular, aninhar; itens, triggers, gráficos, dashboards e regras de descoberta dentro de templates; exportar/importar (YAML); versionar no Git
- [ ] **Macros de usuário**: globais, de template, de host; **macros com contexto** (`{$DISCO.LIMITE:"/var"}`); macros secretas; macros de *vault* (HashiCorp Vault/CyberArk)
- [ ] Ordem de precedência das macros
- [ ] **Dashboards**: widgets (gráfico, *top hosts*, problemas, mapa, *item value*, *honeycomb*, *gauge*…), dashboards de template, compartilhamento
- [ ] **Gráficos** e **mapas de rede** (com ícones, links que mudam de cor, mapas aninhados)
- [ ] **Serviços e SLA** (árvore de serviços de negócio, regras de status, relatórios de SLA)
- [ ] **Monitoramento web**: cenários (*web scenarios*) com vários passos, variáveis, códigos esperados, tempos de resposta
- [ ] Inventário de hosts (manual e automático)
- [ ] Relatórios agendados (PDF) com o *web service*

### Fontes
- 🌐 Manual: *Templates*, *User macros*, *Macros with context*, *Dashboards*, *Network maps*, *Services*, *Web monitoring*, *Scheduled reports*.
- 🌐 [Zabbix — Template guidelines](https://www.zabbix.com/documentation/guidelines/en/template_guidelines): boas práticas oficiais para criar templates.

### Exercícios
- [ ] **E8.8.1** Crie o template `Marcelo IT - Linux Base` com os itens e triggers dos módulos anteriores, usando macros para todos os limites.
- [ ] **E8.8.2** Use macros com contexto para ter limites de disco diferentes por ponto de montagem.
- [ ] **E8.8.3** Template `Marcelo IT - Backup` (item do backup, trigger de atraso) e aplique a vários hosts.
- [ ] **E8.8.4** Exporte os templates em YAML e versione no repositório; importe em outra instalação.
- [ ] **E8.8.5** Dashboard "Visão geral dos clientes" com problemas por cliente, disponibilidade e tráfego do link.
- [ ] **E8.8.6** Mapa de rede do laboratório com links que ficam vermelhos quando a interface cai.
- [ ] **E8.8.7** Cenário web que faz login no sistema Marcelo IT, abre a lista de OS e verifica o texto esperado, medindo o tempo de cada passo.
- [ ] **E8.8.8** Árvore de serviços "Sistema Marcelo IT" (front, API, banco, fila) com SLA de 99,5% e relatório mensal.
- [ ] **E8.8.9** Relatório agendado em PDF enviado por e-mail toda segunda-feira.

### Autoavaliação
1. Qual a ordem de precedência das macros (host, template, global)?
2. Para que serve uma macro com contexto?
3. Por que colocar limites em macros em vez de escrever o número direto no trigger?
4. Como um cenário web detecta que o login falhou?

### Checkpoint — pronto para o ZCS
- [ ] Consigo instalar o Zabbix do zero por pacotes, sem consultar o passo a passo
- [ ] Sei criar e explicar itens de todos os tipos principais, pré-processamento, triggers, ações e templates
- [ ] Tenho um template próprio versionado no Git
- [ ] Respondo as autoavaliações dos módulos 8.1 a 8.8 com ≥ 80% de acerto

---

## Módulo 8.9 — Descoberta automática: LLD, *network discovery* e autorregistro (ZCP) (1,5 semana)

### Conceitos
- [ ] **Low-Level Discovery (LLD)**: regras de descoberta, macros LLD (`{#FSNAME}`, `{#IFNAME}`), protótipos de itens, triggers, gráficos e **hosts**; filtros; *overrides*; tempo de vida dos recursos perdidos
- [ ] LLD nativo (sistemas de arquivos, interfaces, serviços do Windows, SNMP) e LLD personalizado (JSON de um script ou item dependente)
- [ ] **Network discovery**: faixas de IP, verificações (ICMP, SNMP, agente, portas), regras e ações de descoberta (adicionar host, vincular template, colocar em grupo)
- [ ] **Autorregistro de agentes ativos** (*active agent autoregistration*) com `HostMetadata`
- [ ] Protótipos de host (ex.: descobrir VMs de um hipervisor ou containers)

### Fontes
- 🌐 Manual: *Low-level discovery* (e subpáginas), *Network discovery*, *Active agent autoregistration*.
- 🌐 [ZCP — página do treinamento](https://www.zabbix.com/training_professional)
- 📘 *Zabbix 7 Cookbook*: capítulos sobre descoberta.

### Exercícios
- [ ] **E8.9.1** Regra LLD que descobre sistemas de arquivos e cria itens e triggers automaticamente, filtrando `tmpfs`.
- [ ] **E8.9.2** LLD SNMP das interfaces de um switch, ignorando interfaces desativadas.
- [ ] **E8.9.3** LLD personalizado: um script retorna em JSON a lista de clientes com backup configurado e o Zabbix cria um item para cada um.
- [ ] **E8.9.4** *Network discovery* da rede do laboratório que adiciona automaticamente impressoras (detectadas por SNMP) ao grupo `Impressoras` com o template certo.
- [ ] **E8.9.5** Autorregistro: ao instalar o agente com `HostMetadata=linux-web`, o host entra sozinho no grupo e recebe os templates certos.
- [ ] **E8.9.6** *Overrides* em LLD: triggers com severidade diferente para o disco `/` e os demais.

### Autoavaliação
1. Qual a diferença entre LLD e *network discovery*?
2. Para que serve o `HostMetadata` no autorregistro?
3. O que acontece com itens descobertos quando o recurso deixa de existir?

---

## Módulo 8.10 — Monitoramento distribuído com proxies (ZCP) (1 semana)

### Conceitos
- [ ] Por que usar proxies: redes remotas, NAT/firewall, distribuir carga, coletar durante quedas do link
- [ ] Proxy **ativo** x **passivo**
- [ ] Banco local do proxy (SQLite) e *buffer* de dados (modos memória, disco e híbrido nas versões recentes)
- [ ] **Grupos de proxies** com balanceamento e *failover* (a partir da 7.0)
- [ ] Atribuir hosts a proxies
- [ ] Monitorar a saúde do próprio proxy

### Fontes
- 🌐 Manual: *Distributed monitoring* e *Proxies*, *Proxy load balancing and high availability*.

### Exercícios
- [ ] **E8.10.1** Instale um proxy ativo em outra VM (simulando a rede de um cliente) e mova os hosts "do cliente" para ele.
- [ ] **E8.10.2** Corte a conexão entre o proxy e o server por 30 minutos e mostre que os dados chegam depois.
- [ ] **E8.10.3** Crie um grupo com 2 proxies, desligue um e veja os hosts migrarem.
- [ ] **E8.10.4** Monitore as filas e a saúde do proxy com o template oficial.
- [ ] **E8.10.5** Desenhe a arquitetura de monitoramento gerenciado para 10 clientes: um proxy por cliente (em um mini PC ou VM), server central.

---

## Módulo 8.11 — API do Zabbix e automação (ZCP/ZCE) (1 semana)

### Conceitos
- [ ] API JSON-RPC: autenticação (tokens de API), métodos (`host.get`, `host.create`, `item.get`, `problem.get`, `history.get`, `template.get`…), parâmetros comuns (`output`, `filter`, `search`, `selectX`)
- [ ] Biblioteca **zabbix_utils** (Python)
- [ ] Automação: cadastro em massa, relatórios, sincronização com outros sistemas (CMDB, ERP)
- [ ] Ansible e Terraform com Zabbix (coleção `community.zabbix`)
- [ ] Zabbix + Grafana (plugin de *datasource*)

### Fontes
- 🌐 Manual: *API* (visão geral e referência de métodos).
- 🌐 [zabbix_utils (GitHub)](https://github.com/zabbix/python-zabbix-utils)
- 🌐 [Ansible — coleção community.zabbix](https://galaxy.ansible.com/ui/repo/published/community/zabbix/)
- 🌐 [Grafana — plugin do Zabbix](https://grafana.com/grafana/plugins/alexanderzobnin-zabbix-app/)

### Exercícios
- [ ] **E8.11.1** Script Python que lista todos os hosts com problemas ativos, agrupados por cliente.
- [ ] **E8.11.2** Script que cadastra hosts em massa a partir de um CSV (nome, IP, grupo, templates, tags).
- [ ] **E8.11.3** Relatório mensal por cliente (disponibilidade, problemas, tempo de resolução) gerado pela API em PDF (reaproveite a trilha 4).
- [ ] **E8.11.4** Integração com o sistema Marcelo IT: ao cadastrar um cliente com equipamentos no sistema, criar os hosts no Zabbix automaticamente.
- [ ] **E8.11.5** Gerencie hosts e templates com a coleção Ansible `community.zabbix`.
- [ ] **E8.11.6** Dashboard no Grafana usando o Zabbix como fonte de dados.

---

## Módulo 8.12 — Alta disponibilidade, desempenho e banco de dados (ZCE) (1,5 semana)

### Conceitos
- [ ] **HA nativo do Zabbix server** (cluster ativo/*standby*, a partir da 6.0); HA do frontend e do banco
- [ ] Processos internos do server: *pollers*, *trappers*, *preprocessors*, *history syncers*, *housekeeper*, *escalators*, *alerters*…
- [ ] **Caches**: configuração, histórico, tendências, valores; como dimensionar
- [ ] Métricas internas e o template *Zabbix server health*; NVPS (novos valores por segundo); fila (*queue*)
- [ ] *Tuning* dos parâmetros do `zabbix_server.conf`
- [ ] Banco de dados: dimensionamento, **particionamento** / **TimescaleDB**, compressão, *housekeeping*
- [ ] Atualização de versão (*upgrade*) com segurança; backup e restauração

### Fontes
- 🌐 Manual: *High availability*, *Performance tuning*, *Internal checks*, *Housekeeping*, *TimescaleDB setup*, *Upgrade procedure*.
- 🌐 Zabbix Blog — artigos sobre desempenho e escalabilidade.
- 📘 *Zabbix 7 Cookbook*: capítulos de HA e manutenção.

### Exercícios
- [ ] **E8.12.1** Configure o HA com dois servers; desligue o ativo e meça o tempo de *failover*.
- [ ] **E8.12.2** Gere carga (muitos hosts e itens com intervalo curto, via API ou `zabbix_sender`) até a fila crescer; identifique o processo saturado pelo template de saúde e ajuste os parâmetros.
- [ ] **E8.12.3** Migre o banco para TimescaleDB, ative a compressão e compare o tamanho.
- [ ] **E8.12.4** Faça backup completo (banco + configurações) e restaure em outra VM.
- [ ] **E8.12.5** Faça um *upgrade* de versão no laboratório seguindo o procedimento oficial.

---

## Módulo 8.13 — Segurança da instalação Zabbix (ZCE) (1 semana)

### Conceitos
- [ ] **Criptografia** entre componentes: TLS com **PSK** e com **certificados** (server ↔ agente, server ↔ proxy)
- [ ] Frontend com HTTPS; cabeçalhos de segurança
- [ ] Autenticação: usuários internos, **LDAP/Active Directory** (com provisionamento *just-in-time*), **SAML/SSO**, MFA (TOTP e Duo, nas versões recentes)
- [ ] Papéis de usuário (*user roles*) e menor privilégio; tokens de API com validade
- [ ] Macros secretas e integração com cofres de segredos
- [ ] Permissões do agente: `AllowKey`/`DenyKey`, desativar `system.run` quando não for necessário
- [ ] Usuário do banco com permissões mínimas; *firewall* entre componentes
- [ ] Auditoria (*audit log*)

### Fontes
- 🌐 Manual: *Encryption* (PSK e certificados), *Authentication*, *User roles*, *Audit log*, *Best practices for secure Zabbix setup*.

### Exercícios
- [ ] **E8.13.1** Criptografe a comunicação com todos os agentes via PSK e com o proxy via certificados de uma CA própria (reaproveite o módulo 6.3).
- [ ] **E8.13.2** Integre o login com um LDAP (OpenLDAP ou Samba AD no laboratório).
- [ ] **E8.13.3** Ative MFA para os administradores.
- [ ] **E8.13.4** Restrinja as chaves permitidas no agente e mostre que `system.run` é bloqueado.
- [ ] **E8.13.5** Escreva um checklist de segurança da instalação e aplique-o no laboratório.

---

## Módulo 8.14 — Integrações e tópicos avançados (ZCE) (1 semana)

### Conceitos
- [ ] Monitoramento de **VMware/Proxmox**, **Kubernetes** (templates oficiais via Helm), **nuvem** (AWS/Azure/GCP)
- [ ] Monitoramento de bancos (MySQL, PostgreSQL, Redis), servidores web e filas
- [ ] Coleta de métricas Prometheus e integração com OpenTelemetry (novidades da 8.0)
- [ ] *Browser item* (monitoramento sintético com navegador real, a partir da 7.0)
- [ ] Templates complexos e boas práticas de publicação
- [ ] Novidades da versão LTS que você vai certificar

### Exercícios
- [ ] **E8.14.1** Monitore o cluster k3s da trilha 6 com os templates oficiais de Kubernetes.
- [ ] **E8.14.2** Monitore o Proxmox do homelab via API.
- [ ] **E8.14.3** *Browser item* que abre o site da Marcelo IT e mede o tempo de carregamento real.
- [ ] **E8.14.4** Publique um template seu seguindo as diretrizes oficiais (no seu repositório ou no *community-templates*).

---

## Projetos finais

### Projeto A — Monitoramento completo do laboratório e do projeto integrador
Todos os hosts do homelab, o k3s, os bancos, a API e o site monitorados, com templates próprios versionados, LLD, proxy, criptografia, HA, notificações no Telegram com escalonamento, dashboards, mapa, SLA do serviço e relatórios agendados.

### Projeto B — Oferta de "Monitoramento Gerenciado Marcelo IT"
- Arquitetura: server central (VPS ou homelab), um proxy por cliente, criptografia em tudo.
- *Onboarding* automatizado: script/Ansible instala o proxy e os agentes, a API cadastra os hosts.
- Templates padrão por tipo de cliente (escritório, loja, residência): links de internet, roteador, NAS, impressoras, backups, câmeras, estações.
- Portal: usuário somente leitura para o cliente ver o próprio dashboard.
- Integração: problema grave abre OS no sistema Marcelo IT.
- Relatório mensal automático por cliente.
- Documento comercial: o que é monitorado, SLA de atendimento, preço.

---

## ✅ Checklist de conclusão da Trilha 8
- [ ] Laboratório reproduzível documentado no repositório
- [ ] Autoavaliações dos módulos 8.1–8.8 com ≥ 80% de acerto
- [ ] **Certificação ZCU**
- [ ] **Certificação ZCS**
- [ ] Oferta de monitoramento gerenciado com pelo menos 1 cliente (ou cliente piloto)
- [ ] Módulos 8.9–8.11 completos → **ZCP**
- [ ] Módulos 8.12–8.14 completos → **ZCE**
