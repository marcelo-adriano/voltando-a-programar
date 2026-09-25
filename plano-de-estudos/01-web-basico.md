# Trilha 1 — Básico de Desenvolvimento Web

> **Objetivo da trilha:** construir páginas semânticas, acessíveis e responsivas com HTML e CSS, e programar com JavaScript moderno com qualidade: lint, testes, tratamento de erros e código assíncrono.

**Duração:** 12–16 semanas · **Pré-requisitos:** Trilha 0

| Módulo | Tema | Duração |
|--------|------|---------|
| 1.1 | Como a web funciona | 3 dias |
| 1.2 | HTML: estrutura, semântica e acessibilidade | 1,5 semana |
| 1.3 | CSS: fundamentos, cascata, seletores e box model | 1,5 semana |
| 1.4 | CSS: posicionamento, Flexbox e Grid | 1,5 semana |
| 1.5 | Responsividade | 1 semana |
| 1.6 | Formulários e validação | 1 semana |
| 1.7 | JavaScript: fundamentos da linguagem | 2 semanas |
| 1.8 | Ferramentas: npm, ESLint, Prettier, Vite | 3 dias |
| 1.9 | DOM e eventos | 1,5 semana |
| 1.10 | Arrays, objetos e programação funcional | 1 semana |
| 1.11 | Exceções e depuração | 4 dias |
| 1.12 | Assincronia: event loop, Promises, fetch, async/await | 1,5 semana |
| 1.13 | Web Storage e cookies | 4 dias |
| 1.14 | Testes em JavaScript | 1,5 semana |
| 1.15 | Projetos finais da trilha | 2 semanas |

