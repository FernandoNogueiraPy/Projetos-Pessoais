from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class meuaplicativo(App):
  def build(self):
    box = BoxLayout(orientation='vertical')
    label = Label(text='HELLO WORLD')
    label.font_size = 30

    btn = Button(text='Click Aqui')
    btn.font_size = 30

    if btn == True :
      print (' voce e lindo')

    else :
      print(' voce e normal ')



    box.add_widget(label)
    box.add_widget(btn)
    return box




meuaplicativo().run()