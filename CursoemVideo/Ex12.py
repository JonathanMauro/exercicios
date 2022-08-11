#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o preço do produto? R$ '))

desconto = produto - (produto * 5 / 100)

print('O produto que custava R${}, na promoção, vai custar R${}'.format(produto,desconto))