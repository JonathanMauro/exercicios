#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0
valor = 0
cont = 0
while numero != 999:
    numero =  int(input('Digite um número: [999 para parar]  '))
    valor += numero 
    cont += 1    
print('Você digito {} números e a soma deles é {}'.format(cont - 1, valor - 999))
print('FIM!')