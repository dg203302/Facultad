from abc import ABC
class servicio(ABC):
    __nomemp:str
    __nomcont:str
    __direccont:str
    __fechaserv:str
    __comision:float
    def __init__(self,nome,nomc,direc,fec,comi):
        self.__nomemp=nome
        self.__nomcont=nomc
        self.__direccont=direc
        self.__fechaserv=fec
        self.__comision=float(comi)
    def getcontra(self):
        return self.__nomcont
    def getfechacon(self):
        return self.__fechaserv
    def getcosto(self):
        pass
    def tojson(self):
        pass