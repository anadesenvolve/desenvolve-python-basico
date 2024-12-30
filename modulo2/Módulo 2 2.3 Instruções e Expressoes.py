Q1 - Cálculo do salário semanal com desconto

Código:
# Valores iniciais
salario_por_hora = 20  # R$20 por hora
horas_trabalhadas = 40  # 40 horas por semana

# Cálculos
salario_bruto = salario_por_hora * horas_trabalhadas
desconto_inss = salario_bruto * 0.10
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_inss + desconto_sindicato)

# Impressão dos resultados
print(f"Salário semanal bruto: R${salario_bruto:.2f}")
print(f"Desconto INSS (10%): R${desconto_inss:.2f}")
print(f"Desconto Sindicato (5%): R${desconto_sindicato:.2f}")
print(f"Salário semanal líquido: R${salario_liquido:.2f}")

Q2 - Otimização do programa anterior

Código:
# Valores iniciais
salario_por_hora = 20  # R$20 por hora
horas_trabalhadas = 40  # 40 horas por semana

# Cálculos em duas instruções
salario_bruto = salario_por_hora * horas_trabalhadas
salario_liquido = salario_bruto - (salario_bruto * 0.10 + salario_bruto * 0.05)

# Impressão dos resultados
print(f"Salário semanal bruto: R${salario_bruto:.2f}")
print(f"Salário semanal líquido: R${salario_liquido:.2f}")

Q3 - Conversão de moeda BRL para CNY
Você está desenvolvendo um software de conversão de moeda e precisa calcular o valor equivalente em yuan chinês a partir de uma quantia em real. A taxa de câmbio é de 0.69 BRL (real) para 1 CNY (yuan).
Escreva um programa que define em uma variável uma quantia em reais (BRL) e calcula o valor equivalente em yuan (CNY). Imprima o resultado.

Código:
# Valor em reais (BRL) e taxa de câmbio
quantia_brl = 1000  # Valor em reais a ser convertido
taxa_cambio = 0.69  # 1 CNY = 0.69 BRL

# Cálculo do valor em yuan (CNY)
valor_cny = quantia_brl / taxa_cambio

# Impressão do resultado
print(f"R${quantia_brl:.2f} equivalem a ¥{valor_cny:.2f} yuan.")

Q4 - Velocidade média na maratona
# Distância total em quilômetros e tempo em horas
distancia_km = 42.195  # Distância da maratona em km
tempo_horas = 3  # Tempo para completar a maratona em horas

# Conversão e cálculo
distancia_metros = distancia_km * 1000  # Conversão para metros
tempo_segundos = tempo_horas * 3600  # Conversão para segundos
velocidade_media = distancia_metros / tempo_segundos  # Velocidade média em m/s

# Impressão do resultado
print(f"A velocidade média necessária é {velocidade_media:.2f} m/s.")
