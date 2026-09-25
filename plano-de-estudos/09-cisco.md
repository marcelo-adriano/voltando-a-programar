# Trilha 9 — Certificações Cisco (plano para o repositório `certificacoes-cisco`)

> **Objetivo da trilha:** dominar redes corporativas (endereçamento, switching, roteamento, serviços, segurança de infraestrutura, redes sem fio e automação) e conquistar o **CCNA**, abrindo caminho para CCNA Automation, CCNP Enterprise e outras especializações.

**Duração:** 16–24 semanas para o CCNA · **Pré-requisitos:** Trilha 0 (terminal e redes básicas). Python (trilha 4) ajuda na parte de automação.

---

## 1. O mapa de certificações Cisco (2026)

A Cisco reorganizou as certificações em 2026:
- Em **3 de fevereiro de 2026**, a trilha **DevNet** virou **CCNA Automation**, **CCNP Automation** e **CCIE Automation**.
- A trilha **CyberOps** passou a se chamar **CCNA Cybersecurity** (e CCNP Cybersecurity).
- O **CCNA 200-301 v1.1** fica disponível até o fim de **janeiro de 2027**. A **v2.0** do exame (publicada em maio de 2026) entra em vigor em **3 de fevereiro de 2027**.

| Nível | Certificação | Observação |
|-------|--------------|------------|
| Entrada | **CCST Networking** (Cisco Certified Support Technician) | Opcional; bom para validar a base |
| Associado | **CCNA** (exame 200-301) | **Meta principal desta trilha** |
| Associado | **CCNA Automation** (antigo DevNet Associate) | Automação e programabilidade de redes; combina com as trilhas de dev |
| Associado | **CCNA Cybersecurity** (antigo CyberOps Associate) | Operações de segurança |
| Profissional | **CCNP Enterprise** | Exame núcleo (ENCOR) + um exame de concentração (ex.: ENARSI) |
| Especialista | **CCIE** | Prova prática de laboratório; muito avançada |

### Qual versão do CCNA estudar?
- **Se for fazer a prova até janeiro de 2027:** estude o blueprint **v1.1** (6 domínios: Fundamentos de Rede 20%, Acesso à Rede 20%, Conectividade IP 25%, Serviços IP 10%, Fundamentos de Segurança 15%, Automação e Programabilidade 10%).
- **Se for fazer a prova a partir de fevereiro de 2027 (o mais provável, seguindo o cronograma do plano):** estude o blueprint **v2.0**. Ele tem **5 domínios**, dá mais peso a fundamentos e switching, cria um domínio de **IA e operações de rede (10%)**, incorpora a automação em operações e sobe o nível cognitivo: muitos tópicos que pediam "explicar" agora pedem "configurar", e vários que pediam "configurar" agora pedem "resolver problemas".
- Os módulos abaixo cobrem o núcleo comum às duas versões. **Baixe o PDF oficial de *exam topics* da versão que você vai fazer** e marque cada item nele. O blueprint oficial é a fonte da verdade.

