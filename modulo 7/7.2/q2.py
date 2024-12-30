def substituir_vogais():
    frase = input("Digite uma frase: ")
    nova_frase = ''.join('*' if char.lower() in "aeiou" else char for char in frase)
    print(f"Frase modificada: {nova_frase}")

substituir_vogais()
