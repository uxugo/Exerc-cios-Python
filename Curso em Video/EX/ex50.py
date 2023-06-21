n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
n4 = int(input('Digite outro numero: '))
n5 = int(input('Digite outro numero: '))
n6 = int(input('Digite outro numero: '))

valores = 0
soma = 0

if n1 % 2 == 0:
    valores = valores + 1
    soma = n1 + soma
if n2 % 2 == 0:
    valores = valores + 1
    soma = n2 + soma
if n3 % 2 == 0:
    valores = valores + 1
    soma = n3 + soma
if n4 % 2 == 0:
    valores = valores + 1
    soma = n4 + soma
if n5 % 2 == 0:
    valores = valores + 1
    soma = n5 + soma
if n6 % 2 == 0:
    valores = valores + 1
    soma = n6 + soma    
else:
    print('ERROR 404!')

print('A soma de todos os valores impares são {}, foram {} valores ao todo.'.format(soma,valores))