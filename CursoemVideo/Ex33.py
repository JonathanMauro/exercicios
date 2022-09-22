#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Teceiro valor: '))
#verificando o menor valor
if primeiro<segundo and primeiro<terceiro:
    menor = primeiro
if segundo< primeiro and segundo <terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
    
print('O menor valor digitado foi {}'.format(menor))
#verificando o maior valor
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print('O maior valor digitado foi {}'.format(maior))

    
    