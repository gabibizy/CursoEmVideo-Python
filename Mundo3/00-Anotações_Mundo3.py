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
#Aula 19 - Dicionários em Python {}
#Estrutura de dados onde os ínidices podem ser literais (representados por texto).
# Os índices são chamados de chaves ou KEYS

# Valor = print(filme.values()) - Vai mostrar somente os valores ('Star Wars', 1977, 'George Lucas')
# Chave = print(filme.keys()) - Vai mostrar o nome de cada chave (titulo, ano diretor)
# Itens = print(filme.items()) - Vai mostrar os dois campos, key e valor.


dados = {} #ou dados = dict()
dados={'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

#Para adicionar elementos:
dados['sexo']='M'

print(dados['sexo'])
print(dados)
#Para remover um elemento
del dados['idade']
print(dados)

filme={'titulo': 'Star Wars',
       'ano': 1977,
       'diretor':'George Lucas'
}

for k, v in filme.items(): #ao invés do enumerate vc usa o items
    print(f'O {k} é {v}') # mostra o key e o valor de cada campo


pessoas={'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas ['nome'] = 'Leandro' # modificar o valor
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #Como a frase esta dentro de aspas simples o nome da key tem que estar entre aspas duplas
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


#Pode-se fazer uma lista e dentro dela colocar dicionários, como por exemplo:
brasil=[]
estado1={'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2={'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil) 
print(brasil[1]) 
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado={}
brasil=[]
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #método de cópia de um dicionário
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')


# ------------------------------
# Aula 20 - Funções (Parte 1) 
# Funções que já existem no Python: print() len() input() int() float()
# Exemplo: Tudo o que for uma rotina para vc no programa(repetitivo), vc pode criar uma função para que ela faça o comando sem você precisar digitar ele inteiro sempre
# Um exemplo são as linhas que fizemos para dividir a tela, vc pode criar uma função "mostrarlinha()" por exemplo, ao invés de sempre precisar digitar print('-='*30)

# Boas práticas: pular 2 linhas depois da declaração da função
# def = é o comando que declara uma função em Python

def mostraLinha():
    print('-'*30)
print('Curso em Vídeo')
mostraLinha()

# ------------------------------
# Função com parâmetros
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
mensagem('Sistema de alunos')

# ------------------------------

def título(txt):
    print(txt)
    print('-'*30)
título('    Curso em Vídeo  ')
título('    Aprenda Python  ')
título('    Gustavo Guanabara   ')

# ------------------------------
# Sem função
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
# ------------------------------
# Com função
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print('-'*30)


soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)
# ------------------------------
# Quando vc nao tem a quantidade exata de parâmetros coloque um * (símbolo de desempacotar). Ex: 
def contador(*num):
   # for valor in num:
    #    print(f'{valor}, ', end='')
    tam = len(num)
    print(f'Recebi os valors {num} e são ao todo {tam} números' )
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
# ------------------------------
# Dobrar os valores da lista
def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
# ------------------------------

# Somar valores com desempacotamento
def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
# ------------------------------

# AULA 21 - Funções (Parte 2):
    # Interactive Help
    # Docstrings
    # Argumentos Opcionais
    # Escopo de variáveis
    # Retorno de resultados


# Interactive Help - comando: help()
    help(print)

# ------------------------------

# Docstrings
print(print.__doc__) 


# Exemplo:

def contador (i, f, p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c+= p
    print('Fim!')

help(contador)

# ------------------------------

# Parâmetros/Argumentos Opcionais:
def somar(a,b,c=0): # pode colocar os três como parâmetro opcional também
    s = a+b+c
    print(f'A soma vale {s}')
somar(3,2) # se rodar desta forma vai dar erro pois esta faltando passar o valor de um dos parâmetros pra isso não ocorrer
# vc pode colocar um valor opcional no parêmtro lá em cima, para que se por acaso ele nao receber nada ele fique com tal 
# valor

# ------------------------------

# Escopo de variáveis
def teste():
    x = 8 # x é uma variável local pois está declarada somente dentro da função
    print(f'Na função teste, n vale {n}')

n = 2 # n é uma variável global pois esta sendo declarada fora (no programa principal) e pode ser acessada por 
# qualquer lugar (escopo global)
print(f'No programa principal, n vale {2}')
# ------------------------------

def função(b):
    # global n1 - se aqui vc colocar este comando ele não vai criar a variável local e vai considerar somente a global. 
    # É assim que 
    n1 = 4
    b += 1 # 3
    print('-='*20)
    print(f'N1 dentro vale {n1}') # aqui vai ser considerada a variável local que vc criou com o mesmo nome
    print(f'B vale {b} porque ele recebeu o n1 global que vale 2 e não o local')


n1 = 2
função(n1)
print(f'N1 fora vale {n1}')
print('-='*20)


# Retorno de resultados
def somar(a=0,b=0,c=0): # pode colocar os três como parâmetro opcional também
    s = a+b+c
    return(f'As somas valem {s}')
print(somar(3,2))


# Outro exemplo:
def par(n=0):
    if n%2==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('É impar')
    
# ------------------------------

# AULA 22 - Módulos e Pacotes
- Modularização - Surgiu no início da década de 60, quando os sistemas foram ficando maiores.
    - Foco: dividir um programa grande; Aumentar a legibilidade; Facilitar a manutenção; Organização; Ocultação do código detalhado;
        reutilização em outros projetos;
OBS: Exemplos na pasta modulos.

Quando um módulo não é o suficiente utilizamos Pacotes. (quando um módulo fica com muitas funções)

- Pacotes/Bibliotecas: Pasta que contém módulos. Da pra separar por assunto. Dentro do python toda pasta é considerada um pacote


# ------------------------------

# AULA 23 - Tratamento de erros e exceções
Exceção: Não é um erro sintático, o comando esta digitado corretamente mas em alguns casos acontece a exceção.
É utilizado o try: except:
try: # Um mesmo try pode ter vários except
    # operação
except:
    # se eu tentar a operação de cima e ela falhar aqui é mostrado o erro
else:
    # se der certo faz isso
finally:
    # vai acontecer independente se deu certo ou falha
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'Infelizmente tivemos um problema :(\nErro: {erro.__cause__}')
else: 
    print(f'O resultado é {r}') 
finally:
    print('Volte sempre, muito obrigada')
'''


