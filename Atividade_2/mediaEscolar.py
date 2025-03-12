def mediaEscolar(notas):
    media = round(sum(notas) / len(notas), 2)
    print("Notas do aluno:", notas)
    print(f"Média final: {media:.2f}")
    
mediaEscolar([7.5, 8.0, 6.5])