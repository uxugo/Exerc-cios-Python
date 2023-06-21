cores = {'input':'\033[0;4;34m',
         'verde':'\033[0;32m'}

nota_1 = float(input('{}Primeira nota do aluno: {}'.format(cores['verde'] , cores['input'])))
nota_2 = float(input('{}Segunda nota do aluno: {}'.format(cores['verde'] , cores['input'])))
media = (nota_1 + nota_2) / 2
print('{}A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(cores['verde'] , nota_1 , nota_2 , media))