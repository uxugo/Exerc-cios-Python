#introdução
print('='*27)
print(' '*4 + '10 TERMOS DE UMA PA')
print('='*27)

#input para o numero inicial e o intervalo entre eles
inicio = int(input('Primeiro termo: ')) 
intervalo = int(input('Razão: '))

#formula para calcular o decimo numero da variavel inicio
decimo = inicio + (10-1) * intervalo

#laço de repetição
for c in range(inicio , decimo + intervalo , intervalo):
    print(c, end=' - ')

print('ACABOU\n')