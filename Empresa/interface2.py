from tkinter import * #Bliblioteca de interface
from tkinter.ttk import *
from Funcao import * #Arquivo de funções.
import threading  #Essa bliblioteca usa um processador pra cada é multiprocessing




def inicio():
    threading.Thread(target=Iniciar).start()
    # threading.Thread(target=start).start()





# def start():
    # GB = 100
    # download = 0
    # speed = 1
    # while(download<GB):
    #     time.sleep(0.05)
    #     bar['value']+=(speed/GB)*100
    #     download+=speed
    #     percent.set(f"{download/GB*100}%")
    #     text.set(str(download)+"/"+str(GB)+" GB completed")
    #     root.update_idletasks()






root = Tk()
root.title('Coletor de dados FIPE.')
root.geometry("480x400")
root.configure(bg = "#ffffff")


canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 400,
    width = 480,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = r"C:\Users\Moltt\Documents\python\Empresa\Imagemusar.png")
background = canvas.create_image(
    232.0, 202.0,
    image=background_img)




percent = StringVar()
text = StringVar()

bar = Progressbar(root,orient=HORIZONTAL,length=300)
bar.place(x=20,y=150)

percentLabel = Label(root,textvariable=percent).pack()
taskLabel = Label(root,textvariable=text).pack()

texto1 = Label(root, text='Insira o arquivo que o programa irá ler.',font=("Arial Black",11),background='black', foreground='white')
texto1.place(x=20,y=20)

texto2 = Label(root, text='Insira o nome do arquivo que o programa deve salvar ',font=("Arial Black",11),background='black', foreground='white')
texto2.place(x=20,y= 80)

entry1 = Entry(root,font=("Arial",15),width=31)
entry1.place(x=20,y=50)

entry2 = Entry(root,font=("Arial",15),width=31)
entry2.place(x=20,y=110)

btn1 = Button(root,text='Open',command= OpenFile , width=8,font=('Arial',10))
btn1.place(x=380,y=50)

btn4 = Button(root, text='Enviar', width=8,font=('Arial',10))
btn4 = btn4.place(x=380,y=110)

btn2 = Button(root, text='Iniciar' ,command= inicio ,width=8,font=('Arial',10))
btn2.place(x=380,y=360)

btn3 = Button(root, text='Parar', command= stop , width=8,font=('Arial',10))
btn3.place(x=20,y=360)

root.mainloop()

