# 61 - Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro_termo
c = 1
while c <= 10:
    print(termo, end=' ')
    termo += razão
    c+= 1
