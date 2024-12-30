lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]
diferenca = [item for item in lista1 if item not in lista2] + [item for item in lista2 if item not in lista1]
print(diferenca)
