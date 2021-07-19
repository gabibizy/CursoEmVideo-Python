# 10 - Conversor de moedas
real = float(input('Quantidade de dinheiro: R$'))
dolares = real / 5.17
euro = real / 6.14
print(f'R${real:.2f} convertido em dólar fica US${dolares:.2f} e em euro fica EUR${euro:.2f}')
