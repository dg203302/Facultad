from encoder import *
class gestorjugadores:
    __jugadores:list
    __encoder:encoder
    def __init__(self):
        self.__jugadores=[]
        self.__encoder=encoder()
    def registrarpuntaje(self,jugador):
        self.__jugadores.append(jugador)
        self.agregar()
    def agregar(self):
        puntajes=dict(jugador=[jugadores.tojson() for jugadores in self.__jugadores])
        self.__encoder.tojson(puntajes)