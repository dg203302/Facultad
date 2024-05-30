from abc import ABC
class vehiculos(ABC):
    __marca:str
    __modelo:str
    __patente:str
    __impor_bas:float
    __cant_km:float
    def __init__(self,marca,modelo,patente,importebasico,cantidadkm):
        self.__marca=marca
        self.__modelo=modelo
        self.__patente=patente
        self.__impor_bas=float(importebasico)
        self.__cant_km=float(cantidadkm)
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getkm(self):
        return self.__cant_km
    def getimportealquiler(self):
        if self.__cant_km>100:
            imp=self.__impor_bas+(self.__impor_bas*((self.__cant_km/10)/100))
            return imp
        else:
            return self.__impor_bas