# 95 - Aprimore o desafio 93 para que ele funcioe com vários jogadores, incluido um sistema de visualização de detalhes
# do aproveitamento de cada jogador.
jogador = {}
aproveitamento=[]
lista_jogadores=[]
while True:
    print('-'*40)
    jogador['Nome']= str(input('Nome: '))
    jogador['Partidas']=int(input('Quantidade de partidas: '))
    for c in range(1, jogador['Partidas']+1):
        aproveitamento.append(int(input(f'Quantidade de gols na {c}° partida: ')))
    jogador['Gols'] = aproveitamento[:]
    jogador['Total_gols']= sum(aproveitamento)
    aproveitamento.clear()
    lista_jogadores.append(jogador.copy())
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp not in 'SsNn':
        resp = str(input('Comando inválido. Deseja continuar? [S/N]: '))
    elif resp in 'Nn':
        break
print('-='*50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for k, v in enumerate(lista_jogadores):
    print(f'{k:>3} ', end='')
    for j in v.values():
        print(f'{str(j):<15}', end='')
    print()
print('-='*50)
while True:
    resp = int(input('Digite o número do aluno para verificar as notas dele (999 interrompe): '))
    if resp == 999:
        break
    if resp > len(lista_jogadores):
            print('Erro! Não existe jogador com este código. Tente novamente')
    else:
        print('-'*50)
        print(f'O jogador {lista_jogadores[resp]["Nome"]} jogou {lista_jogadores[resp]["Partidas"]} partidas.')
        for i, g in enumerate(lista_jogadores[resp]["Gols"]):
            print(f'    => Na partida {i+1}, fez {g} gols.')
        print(f'Foi um total de {lista_jogadores[resp]["Total_gols"]} gols.')
