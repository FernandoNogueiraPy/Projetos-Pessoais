while True:

    p1 = float(input('Quantos kilos voce pesa ? '))
    p2 = float(input('Qual e a sua altura ? ' ))

    r1 = p2*p2
    r2 = p1/r1

    print(r2)

    if r2 < 18.5:
        print('Abaixo do peso')

    elif r2 < 25 :
        print('Peso Ideal')

    elif r2 < 30 : 
        print('Sobrepeso')

    elif r2 < 40 : 
        print('Obesidade')

    elif r2 < 41 : 
        print('Obsidade morbida')
