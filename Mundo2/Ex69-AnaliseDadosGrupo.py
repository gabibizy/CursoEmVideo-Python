# 69 - Leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar 
# se o usuário quer ou não continuar. No final, mostrar: - Quantas pessoas tem mais de 18 anos; 
# - Quantos homens foram cadastrados; - Quantas mulheres tem menos de 20 anos.
maior = 0
homens = 0
menos_de_20 = 0
resposta = 's'
while resposta in 'Ss':
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: '))
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        menos_de_20 += 1
    resposta = str(input('Deseja continuar? S/N: ')) 
    print('-='*11)
    if resposta in 'Nn':
        break
print(f'{maior} pessoas tem mais de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'{menos_de_20} mulheres tem menos de 20 anos')

