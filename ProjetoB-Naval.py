#Batalha Naval


from math import radians
from random import randint


while True:   #cada barco está localizado em um número e acertando o número o barco será destruido.   
    try:  #posição das embaracações     

        #posição do barco inimigo

        corveta = [6,9,18,65,71,33,42]   
        destroyer = [15,47,99,29,83,67]   
        fragata = [9,36,48,52,63,82]    






# teste 
        print(""" 
        Regras do jogo 

        1 - As embarcações estão de 1 a 100 
        2 - A maquina Jogará podendo eliminar seu barcos
        3 - Quando todos barcos forem eliminados você perde ou maquina
        4 - O Torpedo só pode derrubar Destroyers devido ao seu tamanho
        5 - A artilharia só pode derrubar a corveta e a fragata 

 """)
        tiro = int(input('Faça um disparo de Artilharia:'))      

        if tiro in corveta:     
            print(f"Você Afundou uma Corveta")      
        elif tiro in destroyer:     
            print(f"Você Afundou uma Destroyer")         
        elif tiro in fragata:     
            print(f"Você Afundou uma Fragata")    
        else:     
            print(f"Você jogou na posição {tiro} e errou o disparo de artilharia")        
        torpedo = int(input("Faça um disparo de torpedo" ))        
        if torpedo in corveta:       
            print(f"Você Afundou uma Corveta")        
        elif torpedo in destroyer:       
            print(f"Você Afundou uma Destroyer")  
        elif torpedo in  fragata:       
            print(f"Você Afundou uma Fragata") 
        else:     
            print(f"Você jogou na posição {torpedo} e errou o torpedo " )  




            #posição do barco inimigo x Maquina.

        corveta_inimigo = []    #6 barcos para cada
        destroyer_inimigo= []   
        fragata_inimigo = []    


#Maquina 
        tiro_computador = randint(1,100)
        torpedo_computador = randint(1,100)

        if tiro_computador in corveta_inimigo:
            print(f'A Máquina afundou sua corveta ')
        elif tiro_computador in destroyer_inimigo:
            print(f'A Máquina afundou sua destroyer ')
        elif tiro_computador in fragata_inimigo:
            print(f'A Máquina afundou sua fragata  ')
        else :
            print(f'A Máquina errou o disparo o tiro de Artilharia')
    
        if torpedo_computador in destroyer_inimigo:
            print(f'A Máquina afundou sua destroyer ') 

        elif torpedo_computador not in fragata_inimigo:
            print(f'')

        elif torpedo_computador not in corveta_inimigo:
            print(f'')


        else :
            print(f'A Máquina errou o disparo o tiro de Artilharia')





    except:  print(f"Digite apenas Números.")








