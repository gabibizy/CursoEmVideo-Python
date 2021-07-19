# 65 - Leia vários números inteiros. No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n1 = 0
c = 0
soma= 0
numeros = []
sair = 's'
while sair in 'Ss':
    n1 = int(input('Digite um número: '))
    c += 1
    soma += n1
    numeros.append(n1)
    sair = str(input('Deseja continuar? [S/N]: '))
media = soma / c
print('-'*50)
print(f'A média dos números é {media}')
print(f'O maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')
print('-'*50)
