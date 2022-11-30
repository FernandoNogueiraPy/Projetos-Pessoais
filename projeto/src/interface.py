from tkinter import * #Bliblioteca de interface
from tkinter.ttk import *
import threading
from src.extract import Iniciar, OpenFile, stop , iniciar2 




def inicio():
    threading.Thread(target=Iniciar).start()

def inicio2():
    threading.Thread(target=iniciar2).start()

def parar():
    threading.Thread(target=stop).start()

def progresso(progresso):
    percent.get()
    bar['value']+=progresso
    print(bar['value'])
    percent.set(f"{bar['value']:.2f}%")
    root.update_idletasks()

def salvar_nome():
    global nome_arquivo
    nome_arquivo = entry2.get()

def salvar_nome2():
    global nome_arquivo2
    nome_arquivo2 = entry4.get()
    


root = Tk()
root.title('Coletor de dados FIPE.')
root.geometry("480x400")



nb = Notebook(root)
nb.place(x=0,y=0,width=480,height=400)

tb1 = Frame(nb)
nb.add(tb1,text= 'Consulta FIPE')



canvas = Canvas(
    tb1,
    bg = "#ffffff",
    height = 400,
    width = 480,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = r"Imagemusar.png")
background = canvas.create_image(
    240.0, 202.0,
    image=background_img)



percent = StringVar(tb1,"0")

bar = Progressbar(tb1,orient=HORIZONTAL,length=300)
bar['value'] = 0
bar.place(x=20,y=150)

percentLabel = Label(tb1,textvariable=percent)
percentLabel.place(x=400, y=150)

texto1 = Label(tb1, text='Insira o arquivo que o programa irá ler.',font=("Arial Black",11),background='black', foreground='white')
texto1.place(x=20,y=20)

texto2 = Label(tb1, text='Insira o nome do arquivo que o programa deve salvar ',font=("Arial Black",11),background='black', foreground='white')
texto2.place(x=20,y= 80)
    
entry1 = Entry(tb1,font=("Arial",15),width=31)
entry1.place(x=20,y=50)

entry2 = Entry(tb1,font=("Arial",15),width=31)
entry2.place(x=20,y=110)

btn1 = Button(tb1, text='Open',command= OpenFile , width=8)
btn1.place(x=380,y=50)

btn4 = Button(tb1, text='Enviar',command= salvar_nome, width=8)
btn4.place(x=380,y=110)

btn2 = Button(tb1, text='Iniciar' ,command= inicio ,width=8)
btn2.place(x=380,y=300)

btn3 = Button(tb1, text='Parar', command= parar, width=8)
btn3.place(x=20,y=300)

# ================= ABA 2 - CONSULTA DÉBITOS - ABA 2 ====================== #

tb2 = Frame(nb)
nb.add(tb2,text='Consulta Débitos')

canvas2 = Canvas(
    tb2,
    bg = "#000000",
    height = 400,
    width = 480,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas2.place(x = 0, y = 0)

background_img2 = PhotoImage(file = r"Imagemusar2.png")
background2 = canvas2.create_image(
    232.0, 202.0,
    image=background_img2)

texto3 = Label(tb2, text='Insira o arquivo que o programa irá ler.',font=("Arial Black",11),background='black', foreground='white')
texto3.place(x=20,y=20)

texto4 = Label(tb2, text='Insira o nome do arquivo que o programa deve salvar ',font=("Arial Black",11),background='black', foreground='white')
texto4.place(x=20,y= 80)

entry3 = Entry(tb2,font=("Arial",15),width=31)
entry3.place(x=20,y=50)

entry4 = Entry(tb2,font=("Arial",15),width=31)
entry4.place(x=20,y=110)

btn5 = Button(tb2, text='Open',command= OpenFile , width=8)
btn5.place(x=380,y=50)

btn6 = Button(tb2, text='Enviar',command= inicio, width=8)
btn6.place(x=380,y=110)

btn7 = Button(tb2, text='Iniciar' ,command= inicio2 ,width=8)
btn7.place(x=380,y=300)

btn8 = Button(tb2, text='Parar', command= parar, width=8)
btn8.place(x=20,y=300)

#========================= ABA 3 - REGRAS DE USO - ABA 3 ================#

tb3 = Frame(nb)
nb.add(tb3,text='Regras de uso.')

texto11 = Label(tb3, text=""" Regras de uso, confira antes de usar.

O programa le arquivos execel apenas. 

O programa precisa que contenham todas as colunas
 no Excel que ele ira ler e preencher

O programa só iniciara com todas as colunas escritas 
em Letra maiscula de acordo o exemplo 
e contendo as mesmas colunas.
Exp : 

CONTRATO / RENAVAM / PLACA / MARCA / MODELO /
 ANO / FIPE / DEBITOS / DEBITOS TOTAIS

obs: Não ter espaço entre os nomes das colunas 
nem do lado esquerdo nem direito

exp : O sinal : * Simboliza o Espaço/Backspace  
Errado : [***CONTRATO***]
Correto : [CONTRATO]


""",font=("Arial",10),background='black', foreground='white')
texto1.place(x=0,y=0)






