# 71 - Simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from random import choice
print('-='*11)
print('BANCO CEV')
print('-='*11)
saque = int(input('Qual o valor a ser sacado? R$'))
cédula = 50
total = saque
totcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totcéd = 0
        if total == 0:
            break
print('-='*11)
print('Volte sempre ao BANCO CEV')
 
