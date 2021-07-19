
# 54 - Leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano_nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores')

