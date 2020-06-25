from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
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

        fontstyle = tkFont.Font(family = 'Lucida Grande', size = 25)
        self.message = Label(text = 'El resultado es: ',font = fontstyle)
        self.message.grid(row = 4, column = 0,columnspan = 2, sticky = W + E)
        

    def calcular(self,valor):
        #self.message['text'] = ''
        try:
            valor = int(valor)
            a = Ent_rom.Enteros(valor)
            res = a.conver_Romanos()
            self.message['text'] = 'El resultado es: {}'.format(res)
        except:
            a = Rom_ent.Letras(valor)
            res = a.convertir()
            try:
                res = int(res)
                self.message['text'] = 'El resultado es: {}'.format(str(res))
            except:
                self.message['text'] = '{}'.format(res)
        #print(valor)


if __name__ == '__main__':
    window = Tk()
    Home(window)
    window.mainloop()