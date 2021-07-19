# 51 - Leia o primeiro termo e a razão de um PA. No final, mostre os 10
# primeiros termos dessa progressão

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = primeiro_termo + (10 - 1) * razão
for c in range (primeiro_termo, décimo+razão, razão):
    print(c, end=' ')

