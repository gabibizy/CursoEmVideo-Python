
def leiaDinheiro(p):
    valor = input(p).replace(',', '.')
    if valor.replace('.','',1).isdigit():
        return float (valor)
    else:
       return leiaDinheiro(f'\033[1;31mErro!\033[m Digite o preço: R$')

