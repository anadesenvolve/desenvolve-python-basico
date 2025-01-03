import string

def verificar_palindromo():
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
        
        if frase.lower() == "fim":
            break
        
        # Remover espaços, pontuações e converter para minúsculas
        frase_limpa = ''.join(c for c in frase.lower() if c.isalnum())
        
        if frase_limpa == frase_limpa[::-1]:
            print(f'"{frase}" é palíndromo')
        else:
            print(f'"{frase}" não é palíndromo')

verificar_palindromo()
