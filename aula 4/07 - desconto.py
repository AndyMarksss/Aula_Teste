# Desconto de 5% para valores maiores ou iguais a 40.00

valores = [19.50, 49.00, 100.00, 15.90, 31.49]  ### Cria uma lista chamada valores com alguns números decimais

for valor in valores:  ### Para cada elemento valor na lista valores, execute o bloco de código abaixo
    if valor >= 40.00: ## Se o valor for maior ou igual a 40.00, execute o bloco de código abaixo
        print(valor * 0.95) ### Imprime o valor com desconto de 5% (valor multiplicado por 0.95) na tela
    else: ### Se o valor for menor que 40.00, execute o bloco de código abaixo
        print(valor) ### Imprime o valor original (sem desconto) na tela