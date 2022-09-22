#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('''[1] para converter para Binário 
[2] para converter para Octadecimal 
[3] para converter para Hexadecimal''')
opcao= (int(input('Escolha uma base para conversão: ')))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero,bin(numero)))
    
elif opcao == 2:
    print('{} convertido para OCTADECimal é igual a {}'.format(numero,oct(numero)))
elif opcao == 3:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero,hex(numero)))
else: 
    print('Opção não é válida! Tente novamente.')
    
    

