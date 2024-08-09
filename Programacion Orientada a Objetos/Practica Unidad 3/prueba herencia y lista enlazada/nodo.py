class nodo:
    __datos:object
    __siguiente:object
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def actsig(self,siguiente):
        self.__siguiente=siguiente
    def getsig(self):
        return self.__siguiente
    def __str__(self):
        return f'{self.__datos}'