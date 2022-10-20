import random

p1 = str(input('1 - Coloque seu nome aqui '))
p2 = str(input('2 - Coloque seu nome aqui '))
p3 = str(input('3 - Coloque seu nome aqui '))
p4 = str(input('4 - Coloque seu nome aqui '))

print(f' Sorteando ... ')

lista = [p1,p2,p3,p4]

#ordem de lista
random.shuffle(lista)

print(lista)