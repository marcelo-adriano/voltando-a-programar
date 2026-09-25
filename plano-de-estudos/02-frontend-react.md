# Trilha 2 — Front-end com TypeScript e React

> **Objetivo da trilha:** construir aplicações de página única (SPA) com React e TypeScript, com componentes bem desenhados, estado previsível, rotas, formulários validados, testes e boas práticas de performance e acessibilidade.

**Duração:** 10–14 semanas · **Pré-requisitos:** Trilha 1 completa (especialmente JavaScript, módulos, assincronia e testes)

| Módulo | Tema | Duração |
|--------|------|---------|
| 2.1 | TypeScript: fundamentos | 1,5 semana |
| 2.2 | TypeScript: tipos avançados | 1 semana |
| 2.3 | React: componentes, JSX/TSX e props | 1 semana |
| 2.4 | React: estado e eventos | 1 semana |
| 2.5 | React: ciclo de vida, efeitos e refs | 1 semana |
| 2.6 | Formulários | 1 semana |
| 2.7 | Hooks avançados, Context e hooks personalizados | 1 semana |
| 2.8 | React Router e menus de navegação | 1 semana |
| 2.9 | Buscando dados do servidor | 1 semana |
| 2.10 | Testes com React Testing Library | 1,5 semana |
| 2.11 | Estado global com Redux Toolkit | 1,5 semana |
| 2.12 | Estilização, performance, acessibilidade e deploy | 1 semana |
| 2.13 | Projetos finais | 2 semanas |