### Fontes principais da trilha (use como espinha dorsal)
- 🌐 [MDN Web Docs](https://developer.mozilla.org/pt-BR/) 🇧🇷: a referência oficial de fato. Tem a trilha [Aprendendo desenvolvimento web](https://developer.mozilla.org/pt-BR/docs/Learn).
- 🌐 [web.dev/learn](https://web.dev/learn): cursos do Google: Learn HTML, Learn CSS, Learn Accessibility, Learn Forms, Learn Responsive Design.
- 🌐 [javascript.info](https://javascript.info/) ([versão em português, parcial](https://pt.javascript.info/) 🇧🇷): o melhor tutorial de JavaScript moderno.
- 🌐 [The Odin Project — Foundations](https://www.theodinproject.com/paths/foundations/courses/foundations)
- 🎥🇧🇷 [Curso em Vídeo — HTML5 e CSS3 (módulos 1 a 4) e JavaScript](https://www.cursoemvideo.com/)
- 📘 [*Eloquent JavaScript* — Marijn Haverbeke (gratuito)](https://eloquentjavascript.net/)
- 📘 [*You Don't Know JS Yet* — Kyle Simpson (gratuito no GitHub)](https://github.com/getify/You-Dont-Know-JS)

---

## Módulo 1.1 — Como a web funciona (3 dias)

### Objetivos
- Entender cliente/servidor, navegador, HTTP, DNS e o processo de renderização da página.

### Conceitos
- [ ] Cliente x servidor; navegador como cliente HTTP
- [ ] URL: protocolo, domínio, porta, caminho, query string, fragmento
- [ ] Requisição e resposta HTTP; o que é um recurso estático
- [ ] Como o navegador renderiza: parse do HTML → DOM, CSS → CSSOM, render tree, layout, paint
- [ ] DevTools: abas Elements, Console, Network, Sources, Application, Lighthouse

### Fontes
- 🌐 [MDN — Como a Web funciona](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) 🇧🇷
- 🌐 [MDN — Como os navegadores funcionam](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/How_browsers_work)
- 🌐 [Chrome DevTools — documentação](https://developer.chrome.com/docs/devtools)

### Exercícios
- [ ] **E1.1.1** Abra a aba Network e carregue um site grande. Quantas requisições? Qual o maior arquivo? Quanto tempo até o `DOMContentLoaded`?
- [ ] **E1.1.2** Decomponha 5 URLs reais em suas partes.
- [ ] **E1.1.3** Rode o Lighthouse no `homepage.html` e anote as notas atuais (você vai comparar depois).

### Autoavaliação
1. O que acontece entre digitar a URL e ver a página (resuma em 6 passos)?
2. Por que um `<script>` no `<head>` sem `defer` pode deixar a página lenta?

---

## Módulo 1.2 — HTML: estrutura, semântica e acessibilidade (1,5 semana)

### Objetivos
- Escrever HTML válido, semântico e acessível.
- Saber escolher a tag correta pelo **significado**, não pela aparência.

### Conceitos
- [ ] `<!DOCTYPE html>`, `<html lang>`, `<head>`, `<body>`
- [ ] Metadados: `charset`, `viewport`, `title`, `description`, Open Graph, favicon
- [ ] Texto: `h1`–`h6` (hierarquia!), `p`, `strong` x `b`, `em` x `i`, `blockquote`, `code`, `pre`
- [ ] Listas: `ul`, `ol`, `li`, `dl`/`dt`/`dd`
- [ ] Links: `a`, `href` absoluto/relativo, âncoras `#id`, `target="_blank"` + `rel="noopener"`, `mailto:`, `tel:`
- [ ] Imagens: `img`, `alt` (quando vazio, quando descritivo), `width`/`height`, `loading="lazy"`, `picture`, `srcset`, formatos (WebP, AVIF, SVG)
- [ ] Semântica: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `figure`/`figcaption`, `address`, `time`
- [ ] Elementos em bloco x em linha; `div` e `span` (quando não há tag semântica)
- [ ] Tabelas: `table`, `thead`, `tbody`, `th` com `scope`, `caption` (só para dados tabulares!)
- [ ] Áudio, vídeo, `iframe`
- [ ] Acessibilidade: leitores de tela, navegação por teclado, foco, landmarks, textos alternativos, contraste
- [ ] ARIA: a primeira regra do ARIA ("não use ARIA se existe HTML nativo"), `aria-label`, `aria-expanded`, `aria-current`
- [ ] SEO básico: títulos, descrição, hierarquia de cabeçalhos, HTML semântico
- [ ] Validação: W3C Validator

### Fontes
- 🌐 [web.dev — Learn HTML](https://web.dev/learn/html)
- 🌐 [web.dev — Learn Accessibility](https://web.dev/learn/accessibility)
- 🌐 [MDN — Estruturando conteúdo com HTML](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Structuring_content) 🇧🇷
- 🌐 [HTML Living Standard (WHATWG)](https://html.spec.whatwg.org/multipage/): consulta da especificação.
- 🌐 [W3C Markup Validation Service](https://validator.w3.org/)
- 🌐 [WebAIM](https://webaim.org/): artigos sobre acessibilidade; [verificador de contraste](https://webaim.org/resources/contrastchecker/).
- 🌐 [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/): padrões acessíveis (menu, modal, abas…).
- 🌐🇧🇷 [Guia de boas práticas para acessibilidade digital (gov.br)](https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital)
- 🎥🇧🇷 Curso em Vídeo — HTML5 e CSS3, módulo 1.

### Exercícios
- [ ] **E1.2.1** Corrija o `homepage.html` **sem ajuda de IA**: links do menu (`<a>` dentro de `<li>`), `meta viewport`, acentuação, imagem com extensão correta e `alt` adequado.
- [ ] **E1.2.2** Passe o `homepage.html` no W3C Validator até zerar os erros.
- [ ] **E1.2.3** Recrie em HTML puro (sem CSS) a estrutura de uma notícia de um portal: título, subtítulo, autor, data (`<time>`), imagem com legenda, corpo, citações.
- [ ] **E1.2.4** Crie uma página de receita com lista de ingredientes (`ul`), modo de preparo (`ol`) e tabela nutricional (tabela acessível com `caption` e `scope`).
- [ ] **E1.2.5** Transforme uma página "sopa de `div`" (pegue um exemplo ou escreva uma) em HTML semântico.
- [ ] **E1.2.6** Navegue pelo `homepage.html` **só com o teclado** (Tab, Shift+Tab, Enter). Anote o que não funciona.
- [ ] **E1.2.7** Instale um leitor de tela (NVDA no Windows, Orca no Linux, VoiceOver no Mac) e ouça sua página. O que fica confuso?
- [ ] **E1.2.8** Escreva o `alt` para 10 imagens diferentes (decorativa, logotipo, foto de produto, gráfico, botão com ícone…).
- [ ] **E1.2.9** Adicione metatags Open Graph ao `homepage.html` e teste a pré-visualização de compartilhamento.
- [ ] **E1.2.10** Crie uma página de currículo em HTML puro com todas as seções semânticas adequadas.

### Autoavaliação
1. Qual a diferença entre `section` e `article`? Dê um exemplo de cada.
2. Por que uma página deve ter apenas um `h1` (na prática) e cabeçalhos sem pular níveis?
3. Quando o `alt` de uma imagem deve ser vazio (`alt=""`)?
4. Qual a diferença entre `strong` e `b`?
5. Por que `<div onclick>` é pior que `<button>`?
6. Qual a "primeira regra do ARIA"?

### Projeto 1.2 — Site Marcelo IT Services (versão HTML)
Reescreva o `homepage.html` com:
- Cabeçalho com logo e menu funcional (âncoras para cada seção).
- Seções: apresentação, **serviços** (cada serviço como `article` com título, descrição e ícone), **sobre**, **depoimentos**, **contato** (endereço em `address`, links `tel:` e `mailto:`, link para WhatsApp).
- Rodapé com direitos e redes sociais.

**Critérios de aceite:** zero erros no W3C Validator; navegável por teclado; nota de Acessibilidade ≥ 90 no Lighthouse; hierarquia de cabeçalhos correta (confira com a extensão *HeadingsMap*).

---

## Módulo 1.3 — CSS: fundamentos, cascata, seletores e box model (1,5 semana)

### Objetivos
- Entender **por que** um estilo é aplicado (cascata, especificidade, herança), em vez de sair tentando até funcionar.

### Conceitos
- [ ] Formas de incluir CSS: inline, `<style>`, `<link>` (e por que preferir o último)
- [ ] Sintaxe: seletor, propriedade, valor, declaração, regra
- [ ] Seletores: tipo, classe, id, universal, atributo (`[type="email"]`)
- [ ] Combinadores: descendente (espaço), filho (`>`), irmão adjacente (`+`), irmãos (`~`)
- [ ] Pseudo-classes: `:hover`, `:focus`, `:focus-visible`, `:active`, `:first-child`, `:nth-child()`, `:not()`, `:is()`, `:where()`, `:has()`
- [ ] Pseudo-elementos: `::before`, `::after`, `::placeholder`, `::marker`
- [ ] **Cascata**: origem, importância (`!important`), camadas (`@layer`), especificidade, ordem
- [ ] **Especificidade**: cálculo (id, classe, tipo), por que evitar ids para estilo
- [ ] Herança: propriedades que herdam e que não herdam; `inherit`, `initial`, `unset`
- [ ] **Box model**: content, padding, border, margin; `box-sizing: border-box`
- [ ] Colapso de margens
- [ ] `display`: `block`, `inline`, `inline-block`, `none`
- [ ] Unidades: `px`, `%`, `em`, `rem`, `vw`, `vh`, `ch`; quando usar cada uma
- [ ] Cores: nomes, hex, `rgb()`, `hsl()`, transparência; contraste
- [ ] Tipografia: `font-family`, pilhas de fonte, Google Fonts, `font-size`, `line-height`, `font-weight`
- [ ] Fundos, bordas, `border-radius`, sombras
- [ ] Variáveis CSS (custom properties) e `var()`
- [ ] Reset x normalize; CSS moderno "reset" mínimo
- [ ] Metodologia de nomes: BEM
- [ ] Transições e animações básicas; `prefers-reduced-motion`

### Fontes
- 🌐 [web.dev — Learn CSS](https://web.dev/learn/css): módulos Box Model, Selectors, Cascade, Specificity, Inheritance, Color, Sizing Units.
- 🌐 [MDN — Estilizando com CSS](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Styling_basics) 🇧🇷
- 🌐 [Josh W. Comeau — blog](https://www.joshwcomeau.com/): artigos gratuitos excelentes ("The Surprising Truth About Pixels", "An Interactive Guide to Flexbox"…); curso *CSS for JavaScript Developers* 💲.
- 🎥 [Kevin Powell (YouTube)](https://www.youtube.com/@KevinPowell): o melhor canal de CSS.
- 🌐 [Specificity Calculator](https://specificity.keegan.st/)
- 🌐 [CSS-Tricks — Almanac](https://css-tricks.com/almanac/)
- 🌐 [BEM — Introdução](https://getbem.com/introduction/)
- 🧪 [CSS Diner](https://flukeout.github.io/): jogo de seletores (**faça os 32 níveis**).
- 🎥🇧🇷 Curso em Vídeo — HTML5 e CSS3, módulos 2 e 3.

### Exercícios
- [ ] **E1.3.1** Complete o CSS Diner (32 níveis).
- [ ] **E1.3.2** Calcule a especificidade de 15 seletores à mão e confira no Specificity Calculator.
- [ ] **E1.3.3** Crie uma página com dois estilos em conflito e **preveja** qual vence antes de abrir no navegador (faça 10 casos).
- [ ] **E1.3.4** Desenhe o box model de 3 elementos no papel com valores de `padding`, `border` e `margin`, calcule a largura final com `content-box` e com `border-box` e confira no DevTools.
- [ ] **E1.3.5** Reproduza o colapso de margens e explique quando ele acontece e como evitar.
- [ ] **E1.3.6** Crie um sistema de cores e tipografia com variáveis CSS (`--cor-primaria`, `--espaco-1`…).
- [ ] **E1.3.7** Crie 5 botões (primário, secundário, perigo, desabilitado, só ícone) com estados `:hover`, `:focus-visible` e `:active`.
- [ ] **E1.3.8** Crie um card de serviço com imagem, título, descrição e botão usando BEM.
- [ ] **E1.3.9** Use `::before` e `::after` para criar um selo "Novo" em um card sem alterar o HTML.
- [ ] **E1.3.10** Crie um tema escuro com `prefers-color-scheme` usando só variáveis.
- [ ] **E1.3.11** Faça uma transição suave de cor no hover e desative-a com `prefers-reduced-motion`.
- [ ] **E1.3.12** Resolva 2 desafios "Newbie" do [Frontend Mentor](https://www.frontendmentor.io/) (ex.: *QR code component*, *Blog preview card*).

### Autoavaliação
1. Explique a cascata em 4 etapas.
2. Qual seletor vence: `#menu a` ou `.nav .item a.link`? Por quê?
3. Qual a diferença entre `em` e `rem`? Por que `rem` é mais previsível?
4. O que `box-sizing: border-box` muda?
5. Por que evitar `!important`?
6. Qual a diferença entre `:focus` e `:focus-visible`?

### Projeto 1.3 — Estilizar o site Marcelo IT Services
Primeira versão visual do site (ainda sem Flexbox/Grid, ou usando o mínimo): paleta de cores, tipografia, cards de serviço, botões com estados, tema claro e escuro. Todo o CSS em `style.css`, organizado por seções com comentários.

**Critérios de aceite:** contraste AA em todos os textos; nenhum id usado em seletor de estilo; nenhum `!important`; variáveis CSS para cores e espaçamentos.

---

## Módulo 1.4 — CSS: posicionamento, Flexbox e Grid (1,5 semana)

### Conceitos
- [ ] Fluxo normal do documento
- [ ] `position`: `static`, `relative`, `absolute`, `fixed`, `sticky`; bloco de contenção
- [ ] `z-index` e contextos de empilhamento
- [ ] `float` (só para saber o que é e ler código legado)
- [ ] `overflow`
- [ ] **Flexbox**: eixo principal x transversal; `flex-direction`, `justify-content`, `align-items`, `align-self`, `flex-wrap`, `gap`, `flex-grow`, `flex-shrink`, `flex-basis`, `order`
- [ ] **Grid**: `grid-template-columns/rows`, `fr`, `repeat()`, `minmax()`, `auto-fit` x `auto-fill`, `grid-area`, `grid-template-areas`, linhas nomeadas, `place-items`, subgrid
- [ ] Quando usar Flexbox (uma dimensão) x Grid (duas dimensões)
- [ ] Centralizar qualquer coisa (as 5 formas mais comuns)
- [ ] Layouts clássicos: header/main/footer com rodapé colado embaixo, sidebar, "holy grail", galeria

### Fontes
- 🌐 [CSS-Tricks — A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- 🌐 [CSS-Tricks — A Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- 🌐 [Josh Comeau — An Interactive Guide to Flexbox](https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/) e [An Interactive Guide to CSS Grid](https://www.joshwcomeau.com/css/interactive-guide-to-grid/)
- 🌐 [web.dev — Learn CSS: Layout, Flexbox, Grid](https://web.dev/learn/css/layout)
- 🌐 [MDN — Posicionamento](https://developer.mozilla.org/pt-BR/docs/Web/CSS/position) 🇧🇷
- 🌐 [Every Layout](https://every-layout.dev/): padrões de layout robustos (parte do conteúdo é gratuito).
- 🧪 [Flexbox Froggy](https://flexboxfroggy.com/#pt-br) 🇧🇷: **24 níveis**.
- 🧪 [Grid Garden](https://cssgridgarden.com/#pt-br) 🇧🇷: **28 níveis**.
- 🧪 [Flexbox Zombies](https://mastery.games/flexboxzombies/) e [Grid Critters](https://gridcritters.com/)
- 🎥 Kevin Powell — playlists "Flexbox" e "CSS Grid".

### Exercícios
- [ ] **E1.4.1** Complete Flexbox Froggy e Grid Garden.
- [ ] **E1.4.2** Centralize uma `div` na tela de 5 formas diferentes (flex, grid, position+transform, margin auto, `place-content`).
- [ ] **E1.4.3** Crie um menu de navegação horizontal com logo à esquerda e links à direita (Flexbox).
- [ ] **E1.4.4** Crie um cabeçalho `sticky` que fica no topo ao rolar.
- [ ] **E1.4.5** Crie um layout com rodapé sempre no fim da página, mesmo com pouco conteúdo.
- [ ] **E1.4.6** Crie uma galeria de cards que se ajusta sozinha com `repeat(auto-fit, minmax(250px, 1fr))`, sem media queries.
- [ ] **E1.4.7** Recrie o layout de um painel administrativo com `grid-template-areas` (header, sidebar, conteúdo, footer).
- [ ] **E1.4.8** Crie um modal centralizado com fundo escurecido usando `position: fixed`.
- [ ] **E1.4.9** Crie um tooltip com `position: absolute` relativo ao botão.
- [ ] **E1.4.10** Reproduza o layout de uma revista (texto em colunas, imagem ocupando duas colunas) com Grid.
- [ ] **E1.4.11** Reproduza a página inicial de um site famoso (só o layout, com caixas coloridas).
- [ ] **E1.4.12** Resolva 2 desafios "Junior" do Frontend Mentor.

### Autoavaliação
1. Qual a diferença entre `justify-content` e `align-items` no Flexbox?
2. O que é `flex: 1` (quais três propriedades ele define)?
3. Qual a diferença entre `auto-fit` e `auto-fill`?
4. Em relação a quê um elemento com `position: absolute` se posiciona?
5. Por que um `z-index: 9999` às vezes não funciona?

### Projeto 1.4 — Layout completo do site Marcelo IT Services
Aplicar Flexbox e Grid ao site: menu com Flexbox, grade de serviços com Grid, seção "sobre" com imagem e texto lado a lado, cabeçalho fixo.

---

## Módulo 1.5 — Responsividade (1 semana)

### Conceitos
- [ ] `meta viewport` e por que ele é necessário
- [ ] Mobile first
- [ ] Media queries: `min-width`, `max-width`, `orientation`, `prefers-*`; pontos de quebra baseados no conteúdo
- [ ] Unidades relativas e `clamp()` para tipografia fluida
- [ ] Imagens responsivas: `max-width: 100%`, `srcset`, `sizes`, `picture`, `object-fit`, `aspect-ratio`
- [ ] Container queries (`@container`)
- [ ] Menu "hambúrguer" acessível
- [ ] Tabelas responsivas
- [ ] Teste em dispositivos: modo responsivo do DevTools e celular real

### Fontes
- 🌐 [web.dev — Learn Responsive Design](https://web.dev/learn/design)
- 🌐 [MDN — Design responsivo](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) 🇧🇷
- 🌐 [Utopia — tipografia e espaçamento fluidos](https://utopia.fyi/)
- 🎥 Kevin Powell — curso gratuito *Conquering Responsive Layouts*.
- 🎥🇧🇷 Curso em Vídeo — HTML5 e CSS3, módulo 4.

### Exercícios
- [ ] **E1.5.1** Pegue o layout do E1.4.7 e torne-o mobile first (uma coluna no celular, sidebar a partir de 768px).
- [ ] **E1.5.2** Crie tipografia fluida com `clamp()` para `h1`, `h2` e `p`.
- [ ] **E1.5.3** Use `srcset` e `sizes` para servir 3 tamanhos da mesma imagem. Confira na aba Network qual foi baixada.
- [ ] **E1.5.4** Crie um menu hambúrguer acessível (botão com `aria-expanded`); por enquanto, abra/feche com `:has()` ou checkbox (depois faremos com JS).
- [ ] **E1.5.5** Crie um card que muda de layout (vertical/horizontal) com container query.
- [ ] **E1.5.6** Torne uma tabela de preços responsiva (rolagem horizontal ou cards no celular).
- [ ] **E1.5.7** Resolva 2 desafios "Junior/Intermediate" do Frontend Mentor, pensando em mobile first.

### Autoavaliação
1. O que acontece em um celular se a página não tiver `meta viewport`?
2. Por que mobile first geralmente resulta em CSS mais simples?
3. Quando usar container query em vez de media query?

### Projeto 1.5 — Site Marcelo IT Services responsivo
**Critérios de aceite:** funciona de 320px a 1920px sem rolagem horizontal; menu hambúrguer no celular; imagens responsivas; Lighthouse ≥ 90 em Performance, Acessibilidade, Boas Práticas e SEO; testado em um celular real.

---

## Módulo 1.6 — Formulários e validação (1 semana)

### Conceitos
- [ ] `form`, `action`, `method` (GET x POST)
- [ ] `label` (associação com `for`/`id`), `input` e seus tipos (`text`, `email`, `tel`, `number`, `date`, `checkbox`, `radio`, `file`, `password`, `search`, `url`)
- [ ] `select`, `option`, `textarea`, `fieldset`, `legend`, `button` (`type="submit"` x `"button"` x `"reset"`)
- [ ] Atributos: `name`, `value`, `placeholder` (não substitui o label!), `required`, `minlength`, `maxlength`, `min`, `max`, `step`, `pattern`, `autocomplete`, `inputmode`
- [ ] Validação nativa do HTML5 e pseudo-classes `:valid`, `:invalid`, `:user-invalid`
- [ ] Validação com JavaScript: Constraint Validation API (`checkValidity`, `setCustomValidity`, `validity`) (ver após o módulo 1.9)
- [ ] Mensagens de erro acessíveis (`aria-describedby`, `aria-invalid`, `aria-live`)
- [ ] Estilização de formulários
- [ ] Segurança: validação no cliente **nunca** substitui validação no servidor

### Fontes
- 🌐 [web.dev — Learn Forms](https://web.dev/learn/forms)
- 🌐 [MDN — Formulários web](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Forms) 🇧🇷
- 🌐 [MDN — Validação de formulários do lado do cliente](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Forms/Form_validation) 🇧🇷
- 🌐 [WebAIM — Creating Accessible Forms](https://webaim.org/techniques/forms/)
- 🌐 [httpbin.org](https://httpbin.org/): para enviar formulários e ver o que chega no servidor (`action="https://httpbin.org/post"`).

### Exercícios
- [ ] **E1.6.1** Formulário de cadastro com nome, e-mail, telefone, data de nascimento, senha e confirmação, todos com label e validação nativa.
- [ ] **E1.6.2** Envie o formulário para `httpbin.org/post` com GET e com POST e compare o que muda na URL e no corpo.
- [ ] **E1.6.3** Formulário de pesquisa de satisfação com `radio`, `checkbox`, `select` e `textarea`, agrupados em `fieldset`.
- [ ] **E1.6.4** Use `pattern` para validar CPF no formato `000.000.000-00` e CEP `00000-000`.
- [ ] **E1.6.5** Estilize estados válido/inválido só depois que o usuário interagir (`:user-invalid`).
- [ ] **E1.6.6** Formulário de upload de arquivo aceitando só imagens (`accept`).
- [ ] **E1.6.7** Teste todos os formulários só com teclado e com leitor de tela.

### Autoavaliação
1. Por que `placeholder` não substitui `label`?
2. Quando usar GET e quando usar POST?
3. Por que validar no front-end se o back-end também valida?

### Projeto 1.6 — Formulário de orçamento
No site Marcelo IT Services: nome, e-mail, telefone, CEP, tipo de cliente (residencial/empresarial), serviços desejados (checkboxes do catálogo), urgência, descrição do problema. Validação nativa completa e mensagens acessíveis. (Nos módulos seguintes você vai adicionar JavaScript, ViaCEP e armazenamento.)

---

## Módulo 1.7 — JavaScript: fundamentos da linguagem (2 semanas)

### Objetivos
- Dominar a linguagem **antes** do DOM: tipos, funções, escopo, objetos e módulos.

### Conceitos
- [ ] Onde o JS roda: navegador x Node.js; console
- [ ] Variáveis: `let`, `const`, `var` (e por que evitar `var`); hoisting; zona morta temporal (TDZ)
- [ ] Tipos primitivos: `string`, `number`, `bigint`, `boolean`, `undefined`, `null`, `symbol`; `typeof`
- [ ] Objetos e referência x valor
- [ ] Conversão de tipos: implícita x explícita; `==` x `===`; valores *truthy*/*falsy*
- [ ] Operadores: aritméticos, lógicos (`&&`, `||`, `??`), encadeamento opcional (`?.`), ternário
- [ ] Strings: template literals, métodos (`slice`, `split`, `includes`, `trim`, `padStart`, `replaceAll`)
- [ ] Números: `Number`, `parseInt`, `parseFloat`, `toFixed`, problemas de ponto flutuante (`0.1 + 0.2`), `Math`
- [ ] Condicionais: `if/else`, `switch`
- [ ] Laços: `for`, `while`, `do...while`, `for...of`, `for...in` (e a diferença), `break`, `continue`
- [ ] Funções: declaração, expressão, arrow functions; parâmetros padrão; rest (`...args`) e spread
- [ ] Escopo: global, de função, de bloco; escopo léxico
- [ ] **Closures**
- [ ] Funções de ordem superior e callbacks
- [ ] Objetos: literais, propriedades, métodos, `this`, desestruturação, shorthand, propriedades computadas
- [ ] `this`: regras (chamada simples, método, `new`, `call`/`apply`/`bind`, arrow functions)
- [ ] Protótipos e herança prototípica; `class`, `constructor`, `extends`, `super`, `static`, campos privados `#`
- [ ] Datas: `Date` e `Intl.DateTimeFormat`; `Intl.NumberFormat` para moeda (R$)
- [ ] `JSON.stringify` e `JSON.parse`
- [ ] Módulos ES: `import`/`export`, `export default`, `type="module"` no navegador
- [ ] Modo estrito
- [ ] Recursão
- [ ] Expressões regulares (básico): `test`, `match`, `replace`, grupos

### Fontes
- 🌐 [javascript.info — Parte 1: The JavaScript language](https://javascript.info/) (capítulos 1 a 9). **Fonte principal.**
- 📘 *Eloquent JavaScript*: capítulos 1 a 6.
- 📘 *You Don't Know JS Yet*: *Get Started* e *Scope & Closures*.
- 🌐 [MDN — Guia JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide) 🇧🇷
- 🎥🇧🇷 [Curso em Vídeo — JavaScript](https://www.cursoemvideo.com/)
- 🎥 [freeCodeCamp — JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/)
- 📘 *JavaScript: O Guia Definitivo* — David Flanagan (referência).
- 🌐 [Regex101](https://regex101.com/): testar e entender expressões regulares.
- 🧪 [Exercism — trilha JavaScript](https://exercism.org/tracks/javascript) · [Codewars](https://www.codewars.com/) (8 kyu → 6 kyu)

### Exercícios
**Tipos e operadores**
- [ ] **E1.7.1** Preveja e depois confira no console o resultado de 20 expressões de coerção (`[] + {}`, `"5" - 2`, `"5" + 2`, `null == undefined`, `NaN === NaN`…).
- [ ] **E1.7.2** Função que formata um número como moeda brasileira usando `Intl.NumberFormat`.
- [ ] **E1.7.3** Função que diz se um ano é bissexto.

**Laços e condicionais**
- [ ] **E1.7.4** FizzBuzz de 1 a 100 (com e sem `if` aninhado).
- [ ] **E1.7.5** Imprima uma pirâmide de asteriscos com altura N.
- [ ] **E1.7.6** Tabuada de 1 a 10 formatada.
- [ ] **E1.7.7** Verifique se uma palavra é palíndromo (ignorando acentos e espaços).

**Funções e closures**
- [ ] **E1.7.8** Crie `criarContador()` que retorna funções `incrementar`, `decrementar` e `valor` (closure).
- [ ] **E1.7.9** Implemente `once(fn)`: uma função que só executa uma vez.
- [ ] **E1.7.10** Implemente `memoize(fn)` para uma função de Fibonacci.
- [ ] **E1.7.11** Implemente `debounce(fn, ms)` (entenda antes de usar nos eventos).
- [ ] **E1.7.12** Explique por escrito por que um `for` com `var` e `setTimeout` imprime o mesmo número 3 vezes, e corrija de duas formas.

**Objetos, `this` e classes**
- [ ] **E1.7.13** Crie o objeto `servico` (nome, preço, duração) com método `descricao()`. Use desestruturação para extrair campos.
- [ ] **E1.7.14** Mostre 4 situações em que `this` muda de valor e explique cada uma.
- [ ] **E1.7.15** Crie a classe `Cliente` com campo privado `#cpf`, getter mascarado e método estático `validarCpf()` (implemente o algoritmo dos dígitos verificadores).
- [ ] **E1.7.16** Crie `Servico` e `ServicoRecorrente extends Servico` (com mensalidade). Sobrescreva um método.
- [ ] **E1.7.17** Implemente a mesma herança só com protótipos (sem `class`), para entender o que o `class` faz por baixo.

**Módulos, datas e JSON**
- [ ] **E1.7.18** Separe as funções dos exercícios em módulos (`utils/moeda.js`, `utils/datas.js`) e importe numa página com `type="module"`.
- [ ] **E1.7.19** Função que recebe uma data e retorna "há 3 dias", "há 2 horas" (use `Intl.RelativeTimeFormat`).
- [ ] **E1.7.20** Converta um objeto complexo para JSON e de volta. O que acontece com `Date`, `undefined` e funções?

**Prática contínua**
- [ ] **E1.7.21** 25 exercícios da trilha JavaScript do Exercism (peça mentoria em pelo menos 5).
- [ ] **E1.7.22** 20 katas no Codewars (8 kyu e 7 kyu).
- [ ] **E1.7.23** 10 problemas iniciantes do Beecrowd em JavaScript.

### Autoavaliação
1. Qual a diferença entre `let`, `const` e `var`?
2. O que é uma closure? Dê um uso prático.
3. Qual a diferença entre `==` e `===`? Quando `==` pode ser aceitável?
4. Por que `0.1 + 0.2 !== 0.3`? Como lidar com dinheiro em JS?
5. Explique as 4 regras do `this`.
6. O que o `class` realmente faz em JavaScript?
7. Qual a diferença entre `for...in` e `for...of`?
8. Qual a diferença entre `??` e `||`?

### Projeto 1.7 — Calculadora de orçamento (terminal/console)
Um módulo JS puro, sem DOM, que: recebe uma lista de serviços com preço e quantidade, aplica taxa de deslocamento por distância, desconto progressivo para clientes empresariais, e retorna o orçamento detalhado formatado em R$. Deve estar em módulos ES e ser usado pelo site no módulo 1.9. (Os testes automatizados virão no módulo 1.14.)

---

## Módulo 1.8 — Ferramentas: npm, ESLint, Prettier, Vite (3 dias)

### Conceitos
- [ ] Node.js e npm: `package.json`, `dependencies` x `devDependencies`, `package-lock.json`, scripts, `npx`
- [ ] Versionamento semântico (SemVer) e `^`/`~`
- [ ] **ESLint**: o que é lint, flat config (`eslint.config.js`), regras, plugins, `--fix`, integração com o editor
- [ ] **Prettier**: formatador; separar formatação (Prettier) de qualidade (ESLint)
- [ ] EditorConfig
- [ ] Git hooks com Husky + lint-staged (lint antes do commit)
- [ ] Bundler/servidor de desenvolvimento: **Vite**

### Fontes
- 🌐 [npm Docs](https://docs.npmjs.com/)
- 🌐 [ESLint — Getting Started](https://eslint.org/docs/latest/use/getting-started) e [Configuration Files](https://eslint.org/docs/latest/use/configure/configuration-files)
- 🌐 [Prettier — docs](https://prettier.io/docs/)
- 🌐 [Vite — Guia](https://vite.dev/guide/) ([pt-BR](https://pt.vite.dev/guide/) 🇧🇷)
- 🌐 [Husky](https://typicode.github.io/husky/) e [lint-staged](https://github.com/lint-staged/lint-staged)
- 🌐 [semver.org](https://semver.org/lang/pt-BR/) 🇧🇷

### Exercícios
- [ ] **E1.8.1** `npm init` num projeto novo; entenda cada campo do `package.json`.
- [ ] **E1.8.2** Configure o ESLint com as regras recomendadas. Escreva código com 10 problemas de propósito e veja o ESLint pegá-los.
- [ ] **E1.8.3** Adicione 3 regras personalizadas (ex.: `no-console` como aviso, `eqeqeq`, `prefer-const`) e explique cada uma.
- [ ] **E1.8.4** Configure o Prettier e integre com o ESLint sem conflitos.
- [ ] **E1.8.5** Configure Husky + lint-staged para rodar lint e formatação antes de cada commit.
- [ ] **E1.8.6** Migre o site Marcelo IT Services para um projeto Vite e rode `npm run dev` e `npm run build`. Veja o que o build gera em `dist/`.

### Autoavaliação
1. Qual a diferença entre ESLint e Prettier?
2. O que `^1.2.3` permite instalar?
3. Por que o `package-lock.json` deve ser versionado?

---

## Módulo 1.9 — DOM e eventos (1,5 semana)

### Conceitos
- [ ] O que é o DOM; árvore de nós; `document`, `window`
- [ ] Seleção: `getElementById`, `querySelector`, `querySelectorAll`, `closest`; `NodeList` x `HTMLCollection`
- [ ] Leitura e alteração: `textContent` x `innerHTML` (e o risco de **XSS**), `classList`, `dataset`, atributos, `style`
- [ ] Criação e remoção: `createElement`, `append`, `prepend`, `remove`, `cloneNode`, `<template>`, `DocumentFragment`
- [ ] Eventos: `addEventListener`, objeto `event`, `target` x `currentTarget`, `preventDefault`, `stopPropagation`
- [ ] Fases: captura, alvo e **bubbling**; **delegação de eventos**
- [ ] Eventos comuns: `click`, `input`, `change`, `submit`, `keydown`, `focus`/`blur`, `DOMContentLoaded`, `scroll`, `resize`
- [ ] Eventos de teclado acessíveis
- [ ] `debounce` e `throttle` aplicados a eventos
- [ ] Carregamento de scripts: `defer`, `async`, `type="module"`
- [ ] APIs úteis: `IntersectionObserver`, `dialog` nativo, `Clipboard API`

### Fontes
- 🌐 [javascript.info — Parte 2: Browser: Document, Events, Interfaces](https://javascript.info/document)
- 🌐 [MDN — Manipulando documentos](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Scripting/DOM_scripting) 🇧🇷
- 🌐 [MDN — Introdução a eventos](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Scripting/Events) 🇧🇷
- 📘 *Eloquent JavaScript*: capítulos 14 a 16.
- 🎥 [JavaScript30 — Wes Bos (gratuito)](https://javascript30.com/): 30 projetos com DOM puro, sem frameworks.

### Exercícios
- [ ] **E1.9.1** Menu hambúrguer do site controlado por JS, com `aria-expanded` atualizado e fechamento pela tecla Esc.
- [ ] **E1.9.2** Contador com botões +, − e reset.
- [ ] **E1.9.3** Alternador de tema claro/escuro (depois você vai salvar a escolha no módulo 1.13).
- [ ] **E1.9.4** Filtro do catálogo de serviços: campo de busca filtra os cards enquanto digita (com `debounce`).
- [ ] **E1.9.5** Abas (tabs) acessíveis seguindo o padrão do WAI-ARIA APG (setas do teclado navegam entre as abas).
- [ ] **E1.9.6** Modal com `<dialog>` para "detalhes do serviço".
- [ ] **E1.9.7** Lista com botões "remover" usando **delegação de eventos** (um único listener no pai).
- [ ] **E1.9.8** Renderize o catálogo de serviços a partir de um array de objetos usando `<template>`.
- [ ] **E1.9.9** Demonstre um ataque XSS usando `innerHTML` com entrada do usuário e corrija com `textContent`.
- [ ] **E1.9.10** Animação de "aparecer ao rolar" com `IntersectionObserver`.
- [ ] **E1.9.11** Botão "copiar número do WhatsApp" com a Clipboard API.
- [ ] **E1.9.12** Faça 10 projetos do JavaScript30 (sugestões: 01, 04, 06, 07, 10, 12, 15, 20, 26, 30).

### Autoavaliação
1. Qual a diferença entre `textContent` e `innerHTML`? Qual o risco do segundo?
2. O que é event bubbling? Como a delegação de eventos se aproveita dele?
3. Qual a diferença entre `event.target` e `event.currentTarget`?
4. Qual a diferença entre `defer` e `async`?
5. Quando usar `debounce` e quando usar `throttle`?

### Projeto 1.9 — Site interativo
Site Marcelo IT Services com: menu mobile, catálogo renderizado a partir de dados, busca e filtro por categoria, modal de detalhes, formulário de orçamento que usa a calculadora do projeto 1.7 para mostrar o valor estimado em tempo real.

---

## Módulo 1.10 — Arrays, objetos e programação funcional (1 semana)

### Conceitos
- [ ] Métodos que **não** alteram o array: `map`, `filter`, `reduce`, `find`, `findIndex`, `some`, `every`, `includes`, `slice`, `concat`, `flat`, `flatMap`, `toSorted`, `toReversed`, `with`
- [ ] Métodos que **alteram** (mutáveis): `push`, `pop`, `shift`, `unshift`, `splice`, `sort`, `reverse`
- [ ] `forEach` x `map` (e por que não usar `map` para efeito colateral)
- [ ] `sort` com função comparadora (números, strings com `localeCompare`, objetos por várias chaves)
- [ ] `Array.from`, `Array.of`, spread para copiar
- [ ] Objetos: `Object.keys`, `values`, `entries`, `fromEntries`, `assign`, spread; `structuredClone` (cópia profunda)
- [ ] `Map` e `Set` (e quando usar em vez de objeto/array)
- [ ] Imutabilidade; funções puras; efeitos colaterais
- [ ] Encadeamento de métodos
- [ ] `Object.groupBy`

### Fontes
- 🌐 [javascript.info — Array methods](https://javascript.info/array-methods) e [Map and Set](https://javascript.info/map-set)
- 🌐 [MDN — Array](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array) 🇧🇷
- 📘 *Eloquent JavaScript*: capítulo 5 (Higher-Order Functions).
- 🌐 [Does it mutate?](https://doesitmutate.xyz/): tabela de métodos que alteram ou não o array.

### Exercícios
Use este array de ordens de serviço para todos os exercícios (crie 20 registros):
```js
const ordens = [
  { id: 1, cliente: "Padaria Pão Quente", tipo: "empresarial", servico: "Backup", valor: 250, status: "concluida", data: "2026-03-10", tecnico: "Marcelo" },
  // ...
];
```
- [ ] **E1.10.1** Liste só as ordens concluídas (`filter`).
- [ ] **E1.10.2** Gere uma lista de strings "Cliente — Serviço — R$ valor" (`map`).
- [ ] **E1.10.3** Calcule o faturamento total das ordens concluídas (`filter` + `reduce`).
- [ ] **E1.10.4** Agrupe o faturamento por serviço (com `reduce` e depois com `Object.groupBy`).
- [ ] **E1.10.5** Encontre a primeira ordem de um cliente (`find`) e verifique se **alguma** ordem está atrasada (`some`).
- [ ] **E1.10.6** Ordene por valor decrescente e, em caso de empate, por data (`toSorted`).
- [ ] **E1.10.7** Liste os clientes sem repetição (`Set`).
- [ ] **E1.10.8** Conte ordens por mês (`Map`).
- [ ] **E1.10.9** Calcule o ticket médio por tipo de cliente.
- [ ] **E1.10.10** Reimplemente `map`, `filter` e `reduce` do zero (sem usá-los).
- [ ] **E1.10.11** Atualize o status de uma ordem **sem alterar** o array original.
- [ ] **E1.10.12** Mostre a diferença entre cópia rasa e profunda com um objeto aninhado.
- [ ] **E1.10.13** 15 katas do Codewars focados em arrays (6 kyu).

### Autoavaliação
1. Quais métodos alteram o array original?
2. O que o segundo argumento do `reduce` faz e por que é perigoso omiti-lo?
3. Quando usar `Map` em vez de objeto?
4. O que é uma função pura?

### Projeto 1.10 — Painel de ordens de serviço
Página que exibe as ordens em tabela e mostra indicadores (faturamento do mês, ticket médio, serviço mais vendido), com filtros por status, tipo de cliente e período, e ordenação ao clicar no cabeçalho da coluna.

---

## Módulo 1.11 — Exceções e depuração (4 dias)

### Conceitos
- [ ] Tipos de erro: `SyntaxError`, `ReferenceError`, `TypeError`, `RangeError`
- [ ] `try`, `catch`, `finally`; `throw`
- [ ] Objeto `Error`: `message`, `name`, `stack`, `cause`
- [ ] Erros personalizados (`class ValidacaoError extends Error`)
- [ ] Quando capturar e quando deixar o erro subir
- [ ] Erros em código assíncrono (ver módulo 1.12)
- [ ] Tratamento global: `window.onerror`, `unhandledrejection`
- [ ] Depuração: `console.log` x `console.table` x `console.error`; `debugger`; breakpoints no DevTools (linha, condicional, DOM, XHR); *step over/into/out*; *watch*; *call stack*

### Fontes
- 🌐 [javascript.info — Error handling](https://javascript.info/error-handling)
- 🌐 [MDN — Controle de fluxo e manipulação de erro](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Control_flow_and_error_handling) 🇧🇷
- 🌐 [Chrome DevTools — Debug JavaScript](https://developer.chrome.com/docs/devtools/javascript)
- 📘 *Eloquent JavaScript*: capítulo 8 (Bugs and Errors).

### Exercícios
- [ ] **E1.11.1** Função `dividir(a, b)` que lança `RangeError` para divisão por zero e `TypeError` para argumentos que não são números.
- [ ] **E1.11.2** Crie `ValidacaoError` com um campo `campo` e use no formulário de orçamento para mostrar o erro no campo certo.
- [ ] **E1.11.3** Demonstre que o `finally` executa mesmo com `return` dentro do `try`.
- [ ] **E1.11.4** Parse de JSON inválido vindo do usuário com mensagem amigável.
- [ ] **E1.11.5** Use `cause` para encadear um erro de baixo nível em um erro de negócio.
- [ ] **E1.11.6** Coloque um bug proposital no painel de ordens e encontre-o usando **apenas** breakpoints (sem `console.log`).
- [ ] **E1.11.7** Use um breakpoint condicional para parar só quando `ordem.id === 13`.

### Autoavaliação
1. Quando é melhor **não** capturar uma exceção?
2. Por que `catch (e) {}` vazio é perigoso?
3. O que é a *call stack* que aparece no erro?

---

## Módulo 1.12 — Assincronia: event loop, Promises, fetch, async/await (1,5 semana)

### Conceitos
- [ ] Síncrono x assíncrono; JavaScript é *single-threaded*
- [ ] **Event loop**: call stack, Web APIs, fila de tarefas (macrotasks), fila de microtasks, renderização
- [ ] Callbacks e "callback hell"
- [ ] **Promises**: estados (pending, fulfilled, rejected), `then`, `catch`, `finally`, encadeamento
- [ ] `Promise.all`, `Promise.allSettled`, `Promise.race`, `Promise.any`
- [ ] `async`/`await`; tratamento de erros com `try/catch`; execução sequencial x paralela
- [ ] **fetch**: GET, POST, cabeçalhos, corpo JSON, `response.ok`, status HTTP, `AbortController` (cancelamento e timeout)
- [ ] CORS (conceito)
- [ ] Estados de carregamento, erro e vazio na interface
- [ ] `setTimeout`, `setInterval`, `requestAnimationFrame`
- [ ] Testes assíncronos (ver módulo 1.14)

### Fontes
- 🎥 [Philip Roberts — "What the heck is the event loop anyway?" (JSConf EU)](https://www.youtube.com/watch?v=8aGhZQkoFbQ): **obrigatório**.
- 🎥 [Jake Archibald — "In The Loop" (JSConf Asia)](https://www.youtube.com/watch?v=cCOL7MC4Pl0)
- 🧪 [Loupe](http://latentflip.com/loupe/): visualizador do event loop.
- 🌐 [javascript.info — Promises, async/await](https://javascript.info/async)
- 🌐 [MDN — JavaScript assíncrono](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Async_JS) 🇧🇷
- 🌐 [MDN — Usando Fetch](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API/Using_Fetch) 🇧🇷
- 📘 *Eloquent JavaScript*: capítulo 11 (Asynchronous Programming).
- 📘 *You Don't Know JS* (1ª ed.): *Async & Performance*.
- APIs públicas para praticar: 🌐🇧🇷 [ViaCEP](https://viacep.com.br/), 🌐🇧🇷 [BrasilAPI](https://brasilapi.com.br/) (CEP, CNPJ, feriados, bancos), 🌐 [JSONPlaceholder](https://jsonplaceholder.typicode.com/), 🌐 [PokéAPI](https://pokeapi.co/), 🌐 [Open-Meteo](https://open-meteo.com/) (previsão do tempo, sem chave).

### Exercícios
- [ ] **E1.12.1** Preveja a ordem de saída de 10 trechos de código misturando `console.log`, `setTimeout(0)`, `Promise.resolve().then` e `queueMicrotask`. Confira no Loupe e no console.
- [ ] **E1.12.2** Crie `esperar(ms)` que retorna uma Promise.
- [ ] **E1.12.3** Converta uma função baseada em callback para Promise ("promisify").
- [ ] **E1.12.4** Reescreva um "callback hell" de 4 níveis com Promises encadeadas e depois com `async/await`.
- [ ] **E1.12.5** Busque o CEP no **ViaCEP** ao sair do campo CEP do formulário de orçamento e preencha rua, bairro, cidade e UF. Trate CEP inexistente (`{ erro: true }`) e falha de rede.
- [ ] **E1.12.6** Mostre estado de "carregando…" e desabilite o botão durante a requisição.
- [ ] **E1.12.7** Busque 5 CEPs em **paralelo** com `Promise.all` e compare o tempo com a busca **sequencial**.
- [ ] **E1.12.8** Use `Promise.allSettled` para buscar vários recursos e mostrar quais falharam.
- [ ] **E1.12.9** Implemente timeout de 5 segundos numa requisição com `AbortController`.
- [ ] **E1.12.10** Implemente `retry(fn, tentativas)` com espera exponencial entre tentativas.
- [ ] **E1.12.11** Busque os feriados nacionais do ano na BrasilAPI e mostre-os no site (dias sem atendimento).
- [ ] **E1.12.12** Implemente uma busca com autocompletar que cancela a requisição anterior quando o usuário digita de novo.
- [ ] **E1.12.13** Faça um POST para o JSONPlaceholder e trate as respostas 2xx, 4xx e 5xx.

### Autoavaliação
1. Explique o event loop em 5 frases.
2. Por que `setTimeout(fn, 0)` não executa imediatamente?
3. Qual a diferença entre microtasks e macrotasks?
4. O `fetch` rejeita a Promise quando o servidor responde 404? Como tratar?
5. Qual a diferença entre `Promise.all` e `Promise.allSettled`?
6. Como executar 3 `await` em paralelo em vez de em sequência?
7. O que é CORS e de quem é a "culpa" quando dá erro?

### Projeto 1.12 — Consulta de clima para visitas técnicas
Página onde o técnico informa o CEP do cliente e vê o endereço (ViaCEP), a previsão do tempo para o dia da visita (Open-Meteo, a partir da latitude/longitude) e se a data é feriado (BrasilAPI). Com estados de carregamento, erro e vazio, timeout e novas tentativas.

---

## Módulo 1.13 — Web Storage e cookies (4 dias)

### Conceitos
- [ ] `localStorage` x `sessionStorage`: escopo, duração, limites (~5 MB), apenas strings
- [ ] `setItem`, `getItem`, `removeItem`, `clear`; salvar objetos com JSON
- [ ] Evento `storage` (sincronizar abas)
- [ ] Cookies: `document.cookie`, atributos `Expires`/`Max-Age`, `Path`, `Domain`, `Secure`, `HttpOnly`, `SameSite`
- [ ] Quando usar cada um; **nunca** guardar dados sensíveis (tokens, senhas) no `localStorage`, por causa do risco de XSS
- [ ] IndexedDB (visão geral) para dados maiores
- [ ] LGPD e banner de consentimento de cookies

### Fontes
- 🌐 [MDN — Web Storage API](https://developer.mozilla.org/pt-BR/docs/Web/API/Web_Storage_API) 🇧🇷
- 🌐 [javascript.info — Storing data in the browser](https://javascript.info/data-storage)
- 🌐 [MDN — Cookies HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Guides/Cookies) 🇧🇷
- 🌐 [web.dev — SameSite cookies explained](https://web.dev/articles/samesite-cookies-explained)

### Exercícios
- [ ] **E1.13.1** Salve a preferência de tema (claro/escuro) e aplique ao recarregar, sem "piscar".
- [ ] **E1.13.2** Salve o rascunho do formulário de orçamento enquanto o usuário digita e restaure ao voltar.
- [ ] **E1.13.3** Sincronize o tema entre duas abas abertas com o evento `storage`.
- [ ] **E1.13.4** Crie funções utilitárias `salvar(chave, objeto)` e `carregar(chave, padrao)` com tratamento de JSON inválido.
- [ ] **E1.13.5** Crie, leia e apague um cookie com `Max-Age` e `SameSite=Lax`. Veja na aba Application do DevTools.
- [ ] **E1.13.6** Banner de consentimento de cookies que lembra a escolha do usuário.

### Autoavaliação
1. Qual a diferença entre `localStorage` e `sessionStorage`?
2. Por que não guardar um token de autenticação no `localStorage`?
3. O que o atributo `HttpOnly` impede?
4. O que o `SameSite` protege?

---

## Módulo 1.14 — Testes em JavaScript (1,5 semana)

### Conceitos
- [ ] Por que testar; custo de um bug em produção
- [ ] Pirâmide de testes: unitário, integração, ponta a ponta (E2E)
- [ ] Anatomia de um teste: *Arrange, Act, Assert* (AAA); `describe`, `it`/`test`, `expect`
- [ ] Matchers: `toBe`, `toEqual`, `toStrictEqual`, `toThrow`, `toContain`, `toHaveLength`, `toBeCloseTo`
- [ ] *Setup* e *teardown*: `beforeEach`, `afterEach`, `beforeAll`
- [ ] Testes parametrizados (`test.each`)
- [ ] **Testes assíncronos**: `async/await` no teste, `resolves`/`rejects`
- [ ] Dublês de teste: *mock*, *stub*, *spy*; `vi.fn()`, `vi.spyOn()`, mock de módulo, mock do `fetch`
- [ ] Temporizadores falsos (`vi.useFakeTimers`) para testar `debounce`/`setTimeout`
- [ ] Testes de DOM com `jsdom` e Testing Library (`@testing-library/dom`)
- [ ] Cobertura de código (e por que 100% não é a meta)
- [ ] **TDD**: vermelho → verde → refatorar
- [ ] Testes E2E com **Playwright** (visão geral)
- [ ] O que torna um teste bom: rápido, isolado, determinístico, legível, testa comportamento e não implementação

### Fontes
- 🌐 [Vitest — Guia](https://vitest.dev/guide/) (API compatível com o Jest, integra com Vite)
- 🌐 [Jest — Docs](https://jestjs.io/pt-BR/docs/getting-started) 🇧🇷 (muito usado em empresas; os conceitos são os mesmos)
- 🌐 [Testing Library — DOM Testing Library](https://testing-library.com/docs/dom-testing-library/intro)
- 🌐 [Playwright — docs](https://playwright.dev/docs/intro)
- 🌐 [Kent C. Dodds — "The Testing Trophy"](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications) e ["Write tests. Not too many. Mostly integration."](https://kentcdodds.com/blog/write-tests)
- 🌐 [Martin Fowler — The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- 📘 *Test-Driven Development: By Example* — Kent Beck
- 🌐 [JavaScript Testing Best Practices — Yoni Goldberg](https://github.com/goldbergyoni/javascript-testing-best-practices) (tem tradução 🇧🇷 no repositório)
- 🎥 [Testing JavaScript — Kent C. Dodds](https://testingjavascript.com/) 💲

### Exercícios
- [ ] **E1.14.1** Configure o Vitest no projeto e escreva o primeiro teste para `formatarMoeda`.
- [ ] **E1.14.2** Teste todas as funções utilitárias dos módulos 1.7 e 1.10 (moeda, datas, CPF, palíndromo, agrupamentos).
- [ ] **E1.14.3** Use `test.each` para testar a validação de CPF com 10 casos válidos e 10 inválidos.
- [ ] **E1.14.4** Teste que `dividir` lança os erros corretos (`toThrow`).
- [ ] **E1.14.5** Refaça a calculadora de orçamento (projeto 1.7) **com TDD**: escreva os testes antes, um por regra de negócio.
- [ ] **E1.14.6** Teste a função de busca de CEP **mockando o `fetch`**: sucesso, CEP inexistente, erro de rede, timeout.
- [ ] **E1.14.7** Teste `debounce` com temporizadores falsos.
- [ ] **E1.14.8** Teste `retry` garantindo que a função é chamada N vezes (`vi.fn()`, `toHaveBeenCalledTimes`).
- [ ] **E1.14.9** Teste o filtro do catálogo com jsdom + Testing Library: digitar no campo e verificar os cards visíveis.
- [ ] **E1.14.10** Gere o relatório de cobertura e identifique um trecho importante sem teste.
- [ ] **E1.14.11** Escreva 3 testes E2E com Playwright para o site: navegação pelo menu, envio do formulário válido, erro com formulário inválido.
- [ ] **E1.14.12** Kata de TDD: faça o [String Calculator Kata](https://osherove.com/tdd-kata-1) e o *Bowling Game Kata* em TDD.

### Autoavaliação
1. Qual a diferença entre teste unitário, de integração e E2E?
2. Qual a diferença entre `toBe` e `toEqual`?
3. O que é um mock e quando ele pode tornar o teste inútil?
4. Explique o ciclo do TDD.
5. Por que "testar a implementação" deixa os testes frágeis?
6. Como testar uma função que usa `setTimeout` sem esperar de verdade?

---

## Módulo 1.15 — Projetos finais da trilha (2 semanas)

### Projeto A — Lista de tarefas (projeto do README)
**Requisitos:**
- Adicionar, editar (duplo clique), concluir e remover tarefas.
- Filtros: todas / pendentes / concluídas; contador de pendentes.
- Prioridade (baixa, média, alta) e data de vencimento; destaque para atrasadas.
- Arrastar e soltar para reordenar (API de Drag and Drop).
- Persistência no **localStorage**; sincronização entre abas.
- Exportar e importar as tarefas em JSON (validando o arquivo importado).
- Acessível por teclado e leitor de tela.

**Qualidade exigida:**
- Código em módulos ES, separando **lógica** (funções puras, testáveis) de **interface** (DOM).
- ESLint e Prettier sem avisos; Husky rodando lint antes do commit.
- Testes unitários da lógica com cobertura ≥ 80%; pelo menos 3 testes de DOM; 2 testes E2E.
- Tratamento de erros (JSON inválido, localStorage cheio ou indisponível).
- Deploy no **GitHub Pages**, Netlify ou Vercel.
- README do projeto com prints, como rodar, como testar e decisões tomadas.

### Projeto B — Site Marcelo IT Services (versão final da trilha 1)
Juntar tudo: site responsivo e acessível, catálogo dinâmico com filtro, formulário de orçamento com validação, ViaCEP, cálculo em tempo real e rascunho salvo, tema claro/escuro persistente, testes, lint e deploy.

**Critérios de aceite:** Lighthouse ≥ 90 nas 4 categorias; zero erros no validador; testes passando; publicado online com domínio próprio (opcional).

### Mini-projetos extras (escolha pelo menos 3)
- [ ] Jogo da memória (DOM, timers, estado)
- [ ] Quiz de revisão da própria trilha (JSON de perguntas, pontuação, `localStorage` para o recorde)
- [ ] Conversor de moedas com API de câmbio
- [ ] Relógio mundial com `Intl`
- [ ] Gerador de senhas seguras (`crypto.getRandomValues`)
- [ ] Clone simplificado de um app famoso (ex.: Trello com colunas)
- [ ] Desafios "Intermediate" do Frontend Mentor (2 ou mais)

---

## ✅ Checklist de conclusão da Trilha 1
- [ ] CSS Diner, Flexbox Froggy e Grid Garden completos
- [ ] 10 projetos do JavaScript30
- [ ] 40+ exercícios no Exercism/Codewars
- [ ] Lista de tarefas publicada, com testes e cobertura ≥ 80%
- [ ] Site Marcelo IT Services publicado com Lighthouse ≥ 90
- [ ] Autoavaliações de todos os módulos com ≥ 80% de acerto
- [ ] Artigo/post resumindo a trilha
- [ ] **Opcional:** certificações gratuitas do freeCodeCamp *Responsive Web Design* e *JavaScript Algorithms and Data Structures*
