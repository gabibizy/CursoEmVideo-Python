
# 56 - Leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo; - Qual é o nome do homem mais velho; - Quantas mulheres tem menos de 20 anos.
menor = 0
media = 0
maior = 0
nome_idade = 0
for c in range (0,4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: '))
    media += idade
    if idade > maior and sexo in 'Mm':
        maior = idade
        nome_idade = nome
    if sexo in 'Ff' and idade < 20:
        menor += 1
print(f'A média de idade do grupo é {media/4}')
print(f'O homem mais velho é o {nome_idade}, ele tem {maior} anos')
print(f'{menor} mulheres tem menos de 20 anos')
