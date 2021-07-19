# 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint 
n1 = (randint(0,5))
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
n2 = int(input('Em que número eu pensei?: '))
while n1 != n2:
        print('Poxa, não foi desta vez, tente novamente')
        n2 = int(input('Digite um número de 0 a 5: '))

print(f'Parabéns! Você acertou, o número era {n1}')
