### Login com While

senha_cadastrada = "asd"

### O código a seguir solicita ao usuário que digite uma senha e, em seguida, utiliza um loop while para verificar se a senha digitada corresponde à senha cadastrada. Se a senha digitada for incorreta, o programa exibe uma mensagem de erro e solicita que o usuário tente novamente. O loop continua até que a senha correta seja digitada, momento em que o programa exibe uma mensagem de acesso permitido.
senha_digitada = input("Digite a senha: ")

### O loop while continua a executar enquanto a senha digitada for diferente da senha cadastrada. Dentro do loop, uma mensagem de erro é exibida e o usuário é solicitado a digitar a senha novamente. Quando a senha correta for digitada, o loop será encerrado e a mensagem de acesso permitido será exibida.
while senha_cadastrada != senha_digitada:
    print("Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

print("Acesso permitido.")