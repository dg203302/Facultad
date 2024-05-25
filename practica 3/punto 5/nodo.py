class nodo:
    __dat:object
    __sig:object
    def __init__(self,datos=None,sig=None):
        self.__dat=datos
        self.__sig=sig
    def getsig(self):
        return self.__sig
    def agregsig(self,nodo):
        self.__sig=nodo
    def getdat(self):
        return self.__dat
    def __str__(self):
        return f'{self.__dat}'