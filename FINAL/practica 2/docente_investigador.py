from investigador import *
from docente import *
class docente_investigador(investigador,docente):
    __sueldo:float
    def __init__(self, nombre, apellido, dni, area, incentivo, cargo, horas_asignadas, sueldo):
        super().__init__(nombre, apellido, dni, area, incentivo, cargo, horas_asignadas, sueldo)
        self.__sueldo=sueldo
    def __str__(self) -> str:
        return f' nombre: {self._persona__nombre} apellido: {self._persona__apellido} dni: {self._persona__dni} area: {self._investigador__area} incentivo: {self._investigador__incentivo} cargo: {self._docente__cargo} horas asignadas: {self._docente__horas_asignadas} sueldo: {self.__sueldo}'