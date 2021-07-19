# 09 - Tabuada

n1 = int(input('Digite um número para ver a sua tabuada: '))
print('-'*11)
i = 0
while i < 10:
    i = i + 1
    resultado  = n1 * i
    print(f'{n1} x {i} = {resultado}')
print('-'*11)
