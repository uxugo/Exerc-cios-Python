from random import randint
import time

print('{}\n - Seja bem vindo ao Jogo de Advinhação!! -\n{}'.format('-'*44,'-'*44))
num = int(input('\nDigite um número de 1 a 5: '))

sorteado = randint(1,5)

print('Estou Pensando...')

time.sleep(2)

if num == sorteado:
    print('PARABENS, Você é o Ganhador!\nO número sorteado foi {}, e você escolheu o {}!'.format(sorteado,num))
elif num > 5:
    print('ERROR número invalido, você digitou {}\nEscolha um número de 1 até 5.'.format(num))
else:
    print('É uma Pena, Jovem!.\nO número sorteado foi {}, e você escolheu o {}!'.format(sorteado,num))