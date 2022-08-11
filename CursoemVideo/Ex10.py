#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Quanto dinheiro você possui na carteira? R$'))

dollar = reais / 3.27

print('Com R${:.2f} você pode comprar US${:.2f}'.format(reais,dollar))