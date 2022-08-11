#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
numero = int(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raizQuadrada =  math.sqrt(numero)


print("O dobro de {} vale {}.".format(numero, dobro))
print("O triplo de {} vale {}.".format(numero, triplo))
print("A raiz Quadrada de {} equivale a {}".format(numero, raizQuadrada))