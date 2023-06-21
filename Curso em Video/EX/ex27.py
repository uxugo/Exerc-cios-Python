nome = str(input('Digite seu nome: ')).strip()
primeiro_nome = nome.find(' ')
ultimo_nome = nome.rfind(' ') + 1
print('Seu primeiro nome é {}.'.format(nome[:primeiro_nome]))
print('Seu último nome é {}.'.format(nome[ultimo_nome:]))