#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
""""soma = []
for n in range(1,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 1:
        soma.append(numero)

print(sum(soma))"""


#ou também

soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor'.format(c)))
    soma += num
    cont += 1
print('você informou {} números e a soma foi {}'.format(cont,soma))   