# 52 - Leia um número inteiro e diga se ele é ou não um número primo.
n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        tot += 1
if tot == 2 :
    print(f'O número {n1} é primo')
else:
    print(f'O número {n1} não é primo')

