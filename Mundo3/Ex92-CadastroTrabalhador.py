# 92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
trabalhador={}
trabalhador['Nome']= str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = date.today().year - ano_nasc
trabalhador['CTPS'] = int(input('Número da Carteira de Trabalho (Digite 0 se não tiver): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Ano_contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] =  (trabalhador['Ano_contratação'] + 35) - date.today().year + trabalhador['Idade']
print('-='*40)
for k, v in trabalhador.items():
    print(f'{k}: {v}')