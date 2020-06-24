from tkinter import ttk
from tkinter import *

class Home:
    def __init__(self,window):
        self.ven = window
        self.ven.title('Conversor')

if __name__ == '__main__':
    window = Tk()
    Home(window)
    window.mainloop()