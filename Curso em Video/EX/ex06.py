from math import sqrt

cores = {'input':'\033[34;4m',
         'verde':'\033[0;32m'}
num = float(input('{}Digite um número: {}'.format(cores['verde'] , cores['input'])))
print('{}O dobro de {} vale {}.'.format(cores['verde'] , num , num*2))
print('O triplo de {} vale {}.'.format(num , num*3))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num , sqrt(num)))