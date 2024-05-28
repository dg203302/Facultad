from docente import *
from investigador import *
class docenteinvest(investigador,docente):
    __cate_progincent:str
    __imp_ext:float
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra, categoria=''):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        self.__cate_progincent=categoria_incentivos
        self.__imp_ext=importe_extra
    def tojson(self):
        d=dict(tipo=__class__.__name__,datos=dict(cuil=self._personal__cuil, apellido=self._personal__ape, nombre=self._personal__nom, sueldo_basico=self._personal__sueld_bas, antiguedad=self._personal__antig, carrera=self._docente__carre, cargo=self._docente__cargo, catedra=self._docente__cated, area_investigacion=self._investigador__area_invest, tipo_investigacion=self._investigador__tip_invest, categoria_incentivos=self.__cate_progincent, importe_extra=self.__imp_ext))
        return d