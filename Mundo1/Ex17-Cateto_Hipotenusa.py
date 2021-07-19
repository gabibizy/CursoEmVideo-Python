# 17 - Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa
from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')

