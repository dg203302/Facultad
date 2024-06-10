import tkinter as tk
from tkinter import messagebox
from jugador import *
from gestorjugadores import *
import random
import datetime
class simondice(tk.Tk):
    #atributos para botones
    __colores:list
    __secuencia:list
    __botones:list
    #atributos para botones
    #atributos para funcionalidad
    __indice:int
    __indiceverifi:int
    __puntaje:object
    __contador:int
    #atributos para funcionalidad
    #atributos para el jugador
    __jugadoractual:jugador
    __gestorjugadores:gestorjugadores
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('800x600')
        self.__canvas=tk.Canvas(self,width=800,height=600,confine=True)
        self.__canvas.grid(column=0,row=0)
        self.__canvas.columnconfigure(0,weight=1)
        self.__canvas.rowconfigure(0,weight=1)
        self.__botones=[]
        self.__indiceverifi=0
        self.__colores=['teal','red','yellow','blue']
        self.__secuencia=[]
        self.__contador=0
        self.resizable(width=False,height=False)
        self.__gestorjugadores=gestorjugadores()
        self.registrarjugador()
        self.crearbotones()
        botonini=self.crearbotonincio()
        botoncierre=self.crearbotoncierre()
#registrar jugador
    def salir(self):
        self.destroy()
    def registrar(self,nombre,ventana):
        if nombre.get()=='':
            messagebox.showinfo(message='ingrese su nombre',title='nombre no ingresado')
            return
        else:
            self.__jugadoractual=jugador(nombre.get())
            self.__puntaje=self.crearpuntaje()
            ventana.destroy()
    def registrarjugador(self):
        ventanaregistro=tk.Toplevel(self)
        ventanaregistro.title('registro')
        ventanaregistro.geometry('200x100')
        ventanaregistro.resizable(width=False,height=False)
        ventanaregistro.lift(self)
        ventanaregistro.grab_set()
        ventanaregistro.protocol("WM_DELETE_WINDOW", self.salir)
        textonombre=tk.Label(ventanaregistro,text='datos del jugador')
        textonombre.place(x=2,y=2)
        nombrejuga=tk.Label(ventanaregistro,text='jugador:')
        nombrejuga.place(x=2,y=40)
        nombre=tk.StringVar()
        ingreso=tk.Entry(ventanaregistro,textvariable=nombre)
        ingreso.place(x=50,y=40)
        botonini=tk.Button(ventanaregistro,text='iniciar juego',command=lambda: self.registrar(nombre,ventanaregistro))
        botonini.place(x=60,y=70)
#registrar jugador
#boton de inicio
    def crearbotonincio(self):
        boton=tk.Button(text='INICIAR JUEGO',bg='yellow', command=self.iniciarjuego)
        self.__canvas.create_window(70,25,anchor='center',window=boton)
        return boton
#boton de inicio
#boton de cierre
    def crearbotoncierre(self):
        boton=tk.Button(self,text='SALIR',bg='red',command=self.destroy)
        self.__canvas.create_window(750,25,anchor='center',window=boton)
        return boton
#boton de cierre
#puntaje
    def crearpuntaje(self):
        puntaje=tk.Label(self,fg="black")
        puntaje.config(text=f'{self.__jugadoractual.getnombre()}: {self.__contador}')
        self.__canvas.create_window(400,25,anchor='center',window=puntaje)
        return puntaje
#puntaje
#aumentar puntaje
    def aumentar(self):
        self.__contador+=1
        self.__puntaje.config(text=f'{self.__jugadoractual.getnombre()}:{self.__contador}')
#aumentar puntaje
#reiniciar puntaje
    def reiniciarpunta(self):
        fecha=str(datetime.date.today())
        hora=str(datetime.datetime.now().time())
        self.__jugadoractual.actpuntj(fecha,hora,self.__contador)
        self.__gestorjugadores.registrarpuntaje(self.__jugadoractual)
        self.__contador=0
        self.__puntaje.config(text=f'puntaje:{self.__contador}')
#reiniciar puntaje
#creacion de botones
    def crearbotones(self):
        for i in range(4):
            if i==0:
                boton = self.__canvas.create_arc(20, 50, 750, 580, start=90, extent=90, fill=self.__colores[i], outline='black')
                self.__canvas.tag_bind(boton, '<Button-1>', lambda event, i=i: self.verificarcolor(i))
            if i==1:
                boton = self.__canvas.create_arc(20, 50, 780, 580, start=0, extent=90, fill=self.__colores[i], outline='black')
                self.__canvas.tag_bind(boton, '<Button-1>', lambda event, i=i: self.verificarcolor(i))
            if i==2:
                boton = self.__canvas.create_arc(20, 80, 750, 580, start=180, extent=90, fill=self.__colores[i], outline='black')
                self.__canvas.tag_bind(boton, '<Button-1>', lambda event, i=i: self.verificarcolor(i))
            if i==3:
                boton = self.__canvas.create_arc(20, 80, 780, 580, start=270, extent=90, fill=self.__colores[i], outline='black')
                self.__canvas.tag_bind(boton, '<Button-1>', lambda event, i=i: self.verificarcolor(i))
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
            self.__canvas.itemconfig(self.__botones[self.__colores.index(coloract)],width=5)
            self.after(1500,self.ocultarcolor)
    def ocultarcolor(self):
            coloract=self.__secuencia[self.__indice]
            self.__canvas.itemconfig((self.__botones[self.__colores.index(coloract)]),width=0)
            self.__indice+=1
            self.iluminar()
    def iniciarjuego(self):
        self.generarsecuencia()
        self.iluminar()
#implementacion
if __name__=='__main__':
    ven=simondice()
    ven.mainloop()

    #hacer gestor para guardar puntajes, crear json y todo