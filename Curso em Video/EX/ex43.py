print('-='*9+ '\n| Calculo de IMC |\n' + '-='*9)

kg = float(input('Qual é o seu peso? '))
altura = float(input('E a sua altura? '))

imc = kg / (altura * altura)

grau = ''

if imc > 40:
    grau = 'OBESIDADE GRAVE'
elif imc > 30:
    grau = 'OBESIDADE'
elif imc > 25:
    grau = 'SOBREPESO'
elif imc > 18.5:
    grau = 'NORMAL'
else:
    grau = 'ABAIXO DO PREÇO'

print('O IMC dessa pessoa é de {:.1f}\nVocê está {}'.format(imc , grau))