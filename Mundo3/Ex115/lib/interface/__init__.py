# 115 - Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
# simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            print('valor = int(input(msg)) Vim aqui')
        except (ValueError, TypeError):
            print(f'\033[1;31mErro!\033[m')
            continue
        except KeyboardInterrupt:
            print('Sair')
            return 3
        else:
            print('retornei o valor')
            return valor



def linha(tam=42):
    return '-'* tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')    
        c += 1
    print(linha())
    op = leiaInt('Sua opção: ')
    return op

