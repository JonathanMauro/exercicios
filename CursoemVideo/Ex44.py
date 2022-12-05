#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

preco = float(input('Preço da compra: '))
print('''FORMAS DE PAGAMENTO:
    [1] à vista dinheiro/cheque: 10% de desconto
    [2] à vista no cartão: 5% de desconto
    [3] em até 2x no cartão: preço formal 
    [4] 3x ou mais no cartão: 20% de juros''')
opcao = int(input(' Qual é a opção: '))
print('O preço da compra é de R${:.2f}'.format(preco))
if opcao == 1:
    valor = preco - (preco * 10 / 100)
    print('O valor para pagamento à vista dinheiro/cheque será R${:.2f}'.format(valor))
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
    print('O valor para pagamento à vista no cartão R${:.2f}'.format(valor))
elif opcao == 3:
    valor = preco
    parcela = valor / 2
    print('O valor para pagamento em até duas vezes no cartão é R${:.2f} ou duas parcelas iguais de R${:.2f}'.format(valor, parcela))
    
elif opcao == 4:
    totparcela = int(input('Em quantas parcelas? '))
    valor = preco + (preco * 20 / 100)
    parcela = valor / totparcela
    
    print('O valor para pagamento em 3x ou mais no cartão que é de R${:.2f}, ficará em {}x de R${:.2f} '.format(valor, totparcela, parcela))
    
else:
    valor = 0
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(preco, valor))
