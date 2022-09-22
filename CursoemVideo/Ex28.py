#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 15)
numero = int(input('Em que número eu pensei? '))

resultado = randint(0,5)
print('PROCESSANDO...')
sleep(3)

if resultado == numero:
    print('Parabéns! Você acertou!! O número escolhido foi {}!'.format(resultado))
else: 
    print('Você errou! Eu pensei no {} e não no {}!Tente novamente'.format(resultado, numero))
    