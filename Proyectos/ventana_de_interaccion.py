import tkinter as tk
from gestor import *
class ventana_interaccion(tk.Tk):
    __gestor_de_fechas:gestor_fechas
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('800x680')
if __name__=='__main__':
    ven=ventana_interaccion()
    ven.mainloop()