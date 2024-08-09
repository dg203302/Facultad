from trabajador import *
class nodo:
    __datos:trabajdor
    __siguiente:trabajdor
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
    def get_datos(self):
        return self.__datos
    def get_siguiente(self):
        return self.__siguiente