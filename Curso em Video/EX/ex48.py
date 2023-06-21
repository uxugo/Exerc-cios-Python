soma = 0
quant = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        quant = quant + 1

print('A soma de todos os valores solicitados é {}.'.format(soma))
print('Foram {} itens ao todo.'.format(quant))