import json

def escrever_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as file:
        json.dump(dados, file, indent=4)

def ler_json(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados = json.load(file)
        print(f'Nome: {dados["Nome"]}, Idade (meses): {dados["Idade"]}, Cidade: {dados["Cidade"]}')


pessoa = {"Nome": "Nyx", "Idade": 2, "Cidade": "Juazeiro"}

escrever_json("pessoa.json", pessoa)
ler_json("pessoa.json")
