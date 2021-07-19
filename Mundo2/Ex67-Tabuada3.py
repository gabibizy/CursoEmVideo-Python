
# 67 - Mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
from time import sleep
n1 = tabuada = 0
while True:
    c = 1
    print('-'*50)
    n1 = int(input('Digite o número que deseja ver a tabuada:(Digite um numero negativo para sair): '))
    if n1 < 0:
        print('Finalizando programa...')
        sleep(1)
        break
    while c < 11:
        tabuada = n1 * c
        print(f'{n1} x {c} = {tabuada} ')
        c += 1
print('Fim.')
   