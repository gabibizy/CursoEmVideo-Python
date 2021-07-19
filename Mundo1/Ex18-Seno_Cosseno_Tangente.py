# 18 - Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo
from math import sin, cos, tan, radians
a = float(input('Digite o valor de um ângulo: '))
print(f"Seno: {sin(radians(a)):.2f}")
print(f"Cosseno: {cos(radians(a)):.2f}")
print(f"Tangente: {tan(radians(a)):.2f}")