from random import randint



multa = 80 
vel_carro = randint(70,100)



if vel_carro >= multa:
    print('Você foi multado')
    print('Seu carro estava á', vel_carro )
    if vel_carro >= multa:
     val_multa = (format((vel_carro-80)*7))
     print('O valor que terá que pagar por passar acima da velocidade')
     print(val_multa)

else:
    print('O Radar não te pegou')