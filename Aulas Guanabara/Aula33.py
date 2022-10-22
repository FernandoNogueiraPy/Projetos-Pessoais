numero = str(input('Digite 3 Números'))

n1 = numero[0]
b1 = int(n1)
n2 = numero[1]
b2 = int(n2)
n3 = numero[2]
b3 = int(n3)
if b2>b1<b3:
    print('o menor é {}'.format(b1))
if b1>b2<b3:
    print('o menor é {}'.format(b2))
if b2>b3<b1:
    print('o menor é {}'.format(b3))
if b2<b1>b3:
    print('o maior é {}'.format(b1))
if b1<b2>b3:
    print('o maior é {}'.format(b2))
if b1<b3>b2:
    print('o maior é {}'.format(b3))

if b1 == b3 == b2:
    print('todos sao iguais')

if b1 == b2 < b3:
    print('os dois menores sao {} e {}'.format(b1, b2))
if b1 == b3 < b2:
    print('os dois menores sao {} e {}'.format(b1, b3))
if b3 == b2 < b1:
    print('os dois menores sao {} e {}'.format(b3, b2))

if b1 == b2 > b3:
    print('os dois maiores sao {} e {}'.format(b1, b2))
if b1 == b3 > b2:
    print('os dois maiores sao {} e {}'.format(b1, b3))
if b3 == b2 > b1:
    print('os dois maiores sao {} e {}'.format(b3, b2))


    