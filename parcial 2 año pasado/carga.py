from vehiculos import *
class carga(vehiculos):
    __peso_carga:float
    def __init__(self, marca, modelo, patente, importebasico, cantidadkm, pesocarga):
        super().__init__(marca, modelo, patente, importebasico, cantidadkm)
        self.__peso_carga=pesocarga
    def getimportealquiler(self):
        if self._vehiculos__cant_km>100:
            imp=self._vehiculos__impor_bas+(self._vehiculos__impor_bas*((self._vehiculos__cant_km/10)/100))
            if self.__peso_carga>500:
                impf=imp+(imp*((self.__peso_carga/10)/100))
                return impf
            else:
                return imp
        else:
            return self._vehiculos__impor_bas
    def __str__(self):
        return f'{self._vehiculos__marca}{self._vehiculos__modelo}{self._vehiculos__patente}{self._vehiculos__impor_bas}{self._vehiculos__cant_km}{self.__peso_carga}'