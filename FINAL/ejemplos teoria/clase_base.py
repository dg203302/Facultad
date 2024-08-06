from abc import ABC, abstractmethod
class base(ABC):
    __nombre:str
    __apellido:str
    __dni:str
    def __init__(self,nombre,apellido,dni):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
    @abstractmethod
    def calcular_sueldo(self):
        pass