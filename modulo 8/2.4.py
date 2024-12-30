from collections import defaultdict

def comprimir_tuplas(tuplas):
    dicionario = defaultdict(int)
    for palavra, numero in tuplas:
        dicionario[palavra] += numero
    return list(dicionario.items())


tuplas_originais = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]
resultado = comprimir_tuplas(tuplas_originais)
print(resultado)
