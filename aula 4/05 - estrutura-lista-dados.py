alunos = ["Ana Maria", "Pedro", "Marta", "Mario", "Luiza"]  #### Cria uma lista chamada alunos com os nomes dos alunos

# alunos.append("Carla")  ### Adiciona um novo aluno no final da lista

# alunos.pop()  ### Remove o último aluno da lista

# alunos[0] = "Ana"  ### Altera o nome do primeiro aluno para "Ana"

contador = 0 ### Variável contador para controlar o índice dos alunos na lista

while contador < len(alunos): ### Enquanto o contador for menor que o número de alunos na lista, len(alunos) retorna o número de elementos na lista
    print(f'nome do aluno: {alunos[contador]}')
    contador += 1 #### Incrementa o contador para acessar o próximo aluno
