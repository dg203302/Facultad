import tkinter as tk
from tkinter import messagebox
import subprocess
def apagado():
    messagebox.showinfo(title="apagado comenzado", message="empezo el apagado")
    subprocess.run("shutdown -s")
def reinicia():
    messagebox.showinfo(title="reinicio iniciado", message="comenzo el reinicio")
    subprocess.run("shutdown -r")
def cancelar():
    messagebox.showinfo(title="cancelar", message="cancelaste")
    subprocess.run("shutdown -a")
ven=tk.Tk()
ven.title("SCRIPT DE APAGADO")
ven.geometry("500x500")
ven.resizable(0,0)
ven.config(bg="black")
text1=tk.Label(text="menu apagado:")
text1.grid(row=1,column=1)
apa=tk.Button(ven,text="APAGAAAA", command=apagado, bg="red")
reini=tk.Button(ven,text="REINICIAA", command=reinicia, bg="blue")
canc=tk.Button(ven,text="CANCELAR", command=cancelar, bg="grey")
apa.grid(row=1,column=2)
reini.grid(row=1,column=3)
canc.grid(row=1,column=4)
text2=tk.Label(text="texto random:")
text2.grid(row=2,column=1)
cadena=tk.StringVar()
lect=tk.Entry(ven,textvariable=cadena)
lect.grid(row=2,column=2)
print(cadena)
ven.mainloop()