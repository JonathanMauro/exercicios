#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = int(input('Qual a distância da sua viagem? '))

if(distancia <= 200):
    valor = distancia * 0.50
    print('Você está prestes a começar a uma viagem de {}Km'.format(distancia))
    print('E o preço da sua passagem será de R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('Você está prestes a começar a uma viagem de {}Km'.format(distancia))
    print('E o preço da sua passagem será de R${:.2f}'.format(valor))
    