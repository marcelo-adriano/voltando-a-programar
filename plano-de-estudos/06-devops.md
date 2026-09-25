# Trilha 6 — DevOps e SRE

> **Objetivo da trilha:** entregar software de forma rápida, segura e confiável: administrar Linux, automatizar infraestrutura, construir pipelines de CI/CD, operar containers e Kubernetes, trabalhar em nuvem e manter sistemas saudáveis com observabilidade e práticas de SRE.
>
> DevOps não é um cargo nem uma ferramenta: é cultura + práticas + automação para reduzir o tempo entre "ideia" e "em produção, funcionando".

**Duração:** 14–18 semanas · **Pré-requisitos:** Trilha 0 (Linux, Git, redes), Módulos 3.2–3.3 (Docker). A trilha 9 (redes Cisco) ajuda muito.

| Módulo | Tema | Duração |
|--------|------|---------|
| 6.1 | Cultura DevOps, métricas DORA e fluxo de valor | 3 dias |
| 6.2 | Administração Linux a fundo | 2 semanas |
| 6.3 | Redes para DevOps: DNS, TLS, proxy reverso e balanceamento | 1 semana |
| 6.4 | Homelab e virtualização | 1 semana |
| 6.5 | Containers em produção | 1 semana |
| 6.6 | CI/CD com GitHub Actions | 1,5 semana |
| 6.7 | Gerenciamento de configuração com Ansible | 1,5 semana |
| 6.8 | Infraestrutura como código com Terraform | 1,5 semana |
| 6.9 | Computação em nuvem (AWS) | 2 semanas |
| 6.10 | Kubernetes | 2,5 semanas |
| 6.11 | Observabilidade: métricas, logs e *traces* | 1,5 semana |
| 6.12 | SRE: SLIs, SLOs, incidentes e *postmortems* | 1 semana |
| 6.13 | GitOps, DevSecOps e plataformas | 1 semana |
| 6.14 | Projetos finais | 2–3 semanas |

