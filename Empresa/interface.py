
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog



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

canvas = Canvas(
    tb1,
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

texto1 = Label(tb1, text='Insira o arquivo que o programa irá ler.',background='black', foreground='white',font=("Arial Black",11))
texto1.place(x=20,y=20)


entry1 = Entry(tb1, width=31,font=("Arial",15))
entry1.place(x=20,y=50)

btn1 = Button(tb1, text='Open', width=8)#font=('Arial',10))
btn1.place(x=380,y=50)

btn2 = Button(tb1, text='start' ,width=8)#font=('Arial',10))
btn2.place(x=380,y=340)

btn3 = Button(tb1, text='Stop', width=8)#font=('Arial',10))
btn3.place(x=20,y=340)

#Aba 2 =========================================== #

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

background_img2 = PhotoImage(file = r"C:\Users\Moltt\Documents\python\Empresa\Imagemusar2.png")
background2 = canvas2.create_image(
    232.0, 202.0,
    image=background_img2)

texto1 = Label(tb2, text='Insira o arquivo que o programa irá ler.',background='black', foreground='white',font=("Arial Black",11))
texto1.place(x=20,y=20)

entry1 = Entry(tb2,width=31,font=("Arial",15))
entry1.place(x=20,y=50)

btn1 = Button(tb2, text='Open', width=8)#font =('Arial',10)
btn1.place(x=380,y=50)

btn2 = Button(tb2, text='start' ,width=8)#font=('Arial',10))
btn2.place(x=380,y=340)

btn3 = Button(tb2, text='Stop', width=8)#font=('Arial',10))
btn3.place(x=20,y=340)



root.mainloop()