aluguel = int(input('quantos dias alugado?:'))
km_rodados = float(input("quantos km foi percorrido?"))
calculo_dia = aluguel * 60
calculo_km = km_rodados * 0.15
total_pagar = calculo_dia + calculo_km
print('o resultado final e de {}'.format(total_pagar))
#o carro custa R$60 por dia e R$0,15 por Km rodado
