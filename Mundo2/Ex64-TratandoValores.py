# 64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
# digitados e qual foi a soma entre eles (desconsiderando o flag 999)
n1 = 0
c = 0
soma= 0
while n1 != 999:
    soma += n1
    n1 = int(input('Digite um número: (999 para Parar) '))
    c += 1
print(f'Foram digitados {c-1} números e a soma entre eles é {soma}')
