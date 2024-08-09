from persona import *
class docente(persona):
    __cargo:str
    __horas_asignadas:int
    def __init__(self, nombre, apellido, dni, cargo, horas_asignadas,area='', incentivo='', sueldo=0):
        super().__init__(nombre, apellido, dni, area, incentivo, cargo, horas_asignadas, sueldo)
        self.__cargo=cargo
        self.__horas_asignadas=int(horas_asignadas)