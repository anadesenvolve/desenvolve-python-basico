def tem_elementos_comuns(lista1, lista2):
   
    return bool(set(lista1) & set(lista2))

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7]
resultado = tem_elementos_comuns(lista1, lista2)
print(resultado)  
