# 66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
# digitados e qual foi a soma entre eles (desconsiderando o flag 999)
n1 = c = soma = 0
while True:
    
    n1 = int(input('Digite um número:(999 para Parar) '))
    if n1 == 999:
        break
    soma += n1
    c += 1
print('-'*50)
print(f'Foram digitados {c} números e a soma entre eles é {soma}')
print('-'*50)
