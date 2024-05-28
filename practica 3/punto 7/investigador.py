from personal import *
class investigador(personal):
    __area_invest:str
    __tip_invest:str
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion, categoria_incentivos='', importe_extra='', carrera='', cargo='', catedra='', categoria=''):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        self.__area_invest=area_investigacion
        self.__tip_invest=tipo_investigacion
    def tojson(self):
        d=dict(tipo=__class__.__name__,datos=dict(cuil=self._personal__cuil, apellido=self._personal__ape, nombre=self._personal__nom, sueldo_basico=self._personal__sueld_bas, antiguedad=self._personal__antig, area_investigacion=self.__area_invest, tipo_investigacion=self.__tip_invest))
        return d