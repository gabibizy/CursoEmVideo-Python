# 96 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura
# e comprimento) e mostre a área de terreno.
def área(largura, comprimento):
    tot = largura * comprimento
    print(f'A área de um terreno de {largura} x {comprimento} é de {tot}m²')


print(f' Controle de Terrenos')
print('-'*30)
área((float(input('Largura (m): '))), (float(input('Comprimento (m): '))))
