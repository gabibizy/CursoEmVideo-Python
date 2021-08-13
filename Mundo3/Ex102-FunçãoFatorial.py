# 102 - Crie um programa que tenha uma função fatorial() que receba dois parãmetros: o primeiro que indique o número a 
# calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o 
# processo de cálculo fatorial
from math import factorial
def fatorial (n1, show=False):
    """
    ->  Calcula o fatorial de um número.
    :param n1: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.

    """
    print(f'Calculando o fatorial de {n1}...')
    if show == True:
        c = n1
        f = 1 
        while c > 0:
            print(f'{c}', end=' ')
            print('x' if c> 1 else '=', end=' ')
            f *= c
            c -= 1
        return(f)
    else:
        return(factorial(n1))
        

n1 = (int(input('Digite um número: ')))
print(fatorial(n1, show=True))