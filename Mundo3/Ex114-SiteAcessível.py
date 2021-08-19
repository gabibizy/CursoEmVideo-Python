# 114 - Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://youtube.com.br')
    print('Consegui acessar o site com sucesso!')
except Exception as erro:
    print('O site não está acessível no momento')


# com <variável que recebe o site>.read() da para acessar o conteúdo html do site