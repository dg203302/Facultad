import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pydub import AudioSegment
from pydub.playback import play 
def valida(tex):
    return tex.isdecimal()
def chiwenwen(n):
    if n == 1:
        messagebox.showinfo(message="el culo te vacuno carajooo", title="chinwenwencheada")
    elif n == 4:
        messagebox.showinfo(message="te ponen", title="chinwenwencheada")
    elif n == 5:
        messagebox.showinfo(message="por el culo te la hinco", title="chinwenwencheada")
    elif n == 7 | n == 20:
        messagebox.showinfo(message="en el culo la siente", title="chinwenwencheada")
    elif n == 8:
        messagebox.showinfo(message="el culo te abrocho", title="chinwenwencheada")
    elif n == 9:
        messagebox.showinfo(message="en el culo te la mueve", title="chinwenwencheada")
    elif n == 11:
        messagebox.showinfo(message="chupalo entonce", title="chinwenwencheada")
    elif n == 12:
        messagebox.showinfo(message="chupalo entonce", title="chinwenwencheada")
    elif n == 13:
        messagebox.showinfo(message="en el culo te crece", title="chinwenwencheada")
    elif n == 15:
        messagebox.showinfo(message="en el culo tenes un esguince", title="chinwenwencheada")
def suma():
    n=int(int(n1.get())+int(n2.get()))
    messagebox.showinfo(message=n, title='RESULTADO DE LA SUMA')
    chiwenwen(n)
    return
def resta():
    n=int(int(n1.get())-int(n2.get()))
    messagebox.showinfo(message=n, title='RESULTADO DE LA RESTA')
    chiwenwen(n)
    return
def multiplic():
    n=int(int(n1.get())*int(n2.get()))
    messagebox.showinfo(message=n, title='RESULTADO DE LA MULTIPLICACION')
    chiwenwen(n)
    return
def gemidos():
    s_ven=tk.Toplevel()
    s_ven.title("TROLFACE CARAJO")
    s_ven.geometry("500x500")
    son=AudioSegment.from_wav("C:/Users/Lolma/Downloads/gemidos.wav")
    img=tk.PhotoImage(file="C:/Users/Lolma/Documents/Codigos/Python/trolface.gif")
    imag=tk.Label(s_ven,image=img).pack()
    play(son)
    bcr=ttk.Button(s_ven,text="Cerrar ventana",command=s_ven.destroy)
    bcr.grid(row=1,column=1)
    return
def cierre():
    ven.destroy()
#DECLARACION DE LA VENTANA
ven=tk.Tk()
ven.title("CALCULADORA PETONA")
ven.geometry("120x220")
ven.resizable(0,0)
ven.config(bg="black")
#TITULOS
text1=tk.Label(text="OPERACIONES")
text1.grid(row=4,column=1)
text2=tk.Label(text="NUMEROS:")
text2.grid(row=1,column=1)
#INGRESO DE NUMEROS
n1=ttk.Entry(validate="key", validatecommand=(ven.register(valida), "%S"), justify=tk.CENTER)
n1.grid(row=2,column=1)
n2=ttk.Entry(validate="key", validatecommand=(ven.register(valida), "%S"), justify=tk.CENTER)
n2.grid(row=3,column=1)
#OPERACIONES
sum=tk.Button(ven,text="SUMA", command=suma, bg="red")
res=tk.Button(ven,text="RESTA", command=resta, bg="blue")
mul=tk.Button(ven,text="MULTIPLICACION", command=multiplic, bg="grey")
sum.grid(row=5,column=1)
res.grid(row=6,column=1)
mul.grid(row=7,column=1)
#OPERACIONES TROLL
gem=tk.Button(ven,text="ALGO ESPECIAL", command=gemidos)
gem.grid(row=10, column=1)
#BOTON DE CIERRE
cier=tk.Button(text="SALIR", command=cierre)
cier.grid(row= 13,column= 1)
ven.mainloop()