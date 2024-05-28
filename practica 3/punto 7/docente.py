from personal import *
class docente(personal):
    __carre:str
    __cargo:str
    __cated:str
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria='', area_investigacion='', tipo_investigacion='', categoria_incentivos='', importe_extra=0):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        self.__carre=carrera
        self.__cargo=cargo
        self.__cated=catedra
    def tojson(self):
        d=dict(tipo=__class__.__name__,datos=dict(cuil=self._personal__cuil, apellido=self._personal__ape, nombre=self._personal__nom, sueldo_basico=self._personal__sueld_bas, antiguedad=self._personal__antig, carrera=self.__carre, cargo=self.__cargo, catedra=self.__cated))
        return d