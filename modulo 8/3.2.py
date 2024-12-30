def contar_palavras_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        texto = file.read().lower().split()
        
    contagem_palavras = {}
    for palavra in texto:
        palavra = palavra.strip('.,!?()[]{}":;')
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    
    palavras_ordenadas = dict(sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True))
    
    return palavras_ordenadas


arquivo = "estomago.txt"
resultado = contar_palavras_arquivo(arquivo)
print(resultado)
