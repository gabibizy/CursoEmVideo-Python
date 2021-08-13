# 98 - Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e realize
# a contagem. Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1.    b) De 10 até 0, de 2 em 2.      c) Uma contagem personalizada 
from time import sleep
def contador(inicio, fim, passo): 
    if passo <= -1:
        passo*= -1
    if passo == 0:
        passo = 1
    print('-'*40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
   
    if inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ', flush=True) 
            sleep(0.2)
    else:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ', flush=True) 
            sleep(0.2)
    print()


contador(1,10,1)
contador(10,0,2)
print('-'*40)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), (int(input('Fim: '))), (int(input('Passo: '))))