### Fontes principais da trilha
- 🌐 [react.dev](https://react.dev/) ([pt-br.react.dev](https://pt-br.react.dev/) 🇧🇷): documentação oficial. A seção **Learn** é um curso completo. **Leia inteira.**
- 🌐 [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) ([versão pt-BR, parcial](https://www.typescriptlang.org/pt/docs/) 🇧🇷)
- 🌐 [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
- 🌐 [Total TypeScript — tutoriais gratuitos (Matt Pocock)](https://www.totaltypescript.com/tutorials)
- 📘 *Effective TypeScript* — Dan Vanderkam
- 📘 *Aprendendo React* (Learning React) — Alex Banks e Eve Porcello
- 🎥 [Epic React — Kent C. Dodds](https://www.epicreact.dev/) 💲 · [The Joy of React — Josh Comeau](https://www.joyofreact.com/) 💲
- 🎥 [Full Stack Open — Universidade de Helsinki (gratuito)](https://fullstackopen.com/en/): partes 1 a 7 cobrem React, Node, testes, Redux e TypeScript. **Excelente como curso guia desta trilha e da trilha 3.**
- 🎥🇧🇷 [Rocketseat — conteúdo gratuito de React no YouTube](https://www.youtube.com/@rocketseat)

---

## Módulo 2.1 — TypeScript: fundamentos (1,5 semana)

### Objetivos
- Entender o que o TypeScript resolve, o que ele **não** resolve (os tipos somem em tempo de execução) e tipar código do dia a dia.

### Conceitos
- [ ] O que é TS; transpilação; `tsc`; `tsconfig.json` (`strict`, `target`, `module`, `noUncheckedIndexedAccess`)
- [ ] Inferência de tipos x anotação explícita
- [ ] Tipos básicos: `string`, `number`, `boolean`, `null`, `undefined`, arrays, tuplas
- [ ] `any` x `unknown` x `never` x `void`
- [ ] Tipos de objeto; propriedades opcionais (`?`) e somente leitura (`readonly`)
- [ ] `type` x `interface` (e quando usar cada um)
- [ ] **Union** (`|`) e **intersection** (`&`)
- [ ] Tipos literais (`"pendente" | "concluida"`)
- [ ] **Narrowing**: `typeof`, `instanceof`, `in`, igualdade, *discriminated unions*, *type guards* personalizados (`x is T`)
- [ ] Funções: tipos de parâmetros e retorno, parâmetros opcionais, sobrecarga
- [ ] `enum` x union de literais x objeto `as const`
- [ ] Type assertions (`as`) e por que evitar
- [ ] Non-null assertion (`!`) e por que evitar
- [ ] Classes em TS: modificadores `public`, `private`, `protected`, `readonly`; `implements`
- [ ] Módulos e `import type`
- [ ] Arquivos de declaração (`.d.ts`) e `@types/*`

### Fontes
- 🌐 TypeScript Handbook: *The Basics*, *Everyday Types*, *Narrowing*, *More on Functions*, *Object Types*.
- 🌐 [TypeScript Playground](https://www.typescriptlang.org/play): teste tudo aqui.
- 🌐 Total TypeScript: *Beginner's TypeScript* (gratuito).
- 🎥 Full Stack Open — parte 9 (TypeScript).
- 🧪 [Exercism — trilha TypeScript](https://exercism.org/tracks/typescript)

### Exercícios
- [ ] **E2.1.1** Reescreva em TypeScript (modo `strict`) todos os utilitários da trilha 1 (moeda, datas, CPF, agrupamentos) com os testes.
- [ ] **E2.1.2** Modele os tipos do domínio Marcelo IT: `Cliente`, `Servico`, `OrdemDeServico`, `StatusOS` (union de literais), `Orcamento`.
- [ ] **E2.1.3** Crie uma *discriminated union* `Pagamento = Pix | Cartao | Boleto` e uma função que trata cada caso com `switch`, garantindo **exaustividade** com `never`.
- [ ] **E2.1.4** Escreva um *type guard* `isCliente(x: unknown): x is Cliente` para validar dados vindos de uma API.
- [ ] **E2.1.5** Mostre com exemplo por que `any` desliga a verificação e `unknown` obriga a checar.
- [ ] **E2.1.6** Compare `enum`, union de literais e objeto `as const` para `StatusOS`. Escreva qual prefere e por quê.
- [ ] **E2.1.7** Tipe a resposta do ViaCEP e a função de busca (`Promise<Endereco>`).
- [ ] **E2.1.8** 20 exercícios da trilha TypeScript do Exercism.

### Autoavaliação
1. Os tipos do TS existem quando o código roda no navegador? O que isso implica para validar dados de uma API?
2. Qual a diferença entre `any` e `unknown`?
3. `type` ou `interface`: diferenças práticas?
4. O que é *narrowing*? Cite 4 formas.
5. O que é uma *discriminated union* e como garantir que todos os casos foram tratados?
6. O que faz a opção `strict` do `tsconfig`?

---

## Módulo 2.2 — TypeScript: tipos avançados (1 semana)

### Conceitos
- [ ] **Generics**: funções, interfaces e classes genéricas; restrições (`extends`); valores padrão
- [ ] `keyof`, `typeof` (no nível de tipos), *indexed access types* (`T["campo"]`)
- [ ] *Utility types*: `Partial`, `Required`, `Readonly`, `Pick`, `Omit`, `Record`, `Exclude`, `Extract`, `NonNullable`, `ReturnType`, `Parameters`, `Awaited`
- [ ] *Mapped types* e *conditional types*; `infer`
- [ ] *Template literal types*
- [ ] `satisfies`
- [ ] Validação em tempo de execução com **Zod** e inferência do tipo a partir do schema (`z.infer`)

### Fontes
- 🌐 TypeScript Handbook: *Generics*, *Keyof*, *Typeof*, *Indexed Access*, *Conditional Types*, *Mapped Types*, *Template Literal Types*, *Utility Types*.
- 🌐 Total TypeScript: *TypeScript Generics* e *Type Transformations* (tutoriais gratuitos).
- 🧪 [type-challenges](https://github.com/type-challenges/type-challenges): desafios de tipos (faça os "easy" e alguns "medium").
- 🌐 [Zod — docs](https://zod.dev/)

### Exercícios
- [ ] **E2.2.1** Função genérica `agruparPor<T, K extends keyof T>(itens: T[], chave: K)`.
- [ ] **E2.2.2** Tipo `ApiResponse<T>` com `{ sucesso: true; dados: T } | { sucesso: false; erro: string }`.
- [ ] **E2.2.3** Use `Omit` e `Partial` para criar `NovaOrdem` (sem `id`) e `AtualizacaoOrdem` (campos opcionais).
- [ ] **E2.2.4** Tipo `Getters<T>` que transforma `{ nome: string }` em `{ getNome: () => string }` (mapped + template literal).
- [ ] **E2.2.5** Resolva **todos** os desafios "easy" do type-challenges e 5 "medium".
- [ ] **E2.2.6** Crie schemas Zod para `Cliente` e `OrdemDeServico`, derive os tipos com `z.infer` e valide respostas de API.
- [ ] **E2.2.7** Implemente uma classe genérica `Repositorio<T extends { id: number }>` em memória com `listar`, `buscar`, `criar`, `atualizar`, `remover`, com testes.

### Autoavaliação
1. Para que servem as restrições (`extends`) em generics?
2. Qual a diferença entre `Pick` e `Omit`?
3. Por que validar com Zod se já temos os tipos do TS?
4. O que `satisfies` faz de diferente de uma anotação de tipo?

---

## Módulo 2.3 — React: componentes, JSX/TSX e props (1 semana)

### Conceitos
- [ ] Por que React: UI declarativa x imperativa (compare com o DOM puro da trilha 1)
- [ ] Criando um projeto: **Vite** (`npm create vite@latest` → React + TypeScript); estrutura de pastas
- [ ] JSX/TSX: expressões, atributos (`className`, `htmlFor`), fragmentos, regras
- [ ] Componentes funcionais; um componente por arquivo; nomes em PascalCase
- [ ] **Props**: tipagem com `type`/`interface`, valores padrão, `children` (`React.ReactNode`), desestruturação
- [ ] Renderização condicional (`&&`, ternário, retorno antecipado)
- [ ] Listas e **`key`** (por que índice como key é problemático)
- [ ] Componentes puros; "pensando em React": dividir a UI em uma hierarquia de componentes
- [ ] React DevTools

### Fontes
- 🌐 react.dev — Learn: *Quick Start*, *Thinking in React*, *Describing the UI* (todas as páginas).
- 🌐 React TypeScript Cheatsheet: *Basic → Typing Component Props*.
- 🎥 Full Stack Open — parte 1.

### Exercícios
- [ ] **E2.3.1** Leia *Thinking in React* e faça o exercício da tabela de produtos filtrável **sem olhar a solução**.
- [ ] **E2.3.2** Componente `CardServico` com props tipadas (nome, descrição, preço, ícone, `destaque?: boolean`).
- [ ] **E2.3.3** Componente `Botao` com variantes (`primario | secundario | perigo`) e `children`.
- [ ] **E2.3.4** Componente `Layout` com `Header`, `Footer` e `children` no meio.
- [ ] **E2.3.5** Renderize o catálogo de serviços a partir de um array usando `map` e `key` corretas.
- [ ] **E2.3.6** Mostre um bug causado por usar o índice como `key` (reordenar itens com inputs) e corrija.
- [ ] **E2.3.7** Componente `Badge` de status da OS que muda a cor conforme o `StatusOS`.
- [ ] **E2.3.8** Faça os desafios ao fim de cada página de *Describing the UI* no react.dev.

### Autoavaliação
1. O que significa dizer que o React é declarativo?
2. Por que `key` é necessária em listas? Por que o índice é uma má escolha em listas que mudam?
3. Por que os componentes devem ser puros?
4. O que é `children`?

---

## Módulo 2.4 — React: estado e eventos (1 semana)

### Conceitos
- [ ] Event handlers: `onClick`, `onChange`, `onSubmit`; passar funções x chamar funções; tipagem de eventos (`React.ChangeEvent<HTMLInputElement>`)
- [ ] **`useState`**: estado como "memória" do componente; tipagem (`useState<Cliente | null>(null)`)
- [ ] Renderização e *commit*; estado como *snapshot*; atualizações em lote (*batching*)
- [ ] Atualizador funcional (`setContador(c => c + 1)`)
- [ ] **Imutabilidade**: atualizar objetos e arrays no estado (spread, `map`, `filter`)
- [ ] Estruturando o estado: evitar estado redundante ou duplicado; estado derivado
- [ ] **Elevando o estado** (*lifting state up*); componentes controlados x não controlados
- [ ] Preservar e reiniciar estado (posição na árvore e `key`)
- [ ] `useReducer` (introdução)

### Fontes
- 🌐 react.dev — Learn: *Adding Interactivity* e *Managing State* (todas as páginas, com os desafios).
- 🎥 Full Stack Open — parte 1 (c, d) e parte 2.

### Exercícios
- [ ] **E2.4.1** Contador com +, −, reset e passo configurável.
- [ ] **E2.4.2** Faça **todos os desafios** das páginas *Adding Interactivity* e *Managing State* no react.dev.
- [ ] **E2.4.3** Carrinho de serviços: adicionar, remover, alterar quantidade, total calculado (estado derivado, não armazenado).
- [ ] **E2.4.4** Explique (e demonstre) por que `setX(x + 1)` três vezes seguidas incrementa só 1.
- [ ] **E2.4.5** Acordeão de perguntas frequentes em que só um item fica aberto (estado elevado ao pai).
- [ ] **E2.4.6** Lista de tarefas da trilha 1 reescrita em React (sem persistência ainda), com `useState` e depois com `useReducer`.
- [ ] **E2.4.7** Refatore um estado mal estruturado (com dados duplicados) para uma forma normalizada.

### Autoavaliação
1. Por que alterar o estado diretamente (`lista.push(x)`) não atualiza a tela?
2. O que significa "estado como snapshot"?
3. Quando usar o atualizador funcional?
4. O que é "elevar o estado" e quando fazer?
5. Como forçar um componente a reiniciar o estado?

---

## Módulo 2.5 — React: ciclo de vida, efeitos e refs (1 semana)

### Conceitos
- [ ] **Ciclo de vida** de um componente funcional: montagem, atualização, desmontagem
- [ ] Fases do React: *trigger → render → commit*
- [ ] **`useEffect`**: sincronizar com sistemas externos; array de dependências; função de limpeza (*cleanup*)
- [ ] Por que o efeito roda duas vezes em desenvolvimento (`StrictMode`) e o que isso revela
- [ ] **"You Might Not Need an Effect"**: estado derivado, eventos, reiniciar estado sem efeito
- [ ] Condições de corrida ao buscar dados em efeitos (flag `ignore` ou `AbortController`)
- [ ] **`useRef`**: referência a elementos do DOM (foco, rolagem, medidas) e valores que não causam re-render
- [ ] `useLayoutEffect` (quando raramente usar)
- [ ] Comparação com componentes de classe: `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` (para ler código legado)

### Fontes
- 🌐 react.dev — Learn: *Escape Hatches* (todas as páginas, com desafios). Destaques: *Synchronizing with Effects*, *You Might Not Need an Effect*, *Lifecycle of Reactive Effects*.
- 🌐 react.dev — Reference: [`useEffect`](https://react.dev/reference/react/useEffect), [`useRef`](https://react.dev/reference/react/useRef).
- 🌐 [Dan Abramov — A Complete Guide to useEffect](https://overreacted.io/a-complete-guide-to-useeffect/)

### Exercícios
- [ ] **E2.5.1** Faça todos os desafios de *Escape Hatches* no react.dev.
- [ ] **E2.5.2** Relógio que atualiza a cada segundo, com limpeza do `setInterval` ao desmontar.
- [ ] **E2.5.3** Título da aba (`document.title`) mostrando a quantidade de itens no carrinho.
- [ ] **E2.5.4** Busca de CEP em efeito, com tratamento da condição de corrida (digitar rápido dois CEPs).
- [ ] **E2.5.5** Encontre 3 usos desnecessários de `useEffect` em um código (escreva um de propósito) e remova-os.
- [ ] **E2.5.6** Foco automático no primeiro campo do formulário com `useRef`.
- [ ] **E2.5.7** Componente que registra um listener de `resize` na janela e o remove corretamente.
- [ ] **E2.5.8** Persistência da lista de tarefas no `localStorage` (efeito de sincronização).

### Autoavaliação
1. Para que serve a função retornada pelo `useEffect`?
2. Por que o efeito roda duas vezes em desenvolvimento?
3. Dê 3 exemplos de situações em que você **não** precisa de um efeito.
4. Qual a diferença entre `useRef` e `useState`?
5. O que acontece se o array de dependências estiver faltando uma dependência?

---

## Módulo 2.6 — Formulários (1 semana)

### Conceitos
- [ ] Inputs controlados x não controlados em React
- [ ] Um estado por campo x um objeto de estado para o formulário
- [ ] Validação manual: ao enviar, ao sair do campo (*blur*), ao digitar
- [ ] Mensagens de erro acessíveis
- [ ] **React Hook Form** + **Zod** (`@hookform/resolvers`): registro de campos, erros, `handleSubmit`, `isSubmitting`
- [ ] Formulários com múltiplas etapas (*wizard*)
- [ ] Máscaras de entrada (CPF, telefone, CEP)
- [ ] Upload de arquivos
- [ ] Actions e `useActionState` do React 19 (visão geral)

### Fontes
- 🌐 react.dev — Reference: [`<input>`](https://react.dev/reference/react-dom/components/input), [`<form>`](https://react.dev/reference/react-dom/components/form)
- 🌐 [React Hook Form — docs](https://react-hook-form.com/get-started)
- 🌐 Zod — docs

### Exercícios
- [ ] **E2.6.1** Formulário de cadastro de cliente **só com `useState`**: validação ao enviar e ao sair do campo.
- [ ] **E2.6.2** O mesmo formulário com React Hook Form + Zod. Compare a quantidade de código e de re-renderizações.
- [ ] **E2.6.3** Formulário de orçamento em 3 etapas (dados do cliente → serviços → confirmação) com estado preservado entre as etapas.
- [ ] **E2.6.4** Máscaras de CPF, telefone e CEP; preenchimento automático do endereço pelo ViaCEP.
- [ ] **E2.6.5** Campo dinâmico: lista de equipamentos do cliente (adicionar/remover linhas — `useFieldArray`).
- [ ] **E2.6.6** Validação assíncrona: verificar se o e-mail já existe (simule uma API).

### Autoavaliação
1. O que é um input controlado?
2. Por que o React Hook Form costuma causar menos re-renderizações?
3. Onde colocar o schema Zod para reaproveitá-lo no front e no back-end?

### Projeto 2.6 — Lista de contatos (projeto do README)
**Requisitos:**
- Listar, criar, editar e remover contatos (nome, e-mail, telefone, empresa, observações, favorito).
- Formulário com validação (React Hook Form + Zod), máscara de telefone.
- Busca por nome e filtro por favoritos; ordenação por nome.
- Confirmação antes de remover (modal acessível).
- Persistência no `localStorage` (depois será trocada por uma API na trilha 3).
- Todo em TypeScript `strict`, sem `any`.

---

## Módulo 2.7 — Hooks avançados, Context e hooks personalizados (1 semana)

### Conceitos
- [ ] **`useReducer`** a fundo: ações tipadas (discriminated unions), quando preferir a `useState`
- [ ] **Context API**: `createContext`, `Provider`, `useContext`; *prop drilling*; o custo de re-render do Context
- [ ] Combinar `useReducer` + Context para estado compartilhado
- [ ] **Hooks personalizados**: regras dos hooks, extração de lógica reutilizável, convenção `useAlgo`
- [ ] `useMemo`, `useCallback`, `React.memo`: quando ajudam e quando só atrapalham
- [ ] `useId`, `useTransition`, `useDeferredValue` (visão geral)
- [ ] Composição de componentes: *compound components*, *render props*, *children as function*

### Fontes
- 🌐 react.dev — Learn: *Extracting State Logic into a Reducer*, *Passing Data Deeply with Context*, *Scaling Up with Reducer and Context*, *Reusing Logic with Custom Hooks*.
- 🌐 react.dev — Reference: [Hooks](https://react.dev/reference/react/hooks).
- 🌐 [Kent C. Dodds — How to use React Context effectively](https://kentcdodds.com/blog/how-to-use-react-context-effectively)
- 🌐 [Kent C. Dodds — When to useMemo and useCallback](https://kentcdodds.com/blog/usememo-and-usecallback)
- 🌐 [usehooks-ts](https://usehooks-ts.com/): coleção de hooks prontos (estude o código-fonte de alguns).

### Exercícios
- [ ] **E2.7.1** Tema claro/escuro com Context + hook `useTema()`.
- [ ] **E2.7.2** Carrinho de orçamento com `useReducer` + Context, com ações tipadas (`ADICIONAR`, `REMOVER`, `ALTERAR_QTD`, `LIMPAR`).
- [ ] **E2.7.3** Hooks personalizados com testes: `useLocalStorage<T>`, `useDebounce`, `useFetch<T>`, `useMediaQuery`, `useOnClickOutside`.
- [ ] **E2.7.4** Meça com o React DevTools Profiler uma lista de 1.000 itens, otimize com `React.memo`/`useMemo` e compare. Depois mostre um caso em que a otimização **piorou** ou não mudou nada.
- [ ] **E2.7.5** Componente composto `<Tabs>`, `<Tabs.Lista>`, `<Tabs.Aba>`, `<Tabs.Painel>` com Context interno.
- [ ] **E2.7.6** Sistema de notificações (toasts) global com Context.

### Autoavaliação
1. Quais são as regras dos hooks e por que elas existem?
2. Quando o Context é uma má solução para estado global?
3. `useMemo` sempre melhora a performance? Por quê?
4. O que é *prop drilling* e quais as alternativas?

---

## Módulo 2.8 — React Router e menus de navegação (1 semana)

### Conceitos
- [ ] SPA x MPA; roteamento no cliente; History API
- [ ] React Router: `createBrowserRouter`/`RouterProvider` ou `<BrowserRouter>` + `<Routes>`
- [ ] `Link` x `NavLink` (estado ativo, `aria-current`), `useNavigate`
- [ ] Parâmetros de rota (`/servicos/:id`, `useParams`) e query string (`useSearchParams`)
- [ ] **Rotas aninhadas** e `<Outlet />`; layouts
- [ ] Página 404 e `errorElement`
- [ ] *Loaders* e *actions* (modo *data router*)
- [ ] **Rotas protegidas** (autenticação simulada)
- [ ] *Lazy loading* de rotas (`React.lazy` + `Suspense`)
- [ ] **Menus para boa UX**: indicação da página atual, breadcrumbs, menu responsivo, foco ao trocar de página, rolagem para o topo, títulos de página por rota
- [ ] Configuração do servidor para SPA (redirecionar tudo para `index.html`)

### Fontes
- 🌐 [React Router — docs](https://reactrouter.com/): *Tutorial* e *Start*.
- 🌐 [Nielsen Norman Group — artigos sobre navegação](https://www.nngroup.com/topic/navigation/)
- 🎥 Full Stack Open — parte 7a (React Router).

### Exercícios
- [ ] **E2.8.1** Faça o tutorial oficial do React Router do começo ao fim.
- [ ] **E2.8.2** Site Marcelo IT com rotas: `/`, `/servicos`, `/servicos/:slug`, `/orcamento`, `/sobre`, `/contato`, 404.
- [ ] **E2.8.3** Menu com `NavLink` destacando a página atual e `aria-current="page"`.
- [ ] **E2.8.4** Filtros do catálogo guardados na URL (`?categoria=redes&busca=nas`) para que o link possa ser compartilhado.
- [ ] **E2.8.5** Breadcrumbs gerados a partir das rotas.
- [ ] **E2.8.6** Área `/painel` protegida por login simulado; ao tentar acessar sem login, redireciona e volta depois de logar.
- [ ] **E2.8.7** Lazy loading da área de painel; confira na aba Network que o código só é baixado ao acessar.
- [ ] **E2.8.8** Ao trocar de rota: atualizar `document.title`, rolar para o topo e mover o foco para o `h1`.

### Autoavaliação
1. Por que uma SPA dá erro 404 ao recarregar uma rota interna em alguns servidores?
2. Qual a diferença entre `Link` e `NavLink`?
3. Quando guardar estado na URL em vez de no `useState`?
4. O que o `<Outlet />` faz?

---

## Módulo 2.9 — Buscando dados do servidor (1 semana)

### Conceitos
- [ ] Estados de uma requisição: ocioso, carregando, sucesso, erro; UI para cada um (skeletons)
- [ ] Problemas de buscar com `useEffect` na mão (cache, duplicação, condição de corrida, revalidação)
- [ ] **TanStack Query**: `useQuery`, `useMutation`, chaves de query, cache, `staleTime`, invalidação, atualização otimista
- [ ] Mock de API em desenvolvimento: **MSW** (Mock Service Worker) ou `json-server`
- [ ] Variáveis de ambiente no Vite (`import.meta.env`)
- [ ] Paginação e rolagem infinita
- [ ] `Suspense` e *Error Boundaries*

### Fontes
- 🌐 [TanStack Query — docs](https://tanstack.com/query/latest/docs/framework/react/overview)
- 🌐 [TkDodo's blog — Practical React Query](https://tkdodo.eu/blog/practical-react-query) (série de artigos do mantenedor)
- 🌐 [MSW — docs](https://mswjs.io/docs/)
- 🌐 react.dev — [Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)

### Exercícios
- [ ] **E2.9.1** Hook `useFetch` feito à mão com cancelamento; liste os problemas que ele ainda tem.
- [ ] **E2.9.2** Reescreva com TanStack Query e veja o cache funcionando no *React Query Devtools*.
- [ ] **E2.9.3** Configure o MSW com handlers para `/api/servicos`, `/api/clientes`, `/api/ordens` (CRUD).
- [ ] **E2.9.4** `useMutation` para criar uma OS com atualização otimista e *rollback* em caso de erro.
- [ ] **E2.9.5** Lista de ordens com paginação no servidor.
- [ ] **E2.9.6** Error Boundary que mostra uma mensagem amigável e botão "tentar novamente".

### Autoavaliação
1. Quais problemas o TanStack Query resolve que um `useEffect` com `fetch` não resolve?
2. O que é *stale-while-revalidate*?
3. O que é uma atualização otimista e qual o risco?

---

## Módulo 2.10 — Testes com React Testing Library (1,5 semana)

### Conceitos
- [ ] Filosofia: "quanto mais seus testes se parecem com a forma como o software é usado, mais confiança eles dão"
- [ ] Vitest + `@testing-library/react` + `@testing-library/jest-dom` + `@testing-library/user-event`
- [ ] `render`, `screen`; prioridade das queries: `getByRole` > `getByLabelText` > `getByText` > … > `getByTestId`
- [ ] `getBy` x `queryBy` x `findBy` (e quando usar cada um)
- [ ] `userEvent` x `fireEvent`
- [ ] Testar código assíncrono: `findBy`, `waitFor`
- [ ] Mock de API com **MSW** nos testes
- [ ] Testar componentes com Context, Router e TanStack Query (*wrappers* e `render` customizado)
- [ ] Testar hooks personalizados (`renderHook`)
- [ ] **Testar rotas**: navegação, parâmetros, rota protegida, 404
- [ ] Testes de acessibilidade (`jest-axe` / `vitest-axe`)
- [ ] E2E com Playwright para fluxos críticos
- [ ] Erros comuns com a Testing Library

### Fontes
- 🌐 [Testing Library — React Testing Library](https://testing-library.com/docs/react-testing-library/intro)
- 🌐 [Testing Library — Qual query usar?](https://testing-library.com/docs/queries/about#priority)
- 🌐 [Kent C. Dodds — Common mistakes with React Testing Library](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
- 🧪 [Testing Playground](https://testing-playground.com/): descubra a melhor query para um elemento.
- 🌐 [React Router — Testing](https://reactrouter.com/start/framework/testing) (ou `MemoryRouter` no modo biblioteca)
- 🎥 Full Stack Open — parte 5 (testando React).

### Exercícios
- [ ] **E2.10.1** Teste `CardServico`: renderiza nome, preço formatado e o selo de destaque quando a prop é verdadeira.
- [ ] **E2.10.2** Teste o carrinho: adicionar, remover e alterar quantidade atualizam o total.
- [ ] **E2.10.3** Teste o formulário de cliente: erros aparecem com dados inválidos; `onSubmit` é chamado com os dados certos.
- [ ] **E2.10.4** Teste a busca de CEP com MSW: sucesso, CEP inexistente e erro do servidor.
- [ ] **E2.10.5** Teste o hook `useLocalStorage` com `renderHook`.
- [ ] **E2.10.6** Teste de rotas: clicar no menu leva à página certa; rota inexistente mostra 404; `/painel` redireciona para login se não autenticado.
- [ ] **E2.10.7** Teste de acessibilidade com axe nas páginas principais.
- [ ] **E2.10.8** Crie um `renderComProviders()` que envolve Router, QueryClient e Context de tema.
- [ ] **E2.10.9** Refatore um componente (mudando a implementação interna) e confirme que os testes continuam passando. Se quebrarem, eles estavam testando implementação.
- [ ] **E2.10.10** 3 testes E2E com Playwright: fluxo completo de orçamento, login no painel, criar uma OS.

### Autoavaliação
1. Por que preferir `getByRole` a `getByTestId`?
2. Qual a diferença entre `getBy`, `queryBy` e `findBy`?
3. Por que usar `userEvent` em vez de `fireEvent`?
4. Por que o MSW é melhor que mockar o `fetch` diretamente?

---

## Módulo 2.11 — Estado global com Redux Toolkit (1,5 semana)

### Conceitos
- [ ] Quando você precisa (e quando **não** precisa) de estado global; estado do servidor x estado do cliente
- [ ] Princípios do Redux: *store* única, estado somente leitura, mudanças por funções puras (*reducers*)
- [ ] Fluxo de dados: *action → reducer → store → UI*
- [ ] **Redux Toolkit (RTK)**: `configureStore`, `createSlice`, Immer (mutação "segura"), `createAsyncThunk`
- [ ] `react-redux`: `Provider`, `useSelector`, `useDispatch`; hooks tipados (`useAppSelector`, `useAppDispatch`)
- [ ] Seletores e memoização (`createSelector`)
- [ ] Normalização (`createEntityAdapter`)
- [ ] **RTK Query** (alternativa ao TanStack Query dentro do ecossistema Redux)
- [ ] Redux DevTools: *time-travel debugging*
- [ ] Testar reducers, seletores e componentes conectados
- [ ] Alternativas: Zustand, Jotai, Context + `useReducer`; como escolher

### Fontes
- 🌐 [Redux — Redux Essentials Tutorial](https://redux.js.org/tutorials/essentials/part-1-overview-concepts): **faça do início ao fim**.
- 🌐 [Redux — Redux Fundamentals](https://redux.js.org/tutorials/fundamentals/part-1-overview) (para entender o Redux "puro" por baixo do RTK)
- 🌐 [Redux Style Guide](https://redux.js.org/style-guide/)
- 🌐 [Redux — Writing Tests](https://redux.js.org/usage/writing-tests)
- 🌐 [Zustand — docs](https://zustand.docs.pmnd.rs/)
- 🎥 Full Stack Open — parte 6 (Redux, React Query, Context).

### Exercícios
- [ ] **E2.11.1** Implemente um mini-Redux do zero (`createStore` com `getState`, `dispatch`, `subscribe`) em ~30 linhas para entender a ideia.
- [ ] **E2.11.2** Faça o tutorial *Redux Essentials* completo.
- [ ] **E2.11.3** Migre o carrinho de orçamento de Context para um *slice* do RTK.
- [ ] **E2.11.4** *Slice* de autenticação (usuário, token, status) com `createAsyncThunk` para login.
- [ ] **E2.11.5** Seletores memoizados: total do carrinho, itens por categoria.
- [ ] **E2.11.6** Use `createEntityAdapter` para as ordens de serviço.
- [ ] **E2.11.7** Reescreva as chamadas de API com RTK Query e compare com o TanStack Query.
- [ ] **E2.11.8** Testes: reducers (unitários), seletores e um componente conectado com `render` que cria uma store real.
- [ ] **E2.11.9** Implemente o mesmo carrinho com Zustand. Escreva uma comparação: Context x Redux x Zustand.

### Autoavaliação
1. Por que os reducers precisam ser funções puras?
2. Como o Immer permite "mutar" o estado em um `createSlice`?
3. O que é estado do servidor e por que ele geralmente não deveria estar no Redux?
4. Quando o Redux vale a pena?

### Projeto 2.11 — Loja de serviços com Redux
Catálogo de serviços + carrinho + checkout (simulado) + área do cliente com histórico de pedidos. Estado do carrinho e da autenticação no Redux, dados do servidor via RTK Query (com MSW). Carrinho persistido entre sessões.

---

## Módulo 2.12 — Estilização, performance, acessibilidade e deploy (1 semana)

### Conceitos
- [ ] Opções de estilo: CSS Modules, Tailwind CSS, CSS-in-JS; bibliotecas de componentes acessíveis (Radix UI, shadcn/ui, Headless UI)
- [ ] Design system: tokens, componentes base, Storybook
- [ ] Performance: *code splitting*, lazy loading, tamanho do bundle (`rollup-plugin-visualizer`), imagens, Core Web Vitals (LCP, INP, CLS)
- [ ] Acessibilidade em SPAs: foco, anúncios de mudança (`aria-live`), modais, navegação por teclado
- [ ] Internacionalização (visão geral)
- [ ] Deploy: Vercel, Netlify, GitHub Pages (com rotas de SPA); variáveis de ambiente
- [ ] Frameworks sobre o React (visão geral): **Next.js**, React Router em modo framework; renderização no servidor (SSR), geração estática (SSG), React Server Components

### Fontes
- 🌐 [Tailwind CSS — docs](https://tailwindcss.com/docs)
- 🌐 [CSS Modules](https://github.com/css-modules/css-modules)
- 🌐 [Radix UI](https://www.radix-ui.com/) · [shadcn/ui](https://ui.shadcn.com/)
- 🌐 [Storybook — tutorial](https://storybook.js.org/tutorials/)
- 🌐 [web.dev — Core Web Vitals](https://web.dev/articles/vitals)
- 🌐 [Next.js — Learn](https://nextjs.org/learn)
- 🌐 [patterns.dev](https://www.patterns.dev/): padrões de design, renderização e performance em JavaScript/React (gratuito).

### Exercícios
- [ ] **E2.12.1** Estilize a lista de contatos com CSS Modules e depois com Tailwind. Compare.
- [ ] **E2.12.2** Crie 5 componentes base (Botão, Input, Modal, Card, Badge) com stories no Storybook.
- [ ] **E2.12.3** Analise o bundle, identifique a maior dependência e reduza o tamanho inicial com lazy loading.
- [ ] **E2.12.4** Meça LCP, INP e CLS do site e melhore pelo menos uma métrica.
- [ ] **E2.12.5** Faça o deploy de um projeto na Vercel ou Netlify com rotas de SPA funcionando e variáveis de ambiente.
- [ ] **E2.12.6** Faça o curso *Learn Next.js* e escreva uma comparação: SPA com Vite x Next.js.

---

## Módulo 2.13 — Projetos finais (2 semanas)

### Projeto A — Lista de contatos (versão final)
Requisitos do projeto 2.6, mais: rotas (`/contatos`, `/contatos/novo`, `/contatos/:id`, `/contatos/:id/editar`), busca na URL, TanStack Query + MSW simulando a API, testes (unitários, de componentes, de rotas e 2 E2E), Storybook dos componentes base, deploy.

### Projeto B — Marcelo IT Services SPA
- Site institucional em React + TS, com rotas e todas as funcionalidades da trilha 1.
- **Orçamento online:** escolher serviços, quantidades, endereço (ViaCEP), data desejada (desabilitando feriados via BrasilAPI), resumo e envio.
- **Painel do técnico** (rota protegida): lista de OS com filtros, detalhe da OS, mudança de status, agenda de visitas da semana.
- Estado: Redux Toolkit (carrinho, autenticação) + TanStack Query ou RTK Query (dados do servidor, simulados com MSW até a trilha 3).
- Qualidade: TypeScript `strict`, ESLint, Prettier, Husky, testes com cobertura ≥ 70%, 3+ testes E2E, Lighthouse ≥ 90, axe sem violações.
- CI simples com GitHub Actions rodando lint, testes e build a cada PR (introdução; aprofundado na trilha 6).

### Mini-projetos extras (escolha pelo menos 2)
- [ ] Clone do Kanban (Trello) com arrastar e soltar (`dnd-kit`)
- [ ] Dashboard de métricas com gráficos (Recharts)
- [ ] App de clima com geolocalização
- [ ] Jogo (jogo da velha com histórico, que é o tutorial antigo do React, ou Wordle em português)

---

## ✅ Checklist de conclusão da Trilha 2
- [ ] Documentação *Learn* do react.dev lida, com todos os desafios feitos
- [ ] type-challenges: todos os "easy"
- [ ] Redux Essentials completo
- [ ] Lista de contatos publicada, com testes
- [ ] Marcelo IT Services SPA publicada com painel do técnico
- [ ] Autoavaliações com ≥ 80% de acerto
- [ ] Artigo/post resumindo a trilha
