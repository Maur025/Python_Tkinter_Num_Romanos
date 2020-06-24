from tkinter import ttk
from tkinter import *
import Ent_rom
import Rom_ent

class Home:
    def __init__(self,window):
        self.ven = window
        self.ven.title('Conversor')

        #creating frame container
        frame = LabelFrame(self.ven, text = 'Conversor de Numeros Romanos - Enteros')
        frame.grid(row = 0,column = 0,columnspan = 4, pady = 20)

        Label(frame, text = 'Numero: ').grid(row = 1, column = 0)
        self.number = Entry(frame)
        self.number.focus()
        self.number.grid(row = 1, column = 1)

        ttk.Button(frame, text = 'Convertir', command = lambda : self.calcular(self.number.get())).grid(row = 3, column = 1,columnspan = 3,sticky = E)

        self.message = Label(text = '')
        self.message.grid(row = 4, column = 0,columnspan = 2, sticky = W + E)

    def calcular(self,valor):
        #self.message['text'] = ''
        try:
            valor = int(valor)
            a = Ent_rom.Enteros(valor)
            a.conver_Romanos()
        except:
            a = Rom_ent.Letras(valor)
            a.convertir()
        #print(valor)


if __name__ == '__main__':
    window = Tk()
    Home(window)
    window.mainloop()