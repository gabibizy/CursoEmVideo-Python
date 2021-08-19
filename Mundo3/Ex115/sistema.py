from lib.arquivo.arquivo__init__ import *
from lib.interface import *

arq = r'C:\Users\Admin\Desktop\Dev\Curso em vídeo - Python\Mundo3\Ex115\lista_pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    op = menu(['Listar Pessoas', 'Cadastrar pessoa', 'Sair do sistema'])
    if op == 1:
        cabeçalho('Pessoas Cadastradas')
        listar(arq)
    elif op == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif op == 3:
        cabeçalho('Saindo do sistema. Até logo')
        break
    else:
        print(f'\033[1;31mErro! \033[mDigite uma opção válida(1, 2 ou 3) ')


        