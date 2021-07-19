# 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto; - À vista no cartão: 5% de desconto; - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS GABI '))
valor_prod = float(input('Valor da Compra: R$'))
condição_pag = int(input('''Formas de Pagamento:
 1 - A vista dinheiro/cheque
 2 - A vista no cartão
 3 - Em até 2x no cartão
 4 - 3x ou mais no cartão
 Digite o número da opção: '''))
if condição_pag == 1:
    valor = valor_prod - (valor_prod * 10 / 100)
    print(f'O valor a ser pago com 10% de desconto é R${valor:.2f}')
elif condição_pag == 2:
    valor = valor_prod - (valor_prod * 5 / 100)
    print(f'O valor a ser pago com 5% de desconto é R${valor:.2f}')
elif condição_pag == 3:
    qtd_parcelas = int(input('Quantidade de parcelas: '))
    total = valor_prod / qtd_parcelas
    print(f'O valor total a ser pago é R${valor_prod:.2f} cada parcela sai no valor de R${total:.2f}')
elif condição_pag == 4:
    qtd_parcelas = int(input('Quantidade de parcelas: '))
    valor_com_juros = valor_prod + (valor_prod * 20 / 100)
    total = valor_com_juros / qtd_parcelas
    print(f'O valor total a ser pago com 20% de juros é R${valor_com_juros:.2f} serão {qtd_parcelas}x de R${total:.2f}')
else:
    print('\033[0;;45m Opção inválida, tente novamente')
