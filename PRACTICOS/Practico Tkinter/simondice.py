import tkinter as tk
class simondice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('400x400')
        self.boton1=tk.Button(bg='teal')
        self.boton1.pack(side='left',fill='both',expand=True)
        self.boton2=tk.Button(bg='red')
        self.boton2.pack(side='right',fill='both',expand=True)
        self.boton3=tk.Button(bg='yellow')
        self.boton3.pack(side='left',fill='both',expand=True)
        self.boton4=tk.Button(bg='blue')
        self.boton4.pack(side='bottom',expand=True)
if __name__=='__main__':
    ven=simondice()
    ven.mainloop()