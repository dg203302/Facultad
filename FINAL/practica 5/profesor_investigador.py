from profesor import *
from investigador import *
class docente_investigador(investigador,docente):
    __porcentaje_extra:float
    __horas_extra:int
    def __init__(self,nombre,apellido,dni,materiacargo,sueldo,anosexp,area,horas_asignadas,porcentajeextra,horasextra):
        super().__init__(nombre,apellido,dni,materiacargo,sueldo,anosexp,area,horas_asignadas,porcentajeextra,horasextra)
        self.__porcentaje_extra=porcentajeextra
        self.__horas_extra=horasextra
    def __str__(self):
        return f'{super().__str__()}, procentaje extra: {self.__porcentaje_extra}, horas extra: {self.__horas_extra}'