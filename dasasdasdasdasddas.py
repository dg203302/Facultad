import tkinter as tk
from tkinter import ttk
def abrir_ventana_secundaria():
    s_ven=tk.Toplevel()
    s_ven.title("TROLFACE CARAJO")
    s_ven.geometry("1280x720")
    bcr=tk.Button(s_ven,text="cerrar troleo", command=s_ven.destroy)
    bcr.grid(row=1,column=1)
    s_ven.mainloop()  
# Crear la ventana principal.
ventana_principal = tk.Tk()
ventana_principal.config(width=400, height=300)
ventana_principal.title("Ventana principal")
boton_abrir = ttk.Button(
    ventana_principal,
    text="Abrir ventana secundaria",
    command=abrir_ventana_secundaria
)
boton_abrir.place(x=100, y=100)
ventana_principal.mainloop() 