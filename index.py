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
        #Ingreso de Numeros tanto en Romanos como Enteros
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
            #intentar convertir el valor recibido a un numero entero
            valor = int(valor)
            #Si la conversion es exitosa se instancia la clase Ent_rom
            a = Ent_rom.Enteros(valor)
            #Se llama a la funcion para convertir a numeros romanos y esta se almacena en res
            res = a.conver_Romanos()
            #Por ultimo se imprime los resultados
            self.message['text'] = 'El resultado es: {}'.format(res)
        except:
            #En caso de que el valor no se pueda convertir a entero, se instancia la clase Rom_ent
            a = Rom_ent.Letras(valor)
            #Se llama a la funcion para convertir a numeros enteros
            res = a.convertir()
            try:
                #Aqui se pregunta si el resultao recibido es un numero o una cadena
                res = int(res)
                #Si es un numero se imprime acompañado del mensaje 'El resultado es: '
                self.message['text'] = 'El resultado es: {}'.format(str(res))
            except:
                #Si es un String se imprime directamente lo que se reciba en res
                self.message['text'] = '{}'.format(res)
        #print(valor)

#Se pregunta si el nombre del archivo en el que se esta ejecutando la aplicacion
#es igual a main
if __name__ == '__main__':
    #Si estamos en main se inicialiaz el constructor de interfaz
    window = Tk()
    #La clase home iniciara el formulario 
    Home(window)
    #main loop para que el formlario sea visible y no se pierda
    window.mainloop()