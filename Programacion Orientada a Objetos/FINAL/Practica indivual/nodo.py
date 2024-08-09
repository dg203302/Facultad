class nodo:
    __clientes:object
    __siguiente:object
    def __init__(self, clientes=None, siguiente=None):
        self.__clientes=clientes
        self.__siguiente=siguiente
    def actualizar_siguiente(self,nodo_siguiente):
        self.__siguiente=nodo_siguiente
    def obtener_datos(self):
        return self.__clientes
    def obtener_siguiente(self):
        return self.__siguiente