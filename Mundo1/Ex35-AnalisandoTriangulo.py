# 35 - Leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
if a < b + c and b < a + c and c < a + b:
        print ('Sim pode ser um triangulo')
else:
        print ('Não pode ser um triangulo')
