# from tkinter import *
# from tkinter.ttk import *
# from tkinter import filedialog
# from src.Separar import leitura
# import threading


def inicio():
    threading.Thread(target=leitura).start()


# def progresso(progresso):
#     percent.get()
#     bar['value']+=progresso
#     print(bar['value'])
#     percent.set(f"{bar['value']:.2f}%")
#     root.update_idletasks()


def OpenFile():
    filepath = filedialog.askopenfilename()
    print(filepath)
    local_arquivo = Label(root, text=filepath,font=("Arial",8))
    local_arquivo.place(x=20,y=85)
    entry1.insert(0,filepath)
   


root = Tk()
root.title('Coletor de dados FIPE.')
root.geometry("480x400")
root.configure(bg = "#ffffff")



nb = Notebook(root)
nb.place(x=0,y=0,width=480,height=400)

tb1 = Frame(nb)
nb.add(tb1,text= 'Consulta FIPE')


percent = StringVar(tb1,"0")

bar = Progressbar(tb1,orient=HORIZONTAL,length=300)
bar['value'] = 0
bar.place(x=20,y=150)

texto1 = Label(tb1, text='Insira o arquivo que o programa irá ler.',background='black', foreground='white',font=("Arial Black",11))
texto1.place(x=20,y=20)


entry1 = Entry(tb1, width=31,font=("Arial",15))
entry1.place(x=20,y=50)

btn1 = Button(tb1, text='Open', command= OpenFile, width=8)
btn1.place(x=380,y=50)

btn2 = Button(tb1, text='Start', command= leitura ,width=8)
btn2.place(x=380,y=340)

btn3 = Button(tb1, text='Stop', width=8)
btn3.place(x=20,y=340)


root.mainloop()