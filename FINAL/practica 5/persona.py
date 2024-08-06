class persona:
    __nombre:str
    __apellido:str
    __dni:str
    def __init__(self,nombre,apellido,dni,materiacargo='',sueldo=0,anosexp=0,area='',horas_asignadas=0,porcentajeextra=0,horasextra=0):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_dni(self):
        return self.__dni
    def __str__(self):
        return f' nombre: {self.__nombre}, apellido: {self.__apellido}, dni: {self.__dni}'