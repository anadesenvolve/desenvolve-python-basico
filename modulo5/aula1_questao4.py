import datetime

# Obter a data e hora atuais
agora = datetime.datetime.now()

# Formatando a data e hora
data_formatada = f"Data: {agora.day:02}/{agora.month:02}/{agora.year}"
hora_formatada = f"Hora: {agora.hour:02}:{agora.minute:02}"

# Exibir a data e hora formatadas
print(data_formatada)
print(hora_formatada)

