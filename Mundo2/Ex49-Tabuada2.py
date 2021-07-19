# 49 - Refaça o desafio 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando o laço for
n1 = int(input('Digite um número para ver a sua tabuada: '))
for i in range (1, 11):
    print(f'{n1} x {i:2} = {n1*i}')
