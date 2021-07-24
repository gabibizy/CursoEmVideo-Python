# 81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números 
# foram digitados; B)A lista de valores, ordenada de forma decrescente; C) Se o valor 5 foi digitado e está ou não na lista
n = []
while True:
    n.append(int(input('Digite um número: ')))
    r = input('Deseja continuar? [S/N]: ')
    if r in 'Nn':
        break
    elif r not in 'SsNn':
        r = input('Comando inválido, tente novamente. Deseja continuar? [S/N]: ')
print('-='*30)
print (f'Foram digitados {len(n)} números')
n.sort(reverse=True)
print(n)
if 5 in n:
    print(f'O valor 5 se encontra na {n.index(5)+1}° posição')
else:
    print('O valor 5 não foi digitado')
