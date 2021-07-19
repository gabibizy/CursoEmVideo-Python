"""

--------------------------------------------------Anotações do Mundo 1---------------------------------------------------------


n1 = int(input('Primeiro número = '))
n2 = int(input('Segundo número = '))
soma = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2
potência = n1 ** n2
div_inteira = n1 // n2
resto = n1 % n2
print('{} + {} = {}'.format(n1, n2, soma))
print('{} - {} = {}'.format(n1, n2, subtração))
print('{} * {} = {}'.format(n1, n2, multiplicação))
print('{} / {} = {}'.format(n1, n2, divisão))
print('{} ** {} = {}'.format(n1, n2, potência))
print('{} // {} = {}'.format(n1, n2, div_inteira))
print('{} % {} = {}'.format(n1, n2, resto))

-------------------------------------------------------------------------------------------------------------------------

#ordem de precedência (), **, *, /, //, %, +. -

-------------------------------------------------------------------------------------------------------------------------
# CORES NO TERMINAL:

# Padrão ANSI :
# \033[style;text;back m
#códigos para:
# style 0 = none; 1 = bold; 4 = underline; 7 = negative
# text do 30 ao 37
# back do 40 ao 47
nome = input('Qual é o seu nome? ')
print(' \033[0;;45m Olá, {}!'.format( nome))

"""












