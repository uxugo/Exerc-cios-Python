salario = float(input('Digite aqui o seu salario: R$'))

if salario > 1250:
    aumento = 110
    x = 10
else:
    aumento = 115
    x = 15

novo_salario = (salario / 100) * aumento

print('''Seu salario saiu de R${:.2f}, com o 
aumento de {}%, passou a ser R${:.2f}'''.format(salario,x,novo_salario) )