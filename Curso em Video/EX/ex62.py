print('Gerador de PA\n' , '-='*8)

num = int(input('Primeiro termo: '))
pa = int(input('Razão da PA: '))

termos = 1
cont = 0
fat = num
opcao = 1 

while opcao != 0:
    while cont <= 8:
        termos += 1
        cont += 1
        fat = fat + pa
        if cont == 1:
            print(num , '> ' , end='')
        print(fat, end=' > ')
        print(end='')
        if cont == 9:
            print('FIM')
    
    opcao = int(input('\nQuantos termos você quer mostrar mais? '))
    
    for c in range(0,opcao):
        termos += 1
        c += 1
        fat = fat + pa
        print(fat, end=' > ')
        print(end='')
        if c < opcao:
            c = c
        else:
            print('PAUSA')

print('Progressão finalizada com {} termos mostrados.'.format(termos))