km = float(input('Digite a distancia percorrida: '))

if km <= 200:
    valor = km*0.5
if km > 200:
    valor = km*0.45
print('Você pagará R${:.2f}'.format(valor))
