# 90 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre 
# o conteúdo da estrutura na tela.
aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >=7:
    aluno['Situação']= 'Aprovado'
elif aluno['Media']>=5:
    aluno['Situação']= 'Recuperação'
else:
    aluno['Situação']= 'Recuperação'
print('-='*20)
for k, v in aluno.items():
    print(f'{k}: {v}')
print('-='*20)
