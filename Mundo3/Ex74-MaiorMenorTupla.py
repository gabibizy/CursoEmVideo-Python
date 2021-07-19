# 74 - Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = tuple(randint(i + 1, 100) for i in range(randint(1, 5)))
print(tupla)
print(f'O maior número da tupla é {max(tupla)}')
print(f'O menor número da tupla é {min(tupla)}')

'''
# Outra forma de fazer:
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')

'''
