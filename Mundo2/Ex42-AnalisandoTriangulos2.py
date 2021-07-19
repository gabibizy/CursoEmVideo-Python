
# 42 - Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais; Escaleno: todos os lados diferentes; Isósceles: dois lados iguais;

a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print('Equilátero: todos os lados iguais')
        elif a != b != c != a:
            print ('Escaleno: todos os lados diferentes')
        else :
            print('Isósceles: dois lados iguais')
else:
        print ('Não pode ser um triangulo')

