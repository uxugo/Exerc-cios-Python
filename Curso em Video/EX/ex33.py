n1 = int(input('Digite n° 1: '))
n2 = int(input('Digite n° 2: '))
n3 = int(input('Digite n° 3: '))

x = sorted([n1,n2,n3])

print('O maior numero é {} e o menor é {}.'.format(x[2],x[0]))