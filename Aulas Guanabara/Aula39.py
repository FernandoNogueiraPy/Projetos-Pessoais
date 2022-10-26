p1 = int(input('Digite seu ano de nascimento '))
p2 = int(input('Digite o ano em que está '))

n1 = p2 - p1
n2 = p2 - p1 - 18
n3 = 18 - n1 

print('Sua idade é {}'.format(n1))

if n1 < 18 :
    print ('Voce ainda devera se alistar quando chegar a maior idade.')
    print('Faltam apenas {} anos para seu Alistamento'.format(n3))

elif n1 == 18 :
    print ('Voce já deve se alistar !!!')
    print('Você já tem {} anos , já deve se alistar de acordo com a lei'.format(n1))

elif n1 > 18 : 
    print('Voce já passou do tempo para se alistar ,porém ainda deve se apresentar na junta militar ')
    print('voce está atrasado a {} anos do alistamento obrigatorio'.format(n2))




