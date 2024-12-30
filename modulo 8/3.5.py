def resultado_votacao(votos):
    total_votos = {}
    
    # Contabilizando os votos de cada candidato
    for sessao in votos:
        for candidato, quantidade in sessao.items():
            total_votos[candidato] = total_votos.get(candidato, 0) + quantidade
    
    # Calculando o total geral de votos
    total_geral = sum(total_votos.values())
    
    # Calculando o percentual de votos para cada candidato
    resultado = {
        candidato: (quantidade, round((quantidade / total_geral) * 100, 2))
        for candidato, quantidade in total_votos.items()
    }
    
    return resultado


votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]

resultado = resultado_votacao(votos)
print(resultado)
