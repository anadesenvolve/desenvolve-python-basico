lista = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

while True:
    tamanho = int(input("Tamanho para divisão: "))
    if tamanho == 0:
        break
    sublistas = [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]
    print("Subslistas:", sublistas)
