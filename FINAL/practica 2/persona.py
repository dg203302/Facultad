class persona:
    __nombre:str
    __apellido:str
    __dni:str
    def __init__(self,nombre, apellido, dni, area='', incentivo='', cargo='', horas_asignadas=0, sueldo=0):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni