### Repetição com For

### O código a seguir cria uma lista de alunos e utiliza um loop for para iterar sobre cada elemento da lista, imprimindo o nome de cada aluno na tela. O loop for é uma estrutura de controle de fluxo que permite percorrer elementos de uma coleção (como listas, tuplas, dicionários, etc.) de forma simples e eficiente. Neste exemplo, a variável aluno assume o valor de cada elemento da lista alunos a cada iteração do loop, permitindo que o nome do aluno seja impresso na tela.

alunos = ['Ana', 'Marta', 'Mario', 'Leonid','José', 'Hugo', 'Andy']

# contador = 0
# tamanho = len(alunos)
# while contador < tamanho:
#     print (f'nome do aluno: {alunos[contador]}')
#     contador += 1

for aluno in alunos:
    print (f'nome do aluno: {aluno}')