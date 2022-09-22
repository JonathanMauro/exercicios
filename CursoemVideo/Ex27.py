#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()

separa = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} e o sobrenome é {}'.format(separa[0],separa[-1]))

### OU

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))




