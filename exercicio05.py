real = float(input ('quanto dinheiro voce possui?'))
dolar = real / 5.27
print('com R$ {:.2f} voce pode comprar US$ {:.2f}'.format(real, dolar))

# conversor de reais (R$) em Euros (€)
quantidade_reais_do_usuario = float(input('digite qunato dinheiro voce tem:'))
cotacao_euro = 5.61
quantidade_euros = quantidade_reais_do_usuario / cotacao_euro
print('o resultado final sera {:.2f} euros'.format(quantidade_euros))
# print(f'o resultado final sera {quantidade_euros} euros')

dinheiro_usuario=float(input('digite sua quantidade de dinheiro:'))
cotacao_do_dia= 5.27
dinheiro = dinheiro_usuario / cotacao_do_dia
print('o resultado final e {:.2f} dolares'.format(dinheiro))


