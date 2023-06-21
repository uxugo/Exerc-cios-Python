frase = str(input('Digite uma frase: ')).strip(). upper()
#quantidade de caracteries
qtd = len(frase)
num = 0

inverso = frase[::-1]

print('O inverso de {} é '.format(frase) , end='')
for c in range(0, qtd , 1):
    num = num - 1
    print(frase[qtd + num] , end='')

if inverso == frase:
    print('\nÉ um palíndromo!')
else:
    print('\nNão é um palíndromo!')