n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o elemento {i + 1} da lista 1: ")) for i in range(n1)]

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o elemento {i + 1} da lista 2: ")) for i in range(n2)]

intercalada = []
for i in range(min(len(lista1), len(lista2))):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])

intercalada.extend(lista1[len(lista2):])
intercalada.extend(lista2[len(lista1):])

print("Lista intercalada:", " ".join(map(str, intercalada)))
