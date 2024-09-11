from persona import *
class investigador(persona):
    __area:str
    __horas_asignadas:int
    def __init__(self,nombre,apellido,dni,area,horas_asignadas,sueldo=0,anosexp=0,materiacargo='',porcentajeextra=0,horasextra=0):
        super().__init__(nombre,apellido,dni,materiacargo,sueldo,anosexp,area,horas_asignadas,porcentajeextra,horasextra)
        self.__area=area
        self.__horas_asignadas=int(horas_asignadas)
    def get_area(self):
        return self.__area
    def get_horas_asignadas(self):
        return self.__horas_asignadas
    def __str__(self):
        return f'{super().__str__()}, area: {self.__area}, horas asignadas: {self.__horas_asignadas}'