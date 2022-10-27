#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
number = int(input('Numero: '))
ePrimo = 0

for i in range(1, (number + 1)):        
  if number % i == 0:
    ePrimo += 1
    
if ePrimo  == 2 :
  print('primo')
else:
  print('nao primo')