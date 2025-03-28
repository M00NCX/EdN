import requests
def consultar_cotacao(moeda: str):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url).json()
    chave = f"{moeda}BRL"
    if chave in resposta:
        dados = resposta[chave]
        print(f"Moeda: {dados['code']}")
        print(f"Valor atual: R${dados['bid']}")
        print(f"Valor máximo: R${dados['high']}")
        print(f"Valor mínimo: R${dados['low']}")
        print(f"Última atualização: {dados['create_date']}")
    else:
        print("Moeda inválida ou não encontrada.")
consultar_cotacao("USD")