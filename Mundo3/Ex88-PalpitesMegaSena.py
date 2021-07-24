# 88 - Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Resolução mais simples que estava nos comentários do vídeo: (aparentemente o sample não repete números)
from random import sample
print ('-='*20)
print('         Palpites Mega Sena       ')
print ('-='*20)
qnt = int(input('Quantos jogos deseja sortear? '))
print ('-='*5,f'Sorteando {qnt} jogos','-='*6)
nums = [sample(range(1,61), k=6) for x in range(0,qnt)]
for i in range(0,qnt):
    print(f'Jogo {i+1}: {sorted(nums)[i]}')

'''
from random import randint
lista= []
jogo = []
tot = 1
print ('-='*20)
print('         Palpites Mega Sena       ')
print ('-='*20)
quant = int(input('Quantos jogos deseja sortear? '))
print ('-='*5,f'Sorteando {quant} jogos','-='*6)
while tot <= quant:
    cont=0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    jogo.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {sorted(l)}')
'''