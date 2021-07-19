"""
# ao invés de else if em python é elif
nome = str(input('Qual é o seu nome? '))
if nome == 'Gabriela' or nome ==  'Gabi':
    print('Que nome bonito!')
elif nome == 'José' or nome == 'Maria' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Julia Cláudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))


"""

