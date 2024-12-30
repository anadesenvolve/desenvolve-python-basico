def imprimir_vogais_e_indices(frase):
    vogais = "aeiouAEIOU"
    for indice, char in enumerate(frase):
        if char in vogais:
            print(f"Vogal: {char}, Índice: {indice}")


frase = "O rato roeu a roupa da Alice"
imprimir_vogais_e_indices(frase)
