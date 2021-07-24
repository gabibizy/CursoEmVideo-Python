# 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Primeira nota: ')))
    aluno.append(float(input('Segunda nota: ')))
    aluno.append((aluno[1] + aluno [2]) / 2)
    boletim.append(aluno[:])
    aluno.clear()
    resp = input('Deseja cadastrar mais alunos? ')
    if resp not in 'NnSs':
        resp = input('Comando inválido. Deseja cadastrar mais alunos? ')
    if resp in 'Nn':
        break
print('-='*25) 
print(f'N°         Nome            Média   ')
print('-'*40)
posição=0
for i in boletim:
    print(f'{posição:.<10} {i[0]:.<15} {i[3]:.<15} \n')
    posição+=1
resp= 0
while True:
    resp = int(input('Digite o número do aluno para verificar as notas dele (999 interrompe): '))
    if resp == 999:
        break
    print(f'\n Nome: {boletim[resp][0]} | Primeira nota: {boletim[resp][1]} | Segunda nota: {boletim[resp][2]} | Média: {boletim[resp][3]}\n')
print('-='*30)

