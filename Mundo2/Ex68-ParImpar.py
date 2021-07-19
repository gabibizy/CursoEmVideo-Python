# 68 - Jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder
# mostrando o total de vitórias cosnecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
print('-='*11)
print('Vamos jogar Par ou Ímpar')
print('-='*11)
while True:
    n1 = randint(0,10)
    n2 = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]'))
    resultado = n1 + n2 
    if escolha not in 'PpIi':
        print('Entrada inválida')
        break
    if resultado % 2 == 0 and escolha in 'Pp':
        print(f'Você jogou {n2} e o computador jogou {n1}. {n1} + {n2} = {resultado}. O número é PAR')
        print('-='*11)
        print('VOCÊ GANHOUU!')
        print('-='*11)
        vitorias += 1

    elif resultado % 2 != 0 and escolha in 'Ii':
        print(f'Você jogou {n2} e o computador jogou {n1}. {n1} + {n2} = {resultado}. O número é ÍMPAR')
        print('-='*11)
        print('VOCÊ GANHOUU!')
        print('-='*11)
        vitorias += 1

    elif resultado % 2 == 0:
        print(f'Você jogou {n2} e o computador jogou {n1}. {n1} + {n2} = {resultado}. O número é PAR')
        print('-='*11)
        print('O computador ganhou')
        print('-='*11)
        break
    elif resultado % 2 != 0:
        print(f'Você jogou {n2} e o computador jogou {n1}. {n1} + {n2} = {resultado}. O número é ÍMPAR')
        print('-='*11)
        print('O computador ganhou')
        print('-='*11)
        break
print(f'GAME OVER! Foram {vitorias} vitorias do jogador')
