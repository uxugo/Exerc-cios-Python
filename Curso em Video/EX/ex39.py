from  datetime import date

ano_atual = date.today().year

ano_nasceu = int(input('Ano de nascimento: '))
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nasceu,ano_atual - ano_nasceu,ano_atual))

idade = ano_atual - ano_nasceu

if idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
    print('Seu alistamento foi em {}.'.format(ano_nasceu+18))
elif idade < 18:
    print('Você deverá se alistar em {} anos.'.format(18-idade))
    print('Seu alistamento será em {}.'.format(ano_nasceu+18))
elif idade == 18:
    x = input('É esse ano! Você já se alistou? s/n ')
    resposta = x.lower()
    if resposta == 's':
        print('Perfeito, Aguarde o responsavel da junta militar.')
    elif resposta == 'n':
        print('O que esta perdendo? corra atrás!')
    else:
        print('Error 404!')
else:
    print('Error 102!')