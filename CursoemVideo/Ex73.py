#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.


times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco','Chapecoense', 'Atlético', 'Botafogo', 'Atlético - PR', 'Bahia', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO' )

print('-='*15)
print(f'Lista de times do Brasileirão:  {times}')
print('-='*15)
print(f'Os primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-='*15)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-='*15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição.')