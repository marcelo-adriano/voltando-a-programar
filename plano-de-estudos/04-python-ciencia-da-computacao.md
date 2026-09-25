# Trilha 4 — Ciência da Computação com Python

> **Objetivo da trilha:** dominar Python, programação orientada a objetos, SOLID e padrões de projeto, e construir a base de Ciência da Computação (estruturas de dados, algoritmos, complexidade e noções de sistemas) que separa quem "usa ferramentas" de quem entende o que está fazendo.

**Duração:** 14–18 semanas · **Pré-requisitos:** Trilha 0 (Trilhas 1–3 ajudam, mas não são obrigatórias)

| Módulo | Tema | Duração |
|--------|------|---------|
| 4.1 | Introdução ao Python: sintaxe e estruturas de controle | 1,5 semana |
| 4.2 | Python: coleções, funções, módulos e arquivos | 1,5 semana |
| 4.3 | Python idiomático, tipagem e testes com pytest | 1 semana |
| 4.4 | Projeto prático: scripts de automação | 1 semana |
| 4.5 | POO: classes e objetos | 1,5 semana |
| 4.6 | SOLID | 1 semana |
| 4.7 | Arquitetura de software: Model, Service e Controller | 1,5 semana |
| 4.8 | Padrões de projeto | 2 semanas |
| 4.9 | Complexidade de algoritmos e recursão | 1 semana |
| 4.10 | Estruturas de dados | 2 semanas |
| 4.11 | Algoritmos: busca, ordenação, grafos, programação dinâmica | 2 semanas |
| 4.12 | Fundamentos de sistemas: como o computador funciona | 1,5 semana |
| 4.13 | Projetos finais | 2 semanas |

