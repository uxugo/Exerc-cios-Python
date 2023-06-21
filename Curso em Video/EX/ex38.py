n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

if n1 == n2:
    print('Os números são IGUAIS')
elif n1 > n2:
    maior = 'PRIMEIRO NUMERO'
    print('O {} é maior'.format(maior))
elif n2 > n1:
    maior = 'SEGUNDO NUMERO'
    print('O {} é maior'.format(maior))