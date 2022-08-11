#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
numero  = float(input('Digite um valor: '))

inteiro = int(numero)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero,inteiro ))

###Ou pode ser feito com 

print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero,math.trunc(numero) ))