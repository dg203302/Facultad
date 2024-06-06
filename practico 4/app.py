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
        self.boton=tk.Button(self,bg='red',command=self.boton)
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        self.boton.grid(row=0, column=0, **opts)

        #boton
        #cosas
    def boton(self):
        print('boton tocado!')
if __name__=='__main__':
    ven=app()
    ven.mainloop()