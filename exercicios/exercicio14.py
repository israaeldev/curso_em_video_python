import random
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
a5 = str(input('quinto aluno:'))
a6 = [a1, a2, a3, a4, a5]
random.shuffle(a6)
print('a ordem de apresentacao sera {}'.format(a6))

import random
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
a5 = str(input('quinto aluno:'))
lista = [a1, a2, a3, a4, a5]
random.shuffle(lista)
print('a ordem de apresentacao sera')
print(lista)