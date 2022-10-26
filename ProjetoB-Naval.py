#Batalha Naval


while True:    #cada barco está localizado em um número e acertando o número o barco será destruido.   
    try:  #posição das embaracações     
        corveta = [1,3,9,6,8]   
        destroyer = [5,19]   
        fragata = [17,15,11]    

# teste 
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
            print(f"Você jogou na posição {torpedo} " )  
    except:  print(f"Digite apenas Números.")


