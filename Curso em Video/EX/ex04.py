cores = {'limpa' : '\033[m',
         'input' : '\033[34;4m',
         'vermelho' : '\033[0;31m',
         }

x = input('{}Digite algo: {}'.format(cores['vermelho'] , cores['input']))

print('{}O tipo primitivo desse valor é: {}{}'.format(cores['vermelho'] ,  cores['input'] , x.__class__))
print('{}Só tem espaços? {}{}'.format(cores['vermelho'] , cores['input'] ,x.isspace() ))
print('{}É um número? {}{}'.format(cores['vermelho'] , cores['input'] , x.isalnum() ))
print('{}É alfabetico? {}{}'.format(cores['vermelho'] , cores['input'] ,  x.isalpha()))
print('{}É alfanumerico? {}{}'.format(cores['vermelho'] , cores['input'] , x.isalnum()))
print('{}Está em maiusculas? {}{}'.format(cores['vermelho'] , cores['input'] , x.isupper()))
print('{}Está em minusculas? {}{}'.format(cores['vermelho'] , cores['input'] ,x.islower()))
print('{}Está captalizado? {}{}'.format(cores['vermelho'] , cores['input'] , x.istitle()))