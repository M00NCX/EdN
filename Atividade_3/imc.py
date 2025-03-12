def imcCalculator(massa, altura):
    imc = round(massa / (altura ** 2), 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"
    print(f"Seu IMC: {imc:.2f} - Classificação: {classificacao}")

massaUser = float(input("Digite sua massa em kg: "))
alturaUser = float(input("Digite sua altura em m: "))
imcCalculator(massaUser, alturaUser)