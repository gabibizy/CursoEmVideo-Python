# 72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extensão, de zero até vinte. Seu programa deversá ler um número entre 0 e 20 e mostrá-lo por extenso.
from random import choice
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = int(input('Digite um número de 0 a 20: '))
while n1 > 20 or n1 < 0:
    n1 = int(input('Tente novamente. Digite um número de 0 a 20: '))
print (numeros[n1])
