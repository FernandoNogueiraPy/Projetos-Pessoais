import pandas as pd
from api import get_ref
from verify import verify
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from threading import Thread
import time


ListaC = [40,41,42,43,44,45,46,47,48,49]

Lista_correcao_diesel = ['(diesel)','(DIESEL)',
        ' Diesel',' DIESEL','(die)',' Dies']

Lista_Chat = ["Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio"]
carros_ou_caminhoes = ["Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio"]
lista_modelo = ["Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio"]
lista_valor = ["Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio","Vazio"]

#Seleciona o Arquivo
def OpenFile():
    global filepath
    filepath = filedialog.askopenfilename()
    print(filepath)
    local_arquivo = Label(root, text=filepath,font=("Arial",8))
    local_arquivo.place(x=20,y=85)
    entry1.insert(0,filepath)

#Salve o nome que o Usuario escolher.
def salva_arquivo():
    global salvar_nome_arquivo
    salvar_nome_arquivo = entry2.get()    

#Descobre se é caminhão ou carro 
def leitura(filepath):
    df = pd.read_excel(filepath)


    global tamanho
    tamanho = df.index.stop

    global final_arquivo
    final_arquivo = df['FIPE'].iloc[-1]
   
    global aumento 
    aumento = 100/tamanho


    ref = get_ref()
    for index,row in df.iterrows():
        pega_modelo = (row["MODELO"])
        Tipo = row ["CONTRATO"] #Exp : 44-519190/20
        
        global atual_arquivo
        atual_arquivo = row['FIPE']
       
        

        try:
            Tipo2 = Tipo.split('-')[0]

            global Tipo3
            Tipo3 = int(Tipo2)


            if Tipo3 in ListaC:
    
                pega_ano = (row["ANO"]).split('/')[1]
               
                pega_marca = (row["MARCA"])
                
                pega_modelo = (row["MODELO"])

                preco = verify(ref,3,pega_marca,3,pega_ano,pega_modelo)

                tipo_caminhao = print(f"{preco} caminhao " )

                df['FIPE'][index] = preco
                df.to_excel(f"{salvar_nome_arquivo}.xlsx", index=False)

                mostrar_pega_modelo = (row["MODELO"]).split(' ')[0]

                Lista_Chat.append(mostrar_pega_modelo)
                carros_ou_caminhoes.append("CAMINHÃO")
                lista_modelo.append(pega_marca)
                lista_valor.append(preco)

                limpeza()
                time.sleep(0.003)
                Thread(target=Start).start()
                Thread(target=tipo).start()
                Thread(target=marca).start()
                Thread(target=valor).start()
                time.sleep(1)
                progresso(aumento)


                

            else:
                pega_ano2 = (row["ANO"]).split('/')[1]
              
                pega_marca2 = (row["MARCA"])
           
                pega_modelo2 = (row["MODELO"])
                diesel_car = False
                for diesel in Lista_correcao_diesel:
                    if diesel in pega_modelo2:
                        preco = verify(ref,1,pega_marca2,3,pega_ano2,pega_modelo2)
                        diesel_car = True
                if not diesel_car:
                    preco = verify(ref,1,pega_marca2,1,pega_ano2,pega_modelo2)
                print(f"CARRO {preco} ")
                

                df['FIPE'][index] = preco
                df.to_excel(f"{salvar_nome_arquivo}.xlsx", index=False)

                mostrar_pega_modelo = (row["MODELO"]).split(' ')[0]

                Lista_Chat.append(mostrar_pega_modelo)
                carros_ou_caminhoes.append("CARRO")
                lista_modelo.append(pega_marca2)
                lista_valor.append(preco)

                limpeza()
                time.sleep(0.003)
                Thread(target=Start).start()
                Thread(target=tipo).start()
                Thread(target=marca).start()
                Thread(target=valor).start()
                time.sleep(1)
                progresso(aumento)

            
                
                
            
            
        except:

            mostrar_pega_modelo = (row["MODELO"]).split(' ')[0]
            Lista_Chat.append(mostrar_pega_modelo)
            print(f'Não foi possivel pequisar esse contrato.{pega_modelo}')
            aviso_simples = (f'Não foi possivel pequisar.{mostrar_pega_modelo}')
            df['FIPE'][index]= 'Não foi possivel pesquisar '
            df.to_excel(f"{salvar_nome_arquivo}.xlsx", index=False)
            Lista_Chat.append(aviso_simples)
            lista_valor.append("N/P")
        
            
            limpeza()
            time.sleep(0.003)
            Thread(target=Start).start()
            Thread(target=tipo).start()
            Thread(target=marca).start()
            Thread(target=valor).start()

            time.sleep(2)
            progresso(aumento)

