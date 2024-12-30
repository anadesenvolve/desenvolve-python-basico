def calcula_area_perimetro(dimensoes):
    largura, comprimento = dimensoes
    area = largura * comprimento
    perimetro = 2 * (largura + comprimento)
    return (area, perimetro)

largura = 5
comprimento = 7
dimensoes = (largura, comprimento)

retorno = calcula_area_perimetro(dimensoes)
print(retorno, type(retorno)) >
