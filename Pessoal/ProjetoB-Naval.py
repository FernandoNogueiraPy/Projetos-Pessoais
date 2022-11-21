#Batalha Naval
from random import randint


print(""" 
        Regras do jogo 

        1 - As embarcações estão de 1 a 100 
        2 - A maquina Jogará podendo eliminar seu barcos
        3 - Quando todos barcos forem eliminados você perde ou maquina
        4 - O Torpedo só pode derrubar Destroyers devido ao seu tamanho
        5 - A artilharia só pode derrubar a corveta e a fragata 

 """)

while True:   #cada barco está localizado em um número e acertando o número o barco será destruido.   
    try:  #posição das embaracações     

        
        #posição do barco inimigo

        corveta = [6,9,18,65,71,33,42]   
        destroyer = [15,47,99,29,83,67]   
        fragata = [9,36,48,52,63,82]    

        # teste 
        print(f'----------------------------------------------')
        print ('SUA VEZ : JOGUE ')
        print(f'----------------------------------------------')


        tiro = int(input('Faça um disparo de Artilharia:'))      

           
        if tiro in corveta:  
            print(f'----------------------------------------------')   
            print(f"Você Afundou uma Corveta")    
            print(f'----------------------------------------------')

        elif tiro in destroyer:   
            print(f'----------------------------------------------')  
            print(f"Você Afundou uma Destroyer") 
            print(f'----------------------------------------------')

        elif tiro in fragata:     
            print(f'----------------------------------------------')
            print(f"Você Afundou uma Fragata")    
            print(f'----------------------------------------------')

        else:     
            print(f'------------------------------------------------------------')
            print(f"Você jogou na posição {tiro} e errou o disparo de artilharia")  
            print(f'------------------------------------------------------------')     


        torpedo = int(input("Faça um disparo de torpedo" ))        
        if torpedo in corveta:       
            print(f'----------------------------------------------')
            print(f"Você Afundou uma Corveta")  
            print(f'----------------------------------------------') 

        elif torpedo in destroyer:      
            print(f'----------------------------------------------') 
            print(f"Você Afundou uma Destroyer")  
            print(f'----------------------------------------------')

        elif torpedo in  fragata:   
            print(f'----------------------------------------------')    
            print(f"Você Afundou uma Fragata") 
            print(f'----------------------------------------------')
            
        else: 
            print(f'-------------------------------------------------')    
            print(f"Você jogou na posição {torpedo} e errou o torpedo")  
            print(f'-------------------------------------------------')



        print(f'----------------------------------------------')
        print ('VEZ DA MÁQUINA : AGUARDE.')
        print(f'----------------------------------------------')

            #posição do barco inimigo x Maquina.
        corveta_inimigo = [5,8,17,31,41,61]   
        destroyer_inimigo= [11,43,98,21,81,69]   
        fragata_inimigo = [4,7,13,70,80,90]    


#Maquina 
        tiro_computador = randint(1,100)
        torpedo_computador = randint(1,100)

        if tiro_computador in corveta:
            print(f'----------------------------------------------')
            print(f'A Máquina afundou sua corveta ')
            print(f'----------------------------------------------')

        elif tiro_computador in destroyer:
            print(f'----------------------------------------------')
            print(f'A Máquina afundou sua destroyer ')
            print(f'----------------------------------------------')


        elif tiro_computador in fragata:
            print(f'----------------------------------------------')
            print(f'A Máquina afundou sua fragata  ')
            print(f'----------------------------------------------')

        else :
            print(f'----------------------------------------------')
            print(f'A Máquina errou o disparo o tiro de Artilharia')
            print(f'----------------------------------------------')


        if torpedo_computador in destroyer:
            print(f'----------------------------------------------')
            print(f'A Máquina afundou sua destroyer ') 
            print(f'----------------------------------------------')

        elif torpedo_computador in fragata:
            print(f'----------------------------------------------')
            print(f'O torpedo não foi efetivo contra a fragata , use a artilharia')
            print(f'Use Artilharia contra FRAGATA.')
            print(f'----------------------------------------------')

        elif torpedo_computador in corveta:
            print(f'----------------------------------------------')
            print(f'O torpedo não é eficaz contra corveta devido ao seu tamanho.')
            print(f'Use artilharia contra CORVETA.')
            print(f'----------------------------------------------')

        else :
            print(f'----------------------------------------------')
            print(f'A Máquina errou o disparo o tiro de [TORPEDO] ')
            print(f'----------------------------------------------')



    except:  print(f"Digite apenas Números.")








