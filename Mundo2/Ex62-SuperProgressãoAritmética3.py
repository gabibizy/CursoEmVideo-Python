

# 62 - Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns
# termos. O programa encerra quando ele disser que quer mostrar 0 termos.
from time import sleep
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro_termo
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(termo, end=' ')
        termo += razão
        c+= 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja mostrar a mais? (Digite 0 para sair) '))

print('Saindo do programa...')
sleep(1)
print('Finalizado')
