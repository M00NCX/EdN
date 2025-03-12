def calcuadoraDesconto(nome, preco, desconto):
    descontoValor = round(preco * (desconto / 100), 2)
    precoFinal = round(preco - descontoValor, 2)
    print(f"Produto: {nome}")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Desconto: R$ {descontoValor:.2f} ({desconto}%)")
    print(f"Preço final: R$ {precoFinal:.2f}")
    
calcuadoraDesconto("Camiseta", 50.00, 20)