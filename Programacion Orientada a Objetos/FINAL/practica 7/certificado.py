from empleado import *
from programa import *
class certificado:
    __empleado:empleado
    __programa:programa
    def __init__(self,empleado=None,programa=None):
        self.__empleado=empleado
        self.__programa=programa
    def get_empleado(self):
        return self.__empleado
    def get_programa(self):
        return self.__programa