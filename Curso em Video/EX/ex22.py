nome = str(input('Digite seu nome completo: '))

dividido = nome.split()
juntar_nome_completo = len(''.join(nome.split()))

print('''Olá {}, tudo bom?
Seu nome em maiusculo é: {}.
Seu nome em minusculo é: {}.
Seu nome tem {} letras.
Seu primeiro nome tem {} letras.'''.format(dividido[0],nome.upper(),nome.lower(),juntar_nome_completo,len(dividido[0])))