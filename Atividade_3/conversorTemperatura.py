def conversorTemperatura(valor, origem, destino):
    if origem == "C" and destino == "F":
        convertido = (valor * 9/5) + 32
    elif origem == "C" and destino == "K":
        convertido = valor + 273.15
    elif origem == "F" and destino == "C":
        convertido = (valor - 32) * 5/9
    elif origem == "F" and destino == "K":
        convertido = (valor - 32) * 5/9 + 273.15
    elif origem == "K" and destino == "C":
        convertido = valor - 273.15
    elif origem == "K" and destino == "F":
        convertido = (valor - 273.15) * 9/5 + 32
    else:
        print("Conversão inválida.")
        return
    print(f"{valor}°{origem} equivale a {round(convertido, 2)}°{destino}")
    
valor = float(input("Digite o valor da temperatura: "))
uOrigem = (input("Digite a unidade de origem (C, F ou K): "))
uDestino = (input("Digite a unidade de destino (C, F ou K): "))

conversorTemperatura(valor, uOrigem, uDestino)