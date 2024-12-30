frase = input("Digite uma frase: ")

vogais = sorted([char for char in frase.lower() if char in 'aeiou'])
print(f"Vogais: {vogais}")

consoantes = [char for char in frase if char.isalpha() and char not in 'aeiouAEIOU']
print(f"Consoantes: {consoantes}")
