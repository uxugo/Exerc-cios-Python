cores = {'limpa':'\033[m',
         'input':'\033[4;34m',
         'vermelho':'\033[31m'}
nome = input('{}Escreva seu nome: {}'.format(cores['vermelho'] ,cores['limpa'] + cores['input']))
print('{}É um prazer te conhecer, {}.{}'.format(cores['limpa'] + cores['vermelho'] , nome , cores['limpa']))