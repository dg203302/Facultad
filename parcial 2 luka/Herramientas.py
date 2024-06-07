from abc import ABC,abstractmethod
class herramientas(ABC):
    __marca:str
    __model:str
    __anio_fab:str
    __tip_comb:str
    __pote:str
    __cap_carg:str
    __tarif_alq:float
    __cant_dias:int
    def __init__(self,marc,mode,an,tipo,pot,capa,tari,canti):
        self.__marca=marc
        self.__model=mode
        self.__anio_fab=an
        self.__tip_comb=tipo
        self.__pote=pot
        self.__cap_carg=capa
        self.__tarif_alq=float(tari)
        self.__cant_dias=int(canti)
    def getcapa(self):
        return self.__cap_carg