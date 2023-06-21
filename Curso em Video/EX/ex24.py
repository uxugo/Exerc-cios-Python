city = str(input('Em qual cidade você nasceu? '))

cidade = city.lower()
x = cidade.find('barreiras')

if x == -1:
    print('False')
else:
    print('True')