#Exibe na tela os dados do arquivo
def Start():

    Lista_Posicao13 = Lista_Chat[-13]
    Lista_Posicao12 = Lista_Chat[-12]
    Lista_Posicao11 = Lista_Chat[-11]
    Lista_Posicao10 = Lista_Chat[-10]
    Lista_Posicao9 = Lista_Chat[-9]
    Lista_Posicao8 = Lista_Chat[-8]
    Lista_Posicao7 = Lista_Chat[-7]
    Lista_Posicao6 = Lista_Chat[-6]
    Lista_Posicao5 = Lista_Chat[-5]
    Lista_Posicao4 = Lista_Chat[-4]
    Lista_Posicao3 = Lista_Chat[-3]
    Lista_Posicao2 = Lista_Chat[-2]
    Lista_Posicao1 = Lista_Chat[-1]
    

    

    texto4 = Label(root,text=Lista_Posicao13 ,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=200,y=240)

    texto5 = Label(root,text= Lista_Posicao12 ,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=200,y=260)

    texto6 = Label(root,text= Lista_Posicao11 ,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=200,y=280)

    texto3 = Label(root,text= Lista_Posicao10,font=("Arial Black",11),background='black', foreground='white')
    texto3.place(x=200,y=300)

    texto4 = Label(root,text=Lista_Posicao9 ,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=200,y=320)

    texto5 = Label(root,text= Lista_Posicao8 ,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=200,y=340)

    texto6 = Label(root,text= Lista_Posicao7 ,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=200,y=360)

    texto7 = Label(root,text= Lista_Posicao6 ,font=("Arial Black",11),background='black', foreground='white')
    texto7.place(x=200,y=380)

    texto8 = Label(root,text= Lista_Posicao5,font=("Arial Black",11),background='black', foreground='white')
    texto8.place(x=200,y=400)

    texto9 = Label(root,text=Lista_Posicao4 ,font=("Arial Black",11),background='black', foreground='white')
    texto9.place(x=200,y=420)

    texto10 = Label(root,text= Lista_Posicao3 ,font=("Arial Black",11),background='black', foreground='white')
    texto10.place(x=200,y=440)

    texto11 = Label(root,text= Lista_Posicao2 ,font=("Arial Black",11),background='black', foreground='white')
    texto11.place(x=200,y=460)

    texto12 = Label(root,text= Lista_Posicao1 ,font=("Arial Black",11),background='black', foreground='white')
    texto12.place(x=200,y=480)


    if final_arquivo == atual_arquivo:
        texto12 = Label(root,text= 'Todos os processos foram concluidos.' ,font=("Arial Black",11),background='black', foreground='Green')
        texto12.place(x=20,y=500)

#Faz a limpeza da tela para atualização dos frames
def limpeza():

    limpar = 80*('  ')


    texto4 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=20,y=240)

    texto5 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=20,y=260)

    texto6 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=20,y=280)

    texto3 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto3.place(x=20,y=300)

    texto4 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=20,y=320)

    texto5 = Label(root,text=  limpar ,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=20,y=340)

    texto6 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=20,y=360)

    texto7 = Label(root,text= limpar ,font=("Arial Black",11),background='black', foreground='white')
    texto7.place(x=20,y=380)

    texto8 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto8.place(x=20,y=400)

    texto9 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto9.place(x=20,y=420)

    texto10 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto10.place(x=20,y=440)

    texto11 = Label(root,text= limpar,font=("Arial Black",11),background='black', foreground='white')
    texto11.place(x=20,y=460)

    texto12 = Label(root,text= limpar ,font=("Arial Black",11),background='black', foreground='white')
    texto12.place(x=20,y=480)

