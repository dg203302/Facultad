from personal import *
class nodo:
    __datos:personal
    __siguiente:personal
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=None
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
    def get_datos(self):
        return self.__datos
    def get_siguiente(self):
        return self.__siguiente
    def __str__(self):
        print(self.__datos)