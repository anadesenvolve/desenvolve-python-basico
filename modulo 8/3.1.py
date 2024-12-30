def contagem_caracteres(frase):
    contagem = {}
    for caractere in frase:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem


frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)
