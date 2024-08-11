from objeto_dato import *
class nodo:
    __dato:wachin
    __siguiente:wachin
    def __init__(self,dato=None,siguiente=None):
        self.__dato=dato
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def get_siguiente(self):
        return self.__siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente