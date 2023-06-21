print('='*10+' LOJAS VICTOR '+'='*10)
valor = float(input('Qual o valor das compras? R$'))
print('FORMAS DE PAGAMENTO')

escolha = int(input('''[ 1 ] á vista dinheiro/pix
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é na opção? '''))

if escolha == 1:
    custo = (valor / 100) * 90
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor , custo))
elif escolha == 2:
    custo = (valor / 100) * 95
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor , custo))
elif escolha == 3:
    print('Sua compra deu o valor total de R${:.2f}.'.format(valor))
elif escolha == 4:
    parcelas = int(input('Em quantas parcelas? '))
    custo = (valor / 100) * 120
    valor_parcela = custo / parcelas
    print('O valor de cada parcela será de {:.2f} em {} meses.'.format(valor_parcela,parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor , custo))