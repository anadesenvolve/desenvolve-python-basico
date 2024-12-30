def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    multiplicadores1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(int(cpf[i]) * multiplicadores1[i] for i in range(9))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1
    
    multiplicadores2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(int(cpf[i]) * multiplicadores2[i] for i in range(10))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2
    
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return "Válido"
    
    return "Inválido"

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
print(valida_cpf(cpf))