**Fontes oficiais:**
- 🌐 [Cisco Learning Network — CCNA Exam Topics](https://learningnetwork.cisco.com/s/ccna-exam-topics)
- 🌐 [Blueprint CCNA v1.1 (PDF oficial)](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf)
- 🌐 [Cisco — A new era for Cisco certifications](https://learningnetwork.cisco.com/s/a-new-era-for-cisco-certifications)
- 🌐 [Wendell Odom — CCNA Skills Blog](https://www.certskills.com/): o autor dos livros oficiais analisa cada mudança do blueprint (incluindo a v2.0).

> A prova é aplicada pela **Pearson VUE** (centro de testes ou online). A certificação vale 3 anos e pode ser renovada com créditos de educação continuada ou outra prova. Confira preço e regras atuais no site da Cisco.

---

## 2. Estrutura do repositório `certificacoes-cisco`

```
certificacoes-cisco/
├── README.md                     ← progresso, blueprint com checkboxes, datas das provas
├── ccna/
│   ├── blueprint.md              ← cada tópico oficial com link para anotações e laboratórios
│   ├── anotacoes/                ← um arquivo por tópico
│   ├── labs/
│   │   ├── 01-cli-basica/
│   │   │   ├── topologia.pkt     ← arquivo do Packet Tracer
│   │   │   ├── enunciado.md
│   │   │   └── solucao/          ← configs finais (show running-config) de cada equipamento
│   │   └── ...
│   ├── subnetting/               ← exercícios e o seu gerador de exercícios (Python)
│   ├── flashcards/               ← baralhos Anki exportados
│   └── simulados/                ← registro de notas e dos erros por tema
├── ccna-automation/
│   ├── scripts/                  ← Netmiko, NAPALM, RESTCONF, Ansible
│   └── labs/
└── ccnp-enterprise/
```

---

## 3. Fontes principais da trilha

- 🎥 [**Jeremy's IT Lab — curso completo de CCNA (YouTube, gratuito)**](https://www.youtube.com/@JeremysITLab): aulas + laboratórios de Packet Tracer + baralhos Anki para cada aula. **Espinha dorsal recomendada.**
- 📘 ***CCNA 200-301 Official Cert Guide*, volumes 1 e 2 — Wendell Odom (Cisco Press)**: o livro de referência. Use a edição correspondente à versão da prova.
- 🎥 [Cisco Networking Academy (NetAcad)](https://www.netacad.com/) 🇧🇷: cursos gratuitos autodidatas em português (ex.: *Networking Basics*, *Networking Devices and Initial Configuration*) e o **Packet Tracer** gratuito. O currículo CCNA completo (ITN, SRWE, ENSA) é oferecido por academias parceiras.
- 📘🇧🇷 *CCNA — Guia Completo de Estudo* — Marco Aurélio Filippetti (autor brasileiro; confira a edição mais recente).
- 📘 *CCNA Certification Study Guide* — Todd Lammle (alternativa ao Odom).
- 🎥 [Neil Anderson — Flackbox](https://www.flackbox.com/) e [David Bombal (YouTube)](https://www.youtube.com/@davidbombal)
- 🌐 [Cisco Learning Network — comunidade e grupos de estudo](https://learningnetwork.cisco.com/)
- 🌐 [r/ccna](https://www.reddit.com/r/ccna/): dicas e relatos de quem fez a prova.
- 🧪 **Simulados:** Boson ExSim-Max 💲 (os mais recomendados; explicam cada resposta). Evite *dumps* (perguntas vazadas): violam os termos da Cisco, podem cancelar sua certificação e não ensinam nada.

### Ferramentas de laboratório
| Ferramenta | Para quê | Custo |
|-----------|----------|-------|
| **Cisco Packet Tracer** | Simulador oficial; cobre quase todo o CCNA | Gratuito (conta NetAcad) |
| **Cisco Modeling Labs (CML)** | Imagens reais de IOS/IOS-XE; há uma versão gratuita limitada (poucos nós) | Gratuito limitado / 💲 |
| **GNS3** e **EVE-NG** | Emuladores com imagens reais (e de outros fabricantes) | Gratuitos (imagens Cisco exigem licença) |
| **Cisco DevNet Sandbox** | Equipamentos reais/virtuais na nuvem para automação | Gratuito |
| Equipamentos usados | Switches e roteadores Cisco antigos para praticar cabeamento e console | Baixo |

---

## 4. Método de estudo específico para o CCNA

1. **Uma aula por dia** (Jeremy's IT Lab) + o capítulo correspondente do Odom.
2. **Laboratório da aula no mesmo dia.** Configure digitando, sem copiar e colar.
3. **Anki diário** com o baralho do Jeremy e cartões próprios (comandos, portas, números de protocolos, tempos de STP, distâncias administrativas).
4. **Subnetting todo dia** (10 minutos) até ficar automático, e depois 3 vezes por semana até a prova.
5. **Revisão semanal:** refazer um laboratório antigo **sem olhar a solução**.
6. **Simulados** nas últimas 4–6 semanas. Registre cada erro e o tópico correspondente, e estude os tópicos, não as perguntas.
7. Marque a prova quando estiver com **≥ 85–90% nos simulados** de forma consistente.

---

## Módulo 9.1 — Fundamentos de redes (1,5 semana)

### Conceitos
- [ ] Componentes: roteadores, switches L2 e L3, *firewalls* de próxima geração, IPS, *access points*, controladores de rede sem fio (WLC), *endpoints*, servidores, PoE
- [ ] Topologias: duas camadas (*collapsed core*), três camadas, *spine-leaf*, WAN, SOHO, *on-premises* x nuvem
- [ ] Modelos **OSI** e **TCP/IP**; encapsulamento e PDUs (segmento, pacote, quadro)
- [ ] Meios físicos: cobre (categorias, par trançado, T568A/B, cabo direto x cruzado, Auto-MDIX), fibra (monomodo x multimodo, conectores, SFP)
- [ ] Problemas de interface e cabo: colisões, erros, *duplex* e velocidade incompatíveis
- [ ] **TCP x UDP**: cabeçalhos, *handshake*, janelas, portas conhecidas
- [ ] **Ethernet**: quadro, endereço MAC, *unicast*/*broadcast*/*multicast*
- [ ] Como um **switch** aprende e encaminha (tabela MAC, *flooding*, *aging*)
- [ ] **ARP**
- [ ] Virtualização (VMs, containers, VRFs) e conceitos de nuvem

### Fontes
- 🎥 Jeremy's IT Lab — dias 1 a 5.
- 📘 Odom vol. 1 — parte I.
- 🎥 NetAcad — *Networking Basics*.

### Exercícios
- [ ] **E9.1.1** Crimpe um cabo de rede (se tiver alicate) e teste; explique T568A x T568B.
- [ ] **E9.1.2** No Wireshark, capture um *ping* na rede local e identifique cada camada: quadro Ethernet (MACs), pacote IP, ICMP, e a troca ARP antes dele.
- [ ] **E9.1.3** No Packet Tracer, em modo simulação, acompanhe um quadro atravessando dois switches e veja as tabelas MAC sendo preenchidas.
- [ ] **E9.1.4** Tabela no Anki: 25 portas e protocolos (FTP, SSH, Telnet, SMTP, DNS, DHCP, TFTP, HTTP, POP3, NTP, SNMP, HTTPS, Syslog, RDP…) com TCP/UDP.
- [ ] **E9.1.5** Laboratórios do Jeremy dos dias 1–5.

### Autoavaliação
1. Em que camada atuam hub, switch e roteador?
2. O que o switch faz com um quadro cujo MAC de destino não está na tabela?
3. Qual a diferença entre um cabo monomodo e um multimodo?
4. Por que o TCP é "orientado a conexão"?

---

## Módulo 9.2 — CLI do IOS e configuração básica (1 semana)

### Conceitos
- [ ] Acesso: console, SSH, Telnet (e por que não usar); *terminal emulator* (PuTTY, SecureCRT, `screen`/`minicom`)
- [ ] Modos: usuário, privilegiado, configuração global, interface, linha
- [ ] Ajuda contextual (`?`), completar com Tab, abreviação de comandos, histórico
- [ ] `running-config` x `startup-config`; `copy run start` / `write`; `show version`, `show interfaces`, `show ip interface brief`
- [ ] Configuração básica: *hostname*, senhas (`enable secret`, console, VTY), `service password-encryption`, *banner*, descrição de interfaces, `shutdown`/`no shutdown`
- [ ] **SSH**: domínio, chaves RSA, usuário local, `transport input ssh`, `login local`
- [ ] Backup e restauração de configurações (TFTP/SCP); recuperação de senha (procedimento)
- [ ] Filtros de saída (`| include`, `| section`, `| begin`)

### Fontes
- 🎥 Jeremy's IT Lab — dias 4 e 6.
- 📘 Odom vol. 1 — parte II.
- 🎥 NetAcad — *Networking Devices and Initial Configuration*.

### Exercícios
- [ ] **E9.2.1** Configure do zero um switch e um roteador com *hostname*, senhas seguras, banner, SSH e usuário local. Teste o SSH a partir de um PC do Packet Tracer.
- [ ] **E9.2.2** Salve, reinicie, confira que a configuração persistiu; apague a `startup-config` e reinicie.
- [ ] **E9.2.3** Faça backup da configuração para um servidor TFTP do Packet Tracer e restaure.
- [ ] **E9.2.4** Monte o seu "template de configuração inicial" em texto no repositório.
- [ ] **E9.2.5** Laboratórios do Jeremy correspondentes.

---

## Módulo 9.3 — Endereçamento IPv4 e sub-redes (2 semanas) ⭐

> **O tópico mais importante do CCNA.** Precisa ficar automático: você deve resolver uma questão de sub-rede em menos de 30 segundos.

### Conceitos
- [ ] Estrutura do endereço IPv4; conversão binário ↔ decimal
- [ ] Classes (histórico) e **CIDR**; máscara em decimal e em prefixo (`/24`)
- [ ] Endereços **privados** (RFC 1918), APIPA, *loopback*, *multicast*
- [ ] Para uma rede: **endereço de rede, broadcast, primeiro e último host, quantidade de hosts**
- [ ] **Sub-redes** com máscara fixa; **VLSM** (máscara variável); sumarização de rotas (*supernetting*)
- [ ] Endereçamento de links ponto a ponto (`/30` e `/31`)
- [ ] Verificar configuração IP no Windows, Linux e macOS

### Fontes
- 🎥 Jeremy's IT Lab — dias 7 a 15 (a parte de sub-redes).
- 📘 Odom vol. 1 — parte IV (*IPv4 Addressing*).
- 🌐 [Practical Networking — Subnetting Mastery (gratuito)](https://www.practicalnetworking.net/stand-alone/subnetting-mastery/)
- 🧪 [subnettingpractice.com](https://subnettingpractice.com/) e [subnetting.org](https://www.subnetting.org/): geradores de exercícios.
- 🧪 [Subnet Calculator (apenas para conferir)](https://www.subnet-calculator.com/)

### Exercícios
- [ ] **E9.3.1** 200 exercícios de sub-rede (20 por dia durante 10 dias), cronometrando. Meta: < 30 s por questão.
- [ ] **E9.3.2** Escreva, em Python, um **gerador de exercícios de sub-rede** com correção automática (use o módulo `ipaddress` só para corrigir). Isso junta a trilha 4 com esta.
- [ ] **E9.3.3** Planejamento VLSM: uma empresa com a rede `172.16.0.0/22` precisa de sub-redes para 200, 100, 50, 25 e 10 hosts, mais 4 links ponto a ponto. Faça a tabela.
- [ ] **E9.3.4** Sumarize 8 redes em uma única rota.
- [ ] **E9.3.5** Implemente o plano do E9.3.3 no Packet Tracer e teste o `ping` entre todas as redes.
- [ ] **E9.3.6** Planeje o endereçamento da rede de um cliente real seu (anonimizado).

### Autoavaliação
1. Quantos hosts cabem em um `/27`? E em um `/23`?
2. Qual o broadcast da rede de `192.168.10.77/26`?
3. O que é VLSM e por que ele economiza endereços?
4. Por que se usa `/31` em links ponto a ponto?

---

## Módulo 9.4 — IPv6 (1 semana)

### Conceitos
- [ ] Por que IPv6; formato; regras de abreviação
- [ ] Tipos: *global unicast*, *unique local*, *link-local*, *anycast*, *multicast*; endereços especiais
- [ ] Prefixos e sub-redes (`/64`), **EUI-64**
- [ ] Atribuição: estática, **SLAAC**, DHCPv6 *stateful* e *stateless*
- [ ] **NDP** (substitui o ARP): NS, NA, RS, RA; detecção de endereço duplicado
- [ ] Configuração no IOS (`ipv6 unicast-routing`, `ipv6 address`)
- [ ] Rotas estáticas IPv6

### Fontes
- 🎥 Jeremy's IT Lab — aulas de IPv6.
- 📘 Odom vol. 1 — parte VII (*IPv6*).

### Exercícios
- [ ] **E9.4.1** 50 exercícios de abreviação e expansão de endereços IPv6.
- [ ] **E9.4.2** Calcule endereços EUI-64 a partir de MACs à mão.
- [ ] **E9.4.3** Rede *dual-stack* no Packet Tracer com SLAAC nos PCs e rotas estáticas IPv6 entre roteadores.
- [ ] **E9.4.4** Veja se o seu provedor de internet entrega IPv6 e explique o prefixo recebido.

---

## Módulo 9.5 — VLANs, trunks e roteamento entre VLANs (1,5 semana)

### Conceitos
- [ ] Domínios de colisão e de *broadcast*; por que segmentar
- [ ] **VLANs**: criação, portas de acesso, VLAN de voz, VLAN nativa, VLAN de gerência
- [ ] **Trunks 802.1Q**: *tagging*, VLANs permitidas, VLAN nativa (e o risco de manter a VLAN 1)
- [ ] **DTP** (e por que desativar) e **VTP** (modos, riscos)
- [ ] **Roteamento entre VLANs**: *router-on-a-stick* (subinterfaces) e **switch L3** com SVIs; `ip routing`
- [ ] Protocolos de descoberta: **CDP** e **LLDP**
- [ ] Verificação e solução de problemas (`show vlan brief`, `show interfaces trunk`, `show interfaces switchport`)

### Fontes
- 🎥 Jeremy's IT Lab — aulas de VLANs, DTP/VTP, CDP/LLDP.
- 📘 Odom vol. 1 — parte II (*Implementing VLANs*).

### Exercícios
- [ ] **E9.5.1** Escritório com 3 VLANs (Administrativo, Vendas, Visitantes) em 2 switches conectados por *trunk*.
- [ ] **E9.5.2** Roteamento entre as VLANs com *router-on-a-stick*; depois migre para um switch L3 com SVIs.
- [ ] **E9.5.3** Troque a VLAN nativa, restrinja as VLANs permitidas no *trunk* e desative o DTP.
- [ ] **E9.5.4** Use CDP e LLDP para desenhar a topologia sem olhar o diagrama.
- [ ] **E9.5.5** **Troubleshooting:** peça à IA (ou a um colega) para gerar uma configuração com 5 erros (VLAN errada na porta, VLAN não permitida no *trunk*, VLAN nativa diferente dos dois lados…) e encontre-os só com comandos `show`.

### Autoavaliação
1. O que acontece se a VLAN nativa for diferente nos dois lados de um *trunk*?
2. Por que desativar o DTP?
3. *Router-on-a-stick* x switch L3: vantagens de cada um.

---

## Módulo 9.6 — Spanning Tree e EtherChannel (1,5 semana)

### Conceitos
- [ ] Por que existem *loops* na camada 2 e o que causam (tempestades de *broadcast*, instabilidade da tabela MAC)
- [ ] **STP (802.1D)**: BPDU, eleição da *root bridge* (prioridade + MAC), custo de caminho, *root port*, *designated port*, porta bloqueada; estados e temporizadores
- [ ] **RSTP (802.1w)** e **Rapid PVST+**: papéis (*alternate*, *backup*), convergência rápida
- [ ] Ajustes: prioridade, custo, **PortFast**, **BPDU Guard**, Root Guard, Loop Guard
- [ ] **EtherChannel**: **LACP** e PAgP, modos (*active*, *passive*, *on*), balanceamento de carga, requisitos de compatibilidade; EtherChannel L2 e L3

### Fontes
- 🎥 Jeremy's IT Lab — aulas de STP, RSTP e EtherChannel.
- 📘 Odom vol. 1 — parte III (*Spanning Tree Protocol*).

### Exercícios
- [ ] **E9.6.1** Com 3 switches em triângulo, **preveja** no papel a *root bridge* e o papel de cada porta; depois confira com `show spanning-tree`.
- [ ] **E9.6.2** Force um switch específico a ser *root* para cada VLAN (balanceamento por VLAN com Rapid PVST+).
- [ ] **E9.6.3** PortFast + BPDU Guard nas portas de usuários; conecte um switch "clandestino" e veja a porta entrar em *err-disabled*; recupere.
- [ ] **E9.6.4** EtherChannel LACP entre dois switches com 2 links; derrube um cabo e confirme que o tráfego continua.
- [ ] **E9.6.5** **Troubleshooting:** EtherChannel que não sobe por configurações incompatíveis (velocidade, VLAN, modo).

### Autoavaliação
1. Como é eleita a *root bridge*?
2. Qual a diferença de convergência entre STP e RSTP?
3. O que faz o BPDU Guard?
4. Qual a diferença entre os modos LACP *active* e *passive*? Dois lados em *passive* formam o canal?

---

## Módulo 9.7 — Roteamento: conceitos e rotas estáticas (1 semana)

### Conceitos
- [ ] **Tabela de roteamento**: código do protocolo, prefixo, máscara, próximo salto, **distância administrativa**, **métrica**, *gateway of last resort*
- [ ] Como o roteador decide: **maior prefixo** (*longest prefix match*) → distância administrativa → métrica
- [ ] Rotas conectadas e locais
- [ ] **Rotas estáticas**: de rede, de host, **rota padrão**, **rota flutuante** (*backup*); IPv4 e IPv6
- [ ] Roteamento dinâmico: tipos (vetor de distância x estado de enlace), IGP x EGP; distâncias administrativas padrão (conectada 0, estática 1, eBGP 20, EIGRP 90, OSPF 110, RIP 120…)

### Fontes
- 🎥 Jeremy's IT Lab — aulas de roteamento e rotas estáticas.
- 📘 Odom vol. 1 — parte IV (*IPv4 Routing*).

### Exercícios
- [ ] **E9.7.1** Leia 10 tabelas de roteamento (`show ip route`) e, para cada destino dado, diga qual rota será usada e por quê.
- [ ] **E9.7.2** 4 roteadores em linha com rotas estáticas completas; depois substitua por rotas padrão onde fizer sentido.
- [ ] **E9.7.3** Dois links para a internet: rota padrão principal + rota flutuante de *backup*; derrube o principal e confirme a troca.
- [ ] **E9.7.4** Rotas estáticas IPv6 no mesmo cenário.

---

## Módulo 9.8 — OSPF (1,5 semana)

### Conceitos
- [ ] Estado de enlace: LSAs, LSDB, algoritmo **SPF** (Dijkstra — você implementou na trilha 4!)
- [ ] **OSPFv2 em área única**: *router ID*, vizinhança e **adjacência** (estados), pacotes *hello*, temporizadores *hello*/*dead*
- [ ] Tipos de rede: *broadcast* (eleição de DR/BDR, prioridade) e ponto a ponto
- [ ] Custo e largura de banda de referência
- [ ] Configuração: `router ospf`, `network` com *wildcard* ou `ip ospf <processo> area <área>` na interface; interfaces passivas; divulgar rota padrão (`default-information originate`)
- [ ] Requisitos para formar vizinhança (área, sub-rede, temporizadores, MTU, autenticação, *router ID* único)
- [ ] Verificação e *troubleshooting*: `show ip ospf neighbor`, `show ip ospf interface`, `show ip protocols`, `show ip route ospf`
- [ ] OSPFv3 e multiárea (noções; aprofundado no CCNP)

### Fontes
- 🎥 Jeremy's IT Lab — aulas de OSPF (partes 1 a 3).
- 📘 Odom vol. 2 — parte I (*OSPF*).

### Exercícios
- [ ] **E9.8.1** 5 roteadores em OSPF área 0, com interfaces passivas nas LANs e rota padrão divulgada pelo roteador de borda.
- [ ] **E9.8.2** Em um segmento *broadcast* com 4 roteadores, **preveja** o DR e o BDR; depois altere prioridades para escolher outros.
- [ ] **E9.8.3** Ajuste custos para forçar o tráfego por um caminho específico; mude a largura de banda de referência.
- [ ] **E9.8.4** **Troubleshooting:** 6 cenários em que a vizinhança não forma (área diferente, *hello* diferente, sub-rede diferente, MTU, interface passiva por engano, *router ID* duplicado).
- [ ] **E9.8.5** Explique por escrito a relação entre o SPF do OSPF e o Dijkstra que você implementou.

### Autoavaliação
1. O que precisa ser igual para dois roteadores formarem vizinhança OSPF?
2. Como é escolhido o *router ID*?
3. Para que servem DR e BDR?
4. Como o OSPF calcula o custo de uma interface?

---

## Módulo 9.9 — Redundância de primeiro salto e WAN (1 semana)

### Conceitos
- [ ] **FHRP**: por que o *gateway* é ponto único de falha; **HSRP** (ativo/*standby*, IP e MAC virtuais, prioridade, *preempt*), VRRP e GLBP (comparação)
- [ ] Conceitos de WAN: MPLS, Metro Ethernet, banda larga, 4G/5G, VPNs (*site-to-site* e acesso remoto), **SD-WAN** (visão geral)
- [ ] Conectividade com a internet: IP público, PPPoE (visão geral)

### Fontes
- 🎥 Jeremy's IT Lab — aulas de FHRP e WAN.
- 📘 Odom vol. 2 — partes sobre FHRP e WAN.

### Exercícios
- [ ] **E9.9.1** HSRP entre dois roteadores para a LAN; desligue o ativo durante um `ping -t` e conte as perdas.
- [ ] **E9.9.2** Configure *preempt* e prioridades para que o roteador principal reassuma ao voltar.
- [ ] **E9.9.3** Tabela comparando HSRP, VRRP e GLBP.

---

## Módulo 9.10 — Serviços IP (1,5 semana)

### Conceitos
- [ ] **DHCP**: DORA, servidor DHCP no roteador (pools, exclusões, *gateway*, DNS), **DHCP relay** (`ip helper-address`)
- [ ] **DNS**: papel na rede, configuração do cliente no IOS
- [ ] **NAT**: estático, dinâmico, **PAT** (*overload*); *inside/outside local/global*
- [ ] **NTP**: cliente e servidor, estratos; por que o horário importa (logs, certificados)
- [ ] **SNMP**: *manager*, agente, MIB, OIDs, *traps*; v2c x **v3** (ponte com o Zabbix, trilha 8)
- [ ] **Syslog**: níveis de severidade (0 a 7), envio para um servidor
- [ ] **QoS** (conceitos): classificação, marcação (DSCP), filas, *policing* x *shaping*, voz e vídeo
- [ ] **SSH** (revisão) e **TFTP/FTP** para transferir arquivos

### Fontes
- 🎥 Jeremy's IT Lab — aulas de DHCP, DNS, NAT, NTP, SNMP, Syslog, QoS.
- 📘 Odom vol. 2 — parte III (*IP Services*).

### Exercícios
- [ ] **E9.10.1** DHCP no roteador para 3 VLANs, com o servidor em uma VLAN diferente (use *relay*).
- [ ] **E9.10.2** PAT para a rede interna sair para a "internet"; NAT estático para publicar um servidor web interno. Verifique com `show ip nat translations`.
- [ ] **E9.10.3** NTP: um roteador como servidor, os demais como clientes; confira os horários nos logs.
- [ ] **E9.10.4** Syslog de todos os equipamentos para um servidor (no Packet Tracer ou em uma VM Linux com `rsyslog`).
- [ ] **E9.10.5** SNMPv3 no roteador e coleta pelo **Zabbix** do laboratório (junta com o módulo 8.4).
- [ ] **E9.10.6** Decore os 8 níveis de severidade do Syslog (0 = *emergencies* … 7 = *debugging*).

### Autoavaliação
1. Quais as 4 mensagens do DHCP e para que serve o *relay*?
2. Qual a diferença entre NAT estático, dinâmico e PAT?
3. O que significam *inside local* e *inside global*?
4. Por que o NTP é importante para a segurança e o diagnóstico?

---

## Módulo 9.11 — Fundamentos de segurança de infraestrutura (1,5 semana)

### Conceitos
- [ ] Conceitos: ameaças, vulnerabilidades, mitigação; programas de conscientização; controle de acesso físico
- [ ] Senhas: políticas, complexidade, MFA, certificados, biometria (conceitos)
- [ ] **AAA**: autenticação, autorização, registro; **RADIUS** x **TACACS+**
- [ ] **ACLs IPv4**: padrão e estendidas, numeradas e nomeadas; *wildcard masks*; regra implícita *deny*; posicionamento (padrão perto do destino, estendida perto da origem); ACL nas linhas VTY
- [ ] **Segurança de camada 2**: **port security** (limite de MACs, *sticky*, violações), **DHCP snooping**, **Dynamic ARP Inspection (DAI)**
- [ ] VPNs: IPsec *site-to-site* e acesso remoto (conceitos)
- [ ] **Redes sem fio**: segurança (WPA2, **WPA3**, PSK x Enterprise/802.1X)
- [ ] Endurecimento de dispositivos: desativar serviços não usados, SSH só versão 2, *banners*, senhas criptografadas

### Fontes
- 🎥 Jeremy's IT Lab — aulas de ACLs, *port security*, DHCP snooping, DAI, conceitos de segurança.
- 📘 Odom vol. 2 — parte II (*Security Services*).

### Exercícios
- [ ] **E9.11.1** 30 exercícios de *wildcard mask*.
- [ ] **E9.11.2** ACL padrão que permite só a rede de administração acessar os equipamentos por SSH (nas linhas VTY).
- [ ] **E9.11.3** ACL estendida nomeada: a VLAN de visitantes acessa só a internet (HTTP/HTTPS/DNS), sem acesso às redes internas.
- [ ] **E9.11.4** *Port security* nas portas de usuário (máximo de 2 MACs, *sticky*, violação em *restrict*); teste a violação.
- [ ] **E9.11.5** DHCP snooping + DAI na VLAN de usuários; mostre um servidor DHCP não autorizado sendo bloqueado.
- [ ] **E9.11.6** Checklist de *hardening* de switch/roteador e aplique em todos os equipamentos do laboratório.
- [ ] **E9.11.7** Leia as regras de uma ACL com 10 linhas e diga, para 10 pacotes diferentes, se passam ou não.

### Autoavaliação
1. Onde posicionar uma ACL padrão e uma estendida? Por quê?
2. O que existe no fim de toda ACL?
3. RADIUS x TACACS+: diferenças.
4. Que ataque o DHCP snooping previne? E o DAI?
5. WPA2 x WPA3: o que melhorou?

---

## Módulo 9.12 — Redes sem fio (1 semana)

### Conceitos
- [ ] Princípios de RF: frequências (2,4 GHz, 5 GHz, 6 GHz), canais e sobreposição, interferência, potência
- [ ] Padrões 802.11 (a/b/g/n/ac/ax — Wi-Fi 6/6E — e be — Wi-Fi 7)
- [ ] SSID, BSS, ESS, *roaming*
- [ ] Arquiteturas: AP autônomo, AP leve (*lightweight*) + **WLC** (CAPWAP), gerenciado pela nuvem
- [ ] Modos de AP; conexões físicas do WLC (portas, LAG); acesso de gerência (HTTPS, SSH, TACACS+/RADIUS)
- [ ] Configurar uma WLAN no WLC (GUI): SSID, segurança WPA2/WPA3-PSK, perfis de QoS, configurações avançadas

### Fontes
- 🎥 Jeremy's IT Lab — aulas de Wireless (partes 1 a 4).
- 📘 Odom vol. 2 — parte I (*Wireless LANs*).

### Exercícios
- [ ] **E9.12.1** Com um app de análise de Wi-Fi no celular, mapeie as redes da sua casa ou de um cliente: canais, sobreposição, intensidade do sinal. Proponha um plano de canais.
- [ ] **E9.12.2** No Packet Tracer: WLC + 2 APs leves, 2 WLANs (corporativa e visitantes) em VLANs separadas.
- [ ] **E9.12.3** Tabela comparando os padrões 802.11 (frequências, velocidades teóricas).

---

## Módulo 9.13 — Automação, programabilidade, IA e operações de rede (1,5 semana)

> No blueprint **v2.0**, esse conteúdo aparece junto com operações de rede e ganha um domínio dedicado a **IA** (10%). É aqui que as trilhas de programação viram um diferencial enorme.

### Conceitos
- [ ] Por que automatizar; impacto na gestão da rede
- [ ] Redes tradicionais x **controladores** e **SDN**: planos de dados, de controle e de gerência; *overlay*, *underlay*, *fabric*; APIs *northbound* e *southbound*
- [ ] **Cisco Catalyst Center** (antigo DNA Center) e gerenciamento pela nuvem (visão geral)
- [ ] **APIs REST**: métodos, códigos, autenticação; **JSON** (e ler/interpretar estruturas JSON), XML, YAML
- [ ] Gerenciamento de configuração: **Ansible** e **Terraform** para redes (conceitos)
- [ ] NETCONF, RESTCONF, YANG (visão geral; aprofundado no CCNA Automation)
- [ ] Python para redes: **Netmiko**, NAPALM, `requests` contra APIs
- [ ] **IA e ML em operações de rede**: IA generativa x preditiva, detecção de anomalias, análise de causa raiz, uso responsável de assistentes de IA para configuração e diagnóstico (conferir sempre o que a IA gera)

### Fontes
- 🎥 Jeremy's IT Lab — aulas de automação, SDN, REST, JSON, Ansible.
- 📘 Odom vol. 2 — parte V (*Network Automation*).
- 🌐 [Cisco DevNet](https://developer.cisco.com/) — *learning labs* e **Sandbox** gratuitos.
- 📘 *Network Programmability and Automation* (2ª ed.) — Edelman, Lowe e Oswalt
- 🌐 [Netmiko (GitHub)](https://github.com/ktbyers/netmiko) · [NAPALM — docs](https://napalm.readthedocs.io/)
- 🌐 [Ansible — Network Automation](https://docs.ansible.com/ansible/latest/network/index.html)

### Exercícios
- [ ] **E9.13.1** Interprete 10 estruturas JSON (objetos aninhados, listas) respondendo perguntas sobre elas.
- [ ] **E9.13.2** Script Python com **Netmiko** que entra em todos os equipamentos do laboratório (GNS3/CML ou DevNet Sandbox), coleta `show ip interface brief` e gera um relatório.
- [ ] **E9.13.3** Script de **backup automático de configurações** para um repositório Git, com diff entre versões (ótimo serviço para clientes).
- [ ] **E9.13.4** Playbook **Ansible** que configura VLANs e *banners* em vários switches.
- [ ] **E9.13.5** Consulte a API REST de um equipamento/controlador no DevNet Sandbox com `requests` e com `curl`.
- [ ] **E9.13.6** Use um assistente de IA para gerar a configuração de um cenário, depois **revise e encontre os erros** antes de aplicar. Documente o que a IA errou.
- [ ] **E9.13.7** Desenhe a diferença entre os planos de dados, controle e gerência em uma rede tradicional e em uma SDN.

### Autoavaliação
1. O que são as APIs *northbound* e *southbound*?
2. Qual a diferença entre *overlay* e *underlay*?
3. Quais vantagens a automação traz em relação à configuração manual?
4. Quais os riscos de aplicar configurações geradas por IA sem revisão?

---

## Módulo 9.14 — Revisão, laboratórios integrados e simulados (4–6 semanas)

### Laboratórios integrados (faça sem olhar nenhuma solução)
- [ ] **L1 — Pequena empresa:** 1 roteador, 2 switches, 3 VLANs, *router-on-a-stick*, DHCP, PAT, SSH, *port security*, NTP, Syslog.
- [ ] **L2 — Empresa com filial:** 2 sites ligados por WAN, OSPF, HSRP na matriz, switch L3, EtherChannel, Rapid PVST+ ajustado, ACLs entre departamentos, rota padrão para a internet com *backup*.
- [ ] **L3 — Dual-stack:** o L2 com IPv6 (SLAAC + rotas estáticas IPv6 ou OSPFv3).
- [ ] **L4 — Troubleshooting:** peça a alguém (ou à IA) para "quebrar" o L2 com 10 falhas e resolva todas, registrando o raciocínio.
- [ ] **L5 — Laboratórios de revisão do Jeremy's IT Lab** (os do fim do curso).

### Simulados
- [ ] Faça os simulados **por tema** primeiro, depois os completos com tempo cronometrado.
- [ ] Planilha de erros: questão → tópico → por que errei → o que revisei.
- [ ] Meta: **≥ 85–90% em 3 simulados completos seguidos** antes de marcar a prova.

### Revisão final
- [ ] Refaça todos os cartões do Anki até não errar.
- [ ] Revise o blueprint oficial item por item e marque o que ainda está fraco.
- [ ] Revise os tópicos mais cobrados: sub-redes, OSPF, STP, ACLs, NAT, VLANs, IPv6, *wireless*.
- [ ] Na semana da prova: laboratórios leves e descanso. Nada de conteúdo novo.

---

## Projetos finais

### Projeto A — Rede completa de um cliente fictício (portfólio)
"Clínica Saúde+": 3 andares, recepção com Wi-Fi para visitantes, rede administrativa, VoIP, câmeras, servidor de arquivos (NAS), filial ligada por VPN.
- Documento de levantamento de requisitos.
- Plano de endereçamento IPv4 (VLSM) e IPv6.
- Topologia física e lógica (diagramas).
- Implementação completa no Packet Tracer ou CML (VLANs, STP, EtherChannel, OSPF, HSRP, DHCP, NAT, ACLs, *port security*, DHCP snooping, WLC com 2 WLANs, NTP, Syslog, SNMPv3, SSH).
- Monitoramento dos equipamentos pelo **Zabbix** (trilha 8).
- Backup automático das configurações com Python + Git.
- Documentação de entrega ao cliente (*as built*).

### Projeto B — Ferramentas de automação para o dia a dia
Pacote Python com CLI: backup de configurações, inventário (modelo, versão do IOS, número de série), verificação de conformidade (ex.: "todos os equipamentos têm SSH v2 e NTP configurados?") e relatório HTML.

### Projeto C — Gerador de exercícios de sub-rede (web)
Evolua o E9.3.2 para uma aplicação web (React + API) com modos de treino, cronômetro e estatísticas. Junta as trilhas 1–4 com a 9.

---

## Depois do CCNA

| Próximo passo | Conteúdo principal | Fontes |
|---------------|--------------------|--------|
| **CCNA Automation** (antigo DevNet Associate) | Python, APIs, Git, containers, CI/CD, NETCONF/RESTCONF/YANG, plataformas Cisco, segurança de aplicações | [Cisco DevNet](https://developer.cisco.com/), Sandbox, guia oficial da Cisco Press |
| **CCNP Enterprise — ENCOR** (350-401) | Arquitetura, virtualização, infraestrutura (EIGRP, OSPF avançado, BGP), *wireless*, SD-Access/SD-WAN, segurança, automação | *CCNP and CCIE Enterprise Core ENCOR Official Cert Guide* (Cisco Press), laboratórios no CML/EVE-NG |
| **CCNP Enterprise — ENARSI** (300-410) | Roteamento avançado e serviços (OSPF, EIGRP, BGP, redistribuição, VPN, segurança de infraestrutura, *troubleshooting*) | *CCNP Enterprise Advanced Routing ENARSI Official Cert Guide* |
| **CCNA Cybersecurity** (antigo CyberOps Associate) | Operações de segurança, monitoramento, análise de eventos | Cisco NetAcad, guia oficial da Cisco Press |

> Como as certificações Cisco mudaram bastante em 2026, **confira sempre o nome, o código e o blueprint vigente** no [Cisco Learning Network](https://learningnetwork.cisco.com/) antes de começar a estudar para qualquer uma delas.

---

## ✅ Checklist de conclusão da Trilha 9
- [ ] Curso do Jeremy's IT Lab completo (aulas + laboratórios + Anki)
- [ ] Odom vol. 1 e 2 lidos
- [ ] 200+ exercícios de sub-rede com tempo < 30 s
- [ ] Laboratórios integrados L1–L5 feitos sem consulta
- [ ] ≥ 85–90% em 3 simulados completos seguidos
- [ ] **Certificação CCNA**
- [ ] Projeto "Clínica Saúde+" publicado no repositório
- [ ] Próximo passo escolhido: CCNA Automation, CCNP Enterprise ou CCNA Cybersecurity
