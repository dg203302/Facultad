from persona import *
class trabajdor(persona):
    __sueldo:float
    __numero_de_id:int
    def __init__(self,nombre,apellido,dni,sueldo,numeroid):
        super().__init__(nombre,apellido,dni)
        self.__sueldo=float(sueldo)
        self.__numero_de_id=int(numeroid)
    def get_sueldo(self):
        return self.__sueldo
    def get_id(self):
        return self.__numero_de_id
    def __str__(self):
        return f'{self.get_nombre()} {self.get_apellido()} {self.get_dni()} {self.__sueldo} {self.__numero_de_id}'