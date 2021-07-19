# 45 - Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
n1 = randint(0,2)
n2 = int(input('''Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura
Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
if n2 > 2:
    print('-='*11)
    print('JOGADA INVÁLIDA. Digite um número de 0 a 2')
    print('-='*11)

elif n1 == 0 and n2 == 0 or  n1 == 1 and n2 == 1 or n1 == 2 and n2 == 2:
        print('-='*11)
        print(f'''
        O Computador jogou {itens[n1]}
        O Jogador jogou {itens[n2]}
        NINGUÉM VENCE
        ''')
        print('-='*11)

elif n1 == 1 and n2 == 0:
    print('-='*11)
    print(f'''
        O Computador jogou {itens[n1]}
        O Jogador jogou {itens[n2]}
        COMPUTADOR VENCE
        ''')
    print('-='*11)

elif n1 == 0 and n2 == 2:
    print('-='*11)
    print(f'''
        O Computador jogou {itens[n1]}
        O Jogador jogou {itens[n2]}
        COMPUTADOR VENCE
        ''')
    print('-='*11)

elif n1 == 2 and n2 == 1:
    print('-='*11)
    print(f'''
        O Computador jogou {itens[n1]}
        O Jogador jogou {itens[n2]}
        COMPUTADOR VENCE
        ''')
    print('-='*11)

else:
    print('-='*11)
    print(f'''
        O Computador jogou {itens[n1]}
        O Jogador jogou {itens[n2]}
        JOGADOR VENCE
        ''')
    print('-='*11)
