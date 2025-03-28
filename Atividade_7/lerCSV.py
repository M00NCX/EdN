import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, mode='r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                print(f'Cabeçalho: {", ".join(row)}')
            else:
                print(f'{row[0]} tem {int(row[1]) // 12} anos e {int(row[1]) % 12} meses.')


ler_csv("animal.csv")
