# 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações: - Quantidade de notas; - A maior nota; - A menor nota; - A média da turma; - A situação
# (opcional); Adicione também os docstrings da função
def notas(*n, sit=False):
    """
    -> Funcao para analisar a nota e situação de um aluno.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao mostrar a situacao do aluno
    :return: dicionario com varias informacoes sobre a situacao da turma
    """
    resp = {'total': len(n),
        'maior': max(n),
        'menor':min(n),
        'média': sum(n) / len(n)}
    if sit == True:
        if resp['média'] < 5:
            resp['situação'] = 'Reprovado'
        elif resp['média'] >= 5 and resp['média'] < 7:
            resp['situação'] = 'Recuperação'
        elif resp['média'] >= 7:
            resp['situação'] = 'Aprovado'
    return (resp)

    
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

