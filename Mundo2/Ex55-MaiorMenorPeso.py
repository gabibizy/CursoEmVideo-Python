# 55 - Leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
pesos = [ ]
for p in range(0,5):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
print('O maior peso é {}Kg' .format(max(pesos)))
print('O menor peso é {}Kg' .format(min(pesos)))

