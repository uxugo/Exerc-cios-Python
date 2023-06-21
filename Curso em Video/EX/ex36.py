valor_casa = float(input('Digite aqui o valor da casa: '))
salario = float(input('Digite aqui o seu salário: R$'))
anos = int(input('Digite aqui em quantos anos quer pagar: '))

valor_mensal = valor_casa / (anos * 12) 
condicao = (valor_mensal * 100) / salario

print('Para pagar uma casa de RS{:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor_casa , anos , valor_mensal))

if condicao >= 30:
    print('Não podemos consceder o emprestimo')
else:
    print('Emprestimo aprovado com sucesso')