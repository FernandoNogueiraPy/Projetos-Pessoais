from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from time import sleep
from threading import Thread


Lista_Chat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    

def Start():

    final = 100
    comeco = 0

    final_completo = final -2

    for i in range(comeco,final):

        Lista_Posicao14 = Lista_Chat[-14]
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



        chat = i

        texto3 = Label(root,text= Lista_Posicao14,font=("Arial Black",11),background='black', foreground='white')
        texto3.place(x=20,y=220)

        texto4 = Label(root,text=Lista_Posicao13 ,font=("Arial Black",11),background='black', foreground='white')
        texto4.place(x=20,y=240)

        texto5 = Label(root,text= Lista_Posicao12 ,font=("Arial Black",11),background='black', foreground='white')
        texto5.place(x=20,y=260)

        texto6 = Label(root,text= Lista_Posicao11 ,font=("Arial Black",11),background='black', foreground='white')
        texto6.place(x=20,y=280)

        texto3 = Label(root,text= Lista_Posicao10,font=("Arial Black",11),background='black', foreground='white')
        texto3.place(x=20,y=300)

        texto4 = Label(root,text=Lista_Posicao9 ,font=("Arial Black",11),background='black', foreground='white')
        texto4.place(x=20,y=320)

        texto5 = Label(root,text= Lista_Posicao8 ,font=("Arial Black",11),background='black', foreground='white')
        texto5.place(x=20,y=340)

        texto6 = Label(root,text= Lista_Posicao7 ,font=("Arial Black",11),background='black', foreground='white')
        texto6.place(x=20,y=360)

        texto7 = Label(root,text= Lista_Posicao6 ,font=("Arial Black",11),background='black', foreground='white')
        texto7.place(x=20,y=380)

        texto8 = Label(root,text= Lista_Posicao5,font=("Arial Black",11),background='black', foreground='white')
        texto8.place(x=20,y=400)

        texto9 = Label(root,text=Lista_Posicao4 ,font=("Arial Black",11),background='black', foreground='white')
        texto9.place(x=20,y=420)

        texto10 = Label(root,text= Lista_Posicao3 ,font=("Arial Black",11),background='black', foreground='white')
        texto10.place(x=20,y=440)

        texto11 = Label(root,text= Lista_Posicao2 ,font=("Arial Black",11),background='black', foreground='white')
        texto11.place(x=20,y=460)

        texto12 = Label(root,text= Lista_Posicao1 ,font=("Arial Black",11),background='black', foreground='white')
        texto12.place(x=20,y=480)

        Lista_Chat.append(chat)

        global aumento
        aumento = 100/final
        
        progresso(aumento)

        if Lista_Posicao1 == final_completo:
            texto12 = Label(root,text= 'Todos os processos foram concluidos.' ,font=("Arial Black",11),background='black', foreground='white')
            texto12.place(x=20,y=500)

    

def progresso(aumento):
    percent.get()
    bar['value']+=aumento
    percent.set(f'{bar["value"]:.2f}%')
    root.update_idletasks()


def Fechar():
    quit()


def Inicio_principal():
    Thread(target=Start).start()


def OpenFile():
    filepath = filedialog.askopenfilename()
    print(filepath)
    local_arquivo = Label(root, text=filepath,font=("Arial",8))
    local_arquivo.place(x=20,y=85)
    entry1.insert(0,filepath)




chat = 0

root = Tk()
root.title('Coletor de dados FIPE.')
root.geometry("480x600")
root.configure(bg = "#000000")




texto1 = Label(root, text='Insira o arquivo que o programa irá ler.', font=("Arial Black",11),background='black', foreground='white')
texto1.place(x=20,y=20)

entry1 = Entry(root, font=("Arial",15),width=31)
entry1.place(x=20,y=50)

btn1 = Button(root, text='Open',command= OpenFile, width=8)
btn1.place(x=380,y=50)




texto2 = Label(root,text='Escreva o nome do novo arquivo.',font=("Arial Black",11),background='black', foreground='white')
texto2.place(x=20,y=110)

btn2 = Button(root, text='Salvar', width=8)
btn2.place(x=380,y=140)

entry2 = Entry(root, font=("Arial",15),width=31)
entry2.place(x=20,y=140)




percent = StringVar(root,'0')

bar = Progressbar(root, orient=HORIZONTAL, length=300)
bar ['value'] = 0 
bar.place(x= 20, y=190)

percentLabel = Label(root,textvariable=percent)
percentLabel.place(x=400,y=190)



btn3 = Button(root, text='Start',command= Inicio_principal ,width=8)
btn3.place(x=380,y=560)

btn4 = Button(root, text='Fechar',command= Fechar, width=8)
btn4.place(x=20,y=560)





root.mainloop()