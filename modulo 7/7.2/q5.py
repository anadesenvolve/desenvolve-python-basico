import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []
    
    for palavra in palavras:
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = palavra[0] + ''.join(meio) + palavra[-1]
        else:
            nova_palavra = palavra
        nova_frase.append(nova_palavra)
    
    return ' '.join(nova_frase)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
