class nodo:
    __dat:object
    __sig:object
    def __init__(self,dat=None,sig=None):
        self.__dat=dat
        self.__sig=sig
    def actsig(self,nodosig):
        self.__sig=nodosig
    def getdat(self):
        return self.__dat
    def getsig(self):
        return self.__sig
    def __str__(self):
        return f'{self.__dat}'