from paciente import *
class nodo:
    __datos:paciente
    __siguiente:paciente
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
    def get_siguiente(self):
        return self.__siguiente
    def get_datos(self):
        return self.__datos