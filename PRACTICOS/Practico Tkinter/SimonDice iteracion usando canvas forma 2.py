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
    __canvas:object
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('800x600')
        self.__canvas=tk.Canvas(width=800,height=600)
        self.__canvas.grid(row=0,column=0)
        self.__canvas.columnconfigure(0,weight=1)
        self.__canvas.rowconfigure(0,weight=1)
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
        boton.config(width=50,height=2)
        self.__canvas.create_window(200,25,anchor='center',window=boton)
        return boton
#boton de inicio
#boton de cierre
    def crearbotoncierre(self):
        boton=tk.Button(self,text='SALIR',bg='red',command=self.destroy)
        boton.config(width=100,height=2)
        self.__canvas.create_window(400,570,anchor='center',window=boton)
        return boton
#boton de cierre
#puntaje
    def crearpuntaje(self):
        puntaje=tk.Label(self,fg="black")
        puntaje.config(text=f'puntaje: {self.__contador}',font=('Arial',20))
        self.__canvas.create_window(600,25,anchor='center',window=puntaje)
        return puntaje
#puntaje
#aumentar puntaje
    def aumentar(self):
        self.__contador+=1
        self.__puntaje.config(text=f'puntaje:{self.__contador}',font=('Arial',20))
#aumentar puntaje
#reiniciar puntaje
    def reiniciarpunta(self):
        self.__contador=0
        self.__puntaje.config(text=f'puntaje:{self.__contador}')
#reiniciar puntaje
#creacion de botones
    def crearbotones(self):
        for i in range(4):
            if i==0:
                boton=tk.Button(self,bg=self.__colores[i],command=lambda i=i: self.verificarcolor(i))
                boton.config(width=50,height=15)
                self.__canvas.create_window(20,50,anchor='nw',window=boton)
            elif i==1:
                boton=tk.Button(self,bg=self.__colores[i],command=lambda i=i: self.verificarcolor(i))
                boton.config(width=53,height=15)
                self.__canvas.create_window(400,50,anchor='nw',window=boton)
            elif i==2:
                boton=tk.Button(self,bg=self.__colores[i],command=lambda i=i: self.verificarcolor(i))
                boton.config(width=50,height=15)
                self.__canvas.create_window(20,300,anchor='nw',window=boton)
            elif i==3:
                boton=tk.Button(self,bg=self.__colores[i],command=lambda i=i: self.verificarcolor(i))
                boton.config(width=53,height=15)
                self.__canvas.create_window(400,300,anchor='nw',window=boton)
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