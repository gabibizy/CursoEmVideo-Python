# 60 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120

n1 = int(input('Digite um número: '))
print('-'*30)
c = n1
f = 1 
print(f'Calculando o fatorial de {n1}...')
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c> 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)