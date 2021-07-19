# 15 - Aluguel de carros
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15) 
print(f'O valor total a pagar é de R${total:.2f}')
