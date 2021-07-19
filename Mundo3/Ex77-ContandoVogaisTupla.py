# 77 - Crie um programa que tenha uma tupla com várias palavras (não vale usar acentos). Depois disso, você
# deve mostrar, para cada palavra quais são as suas vogais.
palavras = ('Computador','Mesa', 'Cadeira','Iphone')
for p in palavras:
    print(f'\nAs vogais de {p.upper()} são: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
