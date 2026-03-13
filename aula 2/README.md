# Aula 2 — 05/03/2026 (Quinta-feira)

Repositório de estudo criado para praticar lógica de programação com Python.

## 📂 Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| `soma.py` | Soma de dois números inteiros fornecidos pelo usuário |
| `media_aluno.py` | Cálculo da média de um aluno e exibição da situação final |

---

## 📄 Arquivo: `soma.py`

Este script solicita dois números inteiros ao usuário e exibe a **soma** entre eles.

### Como funciona

1. O programa solicita ao usuário que insira o **primeiro número**.
2. Em seguida, solicita o **segundo número**.
3. Calcula a soma e exibe o resultado.

### Como executar

```bash
python soma.py
```

### Exemplo de uso

```
Digite um número: 5
Digite o segundo número: 3
8
```

---

## 📄 Arquivo: `media_aluno.py`

Este script calcula a **média de um aluno** com base em duas notas inseridas pelo usuário e informa a situação final (aprovado, em recuperação ou reprovado).

### Como funciona

1. O programa solicita ao usuário que insira a **Nota 1** e a **Nota 2**.
2. Calcula a **média aritmética** das duas notas.
3. Exibe a média calculada.
4. Com base na média, informa a **situação do aluno**:
   - **Aprovado** → média maior ou igual a 7
   - **Recuperação** → média maior ou igual a 5 e menor que 7
   - **Reprovado** → média menor que 5

### Critérios de aprovação

| Média           | Situação    |
|-----------------|-------------|
| ≥ 7,0           | Aprovado    |
| ≥ 5,0 e < 7,0   | Recuperação |
| < 5,0           | Reprovado   |

### Como executar

Certifique-se de ter o [Python](https://www.python.org/) instalado (versão 3.x recomendada).

```bash
python media_aluno.py
```

### Exemplo de uso

```
Digite a nota 1: 6.0
Digite a nota 2: 8.0
Média: 7.0
Aprovado
```

```
Digite a nota 1: 4.0
Digite a nota 2: 5.5
Média: 4.75
Reprovado
```

---

## 🛠️ Tecnologias

- **Python 3**

## 📚 Objetivo

Esta aula aborda estruturas condicionais (`if`, `else`) e entrada de dados (`input`) em Python.