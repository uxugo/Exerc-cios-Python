#imports
from time import sleep

print('-'*27+'\n - Leitor de Velocidade - \n'+'-'*27)
velo = int(input('Digite aqui a sua velocidade: '))

print('\n'+' - A velocidade permitida da via é de até 80Km/h.')

#formulas
multa = (velo - 80) * 7

if velo >= 80:
    print('\n{}'.format('Você foi MULTADO!!'))
    print('\n - A via permitia somente 80Km/h, você foi flagrado em {}Km/h.'.format(velo))
    print('   Sendo assim, você sera multado por cada Km acima do limite.\n')
    sleep(1)
    print('-'*15 + '\n' + 'CONSULTANDO O SISTEMA... (Aguarde)\n' + '-'*15)
    sleep(2)
    print('Valor a pagar: R${}\nVelocidade permitida 80Km/h\nVelocidade capturada: {}Km/h'.format(multa,velo))
else:
    print('\n - A via permitia somente 80Km/h, você foi flagrado em {}Km/h.\n'.format(velo))
    sleep(1)
    print('-'*15 + '\n' + 'CONSULTANDO O SISTEMA... (Aguarde)\n' + '-'*15)
    sleep(2)
    print('Você NÃO pagará a Multa, Continue Assim!!')