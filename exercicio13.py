import random 
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
a5 = str(input('quinto aluno:'))
a6 = (a1, a2, a3, a4, a5)
escolhido = random.choice(a6)
print('o aluno sorteado foi {}'.format(escolhido))

from random import choice 
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
a5 = str(input('quinto aluno:'))
a6 = (a1, a2, a3, a4, a5)
escolhido = choice(a6)
print('o aluno sorteado foi {}'.format(escolhido))