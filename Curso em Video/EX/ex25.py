nome = str(input('Qual seu nome completo? '))

n = nome.lower()
x = n.find('silva')
print('Seu nome tem Silva?')
if x == -1:
    print('False')
else:
    print('True')