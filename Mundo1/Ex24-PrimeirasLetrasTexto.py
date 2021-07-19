# 24 - Leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = (input('Digite o nome de uma cidade: ')) 
dividido = cidade.split()
print("SANTO" in dividido[0].upper())

'''
# OU
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

'''


