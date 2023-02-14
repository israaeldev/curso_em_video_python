nome = str(input('digite seu nome completo:')).split()
print ('seu nome tem silva? {}'.format('silva' in nome))

frase = str(input('digite uma frase:')).upper().strip()
print ('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print ('A primeira letra A aparece na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posicao {}'.format(frase.rfind('A')+1))

n = str(input('digite seu nome completo:'))
Nome = n.split()
print(' muito prazer em te conhcer!')
print('seu primeiro nome e {}'.format(Nome[0]))
print('seu ultimo nome e {}'.format(Nome[len(Nome)-1]))