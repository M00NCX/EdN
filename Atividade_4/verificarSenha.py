
def verificarSenha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            break
        if len(senha) >= 8 and any(char.isdigit() for char in senha):
            print("Senha válida!")
            break
        else:
            print("Senha fraca. Deve ter pelo menos 8 caracteres e conter pelo menos um número.")
            
verificarSenha()