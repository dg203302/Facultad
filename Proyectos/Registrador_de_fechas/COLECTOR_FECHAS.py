import tkinter as tk
import datetime
from tkinter import ttk,messagebox
from gestor import *
class ventana_interaccion(tk.Tk):
    __gestor_de_fechas:gestor_fechas
    def __init__(self):
        super().__init__()
        self.title('Simon Dice')
        self.geometry('310x55')
        self.resizable(width=False,height=False)
        self.__gestor_de_fechas=gestor_fechas()
        self.generar_boton_registro()
        self.generar_boton_muestra_fechas()
        self.generar_boton_cierre()
        self.bind('<Escape>', lambda event: self.destroy())
    def salir_limpiando(self):
        self.__gestor_de_fechas.limpiar()
        self.destroy()
    def salir_guardando(self):
        self.__gestor_de_fechas.to_json()
        self.destroy()
    def salir(self):
        ventana_salir=tk.Toplevel(self)
        ventana_salir.geometry('310x55')
        ventana_salir.resizable(width=False,height=False)
        ventana_salir.grab_set()
        ventana_salir.lift(self)
        ventana_salir.resizable(width=False,height=False)
        texto=tk.Label(ventana_salir,text='desea limpiar el registro de fechas???')
        texto.grid(row=0,column=0)
        botonsi=tk.Button(ventana_salir,text='si',bg='red',command=self.salir_limpiando)
        botonsi.grid(row=1,column=0)
        botonno=tk.Button(ventana_salir,text='no',bg='green',command=self.salir_guardando)
        botonno.grid(row=1,column=1)
    def generar_boton_cierre(self):
        boton_cierre=tk.Button(self,text='SALIR',bg='white',command=self.salir)
        boton_cierre.place(x=138,y=30)
    def registrar(self):
        hora=datetime.datetime.now()
        hora_actual=hora.strftime("%H:%M")
        fecha_actual=str(datetime.date.today())
        nueva_fecha=datos_de_registro(hora_actual,fecha_actual)
        self.__gestor_de_fechas.insertar(nueva_fecha)
        messagebox.showinfo(message='FECHA REGISTRADA',title=f'se registro correctamente la fecha:{fecha_actual}, hora:{hora_actual}')
    def generar_boton_registro(self):
        boton_registro_fecha=tk.Button(self,text='REGISTRAR FECHA ACTUAL',bg='red',command=self.registrar)
        boton_registro_fecha.grid(row=0,column=0)
    def mostrar_fechas(self):
        if self.__gestor_de_fechas.verificar()==False:
            messagebox.showinfo(message='no hay fechas registrada!',title='MUY BIEN!')
        else:
            ventanamuestra=tk.Toplevel(self)
            ventanamuestra.geometry('202x290')
            ventanamuestra.resizable(width=False,height=False)
            ventanamuestra.grab_set()
            ventanamuestra.lift(self)
            texto=tk.Label(ventanamuestra,text='FECHAS')
            texto.place(x=80,y=5)
            jugadores=self.__gestor_de_fechas.get_fechas()
            menucontextual=ttk.Treeview(ventanamuestra, columns=("HORA","FECHA"), show='headings')
            menucontextual.place(x=0,y=25)
            menucontextual.heading('#1',text='HORA')
            menucontextual.heading('#2',text='FECHA')
            for jugador in jugadores:
                menucontextual.insert('','end',values=(jugador.get_hora(),jugador.get_dia()))
            menucontextual.column('#1',width=100)
            menucontextual.column('#2',width=100)
            botoncierre=tk.Button(ventanamuestra,text='Cerrar',bg='red',command=ventanamuestra.destroy)
            botoncierre.place(x=80,y=257)
    def generar_boton_muestra_fechas(self):
        boton_muestra_fecha=tk.Button(self,text='MOSTRAR FECHA ACTUAL',bg='blue',command=self.mostrar_fechas)
        boton_muestra_fecha.grid(row=0,column=1)
if __name__=='__main__':
    ven=ventana_interaccion()
    ven.mainloop()