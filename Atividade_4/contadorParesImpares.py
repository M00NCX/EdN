def contadorParesImpares():
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")
    
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


contadorParesImpares()
