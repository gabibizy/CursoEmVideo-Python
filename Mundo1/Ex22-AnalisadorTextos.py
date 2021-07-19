# 22 - Leia o nome completo e mostre: O nome com todas as letras maiúsculas; O nome com todas as letras minúsculas;
# Quantas letras ao todo(sem considerar espaços); Quantas letras tem o primeiro nome;
from time import sleep
frase = str(input('Qual é o seu nome? ')).strip()
print('Analisando seu nome...')
sleep(1)
print(f'Seu nome em maiúsculas: {frase.upper()}')
print(f'Seu nome em minúsculas: {frase.lower()}')
print('Seu nome tem ao todo: ',len(frase)-frase.count(' '),'letras')
dividido = frase.split()
print(f'Seu primeiro nome {dividido[0]} é e ele tem {(len(dividido[0]))} letras')



