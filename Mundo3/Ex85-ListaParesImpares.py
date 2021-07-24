# 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
#separados os valores pares e impares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
num = 0
for c in range(1,8):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Os números pares foram: {sorted(lista[0])}')
print(f'Os números impares foram: {sorted(lista[1])}')

#Uma única lista com duas listas dentro, uma de pares e outra de impares