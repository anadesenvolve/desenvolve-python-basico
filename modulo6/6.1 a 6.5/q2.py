def testa_equilatero(lados):
    return len(set(lados)) == 1

triangulos = [[2,2,2], [3,4,5], [3,2,2], [4,4,4]]
equilateros = list(filter(testa_equilatero, triangulos))
print(equilateros)
