import tkinter as tk
from tkinter import messagebox
import random
class simondice(tk.Tk):
    __botones:list
    __toques:list
    __secuencia:list
    __puntaje:object
    __contador:int
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('800x600')
        self.__botones=[]
        self.__secuencia=[]
        self.__toques=[False,False,False,False]
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
#creacion de botones
    def crearbotones(self):
        for i in range(4):
            if i==0:
                boton=tk.Button(self,bg='teal',command=self.registrartoque1)
                boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
                self.columnconfigure(i % 2,weight=1)
                self.rowconfigure(i // 2,weight=1)
            elif i==1:
                boton=tk.Button(self,bg='red',command=self.registrartoque2)
                boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
                self.columnconfigure(i % 2,weight=1)
                self.rowconfigure(i // 2,weight=1)
            elif i==2:
                boton=tk.Button(self,bg='yellow',command=self.registrartoque3)
                boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
                self.columnconfigure(i % 2,weight=1)
                self.rowconfigure(i // 2,weight=1)
            elif i==3:
                boton=tk.Button(self,bg='blue',command=self.registrartoque4)
                boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
                self.columnconfigure(i % 2,weight=1)
                self.rowconfigure(i // 2,weight=1)
            self.__botones.append(boton)
    def registrartoque1(self):
        self.__toques[0]=True
    def registrartoque2(self):
        self.__toques[1]=True
    def registrartoque3(self):
        self.__toques[2]=True
    def registrartoque4(self):
        self.__toques[3]=True
#creacion de botones
#implementacion
    def generarsecuencia(self,nivel):
        botones=[1,2,3,4]
        self.__secuencia=[random.choice(botones) for _ in range(nivel)]
    def iluminar(self):
        for boton in self.__secuencia:
            if boton==1:
                self.__botones[0].config(bg='white')
                self.after(1000,lambda:self.__botones[0].config(bg='teal'))
            elif boton==2:
                self.__botones[1].config(bg='white')
                self.after(1000,lambda:self.__botones[1].config(bg='red'))
            elif boton==3:
                self.__botones[2].config(bg='white')
                self.after(1000,lambda:self.__botones[2].config(bg='yellow'))
            elif boton==4:
                self.__botones[3].config(bg='white')
                self.after(1000,lambda:self.__botones[3].config(bg='blue'))

    def iniciarjuego(self):
        nivel=1
        while True:
            self.generarsecuencia(nivel)
            self.iluminar()
            break
if __name__=='__main__':
    ven=simondice()
    ven.mainloop()