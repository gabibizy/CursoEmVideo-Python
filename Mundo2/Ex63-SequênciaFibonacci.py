# 63 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros 
# elementos de uma Sequência  de Fibonacci.
# ex: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,...

n1 = int(input('Quantos termos deseja apresentar? '))
t1 = 0
t2 = 1
print(t1, t2, end=' ')
c = 3
while c <= n1:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2 
    t2 = t3
    c += 1 
