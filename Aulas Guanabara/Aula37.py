
p1 = input('Escreva uma númeração qualquer ')

n1 = p1[0]
n2 = p1[1]
n3 = p1[2]
n4 = p1[3]


Numeros_aceitados = ['0','1','2','3','4','5','6','7','8','9'] 

num0 = 0
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9

Letras = ['A','B','C','D','E','F']

A = 10
B = 11
C = 12
D = 13
E = 14
F = 15

if n1 == Numeros_aceitados:

    r1 = n1*16
    t1 = r1*16
    y1 = t1*16

else:
    n1 = p1*16
    t1 = n1*16
    y1 = t1*16

if n2 == Numeros_aceitados:

    r2 = n2*16
    t2 = r2*16

else: 
    r2 = n2*16
    t2 = r2*16

if n3 == Numeros_aceitados:

    r3 = n3*16

else : 
    r3 = n3*16

if n4 == Numeros_aceitados:

    r4 = n4*1

else:
    r4 = n4*1




print(y1,t2,r3,r4)




  