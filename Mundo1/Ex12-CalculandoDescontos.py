# 12 - Calculando desconto
preço = float(input('Preço do produto: R$'))
desconto = preço - (preço * 5 / 100) 
print(f'O valor do produto com desconto de 5% fica R${desconto:.2f}')

