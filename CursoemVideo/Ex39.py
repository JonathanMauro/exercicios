#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Qual o ano de seu nascimento? '))
atual = date.today().year 
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))

if idade == 18:
    print('Você precisa se alistar Imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} para o seu alistamento.'.format(saldo))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano + 18))
      