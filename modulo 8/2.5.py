def listar_pessoas_na_balada():
    fila = []
    while True:
        nome = input("Digite o nome (ou 'sair' para terminar): ")
        if nome.lower() == 'sair':
            break
        idade = int(input(f"Digite a idade de {nome}: "))
        fila.append((nome, idade))

    menores = tuple(nome for nome, idade in fila if idade < 18)
    maiores = tuple(nome for nome, idade in fila if idade >= 18)
    
    return menores, maiores

menores, maiores = listar_pessoas_na_balada()
print("Menores de idade:", menores)
print("Maiores de idade:", maiores)
