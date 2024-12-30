def mesclar_dicionarios(d1, d2):
    resultado = d1.copy()
    for chave, valor in d2.items():
        if chave in resultado:
            resultado[chave] = max(resultado[chave], valor)
        else:
            resultado[chave] = valor
    return resultado


dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)
