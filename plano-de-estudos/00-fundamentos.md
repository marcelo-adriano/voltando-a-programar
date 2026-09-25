# Trilha 0 — Fundamentos

> **Por que começar aqui?** Todas as outras trilhas dependem de saber usar o terminal, o Linux e o Git, e de entender o básico de redes. Sem isso, você gasta energia com a ferramenta em vez de gastar com o conceito.

**Duração:** 4–6 semanas · **Pré-requisitos:** nenhum

| Módulo | Tema | Duração |
|--------|------|---------|
| 0.1 | Aprender a aprender e montar o ambiente | 1 semana |
| 0.2 | Terminal e Linux | 2 semanas |
| 0.3 | Shell script (Bash) | 1 semana |
| 0.4 | Git e GitHub | 1–2 semanas |
| 0.5 | Redes: o mínimo para desenvolvedores | 1 semana |

---

## Módulo 0.1 — Aprender a aprender e montar o ambiente (1 semana)

### Objetivos
- Ter um método de estudo definido (ver seção 2 do [README do plano](./README.md)).
- Ter o ambiente de desenvolvimento pronto: editor, terminal, Linux (nativo ou WSL2), Git, Node.js, Python, Docker.

### Conceitos
- [ ] Memória de trabalho x memória de longo prazo; modo focado x modo difuso
- [ ] Recuperação ativa, repetição espaçada, intercalação
- [ ] Procrastinação e Pomodoro
- [ ] O que é um editor de código x IDE
- [ ] O que é WSL2 (se usar Windows) e por que desenvolver em Linux
- [ ] Gerenciadores de versão: `nvm`/`fnm` (Node), `pyenv`/`uv` (Python)

