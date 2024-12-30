import string

def checa_panagrama(frase):
    alfabeto = set(string.ascii_lowercase)
    frase = set(frase.lower())
  
    if alfabeto <= frase:
        return "É um panagrama"
    else:
        return "Não é um panagrama"

print(checa_panagrama("The quick brown fox jumps over the lazy dog"))  # Saída esperada: É um panagrama
print(checa_panagrama("Python é uma linguagem de programação"))  # Saída esperada: Não é um panagrama
