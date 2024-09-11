from abc import ABC
class calefactor(ABC):
    __marca:str
    __modelo:str
    __paisfabri:str
    __pre_lista:float
    __form_pago:str
    __cant_cuot:int
    __prom:bool
    def __init__(self,marca,mode,pais,prec,fo,can,pr):
        self.__marca=marca
        self.__modelo=mode
        self.__paisfabri=pais
        self.__pre_lista=float(prec)
        self.__form_pago=fo
        self.__cant_cuot=int(can)
        self.__prom=pr
    def getprec(self):
        return self.__pre_lista
    def getmarc(self):
        return self.__marca
    def getmode(self):
        return self.__modelo
    def getprec(self):
        return self.__pre_lista
    def getprom(self):
        return self.__prom
    def getpais(self):
        return self.__paisfabri
    def getimpo(self):
        pass
    def tojson(self):
        pass
    def __lt__(self,otr):
        return self.__pre_lista<otr.__pre_lista
    def __eq__(self,otr):
        return self.__pre_lista==otr.__pre_lista