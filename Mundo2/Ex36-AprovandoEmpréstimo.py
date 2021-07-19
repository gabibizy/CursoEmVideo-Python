# 36 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos você deseja pagar? '))
prestação = valor_casa / (anos * 12)
poder_compra = salario * 30 / 100
if prestação > poder_compra:
    print(f'Poxa, infelizmente não foi aprovado pois o valor da prestação que ficaria em R${prestação:.2f} e isto excede 30% do seu salário ')
else:
    print(f'Parabéns você foi aprovado e o valor da prestação será de R${prestação:.2f}')