#Exibe a marca na tela
def marca():

    Lista_Posicao13 = lista_modelo[-13]
    Lista_Posicao12 = lista_modelo[-12]
    Lista_Posicao11 = lista_modelo[-11]
    Lista_Posicao10 = lista_modelo[-10]
    Lista_Posicao9 = lista_modelo [-9]
    Lista_Posicao8 = lista_modelo [-8]
    Lista_Posicao7 = lista_modelo[-7]
    Lista_Posicao6 = lista_modelo[-6]
    Lista_Posicao5 = lista_modelo[-5]
    Lista_Posicao4 = lista_modelo[-4]
    Lista_Posicao3 = lista_modelo[-3]
    Lista_Posicao2 = lista_modelo[-2]
    Lista_Posicao1 = lista_modelo[-1]




    texto4 = Label(root,text= Lista_Posicao13,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=20,y=240)

    texto5 = Label(root,text= Lista_Posicao12 ,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=20,y=260)

    texto6 = Label(root,text= Lista_Posicao11,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=20,y=280)

    texto3 = Label(root,text= Lista_Posicao10,font=("Arial Black",11),background='black', foreground='white')
    texto3.place(x=20,y=300)

    texto4 = Label(root,text= Lista_Posicao9,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=20,y=320)

    texto5 = Label(root,text=  Lista_Posicao8,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=20,y=340)

    texto6 = Label(root,text= Lista_Posicao7,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=20,y=360)

    texto7 = Label(root,text= Lista_Posicao6 ,font=("Arial Black",11),background='black', foreground='white')
    texto7.place(x=20,y=380)

    texto8 = Label(root,text= Lista_Posicao5,font=("Arial Black",11),background='black', foreground='white')
    texto8.place(x=20,y=400)

    texto9 = Label(root,text= Lista_Posicao4,font=("Arial Black",11),background='black', foreground='white')
    texto9.place(x=20,y=420)

    texto10 = Label(root,text= Lista_Posicao3,font=("Arial Black",11),background='black', foreground='white')
    texto10.place(x=20,y=440)

    texto11 = Label(root,text= Lista_Posicao2,font=("Arial Black",11),background='black', foreground='white')
    texto11.place(x=20,y=460)

    texto12 = Label(root,text= Lista_Posicao1 ,font=("Arial Black",11),background='black', foreground='white')
    texto12.place(x=20,y=480)

#Exibe o tipo do Veiculo
def tipo():

    

    Lista_Posicao13 = carros_ou_caminhoes[-13]
    Lista_Posicao12 = carros_ou_caminhoes[-12]
    Lista_Posicao11 = carros_ou_caminhoes[-11]
    Lista_Posicao10 = carros_ou_caminhoes[-10]
    Lista_Posicao9 = carros_ou_caminhoes [-9]
    Lista_Posicao8 = carros_ou_caminhoes [-8]
    Lista_Posicao7 = carros_ou_caminhoes[-7]
    Lista_Posicao6 = carros_ou_caminhoes[-6]
    Lista_Posicao5 = carros_ou_caminhoes[-5]
    Lista_Posicao4 = carros_ou_caminhoes[-4]
    Lista_Posicao3 = carros_ou_caminhoes[-3]
    Lista_Posicao2 = carros_ou_caminhoes[-2]
    Lista_Posicao1 = carros_ou_caminhoes[-1]




    texto4 = Label(root,text= Lista_Posicao13,font=("Arial Black",10),background='black', foreground='white')
    texto4.place(x=300,y=240)

    texto5 = Label(root,text= Lista_Posicao12 ,font=("Arial Black",10),background='black', foreground='white')
    texto5.place(x=300,y=260)

    texto6 = Label(root,text= Lista_Posicao11,font=("Arial Black",10),background='black', foreground='white')
    texto6.place(x=300,y=280)

    texto3 = Label(root,text= Lista_Posicao10,font=("Arial Black",10),background='black', foreground='white')
    texto3.place(x=300,y=300)

    texto4 = Label(root,text= Lista_Posicao9,font=("Arial Black",10),background='black', foreground='white')
    texto4.place(x=300,y=320)

    texto5 = Label(root,text=  Lista_Posicao8,font=("Arial Black",10),background='black', foreground='white')
    texto5.place(x=300,y=340)

    texto6 = Label(root,text= Lista_Posicao7,font=("Arial Black",10),background='black', foreground='white')
    texto6.place(x=300,y=360)

    texto7 = Label(root,text= Lista_Posicao6 ,font=("Arial Black",10),background='black', foreground='white')
    texto7.place(x=300,y=380)

    texto8 = Label(root,text= Lista_Posicao5,font=("Arial Black",10),background='black', foreground='white')
    texto8.place(x=300,y=400)

    texto9 = Label(root,text= Lista_Posicao4,font=("Arial Black",10),background='black', foreground='white')
    texto9.place(x=300,y=420)

    texto10 = Label(root,text= Lista_Posicao3,font=("Arial Black",10),background='black', foreground='white')
    texto10.place(x=300,y=440)

    texto11 = Label(root,text= Lista_Posicao2,font=("Arial Black",10),background='black', foreground='white')
    texto11.place(x=300,y=460)

    texto12 = Label(root,text= Lista_Posicao1 ,font=("Arial Black",10),background='black', foreground='white')
    texto12.place(x=300,y=480)

