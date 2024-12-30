def pares_unicos(numeros, soma_objetivo):
    pares = set()
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] + numeros[j] == soma_objetivo:
                pares.add(tuple(sorted([numeros[i], numeros[j]])))
    return list(pares)

nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print(resultado)
