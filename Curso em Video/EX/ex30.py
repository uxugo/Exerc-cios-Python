print('{}\n - Leitor de Par ou Impar - \n{}'.format('-'*28 , '-'*28))

num = int(input('Digite um número: '))

res = num % 2

if res == 0:
    print('Esse Número é PAR!')
else:
    print('Esse Número é IMPAR!')