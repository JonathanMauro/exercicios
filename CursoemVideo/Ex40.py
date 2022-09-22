#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))

media = (primeira + segunda) / 2
print('Tirando {:.1f} e {:.1f}, a sua média foi {:.1f}'.format(primeira,segunda,media))

if media >= 5.0 and media <= 6.9:
    print('Você está de RECUPERAÇÃO!')
elif media >=7.0:
    print('Você está APROVADO!')
else:
    print('Você está REPROVADO!')