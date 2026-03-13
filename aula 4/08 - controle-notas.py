### Este código é um exemplo de controle de notas dos alunos. Ele percorre uma lista de notas e classifica cada nota como "Aprovado", "Recuperação" ou "Reprovado" com base em critérios pré-definidos.

notas = [2, 4, 9, 4, 2, 5, 9] ### Cria uma lista chamada notas com alguns números inteiros representando as notas dos alunos

for indice, nota in enumerate(notas): ### Para cada elemento nota na lista notas, execute o bloco de código abaixo. A função enumerate() retorna tanto o índice quanto o valor do elemento atual, permitindo que ambos sejam usados dentro do loop.
    if nota >= 7: ### Se a nota for maior ou igual a 7, execute o bloco de código abaixo
        print(f"Aluno {indice + 1} com a nota: {nota} -> 🟢 Aprovado") ### Imprime o número do aluno (índice + 1) e a nota, seguido de um emoji verde e a palavra "Aprovado" na tela
    elif nota >= 5: ### Se a nota for maior ou igual a 5, execute o bloco de código abaixo
        print(f"Aluno {indice + 1} com a nota: {nota} -> 🟡 Recuperação")
    else: ### Se a nota for menor que 5, execute o bloco de código abaixo
        print(f"Aluno {indice + 1} com a nota: {nota} -> 🔴 Reprovado")