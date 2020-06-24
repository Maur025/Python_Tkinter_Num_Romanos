from tkinter import ttk
from tkinter import *

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

        ttk.Button(frame, text = 'Convertir').grid(row = 3, column = 1,columnspan = 3,sticky = E)

        self.message = Label(text = '')
        self.message.grid(row = 4, column = 0,columnspan = 2, sticky = W + E)


if __name__ == '__main__':
    window = Tk()
    Home(window)
    window.mainloop()