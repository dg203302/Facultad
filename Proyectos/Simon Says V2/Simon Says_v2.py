import tkinter as tk
from tkinter import messagebox,ttk
from jugador import *
from gestorjugadores import *
import random
import datetime
from sonidos import *
class simondice(tk.Tk):
    __colores:list
    __secuencia:list
    __botones:list
    __indice:int
    __indiceverifi:int
    __puntaje:object
    __jugadoractual:jugador
    __gestorjugadores:gestorjugadores
    __jugadores:list
    __menu:object
    __box:object
    __idafter:object
    def __init__(self):
        super().__init__()
        self.title('SIMON SAYS     V1.5')
        self.geometry('800x600')
        self.__botones=[]
        self.__indiceverifi=0
        self.__colores=['teal','red','yellow','blue']
        self.__secuencia=[]
        self.__jugadores=[]
        self.resizable(width=False,height=False)
        self.__gestorjugadores=gestorjugadores()
        self.registrarjugador()
        self.crearbotones()
        self.crearmenu()
        self.crearboxdenivel()
        self.crearbotonincio()
        sonidos.musica_fondo()
        self.bind('<Escape>', lambda event: self.destroy())
    def limpiarjson(self):
        if self.__gestorjugadores.verificjson()==False or self.__jugadores==None:
            messagebox.showinfo(message='NO PLAYERS SAVED',title='ERROR')
        else:
            self.__gestorjugadores.limpiarjson()
            self.__jugadores=self.__gestorjugadores.getjugadores()
            self.__jugadores.sort()
            messagebox.showinfo(title='SCORES RESET', message='SCORES RESET SUCESSFULLY')
    def crearboxdenivel(self):
        self.__box=ttk.Combobox(self,values=('EASY','HARD','HARDCORE'))
        self.__box.place(x=640,y=552)
    def mostrarpuntajes(self):
        if self.__gestorjugadores.verificjson()==False:
            messagebox.showinfo(message='NO PLAYERS SAVED',title='ERROR')
        else:
            ventanamuestra=tk.Toplevel(self)
            ventanamuestra.geometry('510x285')
            ventanamuestra.resizable(width=False,height=False)
            ventanamuestra.grab_set()
            ventanamuestra.lift(self)
            texto=tk.Label(ventanamuestra,text='SCORES GALLERY')
            texto.place(x=150,y=5)
            jugadores=self.__gestorjugadores.getjugadores()
            jugadores.sort()
            menucontextual = ttk.Treeview(ventanamuestra, columns=("PLAYER", "DATE", "TIME", "SCORE", "DIFICULTY"), show='headings')
            menucontextual.place(x=0,y=25)
            menucontextual.heading('#1',text='PLAYER')
            menucontextual.heading('#2',text='DATE')
            menucontextual.heading('#3',text='TIME')
            menucontextual.heading('#4',text='SCORE')
            menucontextual.heading('#5',text='DIFICULTY')
            for jugador in jugadores:
                menucontextual.insert('','end',values=(jugador.getnombre(),jugador.getfecha(),jugador.gethora(),jugador.getpuntaje(),jugador.getnivel()))
            menucontextual.column('#1',width=100)
            menucontextual.column('#2',width=100)
            menucontextual.column('#3',width=100)
            menucontextual.column('#4',width=100)
            menucontextual.column('#5',width=100)
            botoncierre=tk.Button(ventanamuestra,text='CLOSE',bg='red',command=ventanamuestra.destroy)
            botoncierre.place(x=180,y=257)
    def crearmenu(self):
        self.__menu=tk.Menu(self)
        self.config(menu=self.__menu)
        menupuntajes=tk.Menu(self.__menu)
        self.__menu.add_cascade(menu=menupuntajes,label='SCORES')
        menupuntajes.add_command(label='SHOW SCORES',command=self.mostrarpuntajes)
        menupuntajes.add_command(label='CLEAN SCORES', command=self.limpiarjson)
        menupuntajes.add_separator()
        menupuntajes.add_command(label='EXIT',command=self.destroy)
    def salir(self):
        self.destroy()
    def registrar(self,nombre,ventana):
        if nombre.get()=='':
            messagebox.showinfo(message='ENTER A NAME',title='NAME MISSING')
            return
        else:
            self.__jugadoractual=jugador(nombre.get())
            self.__puntaje=self.crearpuntaje()
            ventana.destroy()
    def registrarjugador(self):
        ventanaregistro=tk.Toplevel(self)
        ventanaregistro.title('PLAYER REGISTRY')
        ventanaregistro.geometry('200x100')
        ventanaregistro.resizable(width=False,height=False)
        ventanaregistro.lift(self)
        ventanaregistro.grab_set()
        ventanaregistro.bind('<Escape>', lambda event: self.destroy())
        ventanaregistro.protocol("WM_DELETE_WINDOW", self.salir)
        textonombre=tk.Label(ventanaregistro,text='PLAYER DATA')
        textonombre.place(x=2,y=2)
        nombrejuga=tk.Label(ventanaregistro,text='NAME:')
        nombrejuga.place(x=2,y=40)
        nombre=tk.StringVar()
        ingreso=tk.Entry(ventanaregistro,textvariable=nombre)
        ingreso.place(x=50,y=40)
        botonini=tk.Button(ventanaregistro,text='ENTER GAME',bg='white',command=lambda: self.registrar(nombre,ventanaregistro))
        ventanaregistro.bind('<Return>', lambda event: self.registrar(nombre,ventanaregistro))
        botonini.place(x=60,y=70)
    def crearbotonincio(self):
        boton=tk.Button(text='START',bg='yellow', command=self.iniciarjuego)
        boton.grid(row=3, column=0, columnspan=1)
    def crearpuntaje(self):
        puntaje=tk.Label(self,fg="black")
        puntaje.config(text=f'{self.__jugadoractual.getnombre()}: {self.__jugadoractual.getpuntaje()}')
        puntaje.place(x=400,y=552)
        return puntaje
    def aumentar(self):
        self.__jugadoractual.actpuntaje()
        self.__puntaje.config(text=f'{self.__jugadoractual.getnombre()}:{self.__jugadoractual.getpuntaje()}')
    def reiniciarpunta(self):
        fecha=str(datetime.date.today())
        hora=datetime.datetime.now().time()
        hora_asignar=hora.strftime("%H:%M")
        self.__jugadoractual.registrarjugada(fecha,hora_asignar)
        self.__gestorjugadores.agregarjugada(self.__jugadoractual)
        self.__gestorjugadores.guardarjson()
        self.__jugadores=self.__gestorjugadores.getjugadores()
        self.__jugadores.sort()
        self.__jugadoractual=jugador(self.__jugadoractual.getnombre())
        self.__puntaje.config(text=f'{self.__jugadoractual.getnombre()}:{self.__jugadoractual.getpuntaje()}')
    def crearbotones(self):
        for i in range(4):
            boton=tk.Button(self,bg=self.__colores[i],borderwidth=5,command=lambda i=i: self.verificarcolor(i))
            boton.grid(row=i // 2, column=i % 2, sticky='nswe', padx=10, pady=10)
            self.columnconfigure(i % 2,weight=1)
            self.rowconfigure(i // 2,weight=1)
            self.__botones.append(boton)
    def fueradetiempo(self):
        messagebox.showinfo(title='GAME OVER', message='TIME OVER!')
        self.__indice=0
        self.__indiceverifi=0
        self.reiniciarpunta()
        self.__secuencia=[]
    def temporizar(self, toque):
        if toque=='iniciar':
            self.__idafter=self.after(5000,self.fueradetiempo)
        elif toque=='toque':
            self.after_cancel(self.__idafter)
            self.__idafter=self.after(5000,self.fueradetiempo)
        elif toque=='perder':
            self.after_cancel(self.__idafter)
    def verificarcolor(self,botontocado):
        if self.__secuencia==[]:
            messagebox.showinfo(title='GAME NOT STARTED', message='PLEASE START')
        else:
            if self.__jugadoractual.getnivel()=='HARD' or self.__jugadoractual.getnivel()=='HARDCORE':
                colortoca=self.__colores[botontocado]
                sonidos.ejecutar_sonido('toque')
                if colortoca==self.__secuencia[self.__indiceverifi]:
                    self.__indiceverifi+=1
                    if self.__indiceverifi==len(self.__secuencia):
                        self.__secuencia.append(random.choice(self.__colores))
                        self.__indiceverifi=0
                        self.aumentar()
                        self.iluminar()
                        self.temporizar('toque')
                else:
                    messagebox.showinfo(title='GAME OVER', message='YOU LOST!')
                    self.__indice=0
                    self.__indiceverifi=0
                    self.reiniciarpunta()
                    self.__secuencia=[]
                    self.temporizar('perder')
            elif self.__jugadoractual.getnivel()=='EASY':
                colortoca=self.__colores[botontocado]
                sonidos.ejecutar_sonido('toque')
                if colortoca==self.__secuencia[self.__indiceverifi]:
                    self.__indiceverifi+=1
                    if self.__indiceverifi==len(self.__secuencia):
                        self.__secuencia.append(random.choice(self.__colores))
                        self.__indiceverifi=0
                        self.aumentar()
                        self.iluminar()
                else:
                    messagebox.showinfo(title='GAME OVER', message='YOU LOST!')
                    self.__indice=0
                    self.__indiceverifi=0
                    self.reiniciarpunta()
                    self.__secuencia=[]
    def generarsecuencia(self):
        if self.__jugadoractual.getnivel()=='EASY' or self.__jugadoractual.getnivel()== 'HARD':
            self.__secuencia=[random.choice(self.__colores) for _ in range(1)]
            self.__indice=0
        else:
            self.__secuencia=[random.choice(self.__colores) for _ in range(2)]
            self.__indice=0
    def iluminar(self):
        if self.__indice<len(self.__secuencia) and self.__jugadoractual.getnivel()=='EASY':
            coloract=self.__secuencia[self.__indice]
            sonidos.decir_boton(coloract)
            self.__botones[self.__colores.index(coloract)].config(state='active')
            self.after(750,self.ocultarcolor)
        elif self.__indice<len(self.__secuencia) and (self.__jugadoractual.getnivel()=='HARD' or self.__jugadoractual.getnivel()=='HARDCORE'):
            coloract=self.__secuencia[self.__indice]
            sonidos.decir_boton(coloract)
            self.__botones[self.__colores.index(coloract)].config(state='active')
            self.after(300,self.ocultarcolor)
    def ocultarcolor(self):
            coloract=self.__secuencia[self.__indice]
            self.__botones[self.__colores.index(coloract)].config(state='normal')
            self.__indice+=1
            self.iluminar()
    def iniciarjuego(self):
        if self.__box.get()=='':
            messagebox.showinfo(title='ERROR', message='SELECT A DIFFICULTY')
            return
        else:
            self.__jugadoractual.actnivel(self.__box.get())
            sonidos.ejecutar_sonido('iniciar')
            if self.__jugadoractual.getnivel()=='EASY':
                self.generarsecuencia()
                self.iluminar()
            elif self.__jugadoractual.getnivel()=='HARD' or self.__jugadoractual.getnivel()=='HARDCORE':
                self.temporizar('iniciar')
                self.generarsecuencia()
                self.iluminar()
if __name__=='__main__':
    ven=simondice()
    ven.mainloop()