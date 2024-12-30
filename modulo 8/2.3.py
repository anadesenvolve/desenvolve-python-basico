def ordenar_tuplas(alunos_notas):
    # Ordenar as tuplas pela segunda posição (média) em ordem decrescente
    return sorted(alunos_notas, key=lambda x: x[1], reverse=True)

# Exemplo de uso
alunos_notas = [('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.0), ('David', 8.8)]
resultado = ordenar_tuplas(alunos_notas)
print(resultado)
