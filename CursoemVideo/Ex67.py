#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    for i in range(1,11):
        resultado = numero * i 
        print('{} x {} = {}'.format(numero, i , resultado))
    
print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')