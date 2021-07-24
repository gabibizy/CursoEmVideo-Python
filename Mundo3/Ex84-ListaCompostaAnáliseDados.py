# 84 - Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas; B) Uma listagem com as pessoas mais pesadas; C) Uma listagem com as pessoas mais leves.
pesada = []
leve = []
dado = []
pesos = []
galera = []
while True:
    dado.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    pesos.append(peso)
    dado.append(peso)
    galera.append(dado[:])
    resp = input('Deseja continuar?[S/N]: ')
    if resp not in 'NnSs':
        resp = input('Comando inválido. Deseja continuar?[S/N]: ')
    if resp in 'Nn':
        break
    dado.clear()
print(f'Quantidade de pessoas cadastradas: {len(galera)}')  
for p in galera:
    if p[1] == max(pesos):
        pesada.append(p[0])
    elif p[1] == min(pesos):
        leve.append(p[0])
print(f'O maior peso da lista foi {max(pesos)}Kg, dos usuários {pesada}')
print(f'O menor peso da lista foi {min(pesos)}Kg, dos usuários {leve}')

