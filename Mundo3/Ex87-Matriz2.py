# 87 - Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna. C) O maior valor de segunda linha.
matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {[l,c]}: '))
        
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l] [c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
for l in range (0,3):
    soma += matriz[l][2]
for c in range (0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma de todos os valores pares digitados: {pares}')
print(f'A soma dos valores da terceira coluna: {soma}')
print(f'O maior valor de segunda linha é: {maior}')