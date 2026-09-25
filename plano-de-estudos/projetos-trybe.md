# Projetos da Trybe (turma sd-015-a)

Levantamento dos projetos que entreguei na Trybe (julho de 2021 a agosto de 2022), cruzado com as trilhas deste plano. Para cada projeto: qual trilha e módulo ele cobre, o que ficou bem feito e o que vale a pena refazer agora.

**De onde vieram os dados** (levantados em 25/09/2026 com o `gh`, só leitura):

- Repositórios da organização `tryber` com `sd-015-a` no nome: **45**.
- Meus PRs nesses repositórios: **54 PRs em 40 repositórios** (37 projetos individuais e 3 em grupo).
- Status e resultado: comentários dos robôs de avaliação da Trybe (`trybe-evaluation-feedback-*`, `trybe-tech-ops`) e do lint (`github-actions`). O resultado usado é o **último** comentário de avaliação de cada PR.
- Revisões: reviews e comentários de linha de colegas e instrutores (poucos; estão citados em cada projeto).
- Código: leitura do diff de cada PR.

**Como ler:**

- **Resultado:** o desempenho dado pelo avaliador (Suficiente/Insuficiente), os requisitos cumpridos e quantas vezes o avaliador rodou até a versão final. "Recuperação" indica que o projeto foi entregue no prazo de recuperação.
- **Status do PR:** nos projetos individuais o PR fica sempre **aberto** (a Trybe não faz merge; o PR só serve para a avaliação). Nos projetos em grupo, meus PRs foram **mergeados** na branch do grupo.
- **Prioridade para refazer:** 🔴 alta (requisito faltando, bug real ou falha de segurança) · 🟡 média (funciona, mas tem problemas de conceito que o plano cobre) · 🟢 baixa (só polimento).

> Os comentários completos de cada PR (avaliações, lint e reviews) estão no arquivo `feedback.md` da cópia privada de cada repositório em `github.com/marcelo-adriano/<nome-do-repositório>`.

---

## Resumo

