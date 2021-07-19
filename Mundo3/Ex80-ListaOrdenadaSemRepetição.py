# 80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição 
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
numeros = []
for c in range(0,5):
    valores = int(input('Digite um valor: '))
    if len(numeros) <= 0 or valores <= numeros[0]:
        numeros.insert(0, valores)
    elif len(numeros) <= 1 or valores <= numeros[1]:
        numeros.insert(1, valores)
    elif len(numeros) <= 2 or valores <= numeros[2]:
        numeros.insert(2, valores)
    elif len(numeros) <= 3 or valores <= numeros[3]:
        numeros.insert(3, valores)
    elif len(numeros) <= 4 or valores <= numeros[4]:
        numeros.insert(4, valores)
    else:
        numeros.insert(5, valores)

print(f'Você digitou os valores {numeros}')
'''
# Resolução do Prof°Guanabara:
lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print ('Adicionando ao final da lista..')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')

