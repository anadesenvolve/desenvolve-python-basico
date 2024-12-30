frase = input("Digite uma frase: ").split()
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = [palavra for palavra in frase if sorted(palavra) == sorted(palavra_objetivo)]
print(f"Anagramas: {anagramas}")
