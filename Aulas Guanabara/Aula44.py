p1 = float(input('Qual o valor do seu produto '))

print(' FORMAS DE PAGAMENTO  ')
print('[1] AVISTA OU CARTÃO DE DÉBITO')
print('[2] AVISA CARTÃO DE CRÉDITO ')
print('[3] CHEQUE ')
print('[4] 3X NO CARTÃO DE CRÉDITO')       

p2 = int(input('Escolha a forma de pagamento !'))

if p2 == 1 :
    n1 = p1*10/100
    t1 = p1-n1
    print('Essa forma de pagamento lhe rende um desconto de 10%')
    print('O total a pagar é de {} Reias.'.format(t1))

elif p2 == 2 : 
    n2 = p1*5/100
    t2 = p1-n2
    print('Essa forma de pagamento lhe rende um desconto de 5%')
    print('O total a pagar é de {} Reias.'.format(t2))

elif p2 == 3 :
    print('Essa forma de pagamento não tem desconto')
    print('O total a pagar é de {} Reais.'.format(p1))

elif p2 == 4 : 
    n4 = p1/100*20
    n5 = n4+p1
    print('Essa forma de pagamento tem o acrescimo de 20% a mais no valor')
    print('O total a pagar é de {} Reias.'.format(n5))
