import csv

def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Idade", "Cidade"])
        writer.writerows(dados)

# Exemplo de uso:
pessoas = [
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Mariana", 22, "Belo Horizonte"]
]

escrever_csv("pessoas.csv", pessoas)
print("Arquivo CSV criado com sucesso!")
