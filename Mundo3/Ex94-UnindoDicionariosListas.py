# 94 - Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) A média de idade do grupo
# C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.
pessoa = {}
lista_pessoas=[]
mulher = []
soma = média = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: '))
    if pessoa['Sexo'] not in 'FfMm':
        pessoa['Sexo'] = input('Comando inválido. Sexo [M/F]: ')
    if pessoa['Sexo'] in 'Ff':
        mulher.append(pessoa['Nome'])
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    lista_pessoas.append(pessoa.copy())
    resp = input('Deseja continuar? [S/N]: ')
    if resp not in 'SsNn':
        resp = input('Comando inválido. Deseja continuar? [S/N]: ')
    elif resp in 'Nn':
        break
print('-='*30)
média = soma / len(lista_pessoas)
print(f'- O grupo tem {len(lista_pessoas)} pessoas.\n- A média de idade é de {média:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulher}')
print('- Lista de pessoas acima da média de idade: ')
for p in lista_pessoas:
    if p['Idade'] > média:
        print (f'   Nome: {p["Nome"]}; Sexo: {p["Sexo"]}; Idade: {p["Idade"]}')
