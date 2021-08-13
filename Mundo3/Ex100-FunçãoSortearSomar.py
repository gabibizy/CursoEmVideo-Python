# 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira 
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os 
# valores Pares sorteados pela função anterior.
from random import randint
números=[]
par=[]
print('-='*40)
def sorteia (números):
    print('Sorteando 5 valores... ')
    while len(números) < 5:
        num = randint(0,10)
        if num % 2 == 0:
            par.append(num)
        números.append(num)
    print(números)

def somaPar():
    print('Somando todos os valores pares da lista... ')
    print(f'Resultado: {sum(par)}')


sorteia(números)
print('-'*40)
somaPar()
print('-'*40)
