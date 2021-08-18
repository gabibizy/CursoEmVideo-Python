# 113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[1;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return valor

def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro!\033[m')
        except(KeyboardInterrupt):
            print('\033[1;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return valor
        
i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {i} e o real foi {f}')