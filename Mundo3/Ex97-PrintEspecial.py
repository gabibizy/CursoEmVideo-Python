# 97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parãmetro e mostre uma
# mensagem com tamanho adaptável. Ex: escreva('Olá, mundo!') Saída: 
def escreva(texto):
    print('-'*(len(texto)+4))
    print(f'  {texto}')
    print('-'*(len(texto)+4))


escreva((str(input('Digite algo: '))))

