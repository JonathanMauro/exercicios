#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

imovel = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = float(input('Quantos anos de financiamento: '))
parcela = imovel / anos
minimo = salario * 30 / 100
print('Para pagar uma casa de R${} em {} anos a prestação será de R${}.'.format(imovel, anos, parcela ))

if parcela <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NÃO CONCEDIDO')    
    
    
    