### Fontes
- 🎥🇧🇷 [Aprendendo a Aprender (Coursera)](https://www.coursera.org/learn/aprender): assistir às semanas 1 a 4.
- 📘 *Fixe o Conhecimento* (Make It Stick): capítulos 1–3.
- 🌐 [Documentação do VS Code](https://code.visualstudio.com/docs): "Getting Started" e "User Interface".
- 🌐 [Instalar o WSL (Microsoft)](https://learn.microsoft.com/pt-br/windows/wsl/install) 🇧🇷
- 🌐 [Anki — manual](https://docs.ankiweb.net/)

### Exercícios
- [ ] **E0.1.1** Instale o Anki e crie um baralho "Voltando a Programar". Crie 10 cartões sobre as técnicas de estudo desta página.
- [ ] **E0.1.2** Instale (ou confira) VS Code, Git, Node.js LTS (via `nvm` ou `fnm`), Python 3 (via `uv` ou `pyenv`) e Docker. Anote em `anotacoes/ambiente.md` o comando para ver a versão de cada um.
- [ ] **E0.1.3** Configure no VS Code: formatação ao salvar, Prettier, ESLint, Python, EditorConfig, GitLens, Error Lens. Anote para que serve cada extensão.
- [ ] **E0.1.4** Crie o arquivo `.editorconfig` na raiz deste repositório (indentação, fim de linha, charset).
- [ ] **E0.1.5** Monte sua rotina semanal (dias e horários fixos) e coloque na agenda do celular.
- [ ] **E0.1.6** Configure o GitHub Projects deste repositório com as colunas `A fazer / Estudando / Revisão / Feito`.

### Autoavaliação
1. Por que reler um capítulo é menos eficaz que tentar lembrar dele?
2. O que é o "modo difuso" e quando ele ajuda a resolver um problema?
3. Qual a diferença entre instalar o Node pelo site oficial e usar um gerenciador de versões?

### Projeto 0.1 — Meu ambiente documentado
Arquivo `anotacoes/ambiente.md` com: sistema operacional, ferramentas e versões, extensões, atalhos de teclado que você mais usa, e um passo a passo para recriar o ambiente num computador novo.

---

## Módulo 0.2 — Terminal e Linux (2 semanas)

### Objetivos
- Navegar, criar, mover, buscar e editar arquivos só pelo terminal.
- Entender permissões, processos, variáveis de ambiente, pacotes e SSH.

### Conceitos
- [ ] Shell x terminal x console; Bash e Zsh
- [ ] Sistema de arquivos Linux (FHS): `/`, `/home`, `/etc`, `/var`, `/usr`, `/tmp`, `/opt`
- [ ] Caminhos absolutos e relativos; `.`, `..`, `~`
- [ ] Navegação: `pwd`, `ls`, `cd`, `tree`
- [ ] Arquivos: `touch`, `mkdir -p`, `cp -r`, `mv`, `rm -r`, `ln -s`
- [ ] Leitura: `cat`, `less`, `head`, `tail -f`, `wc`
- [ ] Busca: `find`, `grep` (com regex básica), `which`, `locate`
- [ ] Redirecionamento e pipes: `>`, `>>`, `<`, `|`, `2>`, `2>&1`, `/dev/null`
- [ ] Processamento de texto: `sort`, `uniq`, `cut`, `tr`, `sed`, `awk` (básico), `xargs`
- [ ] Permissões: usuário/grupo/outros, `rwx`, notação octal, `chmod`, `chown`, `umask`, `sudo`
- [ ] Usuários e grupos: `id`, `whoami`, `useradd`, `usermod`, `/etc/passwd`, `/etc/group`
- [ ] Processos: `ps`, `top`/`htop`, `kill`, sinais (`SIGTERM`, `SIGKILL`), `&`, `jobs`, `fg`, `bg`, `nohup`
- [ ] Variáveis de ambiente: `env`, `export`, `PATH`, `.bashrc`/`.zshrc`
- [ ] Pacotes: `apt` (Debian/Ubuntu), `dnf` (Fedora/RHEL); repositórios
- [ ] Editores no terminal: `nano` e o básico de `vim` (sair do vim!)
- [ ] Compactação: `tar`, `gzip`, `zip`
- [ ] SSH: chaves públicas/privadas, `ssh-keygen`, `ssh-copy-id`, `~/.ssh/config`, `scp`, `rsync`
- [ ] Serviços: `systemctl status/start/stop/enable`, `journalctl -u`
- [ ] Disco: `df -h`, `du -sh`, `lsblk`, `mount`

### Fontes
- 🎥 [Missing Semester — aulas 1 (Shell), 2 (Shell Tools), 4 (Data Wrangling), 5 (Command-line Environment)](https://missing.csail.mit.edu/)
- 📘 [*The Linux Command Line* — William Shotts (gratuito)](https://linuxcommand.org/tlcl.php): partes 1 e 2.
- 📘🇧🇷 [Guia Foca GNU/Linux](https://www.guiafoca.org/): níveis iniciante e intermediário.
- 🌐 [Linux Journey](https://linuxjourney.com/): trilhas "Grasshopper" e "Journeyman".
- 🌐 [explainshell.com](https://explainshell.com/): cole um comando e veja o que cada parte faz.
- 🌐 [tldr pages](https://tldr.sh/): exemplos práticos de cada comando (`man` simplificado).
- 🎥🇧🇷 [Diolinux](https://www.youtube.com/@Diolinux) e [LINUXtips](https://www.youtube.com/@LINUXtips): vídeos introdutórios sobre Linux.
- 🧪 [OverTheWire — Bandit](https://overthewire.org/wargames/bandit/): jogo de terminal via SSH. **Meta: nível 0 ao 20.**
- 🧪 [SadServers](https://sadservers.com/): servidores Linux "quebrados" para você consertar (use os fáceis agora; os difíceis na trilha 6).

### Exercícios
- [ ] **E0.2.1** Sem usar interface gráfica, crie esta estrutura em um único comando: `projeto/{src,tests,docs}/` e um `README.md` em cada pasta.
- [ ] **E0.2.2** Encontre todos os arquivos `.log` maiores que 1 MB em `/var/log` (`find` com `-size`).
- [ ] **E0.2.3** Conte quantas linhas de `/etc/passwd` usam `/bin/bash` como shell.
- [ ] **E0.2.4** Liste os 5 comandos que você mais usou (`history | awk ... | sort | uniq -c | sort -rn | head -5`). Entenda cada pedaço do pipe.
- [ ] **E0.2.5** Crie um arquivo com permissão `640` e explique quem pode ler, escrever e executar. Repita com `755` e `600`.
- [ ] **E0.2.6** Crie um usuário `estudante`, um grupo `devs`, adicione o usuário ao grupo e crie uma pasta que só o grupo `devs` consiga escrever.
- [ ] **E0.2.7** Rode `sleep 1000` em segundo plano, encontre o PID, envie `SIGTERM`. Repita e envie `SIGKILL`. Qual a diferença?
- [ ] **E0.2.8** Adicione uma pasta `~/bin` ao `PATH` de forma permanente e coloque um script seu lá.
- [ ] **E0.2.9** Gere um par de chaves SSH `ed25519`, adicione a chave pública ao GitHub e teste com `ssh -T git@github.com`.
- [ ] **E0.2.10** Crie um alias `ll` e uma função `mkcd` (cria a pasta e entra nela) no `.bashrc`.
- [ ] **E0.2.11** Use `tail -f` em um log enquanto gera eventos (ex.: `logger "teste"`), e filtre com `grep`.
- [ ] **E0.2.12** Compacte uma pasta com `tar -czf`, liste o conteúdo sem extrair e extraia em outro lugar.
- [ ] **E0.2.13** Use `rsync` para sincronizar duas pastas e depois rode com `--dry-run --delete`. Explique o que aconteceria.
- [ ] **E0.2.14** Instale o `nginx`, verifique o status com `systemctl`, veja os logs com `journalctl` e acesse `http://localhost`.
- [ ] **E0.2.15** Complete o **Bandit até o nível 10** (semana 1) e **até o nível 20** (semana 2). Anote a solução de cada nível com suas palavras.

### Autoavaliação
1. Qual a diferença entre `>` e `>>`? E entre `|` e `>`?
2. O que significa `chmod 750 arquivo`? Escreva a mesma permissão em letras.
3. Por que `SIGKILL` não pode ser capturado por um programa?
4. O que acontece quando você digita `ls` e aperta Enter? (Pense em `PATH`, processo filho, saída padrão.)
5. Por que a chave privada SSH nunca deve sair do seu computador?
6. Para que serve a pasta `/etc`? E a `/var/log`?
7. Qual a diferença entre `systemctl start` e `systemctl enable`?

### Projeto 0.2 — Meu servidor de estudos
Suba uma VM (VirtualBox, Proxmox, Multipass ou um VPS barato) com Ubuntu Server ou Debian **sem interface gráfica** e, só pelo terminal:
- Crie um usuário não-root com `sudo`.
- Configure acesso SSH por chave e **desative login por senha e login de root**.
- Instale e configure o `nginx` servindo o `homepage.html` deste repositório.
- Documente tudo em `00-fundamentos/projetos/servidor-de-estudos.md`, com os comandos usados.

**Critérios de aceite:** conseguir acessar a página pelo navegador da sua máquina; `ssh root@vm` falha; `ssh usuario@vm` com chave funciona.

---

## Módulo 0.3 — Shell script (Bash) (1 semana)

### Objetivos
- Automatizar tarefas repetitivas com scripts Bash robustos.

### Conceitos
- [ ] Shebang (`#!/usr/bin/env bash`), permissão de execução
- [ ] Variáveis, aspas simples x duplas, substituição de comando `$(...)`
- [ ] Argumentos: `$1`, `$@`, `$#`, `$0`; `shift`; `getopts`
- [ ] Condicionais: `if`, `[[ ]]`, `test`, operadores de arquivo (`-f`, `-d`, `-e`)
- [ ] Laços: `for`, `while`, `until`; ler arquivo linha a linha
- [ ] Funções e `return` x `exit`; códigos de saída (`$?`)
- [ ] `set -euo pipefail` e por que usar
- [ ] `trap` para limpeza
- [ ] Datas: `date +%F`
- [ ] Agendamento: `cron` / `crontab -e` e `systemd timers`
- [ ] Boas práticas: ShellCheck, nomes descritivos, logs

### Fontes
- 🌐 [Bash Guide (Greg's Wiki)](https://mywiki.wooledge.org/BashGuide) e [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls)
- 📘 *The Linux Command Line*: parte 4 (Writing Shell Scripts).
- 🌐 [ShellCheck](https://www.shellcheck.net/): analisador estático, instale no VS Code.
- 🌐 [crontab.guru](https://crontab.guru/): monte e entenda expressões cron.
- 🧪 [Exercism — trilha Bash](https://exercism.org/tracks/bash)

### Exercícios
- [ ] **E0.3.1** Script `saudacao.sh` que recebe um nome como argumento e dá bom dia/boa tarde/boa noite conforme a hora.
- [ ] **E0.3.2** Script que recebe uma pasta e mostra quantos arquivos existem de cada extensão.
- [ ] **E0.3.3** Script que verifica se uma lista de sites (em um arquivo `.txt`) responde com HTTP 200 (`curl -o /dev/null -s -w "%{http_code}"`).
- [ ] **E0.3.4** Script que renomeia todas as fotos de uma pasta para `AAAA-MM-DD_NNN.jpg`.
- [ ] **E0.3.5** Script com `getopts` que aceita `-v` (verbose) e `-o arquivo` (saída).
- [ ] **E0.3.6** Script que alerta (mensagem no terminal ou log) se o uso de disco passar de 80%.
- [ ] **E0.3.7** Faça 10 exercícios da trilha Bash do Exercism.
- [ ] **E0.3.8** Passe todos os seus scripts pelo ShellCheck e corrija os avisos.

### Autoavaliação
1. O que `set -euo pipefail` faz, item por item?
2. Por que `rm -rf $PASTA/` sem aspas é perigoso?
3. Qual a diferença entre `$@` e `$*`?
4. Como agendar um script para rodar todo dia às 2h da manhã?

### Projeto 0.3 — Script de backup com rotação
Um serviço que você oferece aos clientes, agora automatizado:
- `backup.sh ORIGEM DESTINO` gera `backup_AAAA-MM-DD_HHMM.tar.gz`.
- Mantém apenas os **N** backups mais recentes (parâmetro `-k N`, padrão 7).
- Registra início, fim, tamanho e erros em um arquivo de log.
- Sai com código diferente de zero em caso de erro.
- Roda todo dia via `cron` ou `systemd timer`.
- **Extra:** enviar o backup para outra máquina com `rsync` via SSH; verificar integridade com `sha256sum`.

---

## Módulo 0.4 — Git e GitHub (1–2 semanas)

### Objetivos
- Entender o modelo interno do Git (commits, árvores, referências) e não só decorar comandos.
- Trabalhar com branches, merges, rebase, resolução de conflitos e pull requests.

### Conceitos
- [ ] Controle de versão; Git x GitHub
- [ ] As três áreas: working directory, staging (index), repositório
- [ ] `init`, `clone`, `status`, `add`, `commit`, `log`, `diff`, `show`
- [ ] Commit como snapshot; hash SHA; `HEAD`
- [ ] `.gitignore`
- [ ] Branches: `branch`, `switch`/`checkout`, `merge` (fast-forward x merge commit)
- [ ] Conflitos: como surgem e como resolver
- [ ] Remotos: `remote`, `fetch`, `pull`, `push`, `origin`, upstream
- [ ] `rebase` (e a regra: não reescrever histórico compartilhado)
- [ ] Desfazer: `restore`, `reset` (`--soft`, `--mixed`, `--hard`), `revert`, `reflog`
- [ ] `stash`, `cherry-pick`, `tag`, `bisect`, `blame`
- [ ] Fluxos: GitHub Flow, Git Flow, trunk-based development
- [ ] Pull requests, code review, issues, GitHub Projects
- [ ] Conventional Commits e mensagens de commit boas
- [ ] Hooks (`pre-commit`)

### Fontes
- 📘🇧🇷 [*Pro Git* — Scott Chacon (gratuito, em português)](https://git-scm.com/book/pt-br/v2): capítulos 1, 2, 3, 5 e 7; capítulo 10 (Git Internals) para entender o funcionamento por dentro.
- 🧪 [Learn Git Branching](https://learngitbranching.js.org/?locale=pt_BR) 🇧🇷: **faça todos os níveis** (Main e Remote).
- 🧪 [Oh My Git!](https://ohmygit.org/): jogo sobre Git.
- 🎥🇧🇷 [Curso de Git e GitHub — Curso em Vídeo](https://www.cursoemvideo.com/)
- 🎥 [Missing Semester — aula 6 (Version Control)](https://missing.csail.mit.edu/2020/version-control/)
- 🌐 [GitHub Skills](https://skills.github.com/): cursos interativos dentro do GitHub.
- 🌐 [Conventional Commits](https://www.conventionalcommits.org/pt-br/) 🇧🇷
- 🌐 [Oh Shit, Git!?!](https://ohshitgit.com/pt_BR) 🇧🇷: como desfazer os erros mais comuns.
- 🌐 [How to Write a Git Commit Message — Chris Beams](https://cbea.ms/git-commit/)

### Exercícios
- [ ] **E0.4.1** Complete todos os níveis do Learn Git Branching.
- [ ] **E0.4.2** Crie um repositório de teste, faça 5 commits e use `git log --oneline --graph --all`.
- [ ] **E0.4.3** Crie duas branches que alteram a **mesma linha** de um arquivo e faça o merge. Resolva o conflito à mão.
- [ ] **E0.4.4** Repita o E0.4.3 usando `rebase` em vez de `merge`. Compare os gráficos do histórico.
- [ ] **E0.4.5** Faça um commit errado e desfaça de três formas: `reset --soft`, `reset --hard` e `revert`. Explique quando usar cada uma.
- [ ] **E0.4.6** "Perca" um commit com `reset --hard` e recupere-o com `reflog`.
- [ ] **E0.4.7** Use `git bisect` para achar o commit que introduziu um bug (crie um repositório com 20 commits onde um deles quebra um script).
- [ ] **E0.4.8** Use `stash` para guardar uma alteração, trocar de branch, voltar e reaplicar.
- [ ] **E0.4.9** Crie uma tag `v0.1.0` neste repositório e envie para o GitHub.
- [ ] **E0.4.10** Crie templates de issue e de pull request em `.github/` neste repositório.
- [ ] **E0.4.11** Explore `.git/objects` e use `git cat-file -p` para ver um commit, uma árvore e um blob.
- [ ] **E0.4.12** Faça um fork de um repositório público, corrija algo pequeno (um erro de digitação na documentação, por exemplo) e abra um PR de verdade.

### Autoavaliação
1. O que é o staging area e por que ele existe?
2. O que é um "fast-forward merge"?
3. Qual a diferença entre `git fetch` e `git pull`?
4. Por que não se deve fazer `rebase` em uma branch que outras pessoas já usam?
5. Quando usar `revert` em vez de `reset`?
6. O que o Git guarda em um commit: diferenças ou fotos (snapshots)?
7. O que é `HEAD` "destacado" (detached HEAD)?

### Projeto 0.4 — Organizar este repositório
- Estrutura de pastas da seção 5.1 do plano.
- Templates de issue e PR, `.gitignore` e `.editorconfig`.
- Uma issue por módulo da trilha 1, no GitHub Projects.
- Proteção da branch `main` (exigir PR para fazer merge).

---

## Módulo 0.5 — Redes: o mínimo para desenvolvedores (1 semana)

> Esta é uma introdução. A trilha 9 (Cisco) aprofunda tudo isso.

### Objetivos
- Explicar o que acontece quando você digita uma URL no navegador.
- Usar ferramentas de diagnóstico de rede.

### Conceitos
- [ ] Modelos OSI e TCP/IP (camadas e o papel de cada uma)
- [ ] Endereço IP (IPv4 e IPv6), máscara, gateway, IP público x privado, NAT
- [ ] Portas e protocolos de transporte: TCP x UDP; handshake de 3 vias
- [ ] DNS: registros A, AAAA, CNAME, MX, TXT, NS; resolução recursiva
- [ ] DHCP
- [ ] HTTP: métodos, status codes, cabeçalhos; HTTPS e TLS (visão geral)
- [ ] Ferramentas: `ping`, `traceroute`/`mtr`, `ip a`, `ip route`, `ss -tulpn`, `dig`, `nslookup`, `curl -v`, `nc`, `tcpdump`, Wireshark

### Fontes
- 🌐 [Cloudflare Learning Center](https://www.cloudflare.com/pt-br/learning/) 🇧🇷: artigos sobre DNS, HTTP, TLS, CDN, DDoS.
- 🌐 [How DNS Works (quadrinhos)](https://howdns.works/)
- 🌐 [What happens when... (GitHub)](https://github.com/alex/what-happens-when): o que acontece ao digitar `google.com` e apertar Enter.
- 📘 *Redes de Computadores e a Internet* (Computer Networking: A Top-Down Approach) — Kurose e Ross: capítulos 1 e 2.
- 🎥 [Practical Networking](https://www.practicalnetworking.net/): série "Networking Fundamentals".
- 🎥🇧🇷 [Curso de Redes — Curso em Vídeo](https://www.cursoemvideo.com/)
- 🌐 [Wireshark — User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)

### Exercícios
- [ ] **E0.5.1** Descubra seu IP privado, seu IP público, seu gateway e seus servidores DNS.
- [ ] **E0.5.2** Use `dig` para ver os registros A, MX e TXT de um domínio. Use `dig +trace` e explique cada etapa.
- [ ] **E0.5.3** Use `traceroute` até um site no exterior e identifique onde a latência aumenta.
- [ ] **E0.5.4** Faça `curl -v https://example.com` e identifique: resolução DNS, conexão TCP, handshake TLS, requisição, resposta.
- [ ] **E0.5.5** Capture no Wireshark o acesso a um site **HTTP** (sem S) e encontre a requisição `GET` e a resposta. Repita com HTTPS: o que você consegue e o que não consegue ver?
- [ ] **E0.5.6** Use `ss -tulpn` para listar as portas abertas na sua máquina e identifique os programas.
- [ ] **E0.5.7** Com `nc`, crie um "chat" entre dois terminais (um escutando, outro conectando).
- [ ] **E0.5.8** Escreva com suas palavras, em até uma página, "o que acontece quando digito uma URL e aperto Enter".

### Autoavaliação
1. Em que camada do modelo OSI atua um roteador? E um switch comum?
2. Por que o DNS usa principalmente UDP?
3. O que é NAT e por que ele existe no IPv4?
4. Qual a diferença entre os status HTTP 301, 401, 403, 404 e 500?
5. O que o TLS protege e o que ele **não** protege?

### Projeto 0.5 — Mapa da minha rede
Documente a rede da sua casa ou escritório: diagrama (pode usar [draw.io](https://app.diagrams.net/)), faixa de IPs, dispositivos, IPs fixos, serviços expostos. Use `nmap -sn` **apenas na sua própria rede** para descobrir os dispositivos.

---

## ✅ Checklist de conclusão da Trilha 0
- [ ] Bandit até o nível 20
- [ ] Learn Git Branching completo
- [ ] Servidor de estudos funcionando com SSH por chave
- [ ] Script de backup rodando no cron
- [ ] Repositório organizado com issues e Kanban
- [ ] Texto "o que acontece quando digito uma URL"
