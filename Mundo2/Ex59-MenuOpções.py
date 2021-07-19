# 59 - Crie um programa que leia dois valores e mostre um menu na tela: Somar, Multiplicar, maior, novos números,
# sair do programa. E realize a operação solicitada em cada caso
from time import sleep
opt = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while opt != 5 or opt == 4:
    opt = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa

    Digite uma opção: '''))
    if opt == 1:
        print(f'A soma do números é {n1 + n2}')
    elif opt == 2:
        print(f'A soma do números é {n1 * n2}')
    elif opt == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        else:
            print (f'O maior número é o {n2}')
    elif opt == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))  
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção inválida tente novamente')
sleep(1)
print('Fim do programa, volte sempre!')
