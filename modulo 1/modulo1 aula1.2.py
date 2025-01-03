Dissertativa:
O programa solicita ao usuário um número 
𝑛
n entre 1 e 10.
Processamento:
Calcula-se 
𝑛−1
n−1, que será o dígito das dezenas.
Calcula-se 
10−𝑛10−n, que será o dígito das unidades.
O resultado final é dado por 
(𝑛−1)×10+(10−𝑛)
(n−1)×10+(10−n).

9×n é exibido ao usuário.

Pseudocodigo:
INÍCIO
    ESCREVA "Digite um número entre 1 e 10: "
    LEIA n
    SE (n < 1 OU n > 10) ENTÃO
        ESCREVA "Número inválido."
    SENÃO
        dezenas ← n - 1
        unidades ← 10 - n
        resultado ← (dezenas * 10) + unidades
        ESCREVA "O resultado de 9 x ", n, " é: ", resultado
    FIM_SE
FIM


