#Projeto pedra papel tesoura 

from random import randint


opção = int(input(f"Escolha contra quem vai jogar"))

if opção == 0:


    
    while True:
        try: 
            
        
            escolhas = ['papel','pedra','tesoura']
            
            print(" ")
            


            jogador1= input(f"Coloque sua jogada entre - pedra - papel - tesoura\n").strip().lower()



            jogador2= input(f"coloque sua jogada entre - pedra - papel - tesoura\n").strip().lower()
            
            
        
            if jogador1  not in escolhas and jogador2 not in escolhas:
                print(f"Digite uma opção válida:")
                continue

            if jogador1 == "pedra" and jogador2 == "papel":
                print(f"Jogador2 Wins. ")

            elif jogador1 == "tesoura" and jogador2 == "pedra":
                print(f"Jogador2 Wins. ")

            elif jogador1 == "papel" and jogador2== "tesoura":
                print(f"Jogador2 Wins. ")

            elif jogador1 == jogador2:
                print(f"Empate entre os competidores.")


            else: 
                print(f" Jogador1 Wins. ")


        except: print (f"Digite apenas - pedra - papel - tesoura")

if opção == 1:

    while True: 
        try: 
            

            escolhas = ['papel','pedra','tesoura']
            
            print(" ")
            

            jogador1= input(f"Coloque sua jogada entre - pedra - papel - tesoura\n").strip().lower()

            computador = randint(0,2)
            computador_escolhas = escolhas[computador]

        
            if jogador1 not in escolhas:
                print(f"Digite uma opção válida:")
                continue

            print(f"A maquina Jogou {computador_escolhas}")

            if jogador1 == "pedra" and computador_escolhas == "papel":
                print(f"Computador Wins. ")

            elif jogador1 == "tesoura" and computador_escolhas == "pedra":
                print(f"Computador Wins. ")

            elif jogador1 == "papel" and computador_escolhas == "tesoura":
                print(f"Computador Wins. ")

            elif jogador1 == computador_escolhas:
                print(f"Empate entre os competidores.")


            else: 
                print(f" Jogador Wins. ")

        except: print (f"Digite apenas - pedra - papel - tesoura")
    
      
    
