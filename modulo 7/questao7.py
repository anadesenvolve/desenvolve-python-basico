import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []
    
    for nome in nomes:
        criptografado = ''.join([chr((ord(c) + chave - 33) % 94 + 33) for c in nome])
        nomes_criptografados.append(criptografado)
    
    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print(f"Nomes criptografados: {nomes_criptografados}")
print(f"Chave de criptografia: {chave}")
