
while True: 
    p1 = int(input('Digite seu ano de nascimento'))
    p2 = int(input('Digite o ano que voce vai competir'))

    n1 = p2 - p1 

    if n1 <= 0 : 
        print('Não tenta avacalha meu programa :/ ')

    elif n1 <= 9 : 
        print('Voce está na categoria = MIRIM')

    elif n1 <= 14 : 
        print('Você está na categoria = INFANTIL')

    elif n1 <= 19 : 
        print('Você está na categoria = JUNIOR')

    elif n1 >= 20 : 
        print('Você está na caategoria = SÊNIOR')

