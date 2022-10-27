#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0,10)
print('-=-' * 15)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 15)
acertou = False
palpites = 0
while not acertou:
    numero = int(input('Qual é o seu palpite? '))
    palpites +=1
    if numero == computador :
        acertou = True
        print('Parabéns! Você acertou!! O número escolhido foi {}!'.format(computador))
    else: 
        if numero < computador:
            print('Mais... Tente mais uma vez.')
        elif numero < computador:
            print('Menos... Tente mais uma vez.') 
print('Acertou com {} tentativas. Parabéns!'.format(palpites))