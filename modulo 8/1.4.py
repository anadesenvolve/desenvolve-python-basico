A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]


diferenca_A = set(A) - set(B)
diferenca_B = set(B) - set(A)

if diferenca_A:
    print(f"O elemento {diferenca_A.pop()} está faltando na segunda lista")
elif diferenca_B:
    print(f"O elemento {diferenca_B.pop()} está faltando na primeira lista")
