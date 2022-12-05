"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
print()
print('''[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')
print()
option = int(input('Opção: '))

if option == 1:
    resultado = primeiro + segundo
    print('A soma entre {} + {} é {}'.format(primeiro, segundo, resultado))
elif option == 2:
    resultado = primeiro * segundo
    print('A multiplicação entre {} * {} é {}'.format(primeiro, segundo, resultado))
elif option == 3:
    if primeiro > segundo:
        print('O número {} é maior que {}'.format(primeiro, segundo))
    else: 
        print('O número {} é maior que {}'.format(segundo, primeiro))
elif option == 4:
    print('Informe o número novamente: ')
    primeiro = int(input("Primeiro valor: "))
    segundo = int(input("Segundo valor: "))
    
elif option == 5:
    print('Finalizando...')
else:
    print('Opção inválida. Tente novamente')
print('Fim do programa! Volte sempre!')
    
    