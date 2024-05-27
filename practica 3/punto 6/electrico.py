from calefactor import *
class electrico(calefactor):
    __maxpot:str
    def __init__(self,marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion,potencia_max):
        super().__init__(marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion)
        self.__maxpot=potencia_max
    def tojson(self):
        d=dict(tipo=__class__.__name__,atributos=dict(marca=self._calefactor__marca,modelo=self._calefactor__modelo,paisfabric=self._calefactor__paisfabri,precio=self._calefactor__pre_lista,formpago=self._calefactor__form_pago,cantcout=self._calefactor__cant_cuot,promo=self._calefactor__prom,maxpote=self.__maxpot,))
        return d
    def __str__(self):
        return f'{self.__maxpot}'
        