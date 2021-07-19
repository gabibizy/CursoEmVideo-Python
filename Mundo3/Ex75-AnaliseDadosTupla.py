# 75 - Leia 4 valores e guarde-os em uma tupla. No final mostre: A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o valor 3. C) Quais foram os números pares.
tupla =(int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Tupla: {tupla}')
print(f'O número 9 aparece {tupla.count(9)} vez(es) na tupla')
if 3 in tupla:
    print(f'O valor 3 se encontra na {tupla.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado')
for n in tupla:
    if n % 2 == 0:
        print(f'Os números pares digitados são: {n}')
