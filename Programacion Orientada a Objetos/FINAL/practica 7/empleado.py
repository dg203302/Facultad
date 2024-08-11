from persona import *
class empleado(persona):
    __sueldo:float
    __id:int
    def __init__(self,nombre,apellido,dni,sueldo,id):
        super().__init__(nombre,apellido,dni)
        self.__sueldo=sueldo
        self.__id=id
    def get_sueldo(self):
        return self.__sueldo
    def get_id(self):
        return self.__id
    def __str__(self) -> str:
        return f'{super().__str__()}, sueldo:{self.__sueldo}, id: {self.__id}'