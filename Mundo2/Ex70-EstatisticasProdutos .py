# 70 - Leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostrar: - Qual é o total gasto na compra; - Quantos produtos custam mais de R$1.000; 
# Qual é o nome do produto mais barato.
mais_qmil = total = barato = cont = 0
nome_barato = ''
print('-='*11)
print('BEM VINDO A LOJA')
print('-='*11)
resposta = 's'
while resposta in 'Ss':
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    total += preço
    cont += 1
    resposta = str(input('Deseja continuar? [S/N]: ')) 
    if preço > 1000:
        mais_qmil += 1
    if  cont == 1:
        barato = preço
        nome_barato = nome
    else:
        if preço < barato:
            barato = preço
    if resposta in 'Nn':
        break

print(f'Total gasto na compra: R${total}')
print(f'{mais_qmil} produtos custaram mais do que R$1.000')
print(f'O produto mais barato foi o {nome_barato} que saiu por R${barato}')
