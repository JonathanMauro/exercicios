#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Insira um número para saber a tabuada dele: '))

for i in range(0,10):
    
    print('{} x {} = {}'.format(i, numero,i * numero))