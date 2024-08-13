import pygame
import os
class sonidos:
    @classmethod
    def ejecutar_sonido(cls,sonido_a_ejecutar):
        pygame.init()
        pygame.mixer.init()
        ruta_base=os.path.dirname(os.path.abspath(__file__))
        exito=pygame.mixer.Sound(os.path.join(ruta_base, "exito.mp3"))
        iniciar=pygame.mixer.Sound(os.path.join(ruta_base, "iniciar.mp3"))
        if sonido_a_ejecutar=='toque':
            exito.play()
        elif sonido_a_ejecutar=='iniciar':
            iniciar.play()
    @classmethod
    def decir_boton(cls,indice_boton):
        pygame.init()
        pygame.mixer.init()
        ruta_base=os.path.dirname(os.path.abspath(__file__))
        color_1_teal=pygame.mixer.Sound(os.path.join(ruta_base, "TEAL.mp3"))
        color_2_red=pygame.mixer.Sound(os.path.join(ruta_base, "RED.mp3"))
        color_3_yellow=pygame.mixer.Sound(os.path.join(ruta_base, "YELLOW.mp3"))
        color_4_blue=pygame.mixer.Sound(os.path.join(ruta_base, "BLUE.mp3"))
        if indice_boton=='teal':
            color_1_teal.play()
        elif indice_boton=='red':
            color_2_red.play()
        elif indice_boton=='yellow':
            color_3_yellow.play()
        elif indice_boton=='blue':
            color_4_blue.play()
    @classmethod
    def musica_fondo(cls):
        pygame.init()
        pygame.mixer.init()
        ruta_base=os.path.dirname(os.path.abspath(__file__))
        pygame.mixer.music.load(os.path.join(ruta_base, "musica_fondo.mp3"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)