#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
Palavra = input("Digite algo:")
primitivo = type(Palavra)
print("O tipo primitivo é: ",primitivo)

print("Só tem espaços??", Palavra.isspace())

print(" é um número? ",Palavra.isnumeric())

print(" é alfanumérico? ",Palavra.isalnum())

print(" está em maiúsculas? ", Palavra.isupper())

print(" está em minúsculas? ", Palavra.islower())

print("Está capitalizada? ", Palavra.istitle())