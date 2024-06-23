import tkinter as tk
from tkinter import messagebox,ttk
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
#atributos para funcionalidad
#atributos para el jugador
    __jugadoractual:jugador
    __gestorjugadores:gestorjugadores
#atributos para el jugador
#menu
    __menu:object
    __jugadores:list
#menu
#box de nivel
    __box:object
#box de nivel
#idafter
    __idafter:object
#idafter
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('800x605')
        self.__canvas=tk.Canvas(self,width=800,height=600,confine=True)
        self.__canvas.grid(column=0,row=0)
        self.__canvas.columnconfigure(0,weight=1)
        self.__canvas.rowconfigure(0,weight=1)
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
        botonini=self.crearbotonincio()
        self.bind('<Escape>', lambda event: self.destroy())
#creacion del box de menu
    def crearboxdenivel(self):
        self.__box=ttk.Combobox(self,values=('Principiante','Experto','SuperExperto'))
        self.__box.place(x=640,y=552)
#creacion del box de menu
#creacion del menu
    def mostrarpuntajes(self):
        if self.__gestorjugadores.verificjson()==False:
            messagebox.showinfo(message='no hay jugadores registrados',title='error')
        else:
            ventanamuestra=tk.Toplevel(self)
            ventanamuestra.geometry('405x285')
            ventanamuestra.resizable(width=False,height=False)
            ventanamuestra.grab_set()
            ventanamuestra.lift(self)
            texto=tk.Label(ventanamuestra,text='Galeria de Puntajes')
            texto.place(x=150,y=5)
            self.__jugadores=self.__gestorjugadores.getjugadores()
            self.__jugadores.sort()
            menucontextual = ttk.Treeview(ventanamuestra, columns=("Jugador", "Fecha", "Hora", "Puntaje"), show='headings')
            menucontextual.place(x=0,y=25)
            menucontextual.heading('#1',text='Jugador')
            menucontextual.heading('#2',text='fecha')
            menucontextual.heading('#3',text='hora')
            menucontextual.heading('#4',text='puntaje')
            for jugador in self.__jugadores:
                menucontextual.insert('','end',values=(jugador.getnombre(),jugador.getfecha(),jugador.gethora(),jugador.getpuntaje()))
            menucontextual.column('#1',width=100)
            menucontextual.column('#2',width=100)
            menucontextual.column('#3',width=100)
            menucontextual.column('#4',width=100)
            botoncierre=tk.Button(ventanamuestra,text='Cerrar',bg='red',command=ventanamuestra.destroy)
            botoncierre.place(x=180,y=257)
    def crearmenu(self):
        self.__menu=tk.Menu(self)
        self.config(menu=self.__menu)
        menupuntajes=tk.Menu(self.__menu)
        self.__menu.add_cascade(menu=menupuntajes,label='Puntajes')
        menupuntajes.add_command(label='Ver Puntajes',command=self.mostrarpuntajes)
        menupuntajes.add_separator()
        menupuntajes.add_command(label='Salir',command=self.destroy)
#creacion del menu
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
        botonini=tk.Button(ventanaregistro,text='iniciar juego',bg='white',command=lambda: self.registrar(nombre,ventanaregistro))
        ventanaregistro.bind('<Return>', lambda event: self.registrar(nombre,ventanaregistro))
        botonini.place(x=60,y=70)
#registrar jugador
#boton de inicio
    def crearbotonincio(self):
        boton=tk.Button(text='INICIAR JUEGO',bg='yellow', command=self.iniciarjuego)
        self.__canvas.create_window(400,328,anchor='center',window=boton)
        return boton
#boton de inicio
#puntaje
    def crearpuntaje(self):
        puntaje=tk.Label(self,fg="black")
        puntaje.config(text=f'{self.__jugadoractual.getnombre()}: {self.__jugadoractual.getpuntaje()}',font=('Arial',20))
        self.__canvas.create_window(400,25,anchor='center',window=puntaje)
        return puntaje
