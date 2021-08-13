# 99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*param):
    print('Analisando os valores passados...')
    if len(param) == 0 :
        print(f'Foram informados {len(param)} valores ao todo.\nO maior valor informado foi 0')
        print('-='*30)
    else:
        print(f'{param} Foram informados {len(param)} valores ao todo.\nO maior valor informado foi {max(param)}')
        print('-='*30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
