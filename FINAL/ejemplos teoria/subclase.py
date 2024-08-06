from clase_base import *
class subclase(base):
    __sueldo:float
    def __init__(self, nombre, apellido, dni, sueldo):
        super().__init__(nombre, apellido, dni)
        self.__sueldo=float(sueldo)
    def calcular_sueldo(self,bono):
        print(f'sueldo a pagar {self.__sueldo+bono}')

if __name__=='__main__':
    clase=subclase('jose','juan','32323232',12000)
    clase.calcular_sueldo(233333)