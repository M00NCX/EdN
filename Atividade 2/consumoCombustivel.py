def consumoCombustivel(distancia, combustivel):
    consumoMedio = round(distancia / combustivel, 2)
    print(f"Distância percorrida: {distancia} km")
    print(f"Combustível gasto: {combustivel} litros")
    print(f"Consumo médio: {consumoMedio} km/l")
    
consumoCombustivel(300, 25)