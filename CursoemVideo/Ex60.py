#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

#5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial

numero = int(input("Digite um número para calcular o seu fatorial: "))
#fato = factorial(numero)
c =  numero
f = 1
print('Calculando {}! = '.format(numero), end = '')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))
#print('O fatorial de {} é {}'.format(numero, fato))