from docente import *
from investigador import *
class docenteinvest(investigador,docente):
    __cate_progincent:str
    __imp_ext:float
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra, categoria=''):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        self.__cate_progincent=categoria_incentivos
        self.__imp_ext=float(importe_extra)
    def tojson(self):
        d=dict(tipo=__class__.__name__,datos=dict(cuil=self._personal__cuil, apellido=self._personal__ape, nombre=self._personal__nom, sueldo_basico=self._personal__sueld_bas, antiguedad=self._personal__antig, carrera=self._docente__carre, cargo=self._docente__cargo, catedra=self._docente__cated, area_investigacion=self._investigador__area_invest, tipo_investigacion=self._investigador__tip_invest, categoria_incentivos=self.__cate_progincent, importe_extra=self.__imp_ext))
        return d
    def getsueld(self): #mal
        sueld=self.getsueldoce()
        return sueld+self.__imp_ext
    def getimpext(self):
        return self.__imp_ext
    def __gt__(self,otr):
        return self._personal__nom>otr._personal__nom
    def __str__(self):
        return f'{self._personal__cuil} {self._personal__nom} {self._personal__ape} {self._personal__sueld_bas} {self._personal__antig} {self._docente__carre} {self._docente__cargo} {self._docente__cated} {self._investigador__area_invest} {self._investigador__tip_invest} {self.__cate_progincent} {self.__imp_ext}'