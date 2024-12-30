Q1. Fatorial
def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

n = int(input("Digite um número inteiro para calcular o fatorial: "))
print(f"O fatorial de {n} é {fatorial(n)}.")

Q2. Soma dos quadrados
def soma_quadrados(a, b):
    return a**2 + b**2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"A soma dos quadrados é: {soma_quadrados(num1, num2)}.")

Q3. Soma dos digitos
def soma_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

numero = int(input("Digite um número inteiro: "))
print(f"A soma dos dígitos é: {soma_digitos(numero)}.")

Q4. Inverter valor e verificar paridade
def inverteValor(numero):
    invertido = 0
    while numero > 0:
        invertido = invertido * 10 + numero % 10
        numero //= 10
    return invertido

def verificaInverso(original, invertido):
    return (original % 2) == (invertido % 2)

numero = int(input("Digite um número inteiro: "))
invertido = inverteValor(numero)
print(f"O valor invertido é: {invertido}.")
print(f"Original e invertido têm a mesma paridade? {verificaInverso(numero, invertido)}.")

Q5. Perimetros geograficos
import math

def calcula_perimetro_triangulo(a, b, c):
    return a + b + c

def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

def calcula_perimetro_retangulo(lado1, lado2=0):
    if lado2 == 0:
        lado2 = lado1
    return 2 * (lado1 + lado2)

while True:
    print("\n1 - Calcular perímetro triângulo")
    print("2 - Calcular perímetro círculo")
    print("3 - Calcular perímetro retângulo")
    print("4 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        a = int(input("Digite o lado 1: "))
        b = int(input("Digite o lado 2: "))
        c = int(input("Digite o lado 3: "))
        print(f"O perímetro do triângulo é: {calcula_perimetro_triangulo(a, b, c)}.")
    elif opcao == 2:
        raio = int(input("Digite o raio do círculo: "))
        print(f"O perímetro do círculo é: {calcula_perimetro_circulo(raio):.2f}.")
    elif opcao == 3:
        lado1 = int(input("Digite o lado 1: "))
        lado2 = int(input("Digite o lado 2 (ou 0 se for um quadrado): "))
        print(f"O perímetro do retângulo é: {calcula_perimetro_retangulo(lado1, lado2)}.")
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

Q6. lambda:verificar paridade
par_ou_impar = lambda x: "par" if x % 2 == 0 else "ímpar"

print("Digite os valores para verificar a paridade (digite 0 para sair):")
while True:
    numero = int(input())
    if numero == 0:
        break
    print(par_ou_impar(numero))

Q7.Maior ou menor
opcao = int(input("Opções: (1) maior ou (2) menor?\nOpção: "))
if opcao not in [1, 2]:
    print("Opção inválida!")
else:
    numeros = []
    print("Digite os valores de entrada. Digite 0 para finalizar.")
    while True:
        numero = int(input())
        if numero == 0:
            break
        numeros.append(numero)
    
    if opcao == 1:
        resultado = max(numeros, key=lambda x: x)
        print(f"O maior valor é: {resultado}")
    else:
        resultado = min(numeros, key=lambda x: x)
        print(f"O menor valor é: {resultado}")

