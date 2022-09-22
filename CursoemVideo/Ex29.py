#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade <= 80:
    print("Parabéns! Você está dentro do limite de velocidade permitida.")
else:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    
    ultrapassou = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(ultrapassou))
print('Tenha um bom dia" Dirija com segurança!')
        