| # | Projeto | Trilha · módulos | Resultado final | Refazer |
|---|---------|------------------|-----------------|:-------:|
| 1 | [Lessons Learned](#lessons-learned) | 1 · 1.2, 1.3 | Suficiente · 15/15 | 🟢 |
| 2 | [Playground Functions](#playground-functions) | 1 · 1.7 | Suficiente · 13/13 | 🟢 |
| 3 | [Pixels Art](#pixels-art) | 1 · 1.9 | Suficiente · 12/12 | 🟢 |
| 4 | [To Do List](#to-do-list) | 1 · 1.9, 1.13, **1.15 (Projeto A)** | Suficiente · 14/14 | 🔴 |
| 5 | [Color Guess](#color-guess) | 1 · 1.9 | Suficiente · 7/7 | 🟢 |
| 6 | [Meme Generator](#meme-generator) | 1 · 1.6, 1.9 | Suficiente · 7/7 | 🟢 |
| 7 | [Mistery Letter](#mistery-letter) | 1 · 1.3, 1.9 | Suficiente · 18/18 | 🟢 |
| 8 | [Trybewarts](#trybewarts) (dupla) | 1 · 1.4, 1.6 | Suficiente · 21/21 | 🟡 |
| 9 | [JS Unit Tests](#js-unit-tests) | 1 · 1.14 | Suficiente · 10/10 | 🟡 |
| 10 | [Zoo Functions](#zoo-functions) | 1 · 1.10 | Suficiente · 10/10 | 🟢 |
| 11 | [Shopping Cart](#shopping-cart) | 1 · 1.12, 1.13 | Suficiente · 7/7 | 🟡 |
| 12 | [Jest](#jest) | 1 · 1.14 | Suficiente · 4/4 | 🟡 |
| 13 | [Movie Cards Library](#movie-cards-library) | 2 · 2.3 | Suficiente · 16/16 | 🟢 |
| 14 | [Tryunfo](#tryunfo) | 2 · 2.4, 2.6 | Suficiente · 12/12 | 🟡 |
| 15 | [Trybetunes](#trybetunes) | 2 · 2.5, 2.8, 2.9 | Suficiente · 14/14 | 🟡 |
| 16 | [Frontend Online Store](#frontend-online-store-grupo-14) (grupo) | 2 · 2.4, 2.8, 2.9 | Suficiente · 14/15 | 🟡 |
| 17 | [React Testing Library](#react-testing-library) | 2 · 2.10 | Suficiente · 7/7 | 🟢 |
| 18 | [Trybewallet](#trybewallet) | 2 · 2.11 | Suficiente · 9/9 | 🔴 |
| 19 | [Trivia](#trivia-grupo-13) (grupo) | 2 · 2.5, 2.9, 2.11 | Suficiente · 17/18 | 🟡 |
| 20 | [Star Wars Planets Search](#star-wars-planets-search) | 2 · 2.7 | Suficiente · 6/6 | 🟡 |
| 21 | [Recipes App](#recipes-app-grupo-13) (grupo) | 2 · 2.7, 2.8, 2.10, 2.11 | **Insuficiente** · 74/87 | 🟡 |
| 22 | [Trybers and Dragons](#trybers-and-dragons) | 2 · 2.1, 2.2 (+ 4.5, 4.6) | Suficiente · **8/13** | 🔴 |
| 23 | [Docker To Do List](#docker-to-do-list) | 3 · 3.2, 3.3 | Suficiente · 12/12 | 🟢 |
| 24 | [MySQL All For One](#mysql-all-for-one) | 3 · 3.4 | Suficiente · 27/27 | 🟢 |
| 25 | [MySQL One For All](#mysql-one-for-all) | 3 · 3.5, 3.6 | Suficiente · 11/11 | 🟡 |
| 26 | [MongoDB Commerce](#mongodb-commerce) | 3 · 3.13 | Suficiente · 32/32 | 🟢 |
| 27 | [Talker Manager](#talker-manager) | 3 · 3.1, 3.8, 3.9 | Suficiente · 7/7 | 🟡 |
| 28 | [Store Manager](#store-manager) | 3 · 3.9, 3.12 | Suficiente · **11/14** | 🔴 |
| 29 | [Blogs API](#blogs-api) | 3 · 3.10, 3.11 | Suficiente · 13/13 | 🔴 |
| 30 | [Stranger Things (back e front)](#stranger-things-backend-e-frontend) | 3 · 3.2 · 6 · 6.5, 6.6 | Suficiente · 5/5 e 3/3 | 🟡 |
| 31 | [TrybeSmith](#trybesmith) | 3 · 3.9, 3.11 (+ 2.1) | Suficiente · **4/6** | 🔴 |
| 32 | [Car Shop](#car-shop) | 3 · 3.12, 3.13 (+ 5.4) | **Insuficiente** · 11/26 | 🔴 |
| 33 | [Trybe Futebol Clube](#trybe-futebol-clube) | 3 · 3.14 | Suficiente · 32/35 | 🔴 |
| 34 | [Job Insights](#job-insights) | 4 · 4.2, 4.3 | Suficiente · 16/16 | 🟢 |
| 35 | [Inventory Report](#inventory-report) | 4 · 4.5, 4.8 | Suficiente · 23/23 | 🟢 |
| 36 | [Algorithms](#algorithms) | 4 · 4.9, 4.11 | Suficiente · 22/23 | 🟡 |
| 37 | [TING](#ting) | 4 · 4.10 | Suficiente · 17/17 | 🟡 |
| 38 | [Restaurant Orders](#restaurant-orders) | 4 · 4.2, 4.5 | Suficiente · 16/16 | 🟡 |
| 39 | [Tech News](#tech-news) | 4 · 4.4 (+ 3.13) | Suficiente · 12/13 | 🟡 |

*(Stranger Things são dois repositórios, backend e frontend, contados juntos na linha 30. Por isso a tabela tem 39 linhas para 40 repositórios.)*

**Em números:** Suficiente em 38 dos 40 repositórios; 30 com 100% dos requisitos (obrigatórios e bônus). Os dois com Insuficiente são o **Car Shop** e o **Recipes App** (em grupo). Os projetos incompletos se concentram no fim da trilha de back-end (TrybeSmith, Trybers and Dragons, Store Manager, Car Shop, TFC). Nove projetos foram entregues em **recuperação**: todos os de Python, o TFC, o MongoDB Commerce e o Recipes App.

**Repositórios `sd-015-a` sem PR meu (5):** `sd-015-a-live-lectures` (código das aulas ao vivo), `sd-015-a-stranger-things` (repositório base dos dois projetos Stranger Things), `sd-015-a-project-blogs-api-beta` e `sd-015-a-trybe-futebol-clube-beta` (versões beta dos enunciados) e `sd-015-a-project-delivery-app` (projeto final em grupo; não encontrei PR nem commit meu nele).

---

## Padrões que se repetem (o que mais vale a pena estudar)

Estes problemas aparecem em vários projetos. Corrigir o hábito rende mais do que corrigir cada projeto.

1. **Guardar no estado o que pode ser calculado.** `isSaveButtonDisabled`, `hasTrunfo` e `filter` (Tryunfo), `disableButton` (Trybetunes), a lista de alternativas já renderizada em JSX (Trivia) e o placar duplicado entre o estado local e o Redux (Trivia). Calcule durante o render. → Trilha 2, módulos 2.4 e 2.7.
2. **Usar o DOM como banco de dados.** To Do List e Shopping Cart salvam o `innerHTML` da lista no `localStorage`, e o carrinho soma o total lendo o texto dos itens com regex. O certo é guardar um **array de objetos** e renderizar a partir dele. → 1.10 e 1.13 (o Projeto A de 1.15 cobra exatamente isso).
3. **`async` sem `await`.** O teste de rejeição do projeto Jest não espera a Promise; `categoryIds.forEach(async …)` no Blogs API; `this.model.create(user)` sem `await` no TrybeSmith (o token é assinado com uma Promise). → 1.12 e 3.8.
4. **Segurança de autenticação.** Senha em texto puro no banco (Blogs API, TrybeSmith); segredo JWT fixo no código (TrybeSmith); **hash da senha dentro do token** e o segredo JWT devolvido por uma função (TFC). → 3.11 e o OWASP API Top 10 do Projeto 3.14 A.
5. **Testes.** Os três projetos que exigiam cobertura mínima ficaram sem ela (Recipes App 90%, Car Shop 90%, TFC 80%). Além disso, arquivos de teste da própria Trybe foram commitados com `describe.skip` (Trybers and Dragons, TrybeSmith, TFC) e há arquivos de teste vazios (`SaleController.test.js` no Store Manager, `board.e2e.test.ts` no TFC). → 1.14, 2.10 e 3.12.
6. **Arquivos que não deviam estar no Git.** `.env` (Stranger Things), `tempCodeRunnerFile.py` (Inventory Report), `mkt_campaing.txt` (arquivo de saída com erro de digitação, Restaurant Orders), `cypress/fixtures/example.json` (Trybewarts), `.env.example` **apagado** (Store Manager) e `package-lock.json` regenerado com milhares de linhas alteradas em vários PRs. → 0.4 (Git): `.gitignore`, `git add -p` e revisar o diff antes do PR.
7. **Tratamento de erro ausente.** `.then()` sem `.catch()` (Store Manager), `requests.get` sem `timeout` (Tech News), `verify()` do JWT sem `try/catch` (TFC), `.catch(console.log)` sem avisar o usuário (Shopping Cart). → 1.11 e 3.9.
8. **Código de portfólio.** Mensagens e nomes de brincadeira ficaram no código: `"Tá errado meu chapa!"` (Job Insights), `"NÃO SOU OBRIGADO!!! ME PROCESSA!!!"` (Trybers and Dragons), botões `faire/uoter/anrfe` (Meme Generator), página 404 com o texto `algo` (Trybetunes), dados de teste `'coco'`/`'xixi'` (JS Unit Tests). Também sobraram `console.log` e código comentado em vários projetos. Antes de mostrar qualquer um desses repositórios, limpe isso.
9. **Sorteio enviesado.** `Math.round(Math.random() * n)` sorteia as pontas com metade da chance (Pixels Art, Color Guess, Mistery Letter), e `sort(() => Math.random() - 0.5)` não embaralha de forma uniforme (Trivia). O certo é `Math.floor(Math.random() * (n + 1))` e Fisher-Yates. → 1.7.

---

## Trilha 1 — Básico de Desenvolvimento Web

### Lessons Learned
[PR #3](https://github.com/tryber/sd-015-a-project-lessons-learned/pull/3) · aberto · **Módulos 1.2 (HTML semântico) e 1.3 (CSS)** · Suficiente, 15/15 (6 avaliações) · 🟢

- ✅ Usa `header`, `nav`, `main`, `aside`, `article` e `footer`; a imagem tem `alt` descritivo; comentários citam a fonte do trecho de CSS copiado (bom hábito).
- 🔁 Layout com `float` e largura fixa (`main { width: 1050px }`, `#cabecalho { position: fixed }`): não é responsivo. A tabela não tem `caption` nem `thead`. Há texto *lorem ipsum* e um link "Gógli!".
- 🔁 **Refazer como:** o Projeto 1.2–1.5 (site Marcelo IT Services) já cobre tudo isso com Flexbox/Grid e responsividade. Não vale refazer este isoladamente.

### Playground Functions
[PR #20](https://github.com/tryber/sd-015-a-project-playground-functions/pull/20) · aberto · **Módulo 1.7 (fundamentos de JS)** · Suficiente, 13/13 (5 avaliações) · 🟢

- ✅ Quebra os problemas em funções auxiliares com nomes claros (`eachString`, `formatNumber`, `isBiggerThanNine`); o `triangleCheck` ordena os lados antes de comparar (solução elegante).
- 🔁 `highestCount` **altera o array recebido** (`numbersArray.sort(...)`). `isBiggerThanNine` devolve `undefined` para array vazio. `shuffler` percorre o objeto inteiro em vez de consultar `changeLetter[letter]`. `hadThreeTimes` é O(n²).
- 🔁 **Refazer como:** exercício do módulo 1.10: reescrever cada função com `map`/`filter`/`some`/`reduce`, `const` em vez de `let` e sem efeitos colaterais.

### Pixels Art
[PR #2](https://github.com/tryber/sd-015-a-project-pixels-art/pull/2) · aberto · **Módulo 1.9 (DOM e eventos)** · Suficiente, 12/12 (5 avaliações) · 🟢

- ✅ Funções pequenas e reutilizáveis (`adicionarEventos`, `criarLinhas`, `preencherLinhas`); o quadro é gerado dinamicamente.
- 🔁 Um listener por pixel (use **delegação de eventos** no `#pixel-board`). A validação do tamanho está duplicada (`checkTamanhoDoLado` corrige o valor e `construcaoQuadrado` valida de novo) e o `min="1"` do input não bate com o mínimo 5. A paleta usa `div` clicável, que não é acessível por teclado (use `button`).

### To Do List
[PR #1](https://github.com/tryber/sd-015-a-project-todo-list/pull/1) · aberto · **Módulos 1.9 (DOM) e 1.13 (Web Storage); é o Projeto A do módulo 1.15** · Suficiente, 14/14 (8 avaliações) · 🔴

- ✅ Recebeu o comentário "clean code" no PR. Usa `innerText` (e não `innerHTML`) ao criar tarefas, cria e remove elementos corretamente e tem os botões de mover para cima e para baixo.
- 🔁 **Salva o `innerHTML` da lista no `localStorage`** e, ao recarregar, injeta esse HTML de volta. É frágil (qualquer mudança no HTML quebra os dados salvos) e abre espaço para injeção de HTML.
- 🔁 `removerSelecionado` quebra se nada estiver selecionado; permite criar tarefa vazia; os loops `for (...; index += 0)` deveriam ser `while (lista.firstChild)`; `moverPraCima`/`moverPraBaixo` usam `childNodes` (inclui nós de texto) em vez de `children`; sobrou código comentado.
- 🔁 **Refazer como:** é exatamente o **Projeto A da trilha 1** (módulo 1.15). Guardar `[{ id, texto, concluida, prioridade, vencimento }]`, separar lógica pura (testável) do DOM, adicionar testes e acessibilidade por teclado.

### Color Guess
[PR #18](https://github.com/tryber/sd-015-a-project-color-guess/pull/18) · aberto · **Módulo 1.9 (DOM)** · Suficiente, 7/7 (5 avaliações) · 🟢

- ✅ Código curto e legível; usa regex para comparar a cor exibida com a cor da bola.
- 🔁 Depois de acertar, cada novo clique na bola certa soma +3 de novo (falta travar as bolas até o próximo jogo). O placar vive no texto do DOM (`parseInt(pontos.innerText)`); o certo é uma variável. `Math.round(Math.random() * 5)` sorteia as bolas 0 e 5 com metade da chance (veja o padrão 9).

### Meme Generator
[PR #8](https://github.com/tryber/sd-015-a-project-meme-generator/pull/8) · aberto · **Módulos 1.9 (DOM) e 1.6 (formulários, `input type="file"`)** · Suficiente, 7/7 (5 avaliações) · 🟢

- ✅ Usa `FileReader` para o upload, com links para a documentação da MDN no comentário.
- 🔁 Botões com texto de brincadeira (`faire`, `uoter`, `anrfe`) e imagens com `alt=""`. O texto do meme usa `position: absolute` sem o container ter `position: relative`, então fica posicionado em relação à página. Nove `addEventListener` repetidos (um loop ou delegação resolve). `uploadImage` não verifica se um arquivo foi escolhido.

### Mistery Letter
[PR #11](https://github.com/tryber/sd-015-a-project-mistery-letter/pull/11) · aberto · **Módulos 1.9 (DOM) e 1.3 (CSS: `transform`)** · Suficiente, 18/18 (3 avaliações) · 🟢

- ✅ Valida texto vazio ou só com espaços e limpa a carta anterior antes de gerar outra.
- 🔁 **Bug de CSS:** as classes de rotação e de inclinação definem `transform`, então quando as duas estão no mesmo `span` só a última vale e a rotação nunca aparece. O certo é combinar (`transform: rotate() skewX()`) ou usar as propriedades `rotate`/`translate`. `split(' ')` conta espaços duplos como palavras (use `trim().split(/\s+/)`).

### Trybewarts
[PR #9](https://github.com/tryber/sd-015-a-project-trybewarts/pull/9) · aberto · feito em dupla (com Diego) · **Módulos 1.6 (formulários) e 1.4 (Flexbox)** · Suficiente, 21/21 (10 avaliações) · 🟡

- ✅ Monta um objeto com as respostas antes de exibir, tem contador de caracteres, `preventDefault` e botão de envio liberado pelo checkbox de concordância.
- 🔁 **O campo de senha é `type="email"`** (deveria ser `password`). Vários `label for=""` estão vazios e os checkboxes de matérias não têm rótulo (acessibilidade). `box-sizing: 0` é inválido (deveria ser `border-box`). O seletor `input[name=${nome}` não fecha o `]`. `lang="en"` numa página em português. Também foi commitado `cypress/fixtures/example.json`.
- 🔁 **Refazer como:** o Projeto 1.6 (formulário de orçamento) cobre validação nativa, rótulos e mensagens de erro acessíveis. Use este como lista do que **não** fazer.

### JS Unit Tests
[PR #71](https://github.com/tryber/sd-015-a-project-js-unit-tests/pull/71) · aberto · **Módulo 1.14 (testes)** · Suficiente, 10/10 (10 avaliações) · 🟡

- ✅ Os testes de `restaurant` seguem o comportamento passo a passo (cardápio → pedidos → conta) e verificam o resultado final (`pay() === 116`).
- 🔁 Um `it` com dezenas de `assert` (quando um falha, os seguintes nem rodam); nomes de dados de teste de brincadeira; `// assert.fail()` esquecido; `average` com parâmetros confusos (`verifyString(ifString, ifNull, ...)`, em que `ifNull` é o tamanho da lista).
- 🔁 **Refazer como:** exercícios do módulo 1.14 com Jest/Vitest: um comportamento por `it`, `describe` por função, dados de teste com significado e `it.each` para casos em tabela.

### Zoo Functions
[PR #8](https://github.com/tryber/sd-015-a-project-zoo-functions/pull/8) · aberto · **Módulo 1.10 (arrays, objetos, programação funcional)** · Suficiente, 10/10 (8 avaliações) · 🟢

- ✅ Bom uso de `find`, `filter`, `map`, `reduce`, `some` e `every`, de `new Set` para valores únicos e de parâmetros rest; dá crédito aos colegas que ajudaram.
- 🔁 `getEmployeeByName('Fulano')` com nome inexistente **lança `TypeError`** (`const { ...resposta } = undefined`). `getOldestFromFirstSpecies` começa o `reduce` com `0` e depende da ordem das chaves em `Object.values`. O padrão `const retorno = ...; return retorno;` se repete sem necessidade, e há nomes pouco profissionais (`bissin`, `ze`, `bixinho`).

### Shopping Cart
[PR #6](https://github.com/tryber/sd-015-a-project-shopping-cart/pull/6) · aberto · **Módulos 1.12 (fetch/Promises) e 1.13 (localStorage)** · Suficiente, 7/7 (7 avaliações) · aprovado em review · 🟡

- ✅ Tela de carregamento, desestruturação com renomeação (`{ id: sku, title: name }`) e cadeia de Promises organizada.
- 🔁 HTML quebrado: `<span class="total-price">0</p></span>`. O carrinho é salvo como `innerHTML` e o total é somado com regex sobre o texto dos itens (padrão 2), com erro de ponto flutuante no valor exibido. `fetch` sem checar `response.ok`, e os erros só vão para o `console.log`.
- 🔁 **Refazer como:** exercício do módulo 1.12: `async/await`, estado em array, `Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' })` e mensagem de erro para o usuário.

### Jest
[PR #9](https://github.com/tryber/sd-015-a-project-jest/pull/9) · aberto · **Módulo 1.14 (testes: mocks, assíncrono, setup/teardown)** · Suficiente, 4/4 (3 avaliações) · 🟡

- ✅ Mocks com `jest.fn().mockImplementation`, `beforeEach` e `afterEach`, e `resolves` no teste de sucesso.
- 🔁 **O teste "ocupado" não espera a Promise:** `expect(answerPhone(false)).rejects...` sem `await` nem `return`. O teste passa mesmo que a função mude de comportamento. Todo `resolves`/`rejects` precisa de `await expect(...)`. É um conceito central do módulo 1.14; vale refazer os quatro arquivos do zero.

---

## Trilha 2 — Front-end com TypeScript e React

### Movie Cards Library
[PR #110](https://github.com/tryber/sd-015-a-project-movie-cards-library/pull/110) · aberto · **Módulo 2.3 (componentes e props)** · Suficiente, 16/16 (2 avaliações) · review "Aprovado!" · 🟢

- ✅ Componentes pequenos, `PropTypes.exact` no `movie` e desestruturação aninhada das props.
- 🔁 `alt="qualquerCoisa"` na imagem (use o título do filme). `key` gerada a partir do índice (use o título ou um id). Em TypeScript (módulo 2.3), as `PropTypes` viram tipos.

### Tryunfo
[PR #28](https://github.com/tryber/sd-015-a-project-tryunfo/pull/28) · aberto · **Módulos 2.4 (estado e eventos) e 2.6 (formulários)** · Suficiente, 12/12 (4 avaliações) · 🟡

- ✅ A validação é dividida em funções pequenas (`isEmpty`, `countAttr`, `countAnyAttr`, `isNegative`); um único `onInputChange` com nome de propriedade computado serve para todos os inputs.
- 🔁 **`deleteCard` mexe no DOM direto:** lê o nome via `previousSibling.firstChild.innerText` e esconde o card com `target.parentElement.innerHTML = ''`. Esse "apagar na mão" esconde um bug: a lista filtrada (`filter`) não é atualizada quando uma carta é excluída. O certo é `onClick={() => deleteCard(card.cardName)}` e deixar o React renderizar.
- 🔁 Estado derivado guardado em estado (`isSaveButtonDisabled`, `hasTrunfo`, `filter`) com `setState` encadeados em callbacks (padrão 1). Inputs sem `label`.

### Trybetunes
[PR #126](https://github.com/tryber/sd-015-a-project-trybetunes/pull/126) · aberto · **Módulos 2.5 (ciclo de vida), 2.8 (React Router) e 2.9 (dados do servidor)** · Suficiente, 14/14 (12 avaliações) · 🟡

- ✅ Rotas com `Switch` e página 404, estados de carregamento em todas as telas, `async/await` e *barrel file* para as páginas.
- 🔁 **Bugs:** `{response.length && (...)}` exibe um **"0"** na tela quando não há resultados. Na edição de perfil, a regex de e-mail só aceita um caractere antes do `@` e a condição `inputsValues && !emailVerification` **habilita o botão com e-mail inválido** se os campos estiverem preenchidos. O texto alternativo do `<audio>` vira `[object Object]`. A página 404 mostra `algo`.
- 🔁 `getFavorites`, `handleCheck` e `isFavorite` estão copiados entre `Album` e `Favorites` (vire um hook `useFavorites`).
- 🔁 **Refazer como:** exercício de 2.5–2.9: migrar para componentes de função com hooks e TanStack Query (plano 2.9).

### Frontend Online Store (grupo 14)
PRs mergeados na branch do grupo: [#89](https://github.com/tryber/sd-015-a-project-frontend-online-store/pull/89) (req. 4), [#236](https://github.com/tryber/sd-015-a-project-frontend-online-store/pull/236) (req. 7), [#269](https://github.com/tryber/sd-015-a-project-frontend-online-store/pull/269) (req. 8 e 9), [#320](https://github.com/tryber/sd-015-a-project-frontend-online-store/pull/320) (req. 11), [#390](https://github.com/tryber/sd-015-a-project-frontend-online-store/pull/390) (req. 14), [#394](https://github.com/tryber/sd-015-a-project-frontend-online-store/pull/394) (req. 15) · **Módulos 2.4, 2.8 e 2.9** · Resultado final do grupo ([PR #37](https://github.com/tryber/sd-015-a-project-frontend-online-store/pull/37)): Suficiente, 14/15 · todos os meus PRs aprovados por 2 ou 3 colegas · 🟡

- ✅ Foram meus o detalhe do produto, a avaliação com estrelas (integração com `react-star-rating-component`) e o limite de estoque no carrinho. Estado do carrinho elevado para o `App`; bom trabalho em equipe (PRs pequenos por requisito).
- 🔁 A página de detalhe depende do produto guardado no estado do `App`: **ao recarregar ou abrir a URL direto, `attributes.map` quebra** (o `:id` da rota nunca é usado para buscar o produto). No #390, `product.cartQuantity += 1` **altera o objeto do estado** em vez de criar um novo. O redirecionamento é feito com estado + `<Redirect>` em vez de `<Link>`. As avaliações usam `key={index}`. O #269 teve um erro de lint (props sem validação).
- 🔁 **Refazer como:** o Projeto 2.11 (loja de serviços com Redux) é a versão madura deste projeto: carrinho no Redux Toolkit, dados por id com RTK Query e carrinho persistido.

### React Testing Library
[PR #105](https://github.com/tryber/sd-015-a-project-react-testing-library/pull/105) · aberto · **Módulo 2.10 (testes com RTL)** · Suficiente, 7/7 (6 avaliações) · review com elogios · 🟢

- ✅ Consultas por papel (`getByRole` com `name` e `level`), a boa prática do RTL. Helper `renderWithRouter` com `history`. Testes guiados por dados (percorrer `pokemons` e os tipos únicos com `Set`). O revisor destacou a solução no `Pokedex.test.js` ("Boa solução pra não precisar renderizar o `<App />`").
- 🔁 O revisor sugeriu `beforeEach` em quatro arquivos (a renderização está repetida em todos os testes). O teste "botão para resetar o filtro" **clica e não verifica nada**. `expect(image).toBe(src)` está com valor esperado e valor real trocados. Alguns títulos de teste foram copiados errado (o teste de `NotFound` se chama "No favorite pokemon found"). Troque `userEvent.click` síncrono pela API assíncrona atual (`await user.click`).

### Trybewallet
[PR #4](https://github.com/tryber/sd-015-a-project-trybewallet/pull/4) · aberto · **Módulo 2.11 (Redux)** · Suficiente, 9/9 (14 avaliações) · 🔴

- ✅ Componentes `Input` e `Select` reutilizáveis e com `label`, *reducers* imutáveis, `redux-thunk` para a API de câmbio e modo de edição separado.
- 🔁 **Bug de id:** o `id` da despesa é um contador no estado do `ExpenseForm`; como o `Wallet` troca o `ExpenseForm` pelo `EditForm` durante a edição, o formulário é desmontado e o contador **volta a 0**, gerando despesas com ids repetidos. E o `EditForm` usa o `id` como **índice do array** (`expenses[id]`), o que edita a despesa errada depois de qualquer exclusão.
- 🔁 `<Link><button></button></Link>` (elemento interativo dentro de outro); total do cabeçalho sem arredondamento (`toFixed(2)`); variável global `let moeda` sem uso em `ExpenseRow`; a exclusão manda o objeto inteiro quando bastaria o `id`.
- 🔁 **Refazer como:** Redux Toolkit + TypeScript (módulo 2.11), com `createSlice`, `nanoid()` para os ids e seletores para o total.

### Trivia (grupo 13)
PRs mergeados na branch do grupo: [#86](https://github.com/tryber/sd-015-a-project-trivia-react-redux/pull/86) (req. 4, cabeçalho), [#148](https://github.com/tryber/sd-015-a-project-trivia-react-redux/pull/148) (req. 6 e 7, perguntas), [#197](https://github.com/tryber/sd-015-a-project-trivia-react-redux/pull/197) (req. 9, placar), [#267](https://github.com/tryber/sd-015-a-project-trivia-react-redux/pull/267) (req. 16 a 18, ranking) · **Módulos 2.5, 2.9 e 2.11** · Resultado final do grupo ([PR #90](https://github.com/tryber/sd-015-a-project-trivia-react-redux/pull/90)): Suficiente, 17/18 · 🟡

- ✅ Componente `Options` separado; pontuação por dificuldade com um objeto de pesos (`{ hard: 3, medium: 2, easy: 1 }`); cita a fonte do algoritmo de embaralhamento.
- 🔁 **JSX guardado no estado** (`optionsArray` com componentes já renderizados), o que faz as alternativas não refletirem mudanças de props. Placar e acertos duplicados no estado local e no Redux (padrão 1). `sort(() => Math.random() - 0.5)` enviesa o embaralhamento (padrão 9). As perguntas vêm com entidades HTML (`&quot;`) sem decodificar. Ficaram um `console.log` de depuração e um teste comentado. Depois da última pergunta o jogo volta para a primeira.

### Star Wars Planets Search
[PR #64](https://github.com/tryber/sd-015-a-project-starwars-planets-search/pull/64) · aberto · **Módulo 2.7 (hooks, Context)** · Suficiente, 6/6 (8 avaliações) · 🟡

- ✅ Context API com `Provider` próprio, componentes pequenos, filtros removíveis e colunas já usadas saindo do `select`.
- 🔁 **Viola as regras dos hooks:** `FilterPlanets(planet)` e `SortPlanets()` chamam `useContext` e são chamadas **dentro de um `map`** no render, e não começam com `use`. Mova para dentro de um hook `usePlanets()` que devolve a lista já filtrada e ordenada (com `useMemo`).
- 🔁 A ordenação por nome faz `data.sort(...)` **alterando o estado** original. `key={index}` nas linhas. Valores `unknown` quebram a ordenação numérica (há até um comentário "com problema" e código comentado).

### Recipes App (grupo 13)
PRs mergeados na branch do grupo: [#10](https://github.com/tryber/sd-015-a-project-recipes-app/pull/10) (estrutura inicial), [#52](https://github.com/tryber/sd-015-a-project-recipes-app/pull/52) (login), [#535](https://github.com/tryber/sd-015-a-project-recipes-app/pull/535) (página principal), [#771](https://github.com/tryber/sd-015-a-project-recipes-app/pull/771) (receita em progresso), [#774](https://github.com/tryber/sd-015-a-project-recipes-app/pull/774) (correções), [#782](https://github.com/tryber/sd-015-a-project-recipes-app/pull/782) (receitas feitas). PR principal do grupo aberto por mim: [#14](https://github.com/tryber/sd-015-a-project-recipes-app/pull/14) · **Módulos 2.7, 2.8, 2.10 e 2.11 (+ 1.13)** · Resultado final: **Insuficiente, 74/87** (recuperação, 10 avaliações) · 🟡

- ✅ Minhas partes (receita em progresso e receitas feitas): progresso salvo no `localStorage` por receita, `try/catch` no `fetch`, Context para o filtro e a troca do `<Link>` dentro de um botão desabilitado (#771) por `<Redirect>` (#782), uma boa correção.
- 🔁 **O requisito 1 (cobertura de 90%) nunca foi feito: o projeto não tem testes.** Esse é o principal motivo para voltar a ele.
- 🔁 `const { strTags = '' } = doneData` não protege contra `null`, e a API costuma devolver `strTags: null`, **o que faz `strTags.split(',')` quebrar**. A data de conclusão (`doneDate`) é exibida mas nunca salva. O link de compartilhar tem `http://localhost:3000` fixo no código (use `window.location.origin`). Ingredientes e medidas são filtrados separadamente e podem ficar desalinhados. `key={`${index}-${recipe}`}` vira `"0-[object Object]"`. Ficou um `console.log(receita)`. Faltam dependências nos `useEffect`.
- 🔁 **Refazer como:** escrever os testes das telas que foram minhas (módulo 2.10). Refazer o app inteiro sozinho não compensa; o Projeto B de 2.13 (SPA Marcelo IT) cobre o resto.

### Trybers and Dragons
[PR #131](https://github.com/tryber/sd-015-a-project-trybers-and-dragons/pull/131) · aberto · **Módulos 2.1 e 2.2 (TypeScript); os conceitos de POO e SOLID são os de 4.5 e 4.6** · Suficiente, **8/13** (80% dos obrigatórios; 7 avaliações) · 🔴

- ✅ Classes abstratas (`Race`, `Archetype`), interfaces (`Fighter`, `SimpleFighter`), tipo união (`EnergyType`), campos privados com *getters* e cópia defensiva no getter `energy` (`{ ...this._energy }`).
- 🔁 **Incompleto:** faltam `Monster`, `PVP`, `PVE`, `Dragon` e o `index` (requisitos 9 a 13).
- 🔁 **Os 8 arquivos de teste da Trybe foram commitados com `describe.skip`** (padrão 5). `special()` causa dano zero e imprime `'NÃO SOU OBRIGADO!!! ME PROCESSA!!!'` (padrão 8). `Character` fixa `Elf` e `Mage` no construtor. Erros de digitação em nomes públicos (`Figther`, `_instaces`).
- 🔁 **Refazer como:** terminar em TypeScript `strict` (2.1–2.2) e depois refazer em Python como exercício de POO (4.5) aplicando SOLID (4.6).

---

## Trilha 3 — Back-end com Docker, SQL e Node.js

### Docker To Do List
[PR #98](https://github.com/tryber/sd-015-a-project-docker-todo-list/pull/98) · aberto · **Módulos 3.2 (Docker) e 3.3 (Compose)** · Suficiente, 12/12 (10 avaliações) · 🟢

- ✅ Compose com `depends_on` e variáveis de ambiente para os hosts; comandos corretos.
- 🔁 Sugestões do review no PR: não precisa de aspas no filtro do `docker ps` e `docker container rm -f` substitui o `stop` seguido de `rm`. Nos Dockerfiles, `WORKDIR /` (use `/app`), um nome de estágio (`AS ...`) desnecessário e nenhum `.dockerignore`. Os exercícios 3.2 do plano (multi-stage, usuário não-root) vão além.

### MySQL All For One
[PR #115](https://github.com/tryber/sd-015-a-mysql-all-for-one/pull/115) · aberto · **Módulo 3.4 (consultas básicas; `INSERT`, `UPDATE` e `DELETE`)** · Suficiente, 27/27 (7 avaliações) · 🟢

- ✅ Consultas corretas e simples.
- 🔁 `BETWEEN` entre textos (`'...Order #30' AND '...Order #39'`) funciona por ordem alfabética e pegaria `#300`. `DATE(submitted_date) = ...` impede o uso de índice (use um intervalo). O PR commitou um `package-lock.json` de +8.670 linhas.

### MySQL One For All
[PR #64](https://github.com/tryber/sd-015-a-mysql-one-for-all/pull/64) · aberto · **Módulos 3.5 (modelagem/DDL) e 3.6 (joins, agregações)** · Suficiente, 11/11 (23 avaliações) · 🟡

- ✅ Modelagem normalizada com chaves estrangeiras e chaves primárias compostas (`lista_reproduzidos`, `followed`); `CASE` e `REGEXP` no desafio 11; comentários com as fontes.
- 🔁 `valor DOUBLE` para dinheiro (use `DECIMAL(6,2)`); por causa disso o desafio 6 precisou de gambiarra (`CONCAT(MIN(p.valor), '.00')`). O desafio 2 faz `INNER JOIN` **sem `ON`** (produto cartesiano, corrigido com `COUNT(DISTINCT)`). O desafio 3 junta tabelas com `WHERE` em vez de `ON`. `is_following` faz parte da chave primária sem necessidade. Nomes misturam português e inglês (`albuns`, `valor`, `data_assinatura`).
- 🔁 **Refazer como:** o Projeto 3.5 (banco da loja virtual) pede um documento com as decisões de modelagem; use este como primeiro rascunho.

### MongoDB Commerce
[PR #104](https://github.com/tryber/sd-015-a-mongodb-commerce/pull/104) · aberto · **Módulo 3.13 (NoSQL/MongoDB)** · Suficiente, 32/32 (9 avaliações; recuperação) · 🟢

- ✅ Bom domínio dos operadores de atualização: `$elemMatch`, `$addToSet`, `$push` com `$each`/`$sort`, `$pull`, `$pop`, `$inc` em posição de array e `$currentDate`.
- 🔁 `db.produtos.count()` está depreciado (use `countDocuments`). O PR apagou 4.147 linhas do `package-lock.json`. O exercício E3.13.5 (comparar com o modelo relacional) é um bom complemento.

### Talker Manager
[PR #128](https://github.com/tryber/sd-015-a-project-talker-manager/pull/128) · aberto · **Módulos 3.1 (HTTP/REST), 3.8 (Node, `fs`) e 3.9 (Express)** · Suficiente, 7/7 (9 avaliações) · 🟡

- ✅ Cadeia de middlewares de validação pequenos, token com `crypto.randomBytes` (com a fonte citada), status HTTP corretos (400/401/404/201/204) e `express.Router`.
- 🔁 `readFileSync`/`writeFileSync` **bloqueiam o event loop** (use `fs/promises`, módulo 3.8). `id = length + 1` gera ids repetidos depois de uma exclusão. **`PUT` com id inexistente não devolve 404**: `findIndex` retorna -1 e o código grava em `oldTalkers[-1]`. `parseInt` aceita `4.5` como nota "inteira". O ponto da regex de e-mail não está escapado. O `talker.json` foi alterado no commit.

### Store Manager
[PR #148](https://github.com/tryber/sd-015-a-store-manager/pull/148) · aberto · **Módulos 3.9 (camadas MSC) e 3.12 (testes)** · Suficiente, **11/14** (15 avaliações) · 🔴

- ✅ Separação Model/Service/Controller, **queries parametrizadas** (`?`), pool do `mysql2`, testes unitários com Mocha/Chai/Sinon para models, services e controllers de produtos e status corretos (404/409/422).
- 🔁 **Incompleto:** faltam excluir venda e atualizar e validar o estoque (requisitos 10 a 12); `deleteSale` ficou comentado.
- 🔁 `SaleController` usa `.then()` **sem `.catch()`** (um erro no banco derruba o processo). A validação da venda só olha o **primeiro item** do array (`const [{ quantity }] = request.body`). A verificação de nome duplicado busca todos os nomes em vez de usar `UNIQUE` ou `WHERE`. `SaleController.test.js` está vazio. O `.env.example` foi apagado.
- 🔁 **Refazer como:** junto com o TrybeSmith e o Blogs API, vira o **Projeto 3.14 A (API da loja virtual)**: venda em **transação** (estoque + venda + itens), Zod e testes de integração.

### Blogs API
[PR #117](https://github.com/tryber/sd-015-a-project-blogs-api/pull/117) · aberto · **Módulos 3.10 (ORM/migrations) e 3.11 (autenticação)** · Suficiente, 13/13 (18 avaliações) · 🔴

- ✅ Sequelize com migrations, associação N:N (`PostsCategory`), middleware JWT que carrega o usuário, middleware de dono do post (`isUserOwner`), `attributes: { exclude: ['password'] }` nas respostas e `try/catch` em todas as rotas.
- 🔁 **Senha salva e comparada em texto puro** (`userFound.password !== password`). Use bcrypt/argon2 (módulo 3.11).
- 🔁 `categoryIds.forEach(async ...)` **não espera** as inserções: o post é devolvido antes das categorias existirem e erros se perdem. Use `Promise.all` ou `bulkCreate` dentro de uma **transação**. A busca usa igualdade exata em vez de `Op.like`. As pastas `controllers` contêm os routers (rotas e controllers misturados). A configuração do JWT está duplicada e sobraram `console.log`s.

### Stranger Things (backend e frontend)
[Backend PR #96](https://github.com/tryber/sd-015-a-stranger-things-backend/pull/96) e [frontend PR #89](https://github.com/tryber/sd-015-a-stranger-things-frontend/pull/89) · abertos · **Módulo 3.2 (Docker) e trilha 6, módulos 6.5 (containers em produção) e 6.6 (CI/CD)** · Suficiente, 5/5 e 3/3 · 🟡

- ✅ Configuração por variáveis de ambiente, Dockerfile, deploy no Heroku e workflow de lint no GitHub Actions.
- 🔁 **`.env` commitado** nos dois repositórios (não havia segredo, mas o hábito é perigoso). O Dockerfile copia o código **antes** do `npm install` (perde o cache de camadas) e usa Node 14 (fim de suporte). O front usa `require('dotenv')` no navegador, o que é desnecessário no Create React App. **O plano gratuito do Heroku acabou em 2022**, então os dois apps estão fora do ar.
- 🔁 **Refazer como:** exercícios E6.6.4–E6.6.7: imagem no GHCR, deploy no VPS ou em outro provedor e CI de verdade em `.github/workflows`.

### TrybeSmith
[PR #112](https://github.com/tryber/sd-015-a-project-trybesmith/pull/112) · aberto · **Módulos 3.9 e 3.11 (+ 2.1, TypeScript)** · Suficiente, **4/6** (5 avaliações) · 🔴

- ✅ Camadas em classes com injeção pelo construtor, interfaces, tipos do `mysql2` (`ResultSetHeader`, `RowDataPacket`) e `Promise.all` para montar os pedidos.
- 🔁 **Incompleto:** faltam login e cadastro de pedido (requisitos 5 e 6), e os testes deles foram commitados com `describe.skip`.
- 🔁 **Bug:** `UsersService.create` não usa `await` em `this.model.create(user)`, então o token é assinado com uma Promise (o payload vira `{}`) e um erro na inserção passa despercebido. **Segredo JWT fixo no código** (`'superSecret'`) e senha em texto puro. `GET /orders` faz uma consulta por pedido (problema N+1; um `JOIN` com `JSON_ARRAYAGG` resolve). `getById` na verdade busca por `orderId`.

### Car Shop
[PR #89](https://github.com/tryber/sd-015-a-project-car-shop/pull/89) · aberto · **Módulos 3.13 (MongoDB/Mongoose) e 3.12 (testes); a arquitetura é assunto de 5.4** · **Insuficiente, 11/26** (11 avaliações) · 🔴

- ✅ **A melhor arquitetura entre os projetos:** `MongoModel<T>`, `Service<T>` e `Controller<T>` genéricos e abstratos, validação com **Zod** (`VehicleSchema.extend`), roteador genérico (`CustomRouter<T>`), injeção de dependência pelo construtor e cerca de 450 linhas de testes cobrindo as três camadas.
- 🔁 **Provável causa da nota:** a conexão ficou fixa em `mongodb://mongodb:27017/CarShop` (nome do container do Docker; a linha com `localhost` está comentada). Com isso, **todas as rotas de carros falharam no avaliador**, mesmo implementadas. Use `process.env.MONGO_URI`.
- 🔁 Motos não implementadas (requisitos 18 a 26). A validação de id só testa `id.length < 24` (use `isValidObjectId`). O ano máximo está fixo em `2022`.
- 🔁 **Refazer como:** corrigir a conexão, terminar as motos e bater os 90% de cobertura. É o projeto com melhor custo-benefício para refazer, porque a base já é boa.

### Trybe Futebol Clube
[PR #146](https://github.com/tryber/sd-015-a-trybe-futebol-clube/pull/146) · aberto · **Módulo 3.14 (projeto final: TypeScript, Sequelize, JWT, Docker Compose, testes)** · Suficiente, 32/35 (**27 avaliações**; recuperação) · 🔴

- ✅ Maior projeto individual: modelos Sequelize em TypeScript com associações, **bcrypt**, JWT, Dockerfile com cache de camadas (copia o `package*.json` antes do `npm install`), Compose e cerca de 1.500 linhas de testes. As 27 avaliações mostram persistência.
- 🔁 **Segurança:** o token é assinado com `data: { ...result }`, ou seja, a instância inteira do Sequelize, **incluindo o hash da senha** (um JWT só está codificado em base64, não criptografado). `validate()` devolve o **segredo do JWT** (`segredo: this.secret`) para quem chamou. O `verify()` está sem `try/catch` (comentado), então um token inválido vira **erro 500** em vez de 401. As rotas `PATCH /matches/:id` e `/finish` não exigem token.
- 🔁 **Bugs:** `verifyGoals` recusa placar **0** (`!homeTeamGoals`). `GET /matches` responde `201` em vez de `200`. A mensagem de erro do login tem a chave `mensage`. Divisão por zero na eficiência quando o time não jogou.
- 🔁 Faltam os filtros do leaderboard (requisitos 34 e 35) e a cobertura de 80% (requisito 22); `board.e2e.test.ts` está vazio. `getAll`, `getHome` e `getAway` são três cópias do mesmo código (uma função com um parâmetro resolve; ou uma query SQL com agregação). Os **testes E2E da Trybe** foram commitados com `describe.skip`.

---

## Trilha 4 — Ciência da Computação com Python

### Job Insights
[PR #106](https://github.com/tryber/sd-015-a-project-job-insights/pull/106) · aberto · **Módulos 4.2 (coleções e arquivos CSV) e 4.3 (pytest)** · Suficiente, 16/16 (11 avaliações; recuperação) · 🟢

- ✅ `csv.DictReader`, compreensões de lista, `try/except/else` e uma rota nova no Flask.
- 🔁 **Bug:** `type(job["min_salary"]) != int or type(job["min_salary"]) != int` testa o mesmo campo duas vezes (o segundo deveria ser `max_salary`). A variável `list` esconde a função embutida. A deduplicação é O(n²) com `not in` em lista (use `set`). `isinstance` é preferível a `type(x) != int`. `except ValueError: """nada!"""` (use `pass` ou `continue`). O teste de ordenação reaproveita o mesmo `mock_jobs` alterado entre as asserções. A mensagem de erro é de brincadeira (padrão 8).

### Inventory Report
[PR #99](https://github.com/tryber/sd-015-a-inventory-report/pull/99) · aberto · **Módulos 4.5 (POO) e 4.8 (padrões: Iterator, Strategy, Decorator)** · Suficiente, 23/23 (8 avaliações; recuperação) · 🟢

- ✅ O melhor projeto em Python: `Importer` abstrato com `abc`, importadores intercambiáveis injetados no `InventoryRefactor` (Strategy), `Iterator`/`Iterable` próprios, relatório colorido como Decorator, herança `CompleteReport(SimpleReport)` e `Counter.most_common()`.
- 🔁 **Bug:** `InventoryIterator.__next__` nunca lança `StopIteration`: `if not data` não é verdadeiro para um dicionário preenchido, então o laço termina com **`IndexError`**. `Inventory.data_from_file` repete a lógica dos importadores (e usa `"csv" in path` em vez de `endswith`). `main.py` usa três `if` onde caberia um dicionário `{extensão: importador}`. `tempCodeRunnerFile.py` (arquivo temporário do VS Code) foi commitado e gerou o único aviso de lint.

### Algorithms
[PR #98](https://github.com/tryber/sd-015-a-project-algorithms/pull/98) · aberto · **Módulos 4.9 (complexidade e recursão) e 4.11 (ordenação)** · Suficiente, 22/23 (6 avaliações; recuperação) · 🟡

- ✅ Merge sort implementado do zero; palíndromo nas versões iterativa e recursiva; busca de duplicado em O(n) com dicionário.
- 🔁 **Faltou o requisito de desempenho 3.4** (anagramas: 10.000 execuções em até 8,2 s). O `merge` cria fatias (`lista[start:mid]`) a cada chamada; para anagramas, contar letras (`Counter`) é O(n). `strip(" ")` só remove espaços das pontas.
- 🔁 **Refazer como:** exercício E4.11.2 (os 6 algoritmos de ordenação, medindo e plotando o tempo). Este projeto é um bom ponto de partida.

### TING
[PR #96](https://github.com/tryber/sd-015-a-project-ting/pull/96) · aberto · **Módulo 4.10 (estruturas de dados: fila)** · Suficiente, 17/17 (8 avaliações; recuperação) · 🟡

- ✅ Fila encapsulada, importador de `.txt` com tratamento de `FileNotFoundError`, mensagens de erro em `stderr`.
- 🔁 `dequeue` usa `del self._data[0]`, que é **O(n)** (use `collections.deque` ou dois ponteiros; exercício E4.10.3). **Bug na busca:** com mais de um arquivo na fila, as ocorrências de todos os arquivos são juntadas numa única entrada com o nome do **último** arquivo (`instance.search(i)` depois do laço). A verificação de índice `0 > index < len` só funciona por acaso. `exists_word` e `search_by_word` são quase idênticas.

### Restaurant Orders
[PR #95](https://github.com/tryber/sd-015-a-restaurant-orders/pull/95) · aberto · **Módulos 4.2 (dicionários e conjuntos) e 4.5 (POO)** · Suficiente, 16/16 (5 avaliações; recuperação) · 🟡

- ✅ Operações de conjunto (`difference`) para "o que nunca pediu" e "dias em que nunca foi"; controle de estoque com dicionários.
- 🔁 **Bug latente:** `most_frequent = data[0][1]` seguido de `count[most_frequent]` gera `KeyError` se a primeira linha do CSV não for um pedido da própria pessoa (só funciona com o arquivo do projeto). A lógica de `analyze_log.py` está **copiada** em `TrackOrders` (e presa aos nomes `maria`, `arnaldo` e `joao`). `if x not in s: s.add(x)` é redundante em conjuntos; `Counter` simplifica as contagens. Dois arquivos de saída commitados (`mkt_campaign.txt` e `mkt_campaing.txt`).

### Tech News
[PR #113](https://github.com/tryber/sd-015-a-tech-news/pull/113) · aberto · **Módulo 4.4 (automação e web scraping; é o P4.4.8) e 3.13 (MongoDB)** · Suficiente, 12/13 (8 avaliações; recuperação) · 🟡

- ✅ Scraping com seletores CSS do `parsel`, pausa de 1 s entre requisições (respeita o site), consultas com `$regex` e `Counter.most_common`.
- 🔁 **Faltou o menu interativo** (requisito 13; o `menu.py` só exibe o texto). **`requests.get(url)` sem `timeout`**, então o `except requests.Timeout` nunca acontece. `get_tech_news` baixa a mesma página duas vezes (uma para os links e outra para o "próxima") e entra em erro se não houver próxima página. A entrada do usuário vai direto para o `$regex` (use `re.escape`). `"$options": "-i"` deveria ser `"i"`. `.getall().__len__()` deveria ser `len(...)`.
- 🔁 **Refazer como:** o P4.4.8 (scraper de preços com histórico em SQLite) usa as mesmas técnicas. Aproveite para usar `httpx` com timeout e tentativas.

---

## Por onde começar

Na ordem das trilhas do plano, para refazer quando chegar em cada módulo:

1. **Trilha 1 · módulo 1.15:** To Do List → Projeto A (estado em array, testes, acessibilidade). Refazer os testes do **Jest** com `await` antes disso (1.14).
2. **Trilha 2 · módulo 2.11:** Trybewallet em Redux Toolkit + TypeScript (bugs de id) e, depois, o Projeto 2.11. **Módulo 2.10:** testes das telas do Recipes App que foram suas.
3. **Trilha 2 · módulos 2.1–2.2:** terminar o Trybers and Dragons em TypeScript `strict`, sem os `describe.skip`.
4. **Trilha 3 · módulos 3.12–3.13:** Car Shop (conexão por variável de ambiente, motos e cobertura). A base já é boa, então rende muito para pouco esforço.
5. **Trilha 3 · módulo 3.11:** consertar a autenticação do TFC (payload do token, `try/catch`, rotas protegidas) e do Blogs API (bcrypt).
6. **Trilha 3 · módulo 3.14:** Store Manager + TrybeSmith + Blogs API → **API da loja virtual** (Projeto A), com transações, Zod e testes de integração.
7. **Trilha 4:** Algorithms → E4.11.2; TING → E4.10.3; Tech News → P4.4.8; Inventory Report como referência de padrões para o módulo 4.8.
8. **Trilha 6 · módulo 6.6:** refazer o deploy do Stranger Things fora do Heroku, com CI e imagem no GHCR.