### Fontes principais da trilha
- 🌐 [roadmap.sh — DevOps](https://roadmap.sh/devops)
- 🌐 [90DaysOfDevOps — Michael Cade (GitHub)](https://github.com/MichaelCade/90DaysOfDevOps): currículo gratuito, um tema por dia.
- 🌐 [DevOps Exercises — Arie Bregman (GitHub)](https://github.com/bregman-arie/devops-exercises): **milhares de perguntas e exercícios** de Linux, redes, Docker, Kubernetes, AWS, Terraform, Ansible. Ótimo para autoavaliação.
- 📘 *O Projeto Fênix* (The Phoenix Project) — Kim, Behr e Spafford: romance sobre DevOps. Comece por ele.
- 📘 *Manual de DevOps* (The DevOps Handbook) — Kim, Humble, Debois, Willis e Forsgren
- 📘 *Accelerate* — Forsgren, Humble e Kim
- 📘 [*Site Reliability Engineering* e *The Site Reliability Workbook* — Google (gratuitos)](https://sre.google/books/)
- 🎥🇧🇷 [LINUXtips (Jeferson Fernando)](https://www.youtube.com/@LINUXtips): Linux, Docker, Kubernetes, DevOps (tem livros gratuitos no GitHub, como o *Descomplicando o Kubernetes*).
- 🧪 [KodeKloud](https://kodekloud.com/) 💲 (tem planos gratuitos com laboratórios) · 🧪 [Killercoda](https://killercoda.com/) (laboratórios gratuitos no navegador) · 🧪 [SadServers](https://sadservers.com/)

---

## Módulo 6.1 — Cultura DevOps, métricas DORA e fluxo de valor (3 dias)

### Conceitos
- [ ] Origem do DevOps: o "muro da confusão" entre desenvolvimento e operações
- [ ] **As Três Maneiras**: fluxo, *feedback*, aprendizado contínuo
- [ ] **CALMS**: cultura, automação, *lean*, medição, compartilhamento
- [ ] **Métricas DORA**: frequência de deploy, *lead time* de mudanças, taxa de falha de mudanças, tempo de recuperação
- [ ] Integração contínua, entrega contínua e implantação contínua (diferenças)
- [ ] Mapeamento de fluxo de valor (*value stream mapping*)
- [ ] *Trunk-based development* x *feature branches*; *feature flags*
- [ ] *Platform engineering* e *Team Topologies* (visão geral)

### Fontes
- 📘 *O Projeto Fênix* (leitura completa).
- 🌐 [DORA — Research](https://dora.dev/research/) e o relatório *State of DevOps* mais recente.
- 🌐 [Martin Fowler — Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)
- 🌐 [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/)
- 📘 *Team Topologies* — Skelton e Pais

### Exercícios
- [ ] **E6.1.1** Leia *O Projeto Fênix* e escreva as 3 Maneiras com exemplos do livro.
- [ ] **E6.1.2** Mapeie o fluxo de valor do projeto integrador: do commit até estar no ar. Onde estão as esperas?
- [ ] **E6.1.3** Calcule as métricas DORA do seu repositório (commits, deploys, falhas) no último mês.

---

## Módulo 6.2 — Administração Linux a fundo (2 semanas)

### Conceitos
- [ ] Processo de boot: firmware (BIOS/UEFI), bootloader (GRUB), kernel, `initramfs`, **systemd**
- [ ] **systemd**: *units* (service, timer, socket, target), criar um serviço próprio, dependências, `journalctl` (filtros por unidade, tempo, prioridade)
- [ ] Usuários, grupos, `sudoers`, PAM (visão geral)
- [ ] Permissões avançadas: SUID, SGID, *sticky bit*, ACLs (`setfacl`)
- [ ] Pacotes: `apt`/`dpkg`, `dnf`/`rpm`; repositórios; atualizações automáticas
- [ ] **Armazenamento**: partições (`fdisk`, `parted`), sistemas de arquivos (ext4, XFS, Btrfs), `/etc/fstab`, **LVM** (PV, VG, LV, redimensionamento), RAID por software (`mdadm`), *swap*, cotas
- [ ] **Redes no Linux**: `ip` (addr, link, route), `ss`, `nmcli`/Netplan, `/etc/hosts`, `resolv.conf`, `systemd-resolved`, *bonding*, VLANs no Linux
- [ ] **Firewall**: `nftables`/`iptables`, `ufw`, `firewalld`
- [ ] **SSH** avançado: `sshd_config`, *jump hosts*, túneis (`-L`, `-R`, `-D`), `fail2ban`
- [ ] Desempenho e diagnóstico: `top`/`htop`, `vmstat`, `iostat`, `sar`, `free`, `lsof`, `strace`, `dmesg`, *load average*, OOM killer
- [ ] Logs: `rsyslog`, `logrotate`
- [ ] Agendamento: `cron` x *systemd timers*
- [ ] Segurança básica: atualizações, SELinux/AppArmor (conceito), CIS Benchmarks (ponte com a trilha 7)
- [ ] Kernel: módulos, `sysctl`

### Fontes
- 📘 *Linux Bible* — Christopher Negus
- 📘 *How Linux Works* (3ª ed.) — Brian Ward: **excelente para entender o sistema por dentro**.
- 📘 *UNIX and Linux System Administration Handbook* — Nemeth et al. (referência)
- 🌐 [Arch Wiki](https://wiki.archlinux.org/): a melhor documentação de Linux, útil para qualquer distribuição.
- 🌐 [Red Hat — documentação do RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/)
- 🌐 [Brendan Gregg — Linux Performance](https://www.brendangregg.com/linuxperf.html)
- 🧪 [SadServers](https://sadservers.com/): **resolva 20 cenários** (fáceis e médios).
- 🧪 [OverTheWire — Bandit](https://overthewire.org/wargames/bandit/) até o fim (nível 34).
- 🎥🇧🇷 LINUXtips — *Descomplicando o Linux*.

### Exercícios
- [ ] **E6.2.1** Crie um serviço systemd para a API da loja (reinício automático, usuário dedicado, variáveis de ambiente, limites de recursos).
- [ ] **E6.2.2** Substitua o `cron` do script de backup por um *systemd timer* com log no journal.
- [ ] **E6.2.3** Em uma VM com 2 discos extras: crie LVM, um volume lógico, formate, monte via `fstab`, depois **aumente** o volume com o sistema rodando.
- [ ] **E6.2.4** Crie um RAID 1 com `mdadm`, simule a falha de um disco e reconstrua.
- [ ] **E6.2.5** Configure IP fixo com Netplan (ou `nmcli`) e uma rota estática.
- [ ] **E6.2.6** Firewall com `nftables` ou `ufw`: liberar só SSH, HTTP e HTTPS; registrar os bloqueios.
- [ ] **E6.2.7** Instale o `fail2ban` para o SSH e teste (de outra máquina sua) sendo bloqueado.
- [ ] **E6.2.8** Túnel SSH para acessar um banco que só escuta em `localhost` no servidor.
- [ ] **E6.2.9** Descubra com `strace` quais arquivos um programa abre ao iniciar.
- [ ] **E6.2.10** Provoque alto uso de CPU, de memória e de disco (ferramenta `stress-ng`) e identifique cada um com as ferramentas de diagnóstico.
- [ ] **E6.2.11** Complete o Bandit até o nível 34.
- [ ] **E6.2.12** Resolva 20 cenários do SadServers e anote o raciocínio de cada um.
- [ ] **E6.2.13** Configure o `logrotate` para os logs da sua aplicação.
- [ ] **E6.2.14** 50 perguntas da seção Linux do DevOps Exercises.

### Autoavaliação
1. Descreva o processo de boot do Linux até o login.
2. Qual a diferença entre um *service* e um *timer* no systemd?
3. Para que serve o LVM? Qual a vantagem sobre partições fixas?
4. O que significa um *load average* de 4.0 em uma máquina com 2 CPUs?
5. O que é o OOM killer?
6. O que é o bit SUID e por que é um risco de segurança?

### Certificações relacionadas (opcional)
- **LPIC-1** (Linux Professional Institute; exames 101 e 102) ou **LFCS** (Linux Foundation Certified System Administrator, prova prática).
- **RHCSA** (Red Hat, prova prática; muito valorizada no mercado).

---

## Módulo 6.3 — Redes para DevOps: DNS, TLS, proxy reverso e balanceamento (1 semana)

> Se você já fez a trilha 9 (CCNA), revise só os tópicos de aplicação.

### Conceitos
- [ ] Revisão: TCP/IP, sub-redes, NAT, portas (ver trilha 0.5 e trilha 9)
- [ ] **DNS** a fundo: zonas, registros, TTL, DNS autoritativo x recursivo; servidor próprio (Bind ou CoreDNS) e DNS local (Pi-hole/AdGuard Home)
- [ ] **TLS**: certificados, cadeia de confiança, CA, **Let's Encrypt** e ACME (Certbot), mTLS
- [ ] **Proxy reverso**: **Nginx** (server blocks, `proxy_pass`, cabeçalhos, compressão, cache), Caddy, Traefik
- [ ] **Balanceamento de carga**: camada 4 x 7, algoritmos, *health checks*, *sticky sessions*; HAProxy
- [ ] VPN: WireGuard
- [ ] *Forward proxy* (Squid), que você já instala para clientes

### Fontes
- 🌐 [Nginx — documentação](https://nginx.org/en/docs/) e [Nginx Beginner's Guide](https://nginx.org/en/docs/beginners_guide.html)
- 🌐 [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
- 🌐 [Let's Encrypt — How It Works](https://letsencrypt.org/pt-br/how-it-works/) 🇧🇷
- 🌐 [HAProxy — docs](https://docs.haproxy.org/)
- 🌐 [WireGuard — Quick Start](https://www.wireguard.com/quickstart/)
- 🌐 [Julia Evans — zines sobre DNS, HTTP, redes](https://wizardzines.com/) (didáticos)
- 🌐 [SSL Labs — Server Test](https://www.ssllabs.com/ssltest/)

### Exercícios
- [ ] **E6.3.1** Nginx como proxy reverso para o front e a API do projeto integrador, com gzip, cabeçalhos de segurança e cache de estáticos.
- [ ] **E6.3.2** HTTPS com Let's Encrypt em um domínio seu (ou certificado autoassinado + CA própria em laboratório); nota A no SSL Labs.
- [ ] **E6.3.3** Balanceamento entre 3 instâncias da API com Nginx e depois com HAProxy; derrube uma e observe o *health check*.
- [ ] **E6.3.4** Servidor DNS local para o homelab (`*.lab.local`).
- [ ] **E6.3.5** VPN WireGuard para acessar o homelab de fora.
- [ ] **E6.3.6** Crie uma CA própria com `openssl`, emita um certificado de servidor e configure mTLS entre dois serviços.

### Autoavaliação
1. O que acontece em um *handshake* TLS (resumo)?
2. Qual a diferença entre proxy reverso e *forward proxy*?
3. Balanceamento camada 4 x camada 7: diferenças e exemplos.
4. Por que um TTL alto de DNS atrapalha uma migração?

---

## Módulo 6.4 — Homelab e virtualização (1 semana)

> Um homelab é o seu laboratório para todas as trilhas de infraestrutura (DevOps, Segurança, Zabbix, Cisco). Como você trabalha com NAS e redes, ele também vira vitrine de serviços.

### Conceitos
- [ ] Virtualização: hipervisores tipo 1 x tipo 2; KVM/QEMU, **Proxmox VE**, VirtualBox, VMware
- [ ] VMs x containers LXC
- [ ] Templates, *snapshots*, clones, *cloud-init*
- [ ] Rede virtual: bridges, VLANs no Proxmox
- [ ] Armazenamento: ZFS (visão geral), NFS, SMB, iSCSI; **TrueNAS**
- [ ] Backup de VMs (Proxmox Backup Server)
- [ ] Hardware: mini PCs usados, consumo de energia

### Fontes
- 🌐 [Proxmox VE — documentação](https://pve.proxmox.com/pve-docs/) e [wiki](https://pve.proxmox.com/wiki/Main_Page)
- 🌐 [TrueNAS — documentação](https://www.truenas.com/docs/)
- 🌐 [r/homelab](https://www.reddit.com/r/homelab/) e [r/selfhosted](https://www.reddit.com/r/selfhosted/)
- 🎥 [Techno Tim](https://www.youtube.com/@TechnoTim), [Jeff Geerling](https://www.youtube.com/@JeffGeerling), [Lawrence Systems](https://www.youtube.com/@LAWRENCESYSTEMS)
- 🌐 [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)

### Exercícios
- [ ] **E6.4.1** Instale o Proxmox em um PC ou mini PC (ou aninhado em uma VM, só para testes).
- [ ] **E6.4.2** Crie um template Ubuntu com *cloud-init* e clone 3 VMs a partir dele.
- [ ] **E6.4.3** Configure 2 VLANs no Proxmox (gerência e serviços).
- [ ] **E6.4.4** Suba um TrueNAS (ou compartilhamento NFS/SMB) e use-o como destino do seu script de backup.
- [ ] **E6.4.5** Configure backups agendados das VMs e **teste a restauração**.
- [ ] **E6.4.6** Documente o homelab no repositório `homelab` (diagrama, IPs, serviços, como recriar).

---

## Módulo 6.5 — Containers em produção (1 semana)

### Conceitos
- [ ] Revisão dos módulos 3.2 e 3.3 (Docker e Compose)
- [ ] Como containers funcionam: *namespaces*, *cgroups*, *union filesystems*, OCI
- [ ] *Runtimes*: containerd, runc; **Podman** (sem daemon, *rootless*)
- [ ] Registros privados (GitHub Container Registry, Harbor); estratégia de tags (SemVer + SHA do commit)
- [ ] Imagens seguras e pequenas: *multi-stage*, *distroless*, usuário não-root, *read-only filesystem*, *capabilities*
- [ ] Varredura de vulnerabilidades (Trivy, Grype) e SBOM (Syft)
- [ ] Assinatura de imagens (cosign)
- [ ] Limites de recursos (CPU e memória)
- [ ] Logs de containers e *log drivers*
- [ ] Deploy simples com Docker Compose em um VPS; Docker Swarm (visão geral)

### Fontes
- 🌐 [Docker — Security](https://docs.docker.com/engine/security/)
- 🌐 [Podman — docs](https://docs.podman.io/)
- 🌐 [Trivy — docs](https://trivy.dev/)
- 🌐 [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- 🌐 [Julia Evans — "What even is a container"](https://jvns.ca/blog/2016/10/10/what-even-is-a-container/)
- 🎥 [Liz Rice — Containers from Scratch (palestra)](https://www.youtube.com/watch?v=8fi7uSYlOdc)

### Exercícios
- [ ] **E6.5.1** Crie um "container" à mão com `unshare` e `chroot` (siga a palestra da Liz Rice).
- [ ] **E6.5.2** Rode o projeto integrador com Podman *rootless*.
- [ ] **E6.5.3** Reduza a imagem da API ao mínimo (*distroless* ou Alpine) e rode com sistema de arquivos somente leitura e sem *capabilities*.
- [ ] **E6.5.4** Gere o SBOM da imagem, varra com Trivy e assine com cosign.
- [ ] **E6.5.5** Faça deploy do projeto integrador em um VPS barato com Docker Compose, Nginx e HTTPS.

---

## Módulo 6.6 — CI/CD com GitHub Actions (1,5 semana)

### Conceitos
- [ ] Pipeline: etapas (lint → testes → build → varredura de segurança → publicação do artefato → deploy)
- [ ] **GitHub Actions**: *workflows*, *events* (`push`, `pull_request`, `workflow_dispatch`, `schedule`), *jobs*, *steps*, *runners*, *actions* do Marketplace
- [ ] Matriz de versões (`strategy.matrix`)
- [ ] Cache de dependências
- [ ] Artefatos e *outputs* entre jobs
- [ ] **Segredos** e **environments** (com aprovação manual para produção)
- [ ] OIDC para autenticar na nuvem **sem** chaves de longa duração
- [ ] *Reusable workflows* e *composite actions*
- [ ] *Self-hosted runners* (e seus riscos de segurança)
- [ ] Estratégias de deploy: *rolling*, **blue-green**, **canary**, *feature flags*; *rollback*
- [ ] Versionamento automático e *changelog* (semantic-release, release-please)
- [ ] Proteção de branch, *required checks*, Dependabot/Renovate
- [ ] Outras ferramentas: GitLab CI, Jenkins (legado, ainda muito usado), Azure DevOps

### Fontes
- 🌐 [GitHub Actions — documentação](https://docs.github.com/pt/actions) 🇧🇷
- 🌐 [GitHub Skills — cursos de Actions](https://skills.github.com/)
- 🌐 [GitHub — Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
- 📘 *Continuous Delivery* — Jez Humble e David Farley
- 🌐 [GitLab CI/CD — docs](https://docs.gitlab.com/ci/)
- 🌐 [Martin Fowler — Blue Green Deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) e [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html)

### Exercícios
- [ ] **E6.6.1** *Workflow* de CI para a lista de tarefas (trilha 1): lint, testes e cobertura em cada PR.
- [ ] **E6.6.2** Matriz testando a API da loja em 2 versões do Node e com MySQL como *service container*.
- [ ] **E6.6.3** Cache de dependências e compare o tempo do pipeline antes e depois.
- [ ] **E6.6.4** Build e publicação da imagem Docker no GHCR com tags `sha-<commit>` e `vX.Y.Z` a cada *release*.
- [ ] **E6.6.5** Varredura com Trivy que **falha o pipeline** se houver vulnerabilidade crítica.
- [ ] **E6.6.6** Deploy automático no VPS (via SSH) quando há merge na `main`, com *environment* de produção exigindo aprovação.
- [ ] **E6.6.7** Deploy da SPA no GitHub Pages a cada merge.
- [ ] **E6.6.8** *Reusable workflow* compartilhado entre os seus projetos Node.
- [ ] **E6.6.9** Versionamento semântico automático com release-please e *changelog*.
- [ ] **E6.6.10** Configure Dependabot ou Renovate nos repositórios.
- [ ] **E6.6.11** Deploy *blue-green* no VPS com Nginx alternando entre duas versões, com *rollback* em um comando.

### Autoavaliação
1. Qual a diferença entre entrega contínua e implantação contínua?
2. Por que usar OIDC em vez de guardar chaves da nuvem nos segredos?
3. Qual o risco de um *self-hosted runner* em repositório público?
4. *Blue-green* x *canary*: diferenças e quando usar cada um.
5. O que deve fazer um pipeline falhar?

---

## Módulo 6.7 — Gerenciamento de configuração com Ansible (1,5 semana)

### Conceitos
- [ ] Por que gerenciamento de configuração; configuração manual x automatizada; **idempotência**
- [ ] Ansible: *agentless*, SSH; **inventário** (estático, dinâmico, grupos, variáveis de grupo e host)
- [ ] Comandos *ad hoc*
- [ ] **Playbooks**: *plays*, *tasks*, módulos (`apt`, `copy`, `template`, `service`, `user`, `file`, `lineinfile`, `git`, `docker_container`), *handlers*
- [ ] Variáveis, *facts*, precedência de variáveis
- [ ] *Templates* Jinja2
- [ ] Condicionais, laços, *tags*, `--check` e `--diff`
- [ ] **Roles** e estrutura de diretórios; Ansible Galaxy
- [ ] **Ansible Vault** para segredos
- [ ] Testes de *roles* com Molecule
- [ ] Ansible para redes (Cisco IOS; ponte com a trilha 9)

### Fontes
- 🌐 [Ansible — documentação](https://docs.ansible.com/) — *Getting started* e *Playbook guide*.
- 📘 *Ansible for DevOps* — Jeff Geerling · 🎥 [série "Ansible 101" de Jeff Geerling (YouTube, gratuita)](https://www.youtube.com/playlist?list=PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN)
- 🌐 [Molecule — docs](https://ansible.readthedocs.io/projects/molecule/)
- 🧪 KodeKloud / Killercoda — laboratórios de Ansible.

### Exercícios
- [ ] **E6.7.1** Inventário com as 3 VMs do homelab em grupos (`web`, `db`, `monitoramento`).
- [ ] **E6.7.2** Comandos *ad hoc*: *uptime*, espaço em disco e atualização de pacotes em todas.
- [ ] **E6.7.3** Playbook de *baseline* de segurança: usuário admin, chave SSH, desativar login por senha e de root, `ufw`, `fail2ban`, atualizações automáticas, fuso horário, NTP.
- [ ] **E6.7.4** Transforme o playbook em uma *role* reutilizável e teste com Molecule.
- [ ] **E6.7.5** Role `nginx` com *template* Jinja2 de *server block* e *handler* de *reload*.
- [ ] **E6.7.6** Playbook que faz o deploy completo do projeto integrador (Docker, Compose, `.env` com segredos do Vault).
- [ ] **E6.7.7** Rode o mesmo playbook duas vezes e mostre que a segunda execução não muda nada (idempotência).
- [ ] **E6.7.8** Playbook que instala o **agente do Zabbix** em todas as máquinas (ponte com a trilha 8).
- [ ] **E6.7.9** *Role* para configurar estações de trabalho de clientes (programas padrão, usuário, papel de parede) em Linux; pesquise como fazer o mesmo em Windows (WinRM).

### Autoavaliação
1. O que é idempotência e por que é essencial?
2. Qual a diferença entre `copy` e `template`?
3. Quando usar *handlers*?
4. Ansible x Terraform: qual a diferença de propósito?

---

## Módulo 6.8 — Infraestrutura como código com Terraform (1,5 semana)

### Conceitos
- [ ] IaC: declarativo x imperativo; provisionamento x configuração
- [ ] Terraform/OpenTofu: *providers*, *resources*, *data sources*, *variables*, *outputs*, *locals*
- [ ] Ciclo: `init`, `fmt`, `validate`, `plan`, `apply`, `destroy`
- [ ] **State**: o que é, por que é sensível, *remote state* (S3 + *locking*), `terraform import`, `state mv`
- [ ] **Módulos** (próprios e do *registry*)
- [ ] `count`, `for_each`, expressões, funções, `dynamic` blocks
- [ ] Ambientes: *workspaces* x diretórios separados
- [ ] *Drift* de configuração
- [ ] Boas práticas: versionar *providers*, não commitar state nem segredos, `tflint`, `checkov`/`tfsec` (segurança)
- [ ] Terraform no CI (plan no PR, apply após aprovação)
- [ ] OpenTofu (fork aberto) e Pulumi (IaC com linguagens de programação)

### Fontes
- 🌐 [HashiCorp — Terraform Tutorials](https://developer.hashicorp.com/terraform/tutorials): trilhas *Get Started* (Docker, AWS) e *Associate Tutorial List*.
- 🌐 [OpenTofu — docs](https://opentofu.org/docs/)
- 📘 *Terraform: Up & Running* (3ª ed.) — Yevgeniy Brikman
- 🌐 [Terraform Best Practices — Anton Babenko](https://www.terraform-best-practices.com/)
- 🌐 [Provider Proxmox para Terraform (bpg/proxmox)](https://registry.terraform.io/providers/bpg/proxmox/latest/docs): IaC no seu homelab.

### Exercícios
- [ ] **E6.8.1** Siga o tutorial *Get Started — Docker* (Terraform criando containers localmente).
- [ ] **E6.8.2** Crie as VMs do homelab com o *provider* do Proxmox + *cloud-init*.
- [ ] **E6.8.3** Na AWS (conta *free tier*, com **alerta de orçamento configurado primeiro**): VPC, sub-redes pública e privada, *security groups*, uma EC2 e um bucket S3.
- [ ] **E6.8.4** Transforme a VPC em um módulo reutilizável e crie dois ambientes (dev e prod).
- [ ] **E6.8.5** *Remote state* em S3 com *locking*.
- [ ] **E6.8.6** Altere um recurso à mão no console e detecte o *drift* com `plan`.
- [ ] **E6.8.7** Pipeline no GitHub Actions: `plan` comentado no PR, `apply` após merge com aprovação, autenticação por OIDC.
- [ ] **E6.8.8** Rode `checkov` no código e corrija os achados.
- [ ] **E6.8.9** **Destrua tudo** (`terraform destroy`) ao fim de cada sessão para não gerar custo.

### Autoavaliação
1. O que é o *state* do Terraform e por que ele não deve ir para o Git?
2. Qual a diferença entre `count` e `for_each`?
3. O que acontece se duas pessoas rodarem `apply` ao mesmo tempo sem *locking*?
4. O que é *drift*?

### Certificação relacionada (opcional)
- **HashiCorp Certified: Terraform Associate** (confira a versão vigente do exame no site da HashiCorp).

---

## Módulo 6.9 — Computação em nuvem (AWS) (2 semanas)

> Os conceitos valem para Azure e GCP. Escolhi a AWS por ser a mais pedida no mercado. **Configure alertas de orçamento no primeiro dia** e desligue tudo depois de usar.

### Conceitos
- [ ] Modelos IaaS, PaaS, SaaS, FaaS; modelo de responsabilidade compartilhada
- [ ] Regiões, zonas de disponibilidade, *edge locations*
- [ ] **IAM**: usuários, grupos, *roles*, *policies* (JSON), menor privilégio, MFA, **nunca** usar a conta *root* no dia a dia
- [ ] **Rede**: VPC, sub-redes pública/privada, *Internet Gateway*, *NAT Gateway* (e seu custo!), *route tables*, *security groups* x NACLs
- [ ] **Computação**: EC2 (tipos, AMIs, *user data*, *key pairs*), *Auto Scaling Groups*, ELB/ALB
- [ ] **Containers**: ECR, **ECS com Fargate**, EKS (visão geral)
- [ ] **Serverless**: Lambda, API Gateway, EventBridge
- [ ] **Armazenamento**: S3 (classes, *lifecycle*, versionamento, políticas, site estático), EBS, EFS
- [ ] **Bancos**: RDS (MySQL/PostgreSQL), DynamoDB (visão geral), ElastiCache
- [ ] **Mensageria**: SQS, SNS
- [ ] DNS e CDN: Route 53, CloudFront, ACM (certificados)
- [ ] Observabilidade: CloudWatch (métricas, logs, alarmes), CloudTrail (auditoria)
- [ ] Custos: calculadora de preços, *Cost Explorer*, orçamentos, instâncias *spot*/reservadas
- [ ] **AWS Well-Architected Framework** (6 pilares)
- [ ] Alternativas: Azure, GCP, e provedores mais baratos (Hetzner, DigitalOcean, Oracle Cloud *free tier*, Magalu Cloud 🇧🇷)

### Fontes
- 🌐 [AWS Skill Builder](https://skillbuilder.aws/) — *AWS Cloud Practitioner Essentials* (gratuito, com versão em português).
- 🌐 [AWS — documentação](https://docs.aws.amazon.com/pt_br/) 🇧🇷
- 🌐 [AWS Well-Architected Framework](https://docs.aws.amazon.com/pt_br/wellarchitected/latest/framework/welcome.html) 🇧🇷
- 🎥 [freeCodeCamp — AWS Certified Cloud Practitioner (Andrew Brown, gratuito)](https://www.youtube.com/@freecodecamp)
- 🎥 Adrian Cantrill — cursos de certificação AWS 💲 (muito respeitados)
- 🌐 [The Cloud Resume Challenge — Forrest Brazeal](https://cloudresumechallenge.dev/): projeto guiado excelente.
- 🌐 [AWS Free Tier](https://aws.amazon.com/free/)

### Exercícios
- [ ] **E6.9.1** Crie a conta, ative MFA na *root*, crie um usuário administrativo (IAM Identity Center) e **configure um alerta de orçamento de US$ 5**.
- [ ] **E6.9.2** Site estático da Marcelo IT no S3 + CloudFront + HTTPS (ACM) + domínio (Route 53 ou DNS externo).
- [ ] **E6.9.3** Escreva uma *policy* IAM que permite ler só um bucket específico e teste.
- [ ] **E6.9.4** VPC com sub-redes pública e privada; EC2 na pública acessando um RDS na privada.
- [ ] **E6.9.5** API da loja no ECS Fargate com imagem do ECR, atrás de um ALB, com logs no CloudWatch.
- [ ] **E6.9.6** Função Lambda + API Gateway que calcula o orçamento (reaproveite a lógica da trilha 1).
- [ ] **E6.9.7** Fila SQS entre a API e um *worker* de notificações.
- [ ] **E6.9.8** Alarme do CloudWatch que avisa por e-mail (SNS) quando a CPU passa de 80%.
- [ ] **E6.9.9** Faça tudo acima também com Terraform.
- [ ] **E6.9.10** Faça o **Cloud Resume Challenge** completo.

### Autoavaliação
1. O que é o modelo de responsabilidade compartilhada?
2. *Security group* x NACL: diferenças.
3. Por que a sub-rede do banco deve ser privada? Como ele acessa a internet para atualizações?
4. Quais os 6 pilares do Well-Architected?
5. Quais serviços costumam gerar custos inesperados?

### Certificações relacionadas (opcional)
- **AWS Certified Cloud Practitioner** (entrada) → **AWS Certified Solutions Architect – Associate**.
- Alternativas: *Microsoft Azure Fundamentals (AZ-900)*, *Google Cloud Digital Leader*.

---

## Módulo 6.10 — Kubernetes (2,5 semanas)

### Conceitos
- [ ] Por que orquestração; o que o Kubernetes resolve (e a complexidade que traz)
- [ ] **Arquitetura**: *control plane* (API server, etcd, scheduler, controller manager) e nós (kubelet, kube-proxy, *container runtime*)
- [ ] Ambientes locais: **kind**, **minikube**, **k3s** (ótimo para o homelab)
- [ ] `kubectl`: `get`, `describe`, `logs`, `exec`, `apply`, `delete`, `port-forward`, contextos
- [ ] Objetos: **Pod**, **ReplicaSet**, **Deployment** (*rolling update*, *rollback*), **Service** (ClusterIP, NodePort, LoadBalancer), **Ingress** e *Ingress Controller* (Nginx, Traefik), Gateway API
- [ ] **ConfigMap** e **Secret** (e por que Secret não é criptografado por padrão)
- [ ] **Volumes**: PV, PVC, *StorageClass*; **StatefulSet** (bancos)
- [ ] **DaemonSet**, **Job**, **CronJob**
- [ ] *Probes*: *liveness*, *readiness*, *startup*
- [ ] *Requests* e *limits*; QoS; **HPA** (escalonamento automático)
- [ ] *Namespaces*, *labels*, *selectors*, *annotations*
- [ ] **RBAC**, *ServiceAccounts*
- [ ] *NetworkPolicies*
- [ ] **Helm** (charts, values, releases) e Kustomize
- [ ] *Operators* e CRDs (visão geral)
- [ ] Kubernetes gerenciado: EKS, AKS, GKE
- [ ] Segurança: *Pod Security Standards*, imagens confiáveis, segredos externos

### Fontes
- 🌐 [Kubernetes — documentação](https://kubernetes.io/pt-br/docs/home/) 🇧🇷: *Conceitos* e *Tutoriais*.
- 📘🇧🇷 [*Descomplicando o Kubernetes* — LINUXtips (gratuito, GitHub)](https://github.com/badtuxx/DescomplicandoKubernetes)
- 📘 *Kubernetes Up & Running* (3ª ed.) — Burns, Beda, Hightower e Evenson
- 🌐 [Kubernetes The Hard Way — Kelsey Hightower](https://github.com/kelseyhightower/kubernetes-the-hard-way): montar um cluster "na mão" para entender cada peça.
- 🧪 [Killercoda — cenários de Kubernetes e CKA](https://killercoda.com/)
- 🌐 [Helm — docs](https://helm.sh/docs/) · [k3s — docs](https://docs.k3s.io/) · [kind](https://kind.sigs.k8s.io/)
- 🎥 [TechWorld with Nana — Kubernetes Tutorial for Beginners (YouTube)](https://www.youtube.com/@TechWorldwithNana)
- 🧪 KodeKloud — cursos preparatórios para CKA/CKAD 💲

### Exercícios
- [ ] **E6.10.1** Suba um cluster com kind (local) e outro com k3s nas 3 VMs do homelab (1 servidor + 2 agentes).
- [ ] **E6.10.2** Rode um Pod à mão, depois um Deployment com 3 réplicas; apague um Pod e veja o ReplicaSet recriá-lo.
- [ ] **E6.10.3** Faça um *rolling update* de versão e um *rollback*.
- [ ] **E6.10.4** Exponha a API com Service e Ingress (com HTTPS via cert-manager + Let's Encrypt, ou autoassinado).
- [ ] **E6.10.5** Configuração com ConfigMap e senha do banco com Secret; monte como variável e como arquivo.
- [ ] **E6.10.6** MySQL com StatefulSet e PVC; apague o Pod e confirme que os dados persistem.
- [ ] **E6.10.7** *Probes* na API: mostre um Pod saindo do balanceamento quando a *readiness* falha.
- [ ] **E6.10.8** *Requests*/*limits* e HPA; gere carga com k6 e veja o número de réplicas subir.
- [ ] **E6.10.9** CronJob que faz backup do banco toda noite.
- [ ] **E6.10.10** *NetworkPolicy*: só a API pode falar com o banco.
- [ ] **E6.10.11** RBAC: um usuário que só pode ver Pods no *namespace* `dev`.
- [ ] **E6.10.12** Crie um **Helm chart** para o projeto integrador, com valores para dev e prod.
- [ ] **E6.10.13** Faça o *Kubernetes The Hard Way* (pode levar um fim de semana).
- [ ] **E6.10.14** Resolva 20 cenários de Kubernetes no Killercoda.
- [ ] **E6.10.15** 50 perguntas da seção Kubernetes do DevOps Exercises.

### Autoavaliação
1. Qual o papel de cada componente do *control plane*?
2. Qual a diferença entre Deployment e StatefulSet?
3. *Liveness* x *readiness*: o que acontece quando cada uma falha?
4. Qual a diferença entre Service e Ingress?
5. *Requests* x *limits*: o que acontece se um container passar do *limit* de memória? E de CPU?
6. Por que um Secret do Kubernetes não é, por si só, seguro?

### Certificações relacionadas (opcional)
- **KCNA** (Kubernetes and Cloud Native Associate, teórica, entrada) → **CKAD** (desenvolvedor, prática) → **CKA** (administrador, prática) → **CKS** (segurança).

---

## Módulo 6.11 — Observabilidade: métricas, logs e *traces* (1,5 semana)

> O Zabbix (trilha 8) é outra ferramenta forte de monitoramento, especialmente para infraestrutura e redes. Aqui o foco é a pilha *cloud-native*. Saber os dois é um diferencial.

### Conceitos
- [ ] Monitoramento x observabilidade; *known unknowns* x *unknown unknowns*
- [ ] **Métricas**: tipos (*counter*, *gauge*, *histogram*, *summary*); métodos **RED** (Rate, Errors, Duration) e **USE** (Utilization, Saturation, Errors); os 4 sinais de ouro (latência, tráfego, erros, saturação)
- [ ] **Prometheus**: modelo *pull*, *exporters* (node_exporter, mysqld_exporter, blackbox_exporter), *scrape*, PromQL, *recording rules*
- [ ] **Alertmanager**: regras, agrupamento, silêncio, roteamento (e-mail, Telegram)
- [ ] **Grafana**: *datasources*, dashboards, variáveis, alertas
- [ ] **Logs**: logs estruturados (JSON), níveis, correlação; **Loki** + Promtail/Grafana Alloy; pilha ELK/OpenSearch (visão geral)
- [ ] **Traces**: *spans*, contexto, amostragem; **OpenTelemetry** (SDK, *Collector*); **Jaeger** ou **Tempo**
- [ ] Instrumentar a aplicação (métricas de negócio também: OS abertas, orçamentos aprovados)
- [ ] Boas práticas de alerta: alertar sobre sintomas, não causas; evitar fadiga de alertas; *runbooks*
- [ ] kube-prometheus-stack no Kubernetes

### Fontes
- 🌐 [Prometheus — docs](https://prometheus.io/docs/introduction/overview/) e [Querying basics (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- 🌐 [Grafana — tutoriais](https://grafana.com/tutorials/) e [Grafana Loki — docs](https://grafana.com/docs/loki/latest/)
- 🌐 [OpenTelemetry — docs](https://opentelemetry.io/docs/)
- 📘 *Prometheus: Up & Running* (2ª ed.) — Julien Pivotto e Brian Brazil
- 📘 *Observability Engineering* — Majors, Fong-Jones e Miranda
- 📘 SRE Book (Google) — capítulo 6, *Monitoring Distributed Systems*.
- 🌐 [Awesome Prometheus Alerts](https://samber.github.io/awesome-prometheus-alerts/): coleção de regras de alerta prontas.
- 🌐 [Brendan Gregg — The USE Method](https://www.brendangregg.com/usemethod.html)

### Exercícios
- [ ] **E6.11.1** Suba Prometheus + Grafana + node_exporter com Docker Compose e monte um dashboard das VMs do homelab.
- [ ] **E6.11.2** Instrumente a API da loja com `prom-client` (Node) ou `prometheus-client` (Python): métricas RED por rota e métricas de negócio.
- [ ] **E6.11.3** 15 consultas PromQL: taxa de requisições, taxa de erros, latência p95 com `histogram_quantile`, uso de CPU por instância…
- [ ] **E6.11.4** Alertas no Alertmanager enviados ao Telegram: API fora do ar (blackbox_exporter), taxa de erro > 5%, disco > 85%.
- [ ] **E6.11.5** Loki coletando os logs dos containers; consulte com LogQL e correlacione com as métricas no Grafana.
- [ ] **E6.11.6** *Traces* com OpenTelemetry + Jaeger (ou Tempo) na API e no serviço de notificações; encontre a operação mais lenta.
- [ ] **E6.11.7** Instale o kube-prometheus-stack via Helm no k3s.
- [ ] **E6.11.8** Escreva um *runbook* para cada alerta que você criou (o que significa, como investigar, como resolver).

### Autoavaliação
1. Explique RED e USE. Para que tipo de componente serve cada um?
2. Qual a diferença entre *counter* e *gauge*?
3. Por que alertar sobre sintomas e não sobre causas?
4. Como logs, métricas e *traces* se complementam?
5. Prometheus (*pull*) x Zabbix (*pull* e *push*, com agentes): diferenças de abordagem.

---

## Módulo 6.12 — SRE: SLIs, SLOs, incidentes e *postmortems* (1 semana)

### Conceitos
- [ ] O que é SRE ("o que acontece quando você pede a um engenheiro de software para projetar operações")
- [ ] **SLI**, **SLO**, **SLA**; **orçamento de erro** (*error budget*) e políticas de orçamento
- [ ] Alertas baseados em SLO (*burn rate*)
- [ ] ***Toil*** e como reduzi-lo
- [ ] **Gestão de incidentes**: papéis (comandante do incidente, comunicação, operações), severidades, comunicação com clientes (página de status)
- [ ] ***Postmortems*** sem culpados (*blameless*)
- [ ] Plantão (*on-call*) saudável
- [ ] Planejamento de capacidade
- [ ] Recuperação de desastres: RPO e RTO; testes de restauração
- [ ] Engenharia do caos (revisão do módulo 5.10)

### Fontes
- 📘 [*Site Reliability Engineering* (Google, gratuito)](https://sre.google/sre-book/table-of-contents/): capítulos 1–6, 13–15.
- 📘 [*The Site Reliability Workbook* (Google, gratuito)](https://sre.google/workbook/table-of-contents/): capítulos 2 (SLOs), 5 (alertas por SLO), 9 (incidentes), 10 (*postmortems*).
- 🌐 [Google — Postmortem example](https://sre.google/sre-book/example-postmortem/)
- 🌐 [PagerDuty — Incident Response Guide](https://response.pagerduty.com/)
- 🌐 [Atlassian — Incident Management Handbook](https://www.atlassian.com/incident-management)
- 🌐 [danluu/post-mortems (GitHub)](https://github.com/danluu/post-mortems): coleção de *postmortems* públicos de empresas reais.

### Exercícios
- [ ] **E6.12.1** Defina SLIs e SLOs para o projeto integrador (disponibilidade da API, latência do orçamento online, sucesso do envio de e-mails) e calcule o orçamento de erro mensal.
- [ ] **E6.12.2** Crie um dashboard de SLO no Grafana e um alerta por *burn rate*.
- [ ] **E6.12.3** Leia 10 *postmortems* públicos e resuma: causa, detecção, impacto, ações.
- [ ] **E6.12.4** Faça uma simulação de incidente ("*game day*"): peça a alguém (ou use um script aleatório) para quebrar algo no homelab; conduza a resposta e escreva o *postmortem*.
- [ ] **E6.12.5** Defina RPO e RTO para o banco do projeto integrador e **teste** a restauração do backup cronometrando o tempo.
- [ ] **E6.12.6** Suba uma página de status (ex.: Uptime Kuma) para os serviços do homelab.
- [ ] **E6.12.7** Liste o *toil* que você tem hoje no seu trabalho de TI e automatize um item.

### Autoavaliação
1. Qual a diferença entre SLI, SLO e SLA?
2. O que é orçamento de erro e o que acontece quando ele acaba?
3. Por que *postmortems* devem ser sem culpados?
4. O que são RPO e RTO?

---

## Módulo 6.13 — GitOps, DevSecOps e plataformas (1 semana)

### Conceitos
- [ ] **GitOps**: Git como fonte da verdade; reconciliação contínua; **Argo CD** ou Flux
- [ ] **DevSecOps** (ponte com a trilha 7): *shift left*; SAST (Semgrep, CodeQL), SCA (Dependabot, Trivy), DAST (OWASP ZAP), varredura de segredos (gitleaks), varredura de IaC (checkov), SBOM, assinatura de artefatos, SLSA
- [ ] Gestão de segredos: **HashiCorp Vault**, *External Secrets Operator*, *Sealed Secrets*, SOPS
- [ ] *Policy as code*: OPA/Gatekeeper, Kyverno
- [ ] *Platform engineering* e portais internos (Backstage)
- [ ] FinOps (custos na nuvem)

### Fontes
- 🌐 [Argo CD — docs](https://argo-cd.readthedocs.io/)
- 🌐 [OpenGitOps — princípios](https://opengitops.dev/)
- 🌐 [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/)
- 🌐 [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/)
- 🌐 [Semgrep](https://semgrep.dev/docs/) · [gitleaks](https://github.com/gitleaks/gitleaks) · [OWASP ZAP](https://www.zaproxy.org/docs/)
- 🌐 [HashiCorp Vault — tutoriais](https://developer.hashicorp.com/vault/tutorials)
- 🌐 [Kyverno — docs](https://kyverno.io/docs/)

### Exercícios
- [ ] **E6.13.1** Instale o Argo CD no k3s e faça o deploy do projeto integrador a partir de um repositório de manifestos; altere a versão por commit e veja a sincronização.
- [ ] **E6.13.2** Pipeline DevSecOps: Semgrep + gitleaks + Trivy (dependências e imagem) + checkov + ZAP *baseline* contra o ambiente de teste.
- [ ] **E6.13.3** Segredos do Kubernetes vindos do Vault (ou *Sealed Secrets*).
- [ ] **E6.13.4** Política do Kyverno que bloqueia Pods rodando como root ou sem *limits*.

---

## Módulo 6.14 — Projetos finais (2–3 semanas)

### Projeto A — Plataforma completa do Marcelo IT Services
- **Infraestrutura como código**: Terraform provisionando as VMs no Proxmox (homelab) **e** uma versão na AWS (VPC, EKS ou ECS, RDS, S3, CloudFront).
- **Configuração**: Ansible com *roles* de *baseline*, Docker, agente de monitoramento.
- **Kubernetes** (k3s no homelab): Helm chart do sistema, Ingress com HTTPS, HPA, *NetworkPolicies*, backups por CronJob.
- **CI/CD**: GitHub Actions (lint, testes, build, varreduras de segurança, publicação da imagem assinada) + **GitOps com Argo CD** (dev automático, prod com aprovação).
- **Observabilidade**: Prometheus, Grafana, Loki, Tempo/Jaeger, Alertmanager no Telegram; dashboards RED e de negócio.
- **SRE**: SLOs definidos, alertas por *burn rate*, *runbooks*, 1 *postmortem* de *game day*, teste de restauração documentado com RPO/RTO.
- **Documentação**: diagrama da infraestrutura, README de como recriar tudo do zero, ADRs das escolhas.

### Projeto B — Cloud Resume Challenge
Currículo publicado na AWS com contador de visitas (Lambda + DynamoDB), IaC, CI/CD e artigo no blog. Serve como porta de entrada no portfólio.

### Mini-projetos extras (escolha pelo menos 2)
- [ ] Serviços *self-hosted* no homelab: Nextcloud, Vaultwarden, Gitea/Forgejo, Uptime Kuma, Pi-hole
- [ ] *Runner* próprio do GitHub Actions em container efêmero
- [ ] Operador Kubernetes simples (em Python com Kopf ou em Go)
- [ ] ChatOps: bot que faz deploy e mostra status pelo Telegram/Slack

---

## ✅ Checklist de conclusão da Trilha 6
- [ ] *O Projeto Fênix* lido
- [ ] Bandit completo e 20 cenários do SadServers
- [ ] Homelab documentado e reproduzível
- [ ] Pipelines de CI/CD em todos os projetos
- [ ] Terraform + Ansible + Kubernetes + GitOps funcionando juntos
- [ ] Stack de observabilidade com alertas e *runbooks*
- [ ] SLOs e *postmortem* escritos
- [ ] Autoavaliações com ≥ 80% de acerto
- [ ] **Certificações sugeridas:** LFCS ou RHCSA → AWS Cloud Practitioner → Terraform Associate → CKA
