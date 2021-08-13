# 104 - Crie um programa com uma função chamada leiaInt(), que vai funcionar de forma semelhante à função input() do 
# Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n=leiaInt('Digite um número: ')
def leiaInt(msg):
    valor = input(msg)
    if valor.isdecimal():
        return valor
    else:
        print(f'\033[1;31mErro! Digite um número inteiro:\033[m')
    
    return leiaInt(msg)


n = leiaInt('Digite um número: ')
print(f'\033[32mVocê acabou de digitar o número {n}.\033[0;0m')
