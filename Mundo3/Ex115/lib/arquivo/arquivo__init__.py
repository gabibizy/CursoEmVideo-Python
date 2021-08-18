from lib.interface import *


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        print('Não achou o arquivo')
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso ')


def listar(arq):
    try:
        arquivo = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:30}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at') # a = append
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print (f'\nRegistro de {nome} adicionado')
            arquivo.close()



