print('-='*19 + '\n| Analizando se pode virar triangulo |\n' + '-='*19)

r1 = int(input('Digite a primeira linha: '))
r2 = int(input('Digite a segunda linha: '))
r3 = int(input('Digite a terceira linha: '))

ordem = sorted([r1,r2,r3])
n1 = ordem[0]
n2 = ordem[1]
n3 = ordem[2]

soma = n1 + n2

triangulo = ordem.count(r1)

if soma > n3:
    if triangulo == 1:
        triangulo = 'ESCALENO'
    if triangulo == 2:
        triangulo = 'ISÓCELES'
    if triangulo == 3:
        triangulo = 'EQUILATERO'
    print('Pode formar uma triangulo {}'.format(triangulo))
else:
    print('Não pode formar um triangulo')