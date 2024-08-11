from ejemplo import *
class nodo:
    __datos:ejemplo
    __siguiente:ejemplo
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__datos
    def get_siguiente(self):
        return self.__siguiente