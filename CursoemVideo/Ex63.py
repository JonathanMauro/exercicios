#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

#0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print('{}'.format(termo), end=' → ')
print('FIM!')