
from tkinter import *
from tkinter import filedialog
import tkinter as tk



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
canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 400,
    width = 480,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#root.wm_attributes('-transparentcolor', root['bg'])

background_img = PhotoImage(file = r"C:\Users\Moltt\Documents\python\Empresa\Imagemusar.png")
background = canvas.create_image(
    232.0, 202.0,
    image=background_img)


texto1 = Label(root, text='Insira o arquivo que o programa irá ler.', font=("Arial Black",11),background='black', foreground='white')
texto1.place(x=20,y=20)

entry1 = Entry(root, font=("Arial",15),width=31)
entry1.place(x=20,y=50)

btn1 = Button(root, text='Open', width=8,font=('Arial',10))
btn1.place(x=380,y=50)

btn2 = Button(root, text='start' ,width=8,font=('Arial',10))
btn2.place(x=380,y=360)

btn3 = Button(root, text='Stop', width=8,font=('Arial',10))
btn3.place(x=20,y=360)

root.mainloop()