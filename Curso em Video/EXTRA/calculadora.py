def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "1"

print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção (1/2/3/4/): ")

if opcao in ['0','1', '2', '3', '4','5','6','7','8','9']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = soma(num1, num2)
        operacao = "+"
    elif opcao == '2':
        resultado = subtracao(num1, num2)
        operacao = "-"
    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        operacao = "*"
    else:
        resultado = divisao(num1, num2)
        operacao = "/"

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
else:
    print("Opção inválida. Por favor, selecione uma opção válida.")