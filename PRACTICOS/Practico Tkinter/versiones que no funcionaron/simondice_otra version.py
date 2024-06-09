import tkinter as tk
from tkinter import messagebox
import random
import time
class simondice(tk.Tk):
    __botones:list
    __canvas:object
    #__puntaje:object
    #__contador:int
    #gestor con todo (para varios usuarios corte para mostrar despues)
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('800x600')
        self.__canvas=tk.Canvas(self,bg='gray',width=800,height=600)
        self.__canvas.grid(column=0,row=0)
        #self.__contador=0
        self.__botones=[]
        self.resizable(width=False,height=False)
        self.crearbotones()
        #self.__puntaje=self.crearpuntaje()
        #boton de inicio
        #boton_inicio=tk.Button(text='INICIAR JUEGO',bg='yellow')
        #boton_inicio.grid(row=3, column=0, columnspan=1)
        #boton de inicio
        #boton de cierre
        #boton_cierre=tk.Button(self,text='SALIR',bg='red',command=self.destroy)
        #boton_cierre.grid(row=4,column=0,columnspan=2,sticky='nswe')
        #boton de cierre
    '''def crearpuntaje(self):
        puntaje=tk.Label(self,fg="black")
        puntaje.config(text=f'puntaje: {self.__contador}')
        puntaje.grid(row=3, column=1, columnspan=1)
        return puntaje'''
    def crearbotones(self):
        colores=['teal','red','yellow','blue']
        for i in range(4):
            boton=tk.Canvas.create_rectangle(self.__canvas,50, 50, 150, 100, fill='red')
            #boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
            #self.columnconfigure(i % 2,weight=1)
            #self.rowconfigure(i // 2,weight=1)
            self.__botones.append(boton)
    '''def aumentar(self):
        self.__contador+=1
        self.__puntaje.config(text=f'puntaje:{self.__contador}')'''
if __name__=='__main__':
    ven=simondice()
    ven.mainloop()