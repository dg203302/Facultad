class nodo:
    __dat:object
    __sig:object
    def __init__(self,dat=None,sig=None):
        self.__dat=dat
        self.__sig=sig
    def getdat(self):
        return self.__dat
    def getsig(self):
        return self.__sig
    def actsig(self,nodo):
        self.__sig=nodo