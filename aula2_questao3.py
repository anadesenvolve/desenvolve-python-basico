import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
interseccao = list(set(lista1) & set(lista2))
contagem_lista1 = {x: lista1.count(x) for x in interseccao}
contagem_lista2 = {x: lista2.count(x) for x in interseccao}

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção ordenada:", sorted(interseccao))
print("Contagem de elementos nas listas:")
for elem in interseccao:
    print(f"{elem}: (lista1={contagem_lista1[elem]}, lista2={contagem_lista2[elem]})")
