from ..Puntos_pilas
class nodo:
    __dato:object
    __siguiente:object
    def __init__(self,dato=None,siguiente=-1):
        self.__dato=dato
        self.__siguiente=siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def get_siguiente(self):
        return self.__siguiente
class lista_cursores:
    __primero:nodo
    __espacions_disponibles:
    __cantidad_elementos:int
    def __init__(self,)