from abc import ABC
class productos(ABC):
    __nprod:str
    __fech_env:str
    __fech_venc:str
    __tempe_mant_rec:float
    __pais_origen:str
    __num_lote:str
    __costo_base:float
    def __init__(self,nprod,fechae,fechav,tempman,pais,numelo,cost):
        self.__nprod=nprod
        self.__fech_env=fechae
        self.__fech_venc=fechav
        self.__tempe_mant_rec=float(tempman)
        self.__pais_origen=pais
        self.__num_lote=numelo
        self.__costo_base=float(cost)
    def __str__(self):
        return f'-------------------------------------------------------\n{self.__nprod}\norigen: {self.__pais_origen}\ntemperatura recomendada: {self.__tempe_mant_rec}°C\nimporte de venta: {self.getimpvent()}\n-------------------------------------------------------'
    def getimpvent(self):
        pass