# 55 - Leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
pesos = [ ]
for p in range(0,5):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
print(f'O maior peso é {max(pesos)}Kg' )
print(f'O menor peso é {min(pesos)}Kg' )

