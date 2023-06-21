num = int(input('Digite um numero para ver sua tabuada: '))
operador = 0
for c in range(0,10):
    operador = operador + 1
    resultado = operador * num
    print('{} X {} = {}'.format(num , operador , resultado))