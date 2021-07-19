# 57 - Leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o sexo[F/M]: '))
while sexo.upper() not in {'F', 'M'}:
    sexo = str(input('Dados inválidos, informe o sexo [F/M]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso!')
