import math
grau = int(input('Digite um grau para saber \nseu sen, cos e tan: '))
rad = math.radians(grau)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('O Seno de {}° é equivalente a: {:.2f}\nO Cosseno de {}° é equivalente a: {:.2f}\nA Tangente de {}° é equivalente a: {:.2f}'.format(grau,sen,grau,cos,grau,tan))