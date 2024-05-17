from superclase import *
class trabajador(persona):
    __sueldo:float
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.__sueldo=sueldo
    def __str__(self):
        return f'{self._persona__nombre} {self._persona__edad} {self.__sueldo}'