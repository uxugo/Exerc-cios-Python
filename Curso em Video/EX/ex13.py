salario = float(input('Qual o seu salario atualmente? R$'))

ajuste = salario*115 / 100

print('Um funcionario que recebia R${:.2f}, com \no reajuste de 15% irá ganhar R${:.2f}'.format(salario,ajuste))