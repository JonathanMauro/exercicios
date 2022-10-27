#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

from asyncio.proactor_events import _ProactorReadPipeTransport
menor = 0
maior = 0

for c in range(1,6):
    peso  = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
      maior = c
      menor = c 
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))