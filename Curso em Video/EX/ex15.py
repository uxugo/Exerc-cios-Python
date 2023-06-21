dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))

pagar = (60*dias) + (0.15*km)

print('Você deverá pagar R${:.2f}'.format(pagar))