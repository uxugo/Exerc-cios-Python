cores = {'limpa' : '\033[m',
         'input' : '\033[4;34m',
         'azul' : '\033[34m',
         'branco' : '\033[37m',
         'roxo' : '\033[35m',
         'ciano' : '\033[36m',
         }

n1 = int(input('{}Digite um valor: {}'.format(cores['azul'] , cores['limpa'] + cores['input'])))
n2 = int(input('{}Outro valor: {}'.format(cores['limpa'] + cores['branco'] , cores['limpa'] + cores['input'])))
soma = int(n1) + int(n2)

print('{}{}A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['limpa'] , cores['roxo'] , cores['ciano'] , n1 , cores['roxo'] , cores['ciano'] , n2 , cores['roxo'] , cores['ciano'] , soma , cores['roxo']))

#print('{}A soma entre {} e {} é igual a {}.'.format(cores['limpa'] + cores['roxo'] , cores['ciano'] + n1 + cores['roxo'], cores['ciano'] + n1 , cores['ciano'] + soma))