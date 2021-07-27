# 93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
# guardado um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
aproveitamento=[]
jogador['Nome']= str(input('Nome: '))
jogador['Partidas']=int(input('Quantidade de partidas: '))
for c in range(1, jogador['Partidas']+1):
    aproveitamento.append(int(input(f'Quantidade de gols na {c}° partida: ')))
jogador['Gols'] = aproveitamento
jogador['Total_gols']= sum(aproveitamento)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print (f'{k}: {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i, p in enumerate(aproveitamento):
    print(f'    => Na partida {i+1}, fez {p} gols.')
print(f'Foi um total de {jogador["Total_gols"]} gols.')