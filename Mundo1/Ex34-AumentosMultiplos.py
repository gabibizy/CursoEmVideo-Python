# 34 - Pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00,
#calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o salário: R$'))
if salario > 1250:
        aumento = (salario * 10 / 100) + salario
        print(f'O salário que era R${salario:.2f} com aumento de 10% ficou R${aumento:.2f} ')
else:
        aumento = (salario * 15 / 100) + salario
        print(f'O salário que era R${salario:.2f} com aumento de 15% ficou R${aumento:.2f} ')

