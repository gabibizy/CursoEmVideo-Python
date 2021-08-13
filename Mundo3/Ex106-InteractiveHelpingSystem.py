# 106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai 
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. 
while True:
    print('-='*30)
    comando = input('Digite a função ou biblioteca ("FIM" para sair): ')
    if comando in 'FIMfimFim':
        break
    help(comando)

print('-='*30)
