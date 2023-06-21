valor = float(input('Quanto custa esse produto? R$'))

desconto = valor-((valor/100)*5)

print('O produto que custava R${:.2f}, com 5% de \ndesconto custará R${:.2f}'.format(valor,desconto))