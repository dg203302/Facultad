from persona import *
class docente(persona):
    __materia_a_cargo:str
    __sueldo:float
    __anos_experiencia:int
    def __init__(self, nombre,apellido,dni,materiacargo,sueldo,anosexp,area='',horas_asignadas=0,porcentajeextra=0,horasextra=0):
        super().__init__(nombre,apellido,dni,area,horas_asignadas,materiacargo,sueldo,anosexp,porcentajeextra,horasextra)
        self.__materia_a_cargo=materiacargo
        self.__sueldo=float(sueldo)
        self.__anos_experiencia=(anosexp)
    def get_materia_cargo(self):
        return self.__materia_a_cargo
    def get_sueldo(self):
        return self.__sueldo
    def get_anos_experiencia(self):
        return self.__anos_experiencia
    def __str__(self):
        return f'{super().__str__()}, materia a cargo: {self.__materia_a_cargo}, sueldo: {self.__sueldo}, años experiencia: {self.__anos_experiencia}'