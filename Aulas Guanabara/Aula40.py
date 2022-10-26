p1 = float(input('Digite a sua nota do primeiro semestre '))
p2 = float(input('Digite a sua nota do segundo semestre '))

n1 = p1+p2 
n2 = n1/2 

print('Sua Média é {}'.format(n2))

if n2 <= 4.99 :
    print('Voce está abaixo da média e foi reprovado. ')

elif n2 > 5.0 < 6.9 :
    print('Voce está de recuperação.')

elif n2 > 7.0 : 
    print('Voce está aprovado')