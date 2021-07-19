# 53 - Leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
# os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print ('A frase É um palíndromo')
else:
    print ('A frase NÃO é um palíndromo')

