### Cálculo de média e situação do aluno

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    if media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")