# 33 - Leia três números e mostre qual é o maior e qual é o menor

numeros = [ ]
for c in range(0,3):
    num = float(input('Digite um número: '))
    numeros.append(num)
print(f'O maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')

'''
# OU

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
maior = n1
if n2 > maior:
        maior = n2
if n3 >maior:
        maior = n3
print('Maior: ',maior)

# Menor número
menor = n1
if n2 < menor:
        menor = n2
if n3 < menor:
        menor = n3
print('Menor: ', menor)

'''