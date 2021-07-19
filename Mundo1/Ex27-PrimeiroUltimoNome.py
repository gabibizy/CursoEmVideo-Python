# 27 - Leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza primeiro: Ana ultimo: Souza
nome = (input('Digite o nome completo: ')) 
dividido = nome.split()
print('Primeiro nome: {}'.format(dividido[0]))
print('Último nome: {}'.format(dividido[-1]))
