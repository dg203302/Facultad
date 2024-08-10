from datos import *
class nodo:
    __datos=datos_de_registro
    __siguiente=datos_de_registro
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__datos
    def get_siguiente(self):
        return self.__siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente