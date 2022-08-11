#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Uma distância em metros: '))

centimetros = metros * 100
milimetros = metros * 1000
print('A medida de {} metros, corresponde a {} cm e {} mm\n'.format(metros, centimetros, milimetros))