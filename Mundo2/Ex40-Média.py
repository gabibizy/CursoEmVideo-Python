# 40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado; - Média entre 5.0 e 6.9: Recuperação; - Media 7.0 ou superior: Aprovado;
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'A sua média foi {media} você está REPROVADO')
elif media >= 5 and media < 7:
    print(f'A sua média foi {media} você está de RECUPERAÇÃO')
elif media >= 7:
    print(f'Parabéns! A sua média foi {media} você está APROVADO')
