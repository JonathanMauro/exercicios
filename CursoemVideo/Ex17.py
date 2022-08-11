#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

catOposto = float(input('Insira o tamanho do cateto oposto: '))
catAdjacente = float(input('Insira o tamanho do cateto adjacente: '))

hipotenusa = math.hypot(catAdjacente, catOposto)

print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))