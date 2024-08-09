from productos import *
class congelado(productos):
    __nitro:int
    __oxig:int
    __dioxi:int
    __vapo:int
    __metodo:str
    def __init__(self, nprod, fechae, fechav, tempman, pais, numelo, cost, nit, oxi, diox, vapo, metod):
        super().__init__(nprod, fechae, fechav, tempman, pais, numelo, cost)
        self.__nitro=int(nit)
        self.__oxig=int(oxi)
        self.__dioxi=int(diox)
        self.__vapo=int(vapo)
        self.__metodo=metod
    def getimpvent(self):
        return (self._productos__costo_base+(self._productos__costo_base*(15/100)))