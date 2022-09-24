#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import  randint


itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,3)
print('Suas opções:')
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual a sua jogada? '))

print('O computador está escolhendo...')

print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogada]))
print('-=' * 11)

if computador == 0:
    if jogada == 0:
       print('EMPATE !!!! ')
    
    elif jogada == 1:
        print('O JOGADOR GANHOU!!!')
    elif jogada == 2:
        print('O COMPUTADOR GANHOU!!!')
    else:
        print('Jogada inválida! Tente novamente...')
elif computador == 1:
    if jogada == 0:
        print('O JOGADOR GANHOU!!!')
    elif jogada == 1:
        print('EMPATE !!!! ')
    elif jogada == 2:
        print('O COMPUTADOR GANHOU!!!')
        
    else:
          print('Jogada inválida! Tente novamente...')
elif computador == 2:
    if jogada == 0:
        print('O COMPUTADOR GANHOU!!!')
    elif jogada == 1:
        print('O JOGADOR GANHOU!!!')
    elif jogada == 2:
        print('EMPATE !!!! ')
    else:
          print('Jogada inválida! Tente novamente...')

