frase = input("Digite uma frase: ")
vogais = "aeiou"
indices = [i for i, char in enumerate(frase) if char.lower() in vogais]
print(f"{len(indices)} vogais")
print(f"Índices {indices}")
