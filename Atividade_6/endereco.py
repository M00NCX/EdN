import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url).json()
    if "erro" in resposta:
        print("CEP inválido.")
    else:
        print(f"Logradouro: {resposta['logradouro']}")
        print(f"Bairro: {resposta['bairro']}")
        print(f"Cidade: {resposta['localidade']}")
        print(f"Estado: {resposta['uf']}")

consultar_cep("48903210")