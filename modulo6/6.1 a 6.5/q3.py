def ordena_por_comprimento(nomes):
    return sorted(nomes, key=lambda nome: len(nome))

nomes = ["Joao", "Maria", "Jose", "Gabriela", "Sol", "Luna", "Bento", "Enzo", "Fernanda"]
resultado = ordena_por_comprimento(nomes)
print(resultado)
