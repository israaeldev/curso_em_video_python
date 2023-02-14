co =float(input('digite o comprimento do cateto oposto:'))
ca =float(input('digite o comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
co =float(input('digite o comprimento do cateto oposto:'))
ca =float(input('digite o comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))