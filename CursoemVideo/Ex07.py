#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

primeiro = float(input('Digite a primeira nota: '))
segundo = float(input('Digite a segunta nota: '))

media = (primeiro + segundo) / 2

print('A média entra {}  e {} é igual a {}'.format(primeiro,segundo,media))