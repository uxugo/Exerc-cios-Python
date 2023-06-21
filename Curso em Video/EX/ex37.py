num = int(input('Digite aqui um número inteiro: '))

opcao =  int(input('''Escolha a base para conversão:
[ 1 ] converta aqui para BINARIO
[ 2 ] converta aqui para OCTAL
[ 3 ] converta aqui para HEXADECIMAL
Digite sua opção: '''))

if opcao == 1:
    conversao = 'BINARIO'
    resposta = bin(num)
elif opcao == 2:
    conversao = 'OCTAL'
    resposta = oct(num)
elif opcao == 3:
    conversao = 'HEXADECIMAL'
    resposta = hex(num)
else:
    print('Opção invalida, Tente novamente!!')

print('{} foi convertido para {}, é igual a {}'.format(num,conversao,resposta[2:]))