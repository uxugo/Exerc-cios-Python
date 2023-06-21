import random
print('{:^5} Sorteio para aluno apagar o quadro {:^5}'.format(('-')*4,('-')*4))
#print('Alunos:\n1 - João\n2 - Maria\n3 - Pedro\n4 - Jorge')

alun1 = str(input('Primeiro aluno: '))
alun2 = str(input('Segundo aluno: '))
alun3 = str(input('Terceiro aluno: '))
alun4 = str(input('Quarto aluno: '))

sorteio = random.randint(1,4)

if sorteio == 1:
    nome = alun1
elif sorteio == 2:
    nome = alun2
elif sorteio == 3:
    nome = alun3
elif sorteio == 4:
    nome = alun4

print('Parabens {}, você foi o sorteado.'.format(nome))