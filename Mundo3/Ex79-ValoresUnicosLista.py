# 79 - Crie um programa onde o usuário possa digitar vários valores numéricos
#e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
resp= ''
while True:
    n1 = int(input('Digite um valor: '))
    if n1 in numeros:
        print('O número já esta na lista, este não irei acrescentar')
    else:
        numeros.append(n1)
    resp = input('Deseja continuar? [S/N]: ')
    if resp not in 'NnSs':
        print('Comando inválido. Tente novamente')
        resp = input('Deseja continuar? [S/N]: ')
    if resp in 'Nn':
        break
print(sorted(numeros))
print('Programa Finalizado')