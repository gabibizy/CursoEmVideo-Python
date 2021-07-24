# 83 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
#se a expressão passada está com parênteses abertos e fechados na ordem correta.

exp = str(input("Digite uma expressão:"))
pilha = 0
for cont in exp:
    if cont == "(":
        pilha += 1
    if cont == ")":
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0:
    print('Expressão correta')
else:
    print('Expressão incorreta')

'''

# Solução do Prof Guanabara:
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão esta válida')
else:
    print('Sua expressão esta inválida')

'''
