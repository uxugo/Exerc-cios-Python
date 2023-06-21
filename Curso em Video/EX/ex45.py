from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
cores = {'limpa' : '\033[m',
         'verde' : '\033[32m',
         'azul' : '\033[34m',
         'vermelho' : '\033[31m',
         }

computador = randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

player = int(input('Qual é a sua jogada? {}'.format(cores['verde'])))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!{}'.format(cores['limpa']))

print('-='*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[player]))
print('-='*10)

if computador == 0:
    if player == 0:
        print('{}EMPATE!'.format(cores['azul']))
    elif player == 1:
        print('{}JOGADOR GANHOU!'.format(cores['verde']))
    elif player == 2:
        print('{}COMPUTADOR GANHOU!'.format(cores['vermelho']))
    else:
        print('{}ERROR 404!'.format(cores['vermelho']))
elif computador == 1:
    if player == 0:
        print('{}COMPUTADOR GANHOU!'.format(cores['vermelho']))
    elif player == 1:
        print('{}EMPATE!'.format(cores['azul']))
    elif player == 2:
        print('{}JOGADOR GANHOU!'.format(cores['verde']))
    else:
        print('{}ERROR 404!'.format(cores['vermelho']))
elif computador == 2:
    if player == 0:
        print('{}JOGADOR GANHOU!'.format(cores['verde']))
    elif player == 1:
        print('{}COMPUTADOR GANHOU!'.format(cores['vermelho']))
    elif player == 2:
        print('{}EMPATE!'.format(cores['azul']))
    else:
        print('{}ERROR 404!'.format(cores['vermelho']))
print('{}'.format(cores['limpa']))