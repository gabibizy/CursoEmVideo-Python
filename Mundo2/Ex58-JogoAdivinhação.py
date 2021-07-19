# 58 - Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.
import random
c = 0
n1 = (random.randint(0,10))
print('-'*50)
print('Pensei em um número entre 0 e 10. Tente adivinhar')
print('-'*50)
n2 = int(input('Digite um número de 0 a 10: '))
while n1 != n2:
        print('Poxa, não foi desta vez, tente novamente')
        n2 = int(input('Digite um número de 0 a 10: '))
        c += 1
print('-'*50)
print(f'Parabéns! Você acertou após {c} tentativas, o número era {n1}')
print('-'*50)
