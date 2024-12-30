# Solicitar dois números decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcular a diferença absoluta e arredondar
diferenca = round(abs(num1 - num2), 2)

# Exibir o resultado
print(f"A diferença absoluta entre os números é: {diferenca}")
