#leia o cateto oposto e adjascente e me diga a hipotenusa 
import math
co = float(input('Digite o numero do cateto oposto: '))
ca = float(input('Digite o numero do cateto adjascente: '))

co = math.pow(co,2)
ca = math.pow(ca,2)
resultado = math.sqrt(co + ca)
#resultado = h**2 = co**2 + ca**2


print('A hipotenusa é {:.2f}'.format(resultado))