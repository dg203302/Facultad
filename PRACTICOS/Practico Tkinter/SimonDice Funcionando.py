import tkinter as tk
from tkinter import messagebox
import random
class simondice(tk.Tk):
    __colores:list
    __botones:list
    __secuencia:list
    __indice:int
    __indiceverifi:int
    __puntaje:object
    __contador:int
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('800x600')
        self.__botones=[]
        self.__indiceverifi=0
        self.__colores=['teal','red','yellow','blue']
        self.__secuencia=[]
        self.__contador=0
        self.resizable(width=False,height=False)
        self.crearbotones()
        self.__puntaje=self.crearpuntaje()
        botonini=self.crearbotonincio()
        botoncierre=self.crearbotoncierre()
#boton de inicio
    def crearbotonincio(self):
        boton=tk.Button(text='INICIAR JUEGO',bg='yellow', command=self.iniciarjuego)
        boton.grid(row=3, column=0, columnspan=1)
        return boton
#boton de inicio
#boton de cierre
    def crearbotoncierre(self):
        boton=tk.Button(self,text='SALIR',bg='red',command=self.destroy)
        boton.grid(row=4,column=0,columnspan=2,sticky='nswe')
        return boton
#boton de cierre
#puntaje
    def crearpuntaje(self):
        puntaje=tk.Label(self,fg="black")
        puntaje.config(text=f'puntaje: {self.__contador}')
        puntaje.grid(row=3, column=1, columnspan=1)
        return puntaje
#puntaje
#aumentar puntaje
    def aumentar(self):
        self.__contador+=1
        self.__puntaje.config(text=f'puntaje:{self.__contador}')
#aumentar puntaje
#reiniciar puntaje
    def reiniciarpunta(self):
        self.__contador=0
        self.__puntaje.config(text=f'puntaje:{self.__contador}')
#reiniciar puntaje
#creacion de botones
    def crearbotones(self):
        for i in range(4):
            boton=tk.Button(self,bg=self.__colores[i],command=lambda i=i: self.verificarcolor(i))
            boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
            self.columnconfigure(i % 2,weight=1)
            self.rowconfigure(i // 2,weight=1)
            self.__botones.append(boton)
    def verificarcolor(self,botontocado):
        if self.__secuencia==[]:
            messagebox.showinfo(title='juego no iniciado', message='debe iniciar el juego')
        else:
            colortoca=self.__colores[botontocado]
            if colortoca==self.__secuencia[self.__indiceverifi]:
                self.__indiceverifi+=1
                if self.__indiceverifi==len(self.__secuencia):
                    self.__secuencia.append(random.choice(self.__colores))
                    self.__indiceverifi=0
                    self.aumentar()
                    self.iluminar()
            else:
                messagebox.showinfo(title='GAME OVER', message='perdiste!')
                self.__indice=0
                self.reiniciarpunta()
                self.__secuencia=[]
#creacion de botones
#implementacion
    def generarsecuencia(self):
        self.__secuencia=[random.choice(self.__colores) for _ in range(1)]
        self.__indice=0
    def iluminar(self):
        if self.__indice<len(self.__secuencia):
            coloract=self.__secuencia[self.__indice]
            self.__botones[self.__colores.index(coloract)].config(state='active')
            self.after(1000,self.ocultarcolor)
    def ocultarcolor(self):
            coloract=self.__secuencia[self.__indice]
            self.__botones[self.__colores.index(coloract)].config(state='normal')
            self.__indice+=1
            self.iluminar()
    def iniciarjuego(self):
        self.generarsecuencia()
        self.iluminar()
#implementacion
if __name__=='__main__':
    ven=simondice()
    ven.mainloop()