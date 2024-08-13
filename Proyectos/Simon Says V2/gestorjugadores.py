from encoder import *
class gestorjugadores:
    __jugadores:list
    __encoder:encoder
    def __init__(self):
        self.__jugadores=[]
        self.__encoder=encoder()
        self.__encoder.cargarjugadores(self)
    def getjugadores(self):
        return self.__jugadores
    def verificjson(self):
        try:
            juga=self.__jugadores[0]
        except IndexError:
            return False
        else:
            return True
    def cargarjugadores(self,jugador):
        self.__jugadores.append(jugador)
    def agregarjugada(self,jugador):
        self.__jugadores.append(jugador)
    def guardarjson(self):
        jugadas=dict(jugadores=[jugadores.tojson() for jugadores in self.__jugadores])
        self.__encoder.agregarajson(jugadas)
    def limpiarjson(self):
        self.__jugadores=[]
        self.__encoder.limpiar_jugadas()