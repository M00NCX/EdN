from datetime import date

def idadeEmDias(ano_nascimento: int) -> int:
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365 

print(idadeEmDias(2001))