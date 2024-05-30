from vehiculos import *
class pasajeros(vehiculos):
    __cant_asientos:int
    def __init__(self, marca, modelo, patente, importebasico, cantidadkm, cantidadasientos):
        super().__init__(marca, modelo, patente, importebasico, cantidadkm)
        self.__cant_asientos=int(cantidadasientos)
    def getcantasient(self):
        return self.__cant_asientos
    def getimportealquiler(self):
        if self._vehiculos__cant_km>100:
            imp=self._vehiculos__impor_bas+(self._vehiculos__impor_bas*((self._vehiculos__cant_km/10)/100))
            if self.__cant_asientos>4:
                impf=imp+(imp*(1/100))
                return impf
            else:
                return imp
        else:
            return self._vehiculos__impor_bas
    def tojson(self):
        d=dict(tipo=__class__.__name__,atributos=dict(marca=self._vehiculos__marca,modelo=self._vehiculos__modelo,patente=self._vehiculos__patente,importebasico=self._vehiculos__impor_bas,cantidadkm=self._vehiculos__cant_km,cantidadasientos=self.__cant_asientos))
        return d
    def __str__(self):
        return f'{self._vehiculos__marca}{self._vehiculos__modelo}{self._vehiculos__patente}{self._vehiculos__impor_bas}{self._vehiculos__cant_km}{self.__cant_asientos}'