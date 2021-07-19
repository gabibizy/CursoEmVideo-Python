
# 76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.
print('-='*20)
print(f'{"LOJINHA DA GABI":^40}')
print('-='*20)
produtos = ('Computador', 1200.00, 'Mesa', 249.90, 'Cadeira', 300.00, 'Iphone 11', 4200.00 )
for i in produtos:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('-='*20)

