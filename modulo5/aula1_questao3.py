import random

# Gerar um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

while True:
    # Solicitar o palpite do usuário
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
    # Fornecer feedback ao usuário
    if palpite < numero_aleatorio:
        print("Muito baixo, tente novamente!")
    elif palpite > numero_aleatorio:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {palpite}.")
        break
