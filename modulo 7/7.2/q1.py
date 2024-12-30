def imprimir_data_com_nome_mes():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
    dia, mes, ano = data.split('/')
    
    mes_nome = meses[int(mes) - 1]
    
    print(f"Você nasceu em {dia} de {mes_nome} de {ano}.")

imprimir_data_com_nome_mes()
