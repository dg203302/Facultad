#clase principal para crear la ventana base
import tkinter as tk
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('400x300')
        self.resizable(width=False,height=False)
        self.configure(bg='gray')
        #boton
        self.boton1 = tk.Button(self, text='Haz clic', command=self.mostrar_mensaje)
        self.boton1.pack()
        self.canvas1= tk.Canvas(self.boton1, width=100, height=50, bg='red')
        
        self.boton2 = tk.Button(self, text='Haz clic', command=self.mostrar_mensaje)
        self.boton2.pack()
        self.canvas2= tk.Canvas(self.boton2, width=100, height=50, bg='red')
        
        self.boton3 = tk.Button(self, text='Haz clic', command=self.mostrar_mensaje)
        self.boton3.pack()
        self.canvas3= tk.Canvas(self.boton3, width=100, height=50, bg='red')
        
        self.boton4 = tk.Button(self, text='Haz clic', command=self.mostrar_mensaje)
        self.boton4.pack()
        self.canvas4= tk.Canvas(self.boton4, width=100, height=50, bg='red')
        #boton
        #cosas
    def boton(self):
        print('boton tocado!')