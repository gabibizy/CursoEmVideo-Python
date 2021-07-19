# 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar; - Se é a hora de se alistar; - Se já passou do tempo do alistamento.
# Seu programa também deve mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nasc = int(input('Digite o ano de nascimento: '))
idade =  date.today().year - ano_nasc
if idade < 18:
    falta = 18 - idade
    print(f'Você tem {idade} anos. Ainda faltam {falta} anos para você se alistar.')
elif idade == 18:
    print(f'Você tem {idade} anos. É o momento de se alistar!')
elif idade > 18:
    passou = idade - 18
    print(f'Você tem {idade} anos. Já passaram {passou} anos do seu período de alistamento.')