### Fontes principais da trilha
- 🌐🇧🇷 [Tutorial oficial do Python (em português)](https://docs.python.org/pt-br/3/tutorial/)
- 🎥🇧🇷 [Curso em Vídeo — Python 3 (Mundos 1, 2 e 3)](https://www.cursoemvideo.com/): ótima base, com 115 exercícios.
- 🎥 [CS50's Introduction to Programming with Python (CS50P — Harvard, gratuito)](https://cs50.harvard.edu/python/)
- 📘🇧🇷 [*Python Fluente* — Luciano Ramalho (2ª ed., versão online gratuita)](https://pythonfluente.com/): o melhor livro de Python intermediário/avançado, escrito por um brasileiro.
- 📘🇧🇷 [*Pense em Python* — Allen Downey (tradução gratuita)](https://penseallen.github.io/PensePython2e/)
- 📘 [*Automate the Boring Stuff with Python* — Al Sweigart (gratuito)](https://automatetheboringstuff.com/)
- 📘 *Python Crash Course* — Eric Matthes
- 🎥 [CS50x — Introduction to Computer Science (Harvard, gratuito)](https://cs50.harvard.edu/x/): base de CC; faça pelo menos as semanas 0 a 5.
- 🌐 [Real Python](https://realpython.com/): tutoriais aprofundados.
- 🌐🇧🇷 [Refactoring.Guru — Padrões de Projeto](https://refactoring.guru/pt-br/design-patterns)

---

## Módulo 4.1 — Introdução ao Python: sintaxe e estruturas de controle (1,5 semana)

### Conceitos
- [ ] Instalação e ambiente: versões, `python -m venv`, `pip`, **uv** (gerenciador moderno), REPL, VS Code com a extensão Python, Jupyter (visão geral)
- [ ] Filosofia: `import this`; PEP 8 (estilo)
- [ ] Indentação como sintaxe
- [ ] Tipos básicos: `int`, `float`, `str`, `bool`, `None`; tipagem dinâmica e forte
- [ ] Operadores: aritméticos (`//`, `%`, `**`), comparação, lógicos (`and`, `or`, `not`), `is` x `==`, `in`
- [ ] Strings: fatiamento (*slicing*), métodos, **f-strings**, formatação de números
- [ ] Entrada e saída: `input()`, `print()` com `sep` e `end`
- [ ] Conversão de tipos
- [ ] **Controle de fluxo**: `if`/`elif`/`else`, expressão condicional, `match`/`case` (*pattern matching*)
- [ ] **Laços**: `for` com `range`, `while`, `break`, `continue`, `else` em laços
- [ ] `enumerate`, `zip`
- [ ] Números: `round`, módulo `math`, `decimal.Decimal` para dinheiro, `random`

### Fontes
- 🌐🇧🇷 Tutorial oficial: capítulos 1 a 4.
- 🎥🇧🇷 Curso em Vídeo — Python Mundos 1 e 2.
- 🎥 CS50P — semanas 0 a 2 (*Functions*, *Conditionals*, *Loops*).
- 📘 *Automate the Boring Stuff*: capítulos 1 a 3.
- 🌐 [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)

### Exercícios
- [ ] **E4.1.1** Os exercícios **001 a 070** do Curso em Vídeo (Mundos 1 e 2). Faça todos, é volume de prática.
- [ ] **E4.1.2** Os *problem sets* 0, 1 e 2 do CS50P (ex.: *Einstein*, *Bank*, *Meal Time*, *camelCase*, *Coke Machine*, *Vanity Plates*).
- [ ] **E4.1.3** Jogo de adivinhação (o computador sorteia, o usuário tenta, com dicas "maior/menor" e contador de tentativas).
- [ ] **E4.1.4** Calculadora de IMC com classificação usando `match`/`case`.
- [ ] **E4.1.5** Converta o FizzBuzz, o palíndromo e a validação de CPF da trilha 1 para Python e compare as linguagens.
- [ ] **E4.1.6** Mostre com exemplo por que usar `Decimal` para dinheiro.
- [ ] **E4.1.7** 20 problemas iniciantes do Beecrowd em Python.

### Autoavaliação
1. Qual a diferença entre `is` e `==`?
2. O que significa dizer que o Python tem tipagem dinâmica **e** forte?
3. Para que serve o `else` de um `for`?
4. Por que usar ambiente virtual?

---

## Módulo 4.2 — Python: coleções, funções, módulos e arquivos (1,5 semana)

### Conceitos
- [ ] **Listas**: métodos, fatiamento, cópia rasa x profunda, mutabilidade
- [ ] **Tuplas** e desempacotamento; `*resto`
- [ ] **Dicionários**: métodos, iteração, `get`, `setdefault`, `defaultdict`, `Counter`
- [ ] **Conjuntos** e operações (união, interseção, diferença)
- [ ] **Compreensões**: de lista, dicionário, conjunto; expressões geradoras
- [ ] **Funções**: parâmetros posicionais, nomeados, padrão (a armadilha do padrão mutável!), `*args`, `**kwargs`, parâmetros somente nomeados (`*`) e somente posicionais (`/`)
- [ ] Escopo (LEGB), `global`, `nonlocal`, closures
- [ ] Funções como objetos, `lambda`, `map`, `filter`, `sorted` com `key`, `functools` (`reduce`, `partial`, `lru_cache`)
- [ ] Docstrings
- [ ] **Módulos e pacotes**: `import`, `from ... import`, `__name__ == "__main__"`, `__init__.py`, estrutura de projeto
- [ ] Biblioteca padrão essencial: `os`, `sys`, `pathlib`, `shutil`, `datetime`, `json`, `csv`, `re`, `subprocess`, `collections`, `itertools`
- [ ] **Arquivos**: `open` com `with` (gerenciador de contexto), modos, codificação (`utf-8`), leitura linha a linha
- [ ] **Exceções**: `try`/`except`/`else`/`finally`, `raise`, exceções personalizadas, `raise ... from`, EAFP x LBYL
- [ ] Pacotes de terceiros: `pip install`, `requirements.txt`, `pyproject.toml`; PyPI

### Fontes
- 🌐🇧🇷 Tutorial oficial: capítulos 5 a 10.
- 🎥🇧🇷 Curso em Vídeo — Python Mundo 3.
- 🎥 CS50P — semanas 3 a 6 (*Exceptions*, *Libraries*, *Unit Tests*, *File I/O*) e 7 (*Regular Expressions*).
- 📘🇧🇷 *Python Fluente*: capítulos 2 (sequências), 3 (dicionários e conjuntos), 7 (funções como objetos).
- 📘 *Automate the Boring Stuff*: capítulos 4 a 10.
- 🌐 [Python Module of the Week (PyMOTW-3)](https://pymotw.com/3/): exemplos da biblioteca padrão.

### Exercícios
- [ ] **E4.2.1** Os exercícios **071 a 115** do Curso em Vídeo (Mundo 3).
- [ ] **E4.2.2** Os *problem sets* 3 a 7 do CS50P.
- [ ] **E4.2.3** Contador de palavras de um arquivo de texto: as 10 mais frequentes (com `Counter`), ignorando acentos e *stopwords*.
- [ ] **E4.2.4** Leia um CSV de ordens de serviço e gere: faturamento por mês, por serviço e por cliente (repita os exercícios do módulo 1.10, agora em Python). Salve o resultado em JSON.
- [ ] **E4.2.5** Mostre o bug do parâmetro padrão mutável (`def f(x=[])`) e corrija.
- [ ] **E4.2.6** Reescreva 10 laços como compreensões e 3 compreensões complicadas como laços (legibilidade importa).
- [ ] **E4.2.7** Decorador `@medir_tempo` e decorador `@tentar_novamente(vezes=3)`.
- [ ] **E4.2.8** Validador de e-mail, telefone e CEP com expressões regulares (`re`).
- [ ] **E4.2.9** Organize os exercícios em um pacote com módulos e um `__main__.py`.
- [ ] **E4.2.10** 20 exercícios da trilha Python do [Exercism](https://exercism.org/tracks/python).

### Autoavaliação
1. Por que tuplas podem ser chave de dicionário e listas não?
2. O que acontece com `def f(x=[])` quando chamada várias vezes?
3. O que significa `if __name__ == "__main__"`?
4. Qual a diferença entre uma compreensão de lista e uma expressão geradora?
5. O que é EAFP e por que é considerado "pythônico"?
6. O que faz o `with` ao abrir um arquivo?

---

## Módulo 4.3 — Python idiomático, tipagem e testes com pytest (1 semana)

### Conceitos
- [ ] Iteradores e **geradores** (`yield`), protocolo de iteração
- [ ] Gerenciadores de contexto próprios (`__enter__`/`__exit__` e `contextlib.contextmanager`)
- [ ] **Decoradores** a fundo (com argumentos, `functools.wraps`)
- [ ] **Type hints**: anotações, `list[int]`, `dict[str, float]`, `Optional`/`X | None`, `Union`, `Callable`, `TypedDict`, `Protocol`, genéricos; verificação com **mypy** ou pyright
- [ ] `dataclasses` e `enum`
- [ ] **Pydantic** para validação de dados
- [ ] Qualidade: **Ruff** (lint + formatação), mypy, pre-commit
- [ ] **pytest**: testes simples com `assert`, *fixtures*, `parametrize`, `raises`, `tmp_path`, `monkeypatch`, *mocks* (`unittest.mock`), cobertura (`pytest-cov`)
- [ ] `logging` (em vez de `print`)
- [ ] `argparse` ou **Typer** para CLIs

### Fontes
- 📘🇧🇷 *Python Fluente*: capítulos 5 (dataclasses), 8 (type hints), 9 (decoradores e closures), 17 (iteradores e geradores), 18 (`with`).
- 🌐 [pytest — docs](https://docs.pytest.org/en/stable/getting-started.html)
- 🌐 [mypy — docs](https://mypy.readthedocs.io/) e [Python typing — docs](https://docs.python.org/3/library/typing.html)
- 🌐 [Ruff — docs](https://docs.astral.sh/ruff/) · [uv — docs](https://docs.astral.sh/uv/)
- 🌐 [Pydantic — docs](https://docs.pydantic.dev/)
- 🌐 [Real Python — Effective Python Testing With pytest](https://realpython.com/pytest-python-testing/)
- 📘 *Effective Python* — Brett Slatkin (90 dicas específicas)
- 📘 *Python Testing with pytest* — Brian Okken

### Exercícios
- [ ] **E4.3.1** Gerador que lê um arquivo de log gigante e produz só as linhas de erro, sem carregar tudo na memória.
- [ ] **E4.3.2** Gerenciador de contexto `cronometro()` que mostra o tempo do bloco.
- [ ] **E4.3.3** Adicione type hints a todos os exercícios do módulo 4.2 e rode `mypy --strict` até zerar os erros.
- [ ] **E4.3.4** Modele `Cliente`, `Servico` e `OrdemDeServico` com `dataclasses` e `Enum` para o status.
- [ ] **E4.3.5** Os mesmos modelos com Pydantic, validando dados vindos de JSON.
- [ ] **E4.3.6** Testes com pytest para tudo o que você fez no módulo 4.2 (use `parametrize` e *fixtures*). Cobertura ≥ 90%.
- [ ] **E4.3.7** Teste uma função que chama uma API externa usando `monkeypatch` ou `unittest.mock`.
- [ ] **E4.3.8** Configure `pyproject.toml` com Ruff, mypy e pytest, e um hook de pre-commit.

### Autoavaliação
1. Qual a vantagem de um gerador sobre uma lista?
2. Os type hints são verificados quando o programa roda?
3. O que uma *fixture* do pytest resolve?
4. `dataclass` ou Pydantic: quando usar cada um?

---

## Módulo 4.4 — Projeto prático: scripts de automação (1 semana)

> Projeto do README ("scripts simples de automação") ligado ao dia a dia de um prestador de serviços de TI.

### Fontes
- 📘 *Automate the Boring Stuff*: capítulos 9 a 20 (arquivos, planilhas, PDF, e-mail, agendamento, web scraping).
- 🌐 [Requests — docs](https://requests.readthedocs.io/) · [httpx](https://www.python-httpx.org/)
- 🌐 [psutil](https://psutil.readthedocs.io/) (informações do sistema)
- 🌐 [openpyxl](https://openpyxl.readthedocs.io/) (Excel) · [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- 🌐 [Paramiko](https://www.paramiko.org/) e [Fabric](https://www.fabfile.org/) (SSH)
- 🌐 [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/) (CLIs bonitas)

### Projetos (faça pelo menos 4, todos com testes, type hints e CLI)
- [ ] **P4.4.1 Organizador de arquivos:** organiza a pasta Downloads por tipo e data, com modo `--simular` e registro do que foi movido (e desfazer).
- [ ] **P4.4.2 Inventário de máquinas:** coleta sistema operacional, CPU, RAM, disco, IP, MAC e programas instalados (`psutil`, `platform`), e exporta para JSON/Excel. Útil para atender clientes.
- [ ] **P4.4.3 Monitor de sites e serviços:** verifica uma lista de URLs e portas (HTTP, SSH, impressoras de rede), mede o tempo de resposta e avisa (e-mail ou Telegram) quando algo cai. (É uma "prévia" do que o Zabbix faz, na trilha 8.)
- [ ] **P4.4.4 Relatório de backups:** lê o log do script de backup da trilha 0, verifica se o backup de cada cliente rodou e gera um relatório em HTML/PDF.
- [ ] **P4.4.5 Gerador de orçamentos em PDF:** recebe os serviços em JSON e gera um orçamento com a identidade visual da Marcelo IT.
- [ ] **P4.4.6 Automação por SSH:** roda o mesmo comando (ex.: atualização) em várias máquinas Linux e junta as saídas.
- [ ] **P4.4.7 Renomeador em massa** de fotos pela data EXIF.
- [ ] **P4.4.8 Web scraper** de preços de peças de informática em 2 lojas, com histórico em SQLite e alerta de queda de preço (respeite o `robots.txt` e os termos de uso).

---

## Módulo 4.5 — POO: classes e objetos (1,5 semana)

### Conceitos
- [ ] Por que orientação a objetos; objetos como dados + comportamento
- [ ] **Classes e objetos**: `class`, `__init__`, `self`, atributos de instância x de classe
- [ ] Métodos de instância, de classe (`@classmethod`, construtores alternativos) e estáticos (`@staticmethod`)
- [ ] **Encapsulamento**: convenções `_protegido` e `__privado` (*name mangling*), `@property` e *setters* com validação
- [ ] **Herança**, `super()`, sobrescrita de métodos, MRO e herança múltipla, *mixins*
- [ ] **Polimorfismo** e *duck typing*
- [ ] **Abstração**: classes abstratas (`abc.ABC`, `@abstractmethod`) x `typing.Protocol`
- [ ] **Composição x herança** ("prefira composição")
- [ ] Métodos especiais (*dunder*): `__repr__`, `__str__`, `__eq__`, `__hash__`, `__lt__`, `__len__`, `__iter__`, `__getitem__`, `__add__`, `__call__`, `__enter__`/`__exit__`
- [ ] Modelo de dados do Python ("tudo é objeto")
- [ ] Imutabilidade: `@dataclass(frozen=True)`, *value objects*
- [ ] Os 4 pilares da POO e suas críticas

### Fontes
- 🌐🇧🇷 Tutorial oficial: capítulo 9 (Classes).
- 📘🇧🇷 *Python Fluente*: capítulos 1 (modelo de dados), 11 (objetos pythônicos), 13 (interfaces, protocolos e ABCs), 14 (herança), 16 (sobrecarga de operadores).
- 🎥 CS50P — semana 8 (*Object-Oriented Programming*).
- 🌐 [Real Python — Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- 🎥🇧🇷 [Curso de Python — Otávio Miranda (seção de POO)](https://www.youtube.com/@OtavioMiranda)

### Exercícios
- [ ] **E4.5.1** Classe `ContaBancaria` com saldo protegido por `@property`, métodos `depositar`, `sacar` (com exceção `SaldoInsuficiente`) e extrato.
- [ ] **E4.5.2** `ContaCorrente` (cheque especial) e `ContaPoupanca` (rendimento) herdando de `Conta` abstrata.
- [ ] **E4.5.3** Classe `Dinheiro` imutável com `Decimal`, `__add__`, `__sub__`, `__mul__`, `__eq__`, `__lt__`, `__repr__` e formatação em R$.
- [ ] **E4.5.4** Classe `Carrinho` que se comporta como uma coleção (`len(carrinho)`, `for item in carrinho`, `carrinho[0]`, `item in carrinho`).
- [ ] **E4.5.5** Hierarquia de `Equipamento` (Computador, Impressora, Roteador, NAS) com método polimórfico `checklist_manutencao()`.
- [ ] **E4.5.6** Refatore o E4.5.5 trocando herança por composição (ex.: `Equipamento` tem uma lista de `Componente`). Escreva qual versão ficou melhor e por quê.
- [ ] **E4.5.7** Use `Protocol` para definir `Notificador` e crie `EmailNotificador`, `TelegramNotificador` e `WhatsAppNotificador` sem herança.
- [ ] **E4.5.8** Construtores alternativos: `Cliente.de_json()` e `Cliente.de_linha_csv()`.
- [ ] **E4.5.9** Jogo de terminal com POO (ex.: batalha de cartas, jogo da forca ou RPG simples com personagens, itens e combate).
- [ ] **E4.5.10** 10 exercícios de POO no Exercism.

### Autoavaliação
1. Qual a diferença entre atributo de classe e de instância? Qual armadilha existe com atributos de classe mutáveis?
2. Quando usar `@classmethod` e quando usar `@staticmethod`?
3. O Python tem atributos realmente privados?
4. O que é *duck typing*?
5. ABC ou Protocol: qual a diferença?
6. Por que "prefira composição a herança"?
7. Se você sobrescreve `__eq__`, o que acontece com `__hash__`?

---

## Módulo 4.6 — SOLID (1 semana)

### Conceitos
- [ ] **S** — *Single Responsibility Principle*: um motivo para mudar
- [ ] **O** — *Open/Closed Principle*: aberto para extensão, fechado para modificação
- [ ] **L** — *Liskov Substitution Principle*: subtipos substituíveis (o exemplo do quadrado e do retângulo)
- [ ] **I** — *Interface Segregation Principle*: interfaces pequenas e específicas
- [ ] **D** — *Dependency Inversion Principle*: depender de abstrações; injeção de dependência
- [ ] Princípios relacionados: DRY, KISS, YAGNI, Lei de Deméter, coesão e acoplamento, "diga, não pergunte"
- [ ] Críticas e limites do SOLID (não aplicar como dogma)
- [ ] *Code smells* que indicam violação de cada princípio

### Fontes
- 📘 *Código Limpo* (Clean Code) — Robert C. Martin: capítulos sobre funções, classes e sistemas.
- 📘 *Arquitetura Limpa* (Clean Architecture) — Robert C. Martin: parte III (princípios de design).
- 📘 *Agile Software Development: Principles, Patterns, and Practices* — Robert C. Martin (a fonte original do SOLID).
- 🌐 [Real Python — SOLID Principles: Improve Object-Oriented Design in Python](https://realpython.com/solid-principles-python/)
- 🌐🇧🇷 [Refactoring.Guru — Princípios de projeto (SOLID)](https://refactoring.guru/pt-br/design-patterns/book) (no livro "Mergulho nos Padrões de Projeto")
- 🎥🇧🇷 Otávio Miranda e Rodrigo Branas (YouTube) — vídeos sobre SOLID.

### Exercícios
Para cada princípio, escreva primeiro um código que o **viole**, depois refatore, com testes antes e depois.
- [ ] **E4.6.1 SRP:** classe `GeradorDeRelatorio` que busca dados, calcula, formata em HTML e envia por e-mail. Separe as responsabilidades.
- [ ] **E4.6.2 OCP:** cálculo de frete com `if tipo == "sedex" ... elif ...`. Refatore para adicionar uma transportadora sem alterar o código existente.
- [ ] **E4.6.3 LSP:** `Retangulo` e `Quadrado`; mostre o teste que quebra e proponha um modelo correto. Outro exemplo: `Passaro.voar()` e `Pinguim`.
- [ ] **E4.6.4 ISP:** interface `Impressora` com `imprimir`, `escanear`, `enviar_fax`; uma impressora simples é obrigada a implementar tudo. Segregue.
- [ ] **E4.6.5 DIP:** `ServicoDeOrdens` que instancia `MySQLRepositorio` e `SmtpEmail` diretamente. Inverta as dependências e injete implementações falsas nos testes.
- [ ] **E4.6.6** Analise um projeto seu das trilhas anteriores (a API da loja, por exemplo) e liste 5 violações de SOLID com a proposta de correção.
- [ ] **E4.6.7** Escreva um texto curto: "quando aplicar SOLID é exagero" (com exemplo).

### Autoavaliação
1. Explique cada princípio em uma frase e dê um exemplo.
2. Qual a diferença entre *inversão* de dependência e *injeção* de dependência?
3. Como o DIP facilita os testes?
4. O que é coesão? E acoplamento?

### Projeto 4.6 — Aplicar SOLID em um projeto Python (projeto do README)
**Sistema de cálculo de orçamento e cobrança** para a Marcelo IT:
- Regras de preço extensíveis (por serviço, por hora, pacote mensal, urgência, deslocamento por distância).
- Descontos extensíveis (cliente PJ, fidelidade, cupom).
- Formas de pagamento extensíveis (Pix, boleto, cartão) e notificação por canais extensíveis.
- Adicionar uma nova regra, desconto, pagamento ou canal **sem modificar** as classes existentes (OCP).
- Testes para cada regra com dublês injetados (DIP).
- README explicando onde e como cada princípio foi aplicado.

---

## Módulo 4.7 — Arquitetura de software: Model, Service e Controller (1,5 semana)

### Conceitos
- [ ] **Separação de responsabilidades** (*separation of concerns*)
- [ ] **MVC** (Model, View, Controller) clássico x **MSC** (Model, Service, Controller) em APIs
- [ ] Papel de cada camada: *controller* (entrada/saída, HTTP ou CLI), *service* (regras de negócio), *model*/*repository* (dados)
- [ ] Regra da dependência: camadas de dentro não conhecem as de fora
- [ ] DTOs e validação na borda
- [ ] Injeção de dependências e composição na raiz (*composition root*)
- [ ] Tratamento de erros entre camadas
- [ ] Frameworks: **FastAPI** (moderno, tipado), **Flask** (minimalista), **Django** (completo, "baterias inclusas") e onde cada um encaixa
- [ ] ORM em Python: **SQLAlchemy** 2.0 e Alembic (migrations); SQLModel
- [ ] Testes por camada

### Fontes
- 📘 [*Architecture Patterns with Python* (Cosmic Python) — Harry Percival e Bob Gregory (gratuito)](https://www.cosmicpython.com/book/preface.html): capítulos 1 a 6 (Repository, Service Layer, Unit of Work). **Fonte principal.**
- 🌐 [FastAPI — Tutorial](https://fastapi.tiangolo.com/pt/tutorial/) 🇧🇷
- 🌐 [SQLAlchemy 2.0 — Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- 🌐 [Alembic — Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- 🌐 [Flask — Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)
- 🌐 [Django — Tutorial oficial](https://docs.djangoproject.com/pt-br/5.2/intro/tutorial01/) 🇧🇷
- 🌐 [Martin Fowler — Service Layer](https://martinfowler.com/eaaCatalog/serviceLayer.html) e [Repository](https://martinfowler.com/eaaCatalog/repository.html)
- 🎥🇧🇷 [FastAPI do Zero — Eduardo Mendes (Dunossauro), gratuito](https://fastapidozero.dunossauro.com/)

### Exercícios
- [ ] **E4.7.1** Sistema de biblioteca **em CLI** com três camadas (CLI → service → repositório em memória).
- [ ] **E4.7.2** Troque o repositório em memória por SQLite com SQLAlchemy **sem mudar** o service nem os testes do service.
- [ ] **E4.7.3** Troque a CLI por uma API FastAPI **sem mudar** o service.
- [ ] **E4.7.4** Adicione Alembic e crie 3 migrations.
- [ ] **E4.7.5** Testes: service com repositório falso (unitário); API com `TestClient` e banco SQLite em memória (integração).
- [ ] **E4.7.6** Faça o curso *FastAPI do Zero* completo.
- [ ] **E4.7.7** Faça o tutorial oficial do Django e compare a organização do Django (MTV) com a sua em camadas.

### Autoavaliação
1. Em qual camada fica a regra "não agendar visita em feriado"? Por quê?
2. O que ganho quando o service não conhece o banco nem o HTTP?
3. Qual a diferença entre MVC e MSC?
4. O que é a *composition root*?

### Projeto 4.7 — Sistema de Ordens de Serviço em Python (projeto do README)
Aplicação Python com organização em camadas:
- Domínio: clientes, equipamentos, OS, itens, técnicos, status (máquina de estados: *aberta → em diagnóstico → aguardando peça → em execução → concluída → entregue*, com transições válidas).
- Interfaces: **CLI** (Typer) e **API** (FastAPI), usando os **mesmos** services.
- Persistência: SQLAlchemy + Alembic (SQLite em dev, MySQL/PostgreSQL em Docker).
- Relatórios: faturamento, OS atrasadas, tempo médio por tipo de serviço.
- Testes: ≥ 85% de cobertura; mypy `--strict`; Ruff.
- Diagrama das camadas no README.

---

## Módulo 4.8 — Padrões de projeto (2 semanas)

### Conceitos
Para cada padrão: **problema que resolve**, estrutura, quando usar, quando **não** usar, exemplo em Python e exemplo no mundo real.

**Padrões do README**
- [ ] **Iterator** (comportamental): percorrer coleções sem expor a estrutura; em Python, `__iter__`/`__next__` e geradores
- [ ] **Adapter** (estrutural): compatibilizar interfaces (ex.: vários provedores de SMS/e-mail)
- [ ] **Strategy** (comportamental): algoritmos intercambiáveis (ex.: cálculo de frete, formas de pagamento); em Python, muitas vezes basta uma função
- [ ] **Decorator** (estrutural): adicionar comportamento sem herança (e a diferença para o decorador `@` do Python)
- [ ] **Observer** (comportamental): notificar interessados em eventos (ex.: mudança de status da OS)
- [ ] **Factory** (criacional): *Simple Factory*, *Factory Method* e *Abstract Factory*

**Outros padrões importantes**
- [ ] **Singleton** (e por que costuma ser um antipadrão; alternativa em Python: módulo)
- [ ] **Builder**
- [ ] **Facade**
- [ ] **Composite**
- [ ] **Proxy**
- [ ] **Command** (com desfazer/refazer)
- [ ] **Template Method**
- [ ] **State** (máquina de estados da OS)
- [ ] **Chain of Responsibility** (pipeline de validações, middlewares)
- [ ] Padrões de arquitetura: **Repository**, **Unit of Work**, **Dependency Injection**, **Specification**
- [ ] Antipadrões: *God Object*, *Spaghetti Code*, *Golden Hammer*, *Lava Flow*

### Fontes
- 🌐🇧🇷 [Refactoring.Guru — Padrões de Projeto](https://refactoring.guru/pt-br/design-patterns): explicações ilustradas com exemplos em Python. **Fonte principal.**
- 📘 *Use a Cabeça! Padrões de Projetos* (Head First Design Patterns) — Freeman e Robson: o mais didático (exemplos em Java, fáceis de traduzir).
- 📘 *Padrões de Projeto* (Design Patterns) — Gamma, Helm, Johnson, Vlissides ("Gang of Four"): o livro original, para consulta.
- 🌐 [Python Patterns Guide — Brandon Rhodes](https://python-patterns.guide/): como os padrões do GoF se traduzem (ou não) para Python.
- 🌐 [faif/python-patterns (GitHub)](https://github.com/faif/python-patterns): coleção de implementações.
- 📘 *Architecture Patterns with Python*: capítulos 2, 4, 6, 8, 13 (Repository, Service Layer, UoW, Events, DI).
- 🎥🇧🇷 [Otávio Miranda — playlist de Design Patterns com Python](https://www.youtube.com/@OtavioMiranda)

### Exercícios
Implemente cada padrão com testes, em `04-python-cc/padroes/<nome>/`, com um README curto (problema, solução, diagrama).
- [ ] **E4.8.1 Iterator:** iterador que percorre as OS de um técnico por prioridade; depois o mesmo com gerador. Um iterador de paginação que busca páginas de uma API sob demanda.
- [ ] **E4.8.2 Adapter:** interface `EnviadorDeMensagem` e adaptadores para duas "APIs" de terceiros com assinaturas diferentes (simuladas).
- [ ] **E4.8.3 Strategy:** cálculo de frete (Correios, transportadora, retirada) com classes e depois com funções. Compare.
- [ ] **E4.8.4 Decorator:** `Notificador` básico decorado com `ComLog`, `ComRetentativa` e `ComCriptografia`, empilháveis.
- [ ] **E4.8.5 Observer:** ao mudar o status de uma OS, notificar cliente (e-mail), técnico (Telegram) e atualizar o painel, com inscrição e cancelamento de ouvintes.
- [ ] **E4.8.6 Factory:** *Factory Method* para criar equipamentos a partir de um JSON; *Abstract Factory* para "kits" de relatório (PDF x HTML) com cabeçalho, tabela e rodapé coerentes.
- [ ] **E4.8.7 Builder:** montar uma consulta SQL ou um orçamento complexo passo a passo.
- [ ] **E4.8.8 Command:** editor de texto simples com desfazer e refazer.
- [ ] **E4.8.9 State:** máquina de estados da OS (transições inválidas lançam exceção).
- [ ] **E4.8.10 Chain of Responsibility:** validações encadeadas de um pedido (estoque, crédito, endereço, fraude).
- [ ] **E4.8.11 Facade:** uma fachada `FecharOrdem` que coordena estoque, cobrança, notificação e relatório.
- [ ] **E4.8.12 Composite:** estrutura de pastas e arquivos com cálculo de tamanho total; ou orçamento com itens e pacotes de itens.
- [ ] **E4.8.13 Singleton:** implemente, depois escreva por que evitá-lo e reescreva com injeção de dependência.
- [ ] **E4.8.14** Identifique 5 padrões na biblioteca padrão do Python ou em frameworks que você usou (Express, React, FastAPI). Ex.: middlewares do Express = Chain of Responsibility.

### Autoavaliação
1. Qual a diferença entre Strategy e State?
2. Qual a diferença entre Adapter, Facade e Decorator?
3. O padrão Decorator do GoF é a mesma coisa que o `@decorador` do Python?
4. Por que o Singleton é considerado um antipadrão por muitos?
5. Em Python, por que alguns padrões do GoF quase "desaparecem"? (funções de primeira classe, *duck typing*, módulos)
6. Onde o padrão Observer aparece no front-end que você já estudou?

---

## Módulo 4.9 — Complexidade de algoritmos e recursão (1 semana)

### Conceitos
- [ ] O que é um algoritmo; correção x eficiência
- [ ] **Notação Big O**: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!); Ω e Θ (noção)
- [ ] Análise de pior caso, caso médio e melhor caso; complexidade de tempo **e** de espaço
- [ ] Complexidade das operações das estruturas do Python (lista, dicionário, conjunto)
- [ ] **Recursão**: caso base, caso recursivo, pilha de chamadas, limite de recursão, recursão de cauda
- [ ] Recursão x iteração; memoização
- [ ] Dividir e conquistar
- [ ] Análise amortizada (noção, com o exemplo da lista dinâmica)

### Fontes
- 📘 *Entendendo Algoritmos* (Grokking Algorithms) — Aditya Bhargava 🇧🇷: o mais didático; capítulos 1 a 4.
- 🌐 [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- 🌐 [Python — TimeComplexity (wiki)](https://wiki.python.org/moin/TimeComplexity)
- 🎥 CS50x — semana 3 (Algorithms).
- 🎥 [MIT 6.006 — Introduction to Algorithms (OCW, gratuito)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

### Exercícios
- [ ] **E4.9.1** Determine a complexidade de 15 trechos de código (escreva-os variando laços simples, aninhados, laços que dividem por 2, recursão).
- [ ] **E4.9.2** Meça empiricamente (`timeit`) a busca em lista x conjunto para 10³, 10⁴, 10⁵, 10⁶ elementos e faça um gráfico (matplotlib).
- [ ] **E4.9.3** Recursão: fatorial, Fibonacci (ingênuo e memoizado; compare o tempo), soma de dígitos, inverter string, potência rápida, torre de Hanói, permutações de uma string, todos os subconjuntos.
- [ ] **E4.9.4** Percorra recursivamente uma estrutura de pastas e calcule o tamanho total.
- [ ] **E4.9.5** Achatar uma lista aninhada de profundidade arbitrária (recursivo e iterativo com pilha).

### Autoavaliação
1. Por que O(n log n) é muito melhor que O(n²) para n = 1.000.000? Faça a conta.
2. Qual a complexidade de `x in lista` e de `x in conjunto`? Por quê?
3. O que acontece na memória em uma recursão muito profunda?
4. Como a memoização transforma o Fibonacci de O(2ⁿ) em O(n)?

---

## Módulo 4.10 — Estruturas de dados (2 semanas)

### Conceitos
- [ ] **Arrays** estáticos e dinâmicos (como a `list` do Python funciona por dentro)
- [ ] **Listas ligadas**: simples, dupla, circular
- [ ] **Pilhas** (LIFO) e **filas** (FIFO); `collections.deque`; fila circular
- [ ] **Tabelas hash**: função hash, colisões (encadeamento x endereçamento aberto), fator de carga, redimensionamento (como o `dict` funciona)
- [ ] **Árvores**: terminologia; **árvore binária de busca** (inserção, busca, remoção, percursos pré/em/pós-ordem e em largura); árvores balanceadas (AVL e rubro-negra, só o conceito)
- [ ] **Heaps** e filas de prioridade (`heapq`)
- [ ] **Tries** (árvores de prefixo)
- [ ] **Grafos**: representações (matriz de adjacência x lista de adjacência), direcionados, ponderados
- [ ] *Union-Find* (conjuntos disjuntos)
- [ ] Quando usar cada estrutura

### Fontes
- 📘 *Entendendo Algoritmos*: capítulos 2, 5, 6, 7.
- 🌐 [VisuAlgo](https://visualgo.net/pt) 🇧🇷: visualização animada de estruturas e algoritmos.
- 🌐 [Problem Solving with Algorithms and Data Structures using Python (Runestone, gratuito)](https://runestone.academy/ns/books/published/pythonds3/index.html)
- 📘 *Estruturas de Dados e Algoritmos com Python* — Goodrich, Tamassia e Goldwasser
- 🎥 CS50x — semana 5 (Data Structures).
- 🎥 [NeetCode — roadmap e vídeos](https://neetcode.io/roadmap)
- 🧪 [LeetCode](https://leetcode.com/) · 🧪🇧🇷 [Beecrowd](https://judge.beecrowd.com/)

### Exercícios
**Implemente do zero, com testes** (em `04-python-cc/estruturas/`):
- [ ] **E4.10.1** Array dinâmico com redimensionamento (e meça o custo amortizado do `append`).
- [ ] **E4.10.2** Lista ligada simples e dupla: inserir no início/fim/posição, remover, buscar, inverter, detectar ciclo (algoritmo de Floyd).
- [ ] **E4.10.3** Pilha e fila (com lista ligada e com array); fila com duas pilhas.
- [ ] **E4.10.4** Tabela hash com encadeamento e redimensionamento (implemente `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__len__`).
- [ ] **E4.10.5** Árvore binária de busca com todos os percursos, altura, mínimo/máximo e remoção.
- [ ] **E4.10.6** Heap mínimo (inserção, extração, *heapify*) e fila de prioridade de OS por urgência.
- [ ] **E4.10.7** Trie para autocompletar nomes de clientes.
- [ ] **E4.10.8** Grafo com lista de adjacência (usado no módulo 4.11).

**Aplicações e problemas:**
- [ ] **E4.10.9** Verificador de parênteses balanceados (pilha).
- [ ] **E4.10.10** Avaliador de expressões em notação polonesa reversa (pilha).
- [ ] **E4.10.11** Cache LRU (dicionário + lista duplamente ligada; depois com `OrderedDict`).
- [ ] **E4.10.12** 40 problemas do LeetCode nível *Easy* (seguindo as categorias *Arrays & Hashing*, *Two Pointers*, *Stack*, *Linked List*, *Trees* do NeetCode 150).

### Autoavaliação
1. Qual a complexidade de inserir no início de uma `list` do Python? E de um `deque`?
2. Como uma tabela hash consegue O(1) em média? Quando vira O(n)?
3. Por que uma árvore binária de busca pode degradar para O(n)? Como as árvores balanceadas resolvem?
4. Quando usar lista de adjacência e quando usar matriz de adjacência?
5. Para que serve um heap?

---

## Módulo 4.11 — Algoritmos: busca, ordenação, grafos, programação dinâmica (2 semanas)

### Conceitos
- [ ] **Busca**: linear e **binária** (e suas variações: primeira ocorrência, ponto de inserção; `bisect`)
- [ ] **Ordenação**: *bubble*, *selection*, *insertion* (O(n²)); **merge sort**, **quick sort**, **heap sort** (O(n log n)); *counting* e *radix sort*; estabilidade; o Timsort do Python
- [ ] Técnicas: dois ponteiros, janela deslizante, prefixo acumulado
- [ ] **Grafos**: **BFS** (menor caminho sem peso), **DFS**, detecção de ciclos, ordenação topológica, **Dijkstra**, componentes conexos, árvore geradora mínima (Kruskal/Prim)
- [ ] **Algoritmos gulosos** (troco, escalonamento de intervalos)
- [ ] **Programação dinâmica**: subproblemas sobrepostos e subestrutura ótima; *top-down* (memoização) x *bottom-up* (tabulação); mochila 0/1, maior subsequência comum, distância de edição, troco mínimo
- [ ] *Backtracking* (N rainhas, sudoku)
- [ ] Problemas P, NP e NP-completo (conceito)

### Fontes
- 📘 *Entendendo Algoritmos*: capítulos 4, 6 a 11.
- 📘 *Algoritmos: Teoria e Prática* (CLRS) — Cormen, Leiserson, Rivest e Stein 🇧🇷: referência completa (denso, para consulta).
- 📘 *The Algorithm Design Manual* — Steven Skiena (muito prático)
- 🌐 VisuAlgo (ordenação, grafos, programação dinâmica).
- 🎥 MIT 6.006 (OCW).
- 🎥 NeetCode — roadmap (vídeos com explicação de cada problema).
- 🌐 [CP-Algorithms](https://cp-algorithms.com/): referência de algoritmos.
- 🌐 [Sorting Algorithms Animations (Toptal)](https://www.toptal.com/developers/sorting-algorithms)

### Exercícios
- [ ] **E4.11.1** Implemente busca binária iterativa e recursiva, e as variações "primeira ocorrência" e "última ocorrência".
- [ ] **E4.11.2** Implemente os 6 algoritmos de ordenação, teste com listas aleatórias, ordenadas e invertidas, e faça um gráfico comparando o tempo.
- [ ] **E4.11.3** Mostre na prática o que é uma ordenação estável.
- [ ] **E4.11.4** BFS: menor número de "saltos" entre dois roteadores em uma topologia de rede (você vai ver isso de novo no OSPF, trilha 9).
- [ ] **E4.11.5** Dijkstra: rota de menor tempo entre clientes para planejar as visitas do dia (grafo com pesos = minutos).
- [ ] **E4.11.6** Ordenação topológica: ordem de instalação de pacotes com dependências.
- [ ] **E4.11.7** Detectar ciclo em um grafo de dependências.
- [ ] **E4.11.8** Programação dinâmica: troco mínimo, mochila 0/1 (escolher serviços que cabem em um orçamento maximizando o valor), maior subsequência comum, distância de edição (base de um "você quis dizer…?").
- [ ] **E4.11.9** *Backtracking*: N rainhas e resolvedor de sudoku.
- [ ] **E4.11.10** 40 problemas do LeetCode (20 *Easy*, 20 *Medium*) nas categorias *Binary Search*, *Sliding Window*, *Graphs*, *1-D DP* do NeetCode 150.
- [ ] **E4.11.11** 20 problemas do Beecrowd nas categorias Grafos e Paradigmas.

### Autoavaliação
1. Por que a busca binária exige a lista ordenada? Qual a complexidade?
2. Por que o quick sort é O(n²) no pior caso e mesmo assim é muito usado?
3. Quando usar BFS e quando usar DFS?
4. Por que o Dijkstra não funciona com pesos negativos?
5. Como reconhecer que um problema pode ser resolvido com programação dinâmica?
6. O que significa um problema ser NP-completo?

---

## Módulo 4.12 — Fundamentos de sistemas: como o computador funciona (1,5 semana)

> Este módulo cria a ponte com DevOps, redes e segurança.

### Conceitos
- [ ] Representação de dados: binário, hexadecimal, complemento de dois, ponto flutuante (IEEE 754), ASCII e Unicode/UTF-8
- [ ] Lógica booleana e portas lógicas; da porta lógica à CPU (visão geral)
- [ ] Arquitetura de computadores: CPU, registradores, memória, cache (hierarquia de memória e latências), barramentos
- [ ] Linguagens compiladas x interpretadas; *bytecode*; como o CPython executa seu código (`dis`)
- [ ] **Sistemas operacionais**: processos x threads, escalonamento, memória virtual, paginação, chamadas de sistema, sistema de arquivos
- [ ] **Concorrência** x **paralelismo**; condições de corrida, *locks*, *deadlock*; o GIL do Python; `threading`, `multiprocessing`, `asyncio`
- [ ] Redes do ponto de vista do programador: *sockets* TCP e UDP
- [ ] Noções de compiladores: análise léxica, sintática, AST (visão geral)

### Fontes
- 📘 *Code: The Hidden Language of Computer Hardware and Software* — Charles Petzold (leitura prazerosa, sem pré-requisitos)
- 🎥 [Nand2Tetris — Build a Modern Computer from First Principles (Coursera/site, gratuito)](https://www.nand2tetris.org/): parte 1 (do NAND à CPU).
- 📘 [*Operating Systems: Three Easy Pieces* — Remzi e Andrea Arpaci-Dusseau (gratuito)](https://pages.cs.wisc.edu/~remzi/OSTEP/): partes de virtualização e concorrência.
- 📘 *Computer Systems: A Programmer's Perspective* (CS:APP) — Bryant e O'Hallaron (avançado)
- 🎥 CS50x — semanas 1 a 4 (C e memória) — programar um pouco em C ajuda muito a entender memória.
- 🎥 [Crash Course Computer Science (YouTube)](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo)
- 🎥🇧🇷 Fabio Akita (Akitando) — séries sobre como computadores e sistemas operacionais funcionam.
- 🌐 [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832)
- 📘 [*Crafting Interpreters* — Robert Nystrom (gratuito)](https://craftinginterpreters.com/) (se quiser ir fundo em compiladores)
- 🌐 [Real Python — Async IO in Python](https://realpython.com/async-io-python/)

### Exercícios
- [ ] **E4.12.1** Converta 20 números entre decimal, binário e hexadecimal à mão; confira com Python.
- [ ] **E4.12.2** Mostre em Python os bytes de uma string com acentos em UTF-8 e em Latin-1 e explique o "mojibake" (`Ã§Ã£o`).
- [ ] **E4.12.3** Faça os projetos 1 a 3 do Nand2Tetris (portas lógicas, ALU, memória).
- [ ] **E4.12.4** Use `dis` para ver o *bytecode* de 3 funções e explique uma delas.
- [ ] **E4.12.5** Crie uma condição de corrida com `threading` (contador compartilhado), mostre o resultado errado e corrija com `Lock`.
- [ ] **E4.12.6** Baixe 50 páginas: sequencial, com `threading`, com `asyncio` + `httpx` e compare o tempo. Faça o mesmo com uma tarefa de CPU (com `multiprocessing`) e explique a diferença (GIL).
- [ ] **E4.12.7** Servidor e cliente de chat TCP com `socket` puro.
- [ ] **E4.12.8** Escreva um programa em C que aloca memória com `malloc`, esquece o `free`, e observe com `valgrind`.

### Autoavaliação
1. Qual a diferença entre processo e thread?
2. O que é memória virtual?
3. Concorrência e paralelismo são a mesma coisa?
4. O que é o GIL e quando ele atrapalha?
5. Por que ler da RAM é muito mais lento que ler do cache da CPU?
6. O que é uma chamada de sistema (*syscall*)?

---

## Módulo 4.13 — Projetos finais (2 semanas)

### Projeto A — Sistema de Ordens de Serviço (versão final)
O projeto 4.7 completo, com: padrões aplicados (State na OS, Observer nas notificações, Strategy no cálculo de preços, Repository + Unit of Work, Factory para relatórios), SOLID documentado, API FastAPI + CLI, Docker Compose, testes ≥ 85%, mypy `--strict`, CI no GitHub Actions.

### Projeto B — Biblioteca de estruturas de dados
Pacote Python `estruturas` publicado no **TestPyPI**, com: lista ligada, pilha, fila, tabela hash, árvore binária de busca, heap, trie e grafo (BFS, DFS, Dijkstra), type hints, testes, documentação e benchmarks comparando com as estruturas nativas.

### Projeto C — Otimizador de rotas de visitas técnicas
Dado um conjunto de clientes (endereços → coordenadas) e janelas de horário, sugerir a ordem das visitas do dia minimizando o deslocamento. Comece com força bruta (poucos clientes), depois uma heurística gulosa (vizinho mais próximo) e compare. Integre com a API do projeto A.

### Mini-projetos extras (escolha pelo menos 2)
- [ ] Interpretador de uma calculadora com variáveis (analisador léxico + sintático + AST)
- [ ] Jogo com Pygame (Snake, Tetris) aplicando POO e padrões
- [ ] Bot de Telegram para consultar o status de uma OS
- [ ] Análise de dados com pandas das OS do ano (faturamento, sazonalidade), com gráficos
- [ ] CS50x completo, com o projeto final

---

## ✅ Checklist de conclusão da Trilha 4
- [ ] 115 exercícios do Curso em Vídeo **ou** todos os *problem sets* do CS50P
- [ ] 4 scripts de automação com testes
- [ ] Todos os padrões de projeto implementados e documentados
- [ ] 80+ problemas do LeetCode/Beecrowd
- [ ] Sistema de OS em Python finalizado
- [ ] Biblioteca de estruturas de dados publicada no TestPyPI
- [ ] Autoavaliações com ≥ 80% de acerto
- [ ] Artigo/post resumindo a trilha
- [ ] **Opcional:** certificado do CS50P ou CS50x (gratuito)
