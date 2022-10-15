distancia = 200 
viagem = float(input('Qual a distancia da Sua viagem em KM'))

if viagem <= distancia:
    preco1 = viagem*0.50
    print(preco1)

else:
    preco2 = viagem*0.45
    print(preco2)