#Exibe o valor do Veículo 
def valor():
    Lista_Posicao13 = lista_valor[-13]
    Lista_Posicao12 = lista_valor[-12]
    Lista_Posicao11 = lista_valor[-11]
    Lista_Posicao10 = lista_valor[-10]
    Lista_Posicao9 = lista_valor [-9]
    Lista_Posicao8 = lista_valor [-8]
    Lista_Posicao7 = lista_valor[-7]
    Lista_Posicao6 = lista_valor[-6]
    Lista_Posicao5 = lista_valor[-5]
    Lista_Posicao4 = lista_valor[-4]
    Lista_Posicao3 = lista_valor[-3]
    Lista_Posicao2 = lista_valor[-2]
    Lista_Posicao1 = lista_valor[-1]




    texto4 = Label(root,text= Lista_Posicao13,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=380,y=240)

    texto5 = Label(root,text= Lista_Posicao12 ,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=380,y=260)

    texto6 = Label(root,text= Lista_Posicao11,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=380,y=280)

    texto3 = Label(root,text= Lista_Posicao10,font=("Arial Black",11),background='black', foreground='white')
    texto3.place(x=380,y=300)

    texto4 = Label(root,text= Lista_Posicao9,font=("Arial Black",11),background='black', foreground='white')
    texto4.place(x=380,y=320)

    texto5 = Label(root,text=  Lista_Posicao8,font=("Arial Black",11),background='black', foreground='white')
    texto5.place(x=380,y=340)

    texto6 = Label(root,text= Lista_Posicao7,font=("Arial Black",11),background='black', foreground='white')
    texto6.place(x=380,y=360)

    texto7 = Label(root,text= Lista_Posicao6 ,font=("Arial Black",11),background='black', foreground='white')
    texto7.place(x=380,y=380)

    texto8 = Label(root,text= Lista_Posicao5,font=("Arial Black",11),background='black', foreground='white')
    texto8.place(x=380,y=400)

    texto9 = Label(root,text= Lista_Posicao4,font=("Arial Black",11),background='black', foreground='white')
    texto9.place(x=380,y=420)

    texto10 = Label(root,text= Lista_Posicao3,font=("Arial Black",11),background='black', foreground='white')
    texto10.place(x=380,y=440)

    texto11 = Label(root,text= Lista_Posicao2,font=("Arial Black",11),background='black', foreground='white')
    texto11.place(x=380,y=460)

    texto12 = Label(root,text= Lista_Posicao1 ,font=("Arial Black",11),background='black', foreground='white')
    texto12.place(x=380,y=480)

#Aumenta a barra de porcentagem do programa.
def progresso(aumento):
    percent.get()
    bar['value']+=aumento
    percent.set(f'{bar["value"]:.2f}%')
    root.update_idletasks()

#Encerra os processos.  
def Fechar():
    quit()

#Ativa a função de leitura em paralelo com outros processos
def ativar():
    leitura(filepath)

#Ativa a função de Start em paralelo com outros processos
def Inicio_principal():
    Thread(target=ativar).start()

#Ativa a função de OpenFile em paralelo com outros 
def abrir_arquivo():
    Thread(target=OpenFile).start()







root = Tk()
root.title('Coletor de dados FIPE.')
root.geometry("500x600")
root.configure(bg = "#000000")




texto1 = Label(root, text='Insira o arquivo que o programa irá ler.', font=("Arial Black",11),background='black', foreground='white')
texto1.place(x=20,y=20)

entry1 = Entry(root, font=("Arial",15),width=31)
entry1.place(x=20,y=50)

btn1 = Button(root, text='Open',command= abrir_arquivo, width=8)
btn1.place(x=380,y=50)




texto2 = Label(root,text='Escreva o nome do novo arquivo.',font=("Arial Black",11),background='black', foreground='white')
texto2.place(x=20,y=110)

btn2 = Button(root,command= salva_arquivo,text='Salvar', width=8)
btn2.place(x=380,y=140)

entry2 = Entry(root, font=("Arial",15),width=31)
entry2.place(x=20,y=140)





percent = StringVar(root,'0')

bar = Progressbar(root, orient=HORIZONTAL, length=300)
bar ['value'] = 0 
bar.place(x= 20, y=190)

percentLabel = Label(root,textvariable=percent)
percentLabel.place(x=400,y=190)


texto3 = Label(root,text= "MARCA                 /    MODELO    /   TIPO   /    PREÇO      ",font=("Arial Black",11),background='black', foreground='Yellow')
texto3.place(x=20,y=220)


btn3 = Button(root, text='Start',command= Inicio_principal ,width=8)
btn3.place(x=380,y=560)

btn4 = Button(root, text='Fechar',command= Fechar, width=8)
btn4.place(x=20,y=560)





root.mainloop()