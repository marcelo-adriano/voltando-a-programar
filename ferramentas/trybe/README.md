# Ferramentas: projetos da Trybe

Scripts usados para copiar os repositórios da turma **sd-015-a** da organização `tryber` para a minha conta e para montar a análise em [`plano-de-estudos/projetos-trybe.md`](../../plano-de-estudos/projetos-trybe.md).

**Requisitos:** `gh` autenticado (com os escopos `repo` e `read:org`), `git`, `bash` e Python 3 (só biblioteca padrão).

> ⚠️ Tudo o que os scripts geram (listas, `prs.json`, `feedback/`, `mirrors/`) contém dados de repositórios privados da Trybe e está no [`.gitignore`](.gitignore). Não force o `git add` desses arquivos: este repositório é público.

## Scripts

| Script | O que faz | Escreve no GitHub? |
|--------|-----------|:------------------:|
| `listar.sh` | Gera `repos.txt` (repositórios da turma) e `prs.tsv` (meus PRs neles). | Não |
| `mirror.sh <repo>` | Clona `tryber/<repo>` com `git clone --mirror`, cria `marcelo-adriano/<repo>` **privado**, desliga o GitHub Actions, envia branches e tags e faz um commit com o `feedback.md` na branch padrão. Pode ser rodado de novo: pula o que já foi feito e confere se todas as branches e tags chegaram. | **Sim** |
| `run_all.sh` | Roda o `mirror.sh` para cada repositório de `repos.txt` e anota as falhas em `failed.txt`. | **Sim** |
| `gen_feedback.py <repo> <pr>...` | Imprime o markdown com os comentários, as reviews e os comentários de linha dos PRs. Usado pelo `mirror.sh`. | Não |
| `fetch_all.py` | Baixa os dados de todos os PRs de `prs.tsv` (PR, comentários, reviews, arquivos e diffs) para `prs.json`. | Não |
| `summarize.py` | Lê `prs.json` e mostra, por PR, a última avaliação da Trybe, os requisitos que faltaram, o lint e os comentários; grava `summary.json`. | Não |
| `show.py <repo> [pr...] [--max N]` | Mostra as linhas adicionadas nos PRs de um repositório (para ler o código sem clonar). | Não |

## Como usar

```bash
cd ferramentas/trybe
./listar.sh                      # gera repos.txt e prs.tsv

# Análise (só leitura)
./fetch_all.py                   # prs.json
./summarize.py | less            # resumo das avaliações
./show.py todo-list --max 80     # código do PR

# Cópia para a minha conta (escreve no GitHub!)
./mirror.sh sd-015-a-project-algorithms   # teste com um repositório pequeno
./run_all.sh > run_all.log 2>&1           # todos os repositórios
```

Variáveis de ambiente: `TURMA` (padrão `sd-015-a`) e `AUTOR` (padrão `marcelo-adriano`) no `listar.sh` e no `gen_feedback.py`; `DESTINO` (padrão `marcelo-adriano`) no `mirror.sh`.

**Observações:**

- As refs `refs/pull/*` do clone espelho não são enviadas, porque o GitHub recusa push nelas. As branches dos alunos estão em `refs/heads` e são copiadas; só ficam de fora commits que existam apenas em PRs abertos a partir de forks.
- Os projetos da Trybe trazem workflows que rodariam em cada branch enviada; o `mirror.sh` desliga o Actions **antes** do push para não gastar os minutos da conta.
