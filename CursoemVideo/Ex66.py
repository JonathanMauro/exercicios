#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = soma = 0
while True:
    valor = int(input('Digite um valor: (999 para parar)  '))
    if valor == 999:
        break
    soma = soma + valor
    cont += 1 
print('Você digitou {} números e a soma deles é {}'.format(cont - 1, soma - 999))
