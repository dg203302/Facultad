from persona import *
class investigador(persona):
    __area:str
    __incentivo:str
    def __init__(self,nombre, apellido, dni, area, incentivo, cargo='', horas_asignadas=0, sueldo=0):
        super().__init__(nombre, apellido, dni, area, incentivo, cargo, horas_asignadas, sueldo)
        self.__area=area
        self.__incentivo=incentivo