#puntaje
#aumentar puntaje
    def aumentar(self):
        self.__jugadoractual.actpuntaje()
        self.__puntaje.config(text=f'{self.__jugadoractual.getnombre()}:{self.__jugadoractual.getpuntaje()}')
#aumentar puntaje
#reiniciar puntaje
    def reiniciarpunta(self):
        fecha=str(datetime.date.today())
        hora=str(datetime.datetime.now().time())
        self.__jugadoractual.registrarjugada(fecha,hora)
        self.__gestorjugadores.agregarjugada(self.__jugadoractual)
        self.__gestorjugadores.guardarjson()
        self.__jugadores=self.__gestorjugadores.getjugadores()
        self.__jugadores.sort()
        self.__jugadoractual=jugador(self.__jugadoractual.getnombre())
        self.__puntaje.config(text=f'{self.__jugadoractual.getnombre()}:{self.__jugadoractual.getpuntaje()}')
#reiniciar puntaje
#creacion de puntaje
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
                boton = self.__canvas.create_arc(20, 100, 750, 580, start=180, extent=90, fill=self.__colores[i], outline='black')
                self.__canvas.tag_bind(boton, '<Button-1>', lambda event, i=i: self.verificarcolor(i))
            if i==3:
                boton = self.__canvas.create_arc(20, 100, 780, 580, start=270, extent=90, fill=self.__colores[i], outline='black')
                self.__canvas.tag_bind(boton, '<Button-1>', lambda event, i=i: self.verificarcolor(i))
            self.__botones.append(boton)
#temporizador
    def fueradetiempo(self):
        messagebox.showinfo(title='GAME OVER', message='perdiste por tiempo!')
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
#temporizador
#verificar colores
    def verificarcolor(self,botontocado):
        if self.__secuencia==[]:
            messagebox.showinfo(title='juego no iniciado', message='debe iniciar el juego')
        else:
            if self.__jugadoractual.getnivel()=='Experto' or self.__jugadoractual.getnivel()=='SuperExperto':
                colortoca=self.__colores[botontocado]
                if colortoca==self.__secuencia[self.__indiceverifi]:
                    self.__indiceverifi+=1
                    if self.__indiceverifi==len(self.__secuencia):
                        self.__secuencia.append(random.choice(self.__colores))
                        self.__indiceverifi=0
                        self.aumentar()
                        self.iluminar()
                        self.temporizar('toque')
                else:
                    messagebox.showinfo(title='GAME OVER', message='perdiste!')
                    self.__indice=0
                    self.__indiceverifi=0
                    self.reiniciarpunta()
                    self.__secuencia=[]
                    self.temporizar('perder')
            elif self.__jugadoractual.getnivel()=='Principiante':
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
                    self.__indiceverifi=0
                    self.reiniciarpunta()
                    self.__secuencia=[]
#verificar colores
#creacion de botones
#implementacion
#generacion de secuencia de colores
    def generarsecuencia(self):
        if self.__jugadoractual.getnivel()=='Principiante' or self.__jugadoractual.getnivel()== 'Experto':
            self.__secuencia=[random.choice(self.__colores) for _ in range(1)]
            self.__indice=0
        else:
            self.__secuencia=[random.choice(self.__colores) for _ in range(2)]
            self.__indice=0
#generacion de secuencia de colores
#iluminar y ocultar colores
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
#iluminar y ocultar colores
    def iniciarjuego(self):
        if self.__box.get()=='':
            messagebox.showinfo(title='error', message='debe seleccionar una dificultad')
            return
        else:
            self.__jugadoractual.actnivel(self.__box.get())
            if self.__jugadoractual.getnivel()=='Principiante':
                self.generarsecuencia()
                self.iluminar()
            elif self.__jugadoractual.getnivel()=='Experto' or self.__jugadoractual.getnivel()=='SuperExperto':
                self.temporizar('iniciar')
                self.generarsecuencia()
                self.iluminar()
#implementacion
if __name__=='__main__':
    ven=simondice()
    ven.mainloop()

    #hacer gestor para guardar puntajes, crear json y todo