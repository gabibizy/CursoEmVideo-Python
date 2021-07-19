# 11 - Pintando parede
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura *  altura
qtd_tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e a sua área é de {}m². \nA quantidade de tinta que vc va precisar é de {}l' .format(largura, altura, area, qtd_tinta))
