'''
Variáveis compostas: Tuplas, listas e dicionarios

Tuplas = As Tuplas são IMUTÁVEIS (não tem como mudar ela após definida)
Elas aceitam tipos diferentes de variáveis juntas em uma mesma tupla.

Tula = () parece que a partir do python 3.5 não precisa nem colocar mais dentro disso
Lista = []
Dicionário = {}

Comando SORTED organiza em ordem alfabética

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))
for comida in lanche:
    print (f'Eu comi {comida}')
print ('Comi pra caramba')

for cont in range(0, len(lanche)):
    print (f'Eu comi {lanche[cont]}')
print ('Comi pra caramba')


Aula de LISTAS []
Listas são mutáveis
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

Para mudar o item de uma lista:
lanche[3]='picolé'

Adicionar elemento no final da lista:
lanche.append['cookie']

Adicionar elemento em um lugar específico da lista:
lanche.insert[0, 'cachorro quente']

Apagar um item da lista e reposiciona a contagem dos ínidices
del lanche [3]
lanche.pop[3]  ------lanche.pop[] remove o ultimo elemento-----Geralmente o pop é pra eliminar o ultimo elemento mas tbm da pra escolher qual apagar
lanche.remove['pizza'] -------Com o remove vc escolhe pelo valor do item o que vc quer apagar, não pela posição

Verificar se a pizza esta no lanche para apagar
if 'pizza' in lanche:
    lanche.remove['pizza']

Criar uma lista atraves de ranges:
valores = list[range[4, 11]]

OBS: Enumerate mostra a posição e o valor dela.
Exemplos da aula:
#--------------------------------------------
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2,2)
if 4 in num:
    num.remove(4) # Procura a partir do início da lista o número que vc quer eliminar e elimina o primeiro deste numero.
else:
    print('Não achei o número 4')
num.sort()
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos')

#------------------------------------------
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# ------------------------------

# Criar uma ligação entre as listas (se uma mudar as duas mudam)
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# ------------------------------

#Criar uma cópia da lista (se uma mudar a outra não muda)
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# ------------------------------


# AULA 18 - Variáveis Compostas

dados = []
dados.append('Pedro')
dados.append(25)
pessoa = []
pessoa.append(dados[:])
print(pessoa)

# ------------------------------

pessoa = [['Pedro', 25], ['Maria', 19], ['João, 32']]
print(pessoa)
# ------------------------------

pessoa = [['Pedro', 25], ['Maria', 19], ['João, 32']]
print(pessoa[0][0]) #print: Pedro
print (pessoa[1]) # Maria 19

# ------------------------------
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #[:] Fazendo uma cópia da lista
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
# ------------------------------

galera = [['João', 19], ['Ana ', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade')

# ------------------------------
galera = list()
dado = list ()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
# print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} pessoas maiores de idade e {totmen} menores de idade')

# ------------------------------

Aula 19 - Dicionários em Python





'''
