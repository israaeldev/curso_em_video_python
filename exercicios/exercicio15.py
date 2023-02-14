nome = str(input('digite seu nome completo:')).strip()
print('analisando seu nome...')
print('seu nome em maiusculo e {}'.format(nome.upper()))
print('seu nome em minusculas e {}'.format(nome.lower()))
print('seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))


name = str(input('digite seu nome completo:')).strip()
print ('analisando seu nome...')
print('seu nome maiusculo e {}'.format(name.upper()))
print('seu nome minusculo e {}'.format(name.lower()))
print('seu nome possui {} letras'.format(len(name) - name.count(' ')))
separa = name.split()
print('seu ultimo nome e {} e tem {} letras'.format(separa [2], len(separa[2])))

