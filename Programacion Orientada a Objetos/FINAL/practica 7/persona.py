class persona:
    __nombre:str
    __apellido:str
    __dni:str
    def __init__(self,nombre,apellido,dni):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
    def get_nombre_persona(self):
        return self.__nombre
    def get_apellido_persona(self):
        return self.__apellido
    def get_dni_persona(self):
        return self.__dni
    def __str__(self) -> str:
        return f'nombre: {self.__nombre}, apellido: {self.__apellido}, dni: {self.__dni}'