# 82 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que 
#vão conter apenas os valores pares e os ímpares digitados, respectivamente. Ao final mostre o conteúdo das três listas
#geradas
n = []
p = []
i = []
while True:
    num = int(input('Digite um número: '))
    n.append(num)
    if num % 2 == 0:
        p.append(num)
    else:
        i.append(num)
    r = input('Deseja continuar? [S/N]: ')
    if r in 'Nn':
        break
    elif r not in 'SsNn':
        r = input('Comando inválido, tente novamente. Deseja continuar? [S/N]: ')
print(f'Lista: {n}')
print(f'Lista Pares: {p}')
print(f'Lista Ímpares: {i}')
