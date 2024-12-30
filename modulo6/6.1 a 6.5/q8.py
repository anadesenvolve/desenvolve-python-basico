def avalia_tabuleiro(tabuleiro):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]

    return "Empate"

# Testando a função
tabuleiro1 = [['X', 'O', 'X'], [' ', 'X', 'O'], ['O', ' ', 'X']]
tabuleiro2 = [['X', 'O', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']]
tabuleiro3 = [[' ', ' ', ' '], ['X', ' ', 'O'], ['O', 'X', 'X']]
tabuleiro4 = [['O', 'O', 'O'], ['X', ' ', 'X'], ['O', 'X', 'X']]
tabuleiro5 = [['X', 'X', 'O'], ['X', ' ', 'O'], ['O', 'O', 'X']]

print(avalia_tabuleiro(tabuleiro1))  # Empate
print(avalia_tabuleiro(tabuleiro2))  # O
print(avalia_tabuleiro(tabuleiro3))  # Empate
print(avalia_tabuleiro(tabuleiro4))  # O
print(avalia_tabuleiro(tabuleiro5))  # Empate
