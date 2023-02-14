from random import choice
from time import sleep
pesquisa = int(input('Adivinhe o numero que a maquina esta pensando:'))
numeros = [0, 1, 2, 3, 4, 5]
escolhido = choice(numeros) # choice ou randint (0, 5)
print('processando...')
sleep (3)
print('O numero escolhido pela maquina foi {}'.format(escolhido))
if pesquisa == (escolhido):
    print('Parabens, voce venceu o jogo.')
else:
    print('A maquina venceu o jogo, tente outra vez.')
