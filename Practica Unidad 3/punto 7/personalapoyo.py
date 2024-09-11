from personal import *
class personalapoyo(personal):
    __categoria:int
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria,carrera='', cargo='', catedra='', area_investigacion='', tipo_investigacion='', categoria_incentivos='', importe_extra=''):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        self.__categoria=int(categoria)
    def getsueld(self):
        if self.__categoria>=1 and self.__categoria <=10:
            porc1=self._personal__sueld_bas+(self._personal__sueld_bas*(self._personal__antig/100))
            return porc1+(porc1*(10/100))
        elif self.__categoria>=11 and self.__categoria <=20:
            porc1=self._personal__sueld_bas+(self._personal__sueld_bas*(self._personal__antig/100))
            return porc1+(porc1*(20/100))
        elif self.__categoria>=21 and self.__categoria <=22:
            porc1=self._personal__sueld_bas+(self._personal__sueld_bas*(self._personal__antig/100))
            return porc1+(porc1*(30/100))
    def tojson(self):
        d=dict(tipo=__class__.__name__,datos=dict(cuil=self._personal__cuil, apellido=self._personal__ape, nombre=self._personal__nom, sueldo_basico=self._personal__sueld_bas, antiguedad=self._personal__antig,categoria=self.__categoria))
        return d