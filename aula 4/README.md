# Aula 4 — 12/03/2026 (Quinta-feira)

Quarta aula do curso de **Algoritmo e Lógica de Programação**, com foco em **estruturas de repetição** (`while` e `for`) e **listas**.

## 📂 Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| `01 - repeticao.py` | Introdução ao loop `while` com contador |
| `02 - Tabuada.py` | Tabuada de um número usando `while` |
| `03 - login.py` | Simulação de login com validação por `while` |
| `04 - menu.py` | Menu de opções interativo usando `while` |
| `05 - estrutura-lista-dados.py` | Percorrendo uma lista de alunos com `while` |
| `06 - repeticao-for.py` | Introdução ao loop `for` com lista de alunos |
| `07 - desconto.py` | Aplicação de desconto em lista de preços usando `for` |
| `08 - controle-notas.py` | Controle de notas com `for` e `enumerate` |

---

## 📄 `01 - repeticao.py` — Repetição com While

Demonstra o funcionamento básico do loop `while` usando um contador.

- Imprime o nome `"Fernando"` enquanto o `contador` for menor que 3.
- A cada iteração, o contador é incrementado em 1.

```bash
python "01 - repeticao.py"
```

---

## 📄 `02 - Tabuada.py` — Tabuada com While

Solicita um número ao usuário e exibe sua tabuada completa (de 1 a 10) usando `while`.

```bash
python "02 - Tabuada.py"
```

**Exemplo:**
```
Digite um número para ver a tabuada: 5
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## 📄 `03 - login.py` — Login com While

Simula um sistema de autenticação por senha. O loop continua solicitando a senha até que o valor correto seja digitado.

```bash
python "03 - login.py"
```

**Exemplo:**
```
Digite a senha: 123
Senha incorreta. Tente novamente.
Digite a senha: asd
Acesso permitido.
```

---

## 📄 `04 - menu.py` — Menu de Opções com While

Exibe um menu interativo com quatro opções (nome, nota, situação e sair). O loop se encerra quando o usuário escolhe a opção `0`.

```bash
python "04 - menu.py"
```

**Opções disponíveis:**
- `1` — Mostrar nome
- `2` — Mostrar nota
- `3` — Mostrar situação
- `0` — Sair

---

## 📄 `05 - estrutura-lista-dados.py` — Listas com While

Cria uma lista de alunos e percorre cada elemento usando `while` com índice manual (variável `contador`).

Demonstra operações básicas de lista:
- `append()` — adicionar elemento
- `pop()` — remover o último elemento
- Acesso por índice

```bash
python "05 - estrutura-lista-dados.py"
```

---

## 📄 `06 - repeticao-for.py` — Repetição com For

Percorre uma lista de alunos usando o loop `for`, de forma mais simples e legível do que o `while`.

```bash
python "06 - repeticao-for.py"
```

**Exemplo:**
```
nome do aluno: Ana
nome do aluno: Marta
...
```

---

## 📄 `07 - desconto.py` — Desconto com For

Percorre uma lista de preços e aplica **5% de desconto** em valores maiores ou iguais a R$ 40,00.

```bash
python "07 - desconto.py"
```

**Exemplo:**
```
19.5
46.55
95.0
15.9
31.49
```

---

## 📄 `08 - controle-notas.py` — Controle de Notas com For e Enumerate

Percorre uma lista de notas usando `for` com `enumerate()` e classifica cada aluno como **Aprovado**, **Recuperação** ou **Reprovado**.

| Nota        | Situação    |
|-------------|-------------|
| ≥ 7         | 🟢 Aprovado  |
| ≥ 5 e < 7  | 🟡 Recuperação |
| < 5         | 🔴 Reprovado  |

```bash
python "08 - controle-notas.py"
```

---

## 🛠️ Tecnologias

- **Python 3**

## 📚 Objetivo

Esta aula aborda as estruturas de repetição `while` e `for`, manipulação de listas e tomada de decisão com `if/elif/else` em Python.
