def aumentar(n, porc_a):
    preço = n + (n * porc_a /100 )
    return moeda(preço)


def diminuir(n, porc_d):
    preço = n - (n * porc_d /100)
    return moeda(preço)


def metade(n):
    preço = n / 2
    return moeda(preço)


def dobro(n):
    preço = n * 2
    return moeda(preço)


def moeda(n):
    return (f'R${n:.2f}'.replace('.', ','))


def resumo(n, porc_a, porc_d):
    print('-'*30)
    print('        RESUMO DO VALOR  ')
    print('-'*30)
    print(f'Preço analisado:    {moeda(n)}')
    print(f'Metade do preço:    {metade(n)}')
    print(f'Dobro do preço:     {dobro(n)}')
    print(f'80% de aumento:     {aumentar(n, porc_a)}')
    print(f'35% de redução:     {diminuir(n, porc_d)}')
    print('-'*30)
