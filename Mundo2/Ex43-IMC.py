# 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso; Entre 18.5 e 25: Peso ideal; 25 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade Mórbida;
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, você esta Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.1f}, você esta no Peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.1f}, você esta com Sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é de {imc:.1f}, você esta com Obesidade')
elif imc > 40:
    print(f'Seu IMC é de {imc:.1f}, você esta com Obesidade Mórbida')
