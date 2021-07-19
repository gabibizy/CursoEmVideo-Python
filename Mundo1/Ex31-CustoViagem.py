# 31 - Pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobranco R$0,50 por Km
#para viagens de até 200Km e R$0,45 para viagens mais longas
distância = float(input('Digite a distância da viagem: '))
if distância <= 200:
        passagem = distância * 0.50
        print(f'A distância é de {distância}Km e preço da passagem ficou R${passagem:.2f}')
else:
        passagem = distância * 0.45
        print(f'A distância é de {distância}Km e preço da passagem ficou R${passagem:.2f}')

