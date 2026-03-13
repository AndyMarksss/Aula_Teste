### Tabuada com While 

contador = 1

### O código a seguir solicita ao usuário que digite um número e, em seguida, utiliza um loop while para calcular e exibir a tabuada desse número de 1 a 10. A variável contador é inicializada em 1 e é incrementada a cada iteração do loop até atingir o valor 10, momento em que o loop é encerrado.
numero = int(input("Digite um número para ver a tabuada: "))

### O loop while continua a executar enquanto o contador for menor ou igual a 10. Dentro do loop, o resultado da multiplicação do número pelo contador é calculado e impresso no formato "número x contador = resultado". Após cada iteração, o contador é incrementado em 1 para avançar para a próxima multiplicação.
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1