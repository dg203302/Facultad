from profesor_investigador import *
class nodo:
    __datos:persona
    __siguiente:persona
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def get_datos(self):
        return self.__datos
    def get_siguiente(self):
        return self.__siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente