def classificadorIdade(idade):
    if idade < 0:
        print("Idade inválida")
    elif idade <= 12:
        print("Você é uma criança")
    elif  idade<= 17:
        print("Você é um adolescente")
    elif idade <= 59:
        print("Você é um Adulto")
    else:
        print("Você é um idoso")

idadeUser = int(input("Digite sua idade: "))
classificadorIdade(idadeUser)