# 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma 
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
def voto(ano_nasc):
    from datetime import date # Escopo de importação - Economiza memória. Importar a biblioteca só dentro da função pq ela não é utilizada no resto do programa. 
    idade = date.today().year - ano_nasc 
    if idade >=16 and idade <18 or idade >=65 :
        return(f'{idade} anos: VOTO OPCIONAL')
    if idade >= 18:
        return(f'{idade} anos: VOTO OBRIGATÓRIO')
    if idade < 16:
        return(f'{idade} anos: VOTO NEGADO')

ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))
