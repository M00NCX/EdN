def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao not in ['+', '-', '*', '/']:
                print("Erro: Operação inválida.")
                continue

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não permitida.")
                    continue
                resultado = num1 / num2

            print(f"Resultado: {resultado}")
            break
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de inserir números válidos.")
            
calculadora()