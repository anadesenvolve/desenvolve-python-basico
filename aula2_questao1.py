import random

valores = [random.randint(-100, 100) for _ in range(20)]
ordenada = sorted(valores)
indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

print("Lista ordenada (sem modificar a original):")
print(ordenada)
print("\nLista original:")
print(valores)
print("\nÍndice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
