def conversorMoeda(real, dolar, euro):
    convertidoDolar = round(real / dolar, 2)
    convertidoEuro = round(real / euro, 2)
    print(f"Valor em reais: R$ {real:.2f}")
    print(f"Valor em dólares: US$ {convertidoDolar:.2f}")
    print(f"Valor em euros: € {convertidoEuro:.2f}")
    
conversorMoeda(100.00, 5.20, 6.15)