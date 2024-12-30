import random
import math

# Solicitar o número de valores a serem gerados
n = int(input("Digite o número de valores aleatórios a serem gerados: "))

# Gerar números aleatórios e calcular a soma
soma = sum(random.randint(0, 100) for _ in range(n))

# Calcular a raiz quadrada da soma
raiz = math.sqrt(soma)

# Exibir o resultado
print(f"A raiz quadrada da soma dos valores é: {raiz:.2f}")
