'''– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
from datetime import date

ano_nascimento = int(input('Digite aqui o ano que nasceu: '))

ano = date.today().year
idade = ano - ano_nascimento

if idade > 25:
    categoria = 'MASTER'
elif idade  <= 25 and idade < 19:
    categoria = 'SÊNIOR'
elif idade <= 19 and idade <9:
    categoria = 'JÚNIOR'
elif 9 > idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 9:
    categoria = 'MIRIM'

print('Sua idade é: {}'.format(idade))

print('Classificação: {}'.format(categoria))