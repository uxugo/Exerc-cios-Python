from time import sleep

print('\033[1;33;40m-'*5+"Selecione a operação"+'-'*5)
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão\n"+'-'*30)

opcao = int(input(" - Digite a opção (1/2/3/4): "))

opcao = str(opcao)

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    resultado = num1 + num2
    operador = '+'
elif opcao == '2':
    resultado = num1 - num2
    operador = '-'
elif opcao == '3':
    resultado = num1 * num2
    operador = '*'
elif opcao == '4':
    if num1 or num2 == '0':
        resultado = num1 / num2
        operador = '/'
    else:
        print:('Erro: Divisão por zero!')
else:
    print('ERROR 404!\nOperação Invalida!')
    resultado = error
    operador = error

print('Aguarde o Resultado...\n' + '-'*30)
sleep(3)
print('Resultado: {} {} {} = {}'.format(num1,operador,num2,resultado))