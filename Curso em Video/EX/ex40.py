nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda a nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    resultado = 'APROVADO'
elif 7 > media >= 5:
    resultado = 'RECUPERAÇÃO'
else:
    resultado = 'REPROVADO'
print('A media entre {} e {} é: {}! {}'.format(nota1 , nota2 , media , resultado))