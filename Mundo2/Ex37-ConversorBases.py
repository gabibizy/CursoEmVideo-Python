# 37 - Leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
# 1 para binário; 2 para octal; 3 para hexadecimal;
n1 = int(input('Digite um número: '))
base = int(input('''Qual base de conversão você deseja utilizar? Digite o número da opção desejada:
[1] - Binário
[2] - Octal
[3] - Hexadecimal
Sua opção: '''))
if base == 1:
    print (f'{n1} convertido para BINÁRIO é igual a {bin(n1)[2:]}')
elif base == 2:
    print (f'{n1} convertido para OCTAL é igual a {oct(n1)[2:]}')
elif base == 3:
    print (f'{n1} convertido para HEXADECIMAL é igual a {hex(n1)[2:]}')
else:
    print('Opção inválida, tente novamente')
