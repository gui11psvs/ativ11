# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)
def classificar_idade(idade)
    if idade <= 12:
    return "criança"
        return "criança"
    elif idade <= 17:
        return "adolescente"
    elif idade <= 59:
        return "idoso"
    elif idade <= 60:
         
try:
    idade = int(input("digete a idade da pessoa: "))
    if idade < 0:
        print ("a idade não pode ser negativa.")
    else:
        faixa_estaria = classificar_idade(idade)
        print(f"a pessoa de {idade} anos e classificada como: {faixa_etaria}.")
except valueerror:
    print("por favor, insira um número inteiro válido.")
    