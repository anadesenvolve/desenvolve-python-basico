
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))


if distancia <= 100:
    custo_frete = peso * 1.00
elif 101 <= distancia <= 300:
    custo_frete = peso * 1.50
else:
    custo_frete = peso * 2.00

if peso > 10:
    custo_frete += 10.00

print(f"O valor do frete é: R${custo_frete:.2f}")
