# 91 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
jogador = {}
lista=[]
print('Tabela de valores:')
for c in range(1,5):
    sleep(1)
    jogador['posição']= int(c)
    jogador['num'] = randint(1,6)
    print(f'    Jogador {jogador["posição"]} tirou {jogador["num"]}')
    lista.append(jogador.copy())
print('-='*20)
print('Ranking dos jogadores:')
i=1
ordenar =  sorted(lista, key=lambda row:row['num'] , reverse=1 )
for j in ordenar:
    sleep(1)
    print(f'    {i}°lugar: Jogador {j["posição"]} com {j["num"]}')
    i+=1
    
