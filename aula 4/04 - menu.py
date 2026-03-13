### Menu de opções com While

### O código a seguir implementa um menu de opções utilizando um loop while. O menu apresenta quatro opções: mostrar nome, mostrar nota, mostrar situação e sair. O usuário é solicitado a escolher uma opção digitando o número correspondente. O loop continua a exibir o menu e processar as escolhas do usuário até que a opção de sair (0) seja selecionada. Se o usuário escolher uma opção inválida, uma mensagem de erro é exibida e o menu é apresentado novamente.

opcao = None

### O loop while continua a executar enquanto a variável opcao for diferente de "0". Dentro do loop, o menu de opções é exibido e o usuário é solicitado a escolher uma opção. Dependendo da escolha do usuário, uma mensagem correspondente é exibida. Se a opção escolhida for "0", uma mensagem de saída é exibida e o loop é encerrado. Se a opção escolhida for inválida, uma mensagem de erro é exibida e o menu é apresentado novamente.
while opcao != "0":
    
    print("\n1 - Mostrar nome")
    print("2 - Mostrar nota")
    print("3 - Mostrar situação")
    print("0 - Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        print("\nNome: João")
    elif opcao == "2":
        print("\nNota: 8.5")
    elif opcao == "3":
        print("\nSituação: Aprovado")
    elif opcao == "0":
        print("Saindo...")
    else:
        print("\nOpção inválida. Tente novamente.")   