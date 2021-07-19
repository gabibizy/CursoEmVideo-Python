# 41 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua 
# categoria, de acordo com a idade: - Até 9 anos: Mirim; - Até 14 anos: Infantil; - Até 19 anos: Junior; 
# - Até 25 anos: Sênior; - Acima: Master
from datetime import date
ano_nasc = int(input('Digite o ano de nascimento: '))
idade =  date.today().year - ano_nasc
if idade <= 9:
    print(f'Idade: {idade} anos. Categoria: Mirim')
elif idade <=14:
    print(f'Idade: {idade} anos. Categoria: Infantil')
elif idade <= 19:
    print(f'Idade: {idade} anos. Categoria: Junior')
elif idade <= 25:
    print(f'Idade: {idade} anos. Categoria: Sênior')
else:
    print(f'Idade: {idade} anos. Categoria: Master')

