#pedir o numero
num = int(input('Digite um numero: '))
#total de vezes dividida
total = 0
#laço para
for c in range(1,num + 1 , 1):
    if num % c == 0:
        print('\033[32m' , end='')
        total = total + 1
    else:
        print('\033[m', end='')
    print(c , end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num , total))
if total == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO é PRIMO!')