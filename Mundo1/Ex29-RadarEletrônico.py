# 29 - Escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 para cada Km acima do limite.
velocidade = int(input('Digite a velocidade: '))
multa = 0
if velocidade > 80 :
        multa = (velocidade - 80) * 7
        print(f'A velocidade ultrapassou 80Km/h, vc foi multado e o valor da multa é de R${multa:.2f}')
else:
        print('Show! Você esta dentro da velocidade permitida')

