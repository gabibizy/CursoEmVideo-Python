# 73 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, 
# na ordem de colocação. Depois mostre: A) Apenas os 5 primeirs colocados
# B) Os últimos 4 colocados na tabela. C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela esta o time da Chapeconense.
brasileirão = ('Athetico-PR', 'Bragantino', 'Palmeiras', 'Fortaleza', 'Atlético-MG', 'Flamengo', 'Bahia', 'Santos', 'Juventude', 'Corinthians', 'Atlético-GO', 'Ceará SC', 'Fluminense', 'Internacional', 'América-MG', 'Sport Recife', 'Sao Paulo', 'Chapecoense', 'Cuiabá', 'Grêmio')
print('-='*11)
print('Tabela do Brasileirão: ',brasileirão)
print('-='*11)
print('A)', brasileirão[:5])
print('-='*11)
print('B)',brasileirão[-4:])
print('-='*11)
print('C)',sorted(brasileirão))
print('-='*11)
print('D)',brasileirão.index('Chapecoense')+1)
print('-='*11)
