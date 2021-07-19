# 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
posicao_maior = []
posicao_menor = []
for c in range(1,6):
    numeros.append(list(input('Digite um valor: ')))
for posicao, valores in enumerate(numeros):
    if valores == max(numeros):
        posicao_maior.append(posicao)
    if valores == min(numeros):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor da lista é {max(numeros)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(numeros)}, nas posições {posicao_menor}')
