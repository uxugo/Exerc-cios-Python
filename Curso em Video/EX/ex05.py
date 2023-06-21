# faça um programa 
#que leia um número inteiro 
#e mostre na tela o sucessor 
#3 seu antecessor.#

n = int(input('\033[35mDigite um número: '))
suc = n+1
ant = n-1
print('O sucessor do numero {} é: {}. E seu antessesor é: {}\033[m'.format(n,suc,ant))