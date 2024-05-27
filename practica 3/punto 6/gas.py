from calefactor import *
class gas(calefactor):
    __matri:str
    __calori:str
    def __init__(self,marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion,matricula,calorias):
        super().__init__(marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion)
        self.__matri=matricula
        self.__calori=calorias
    def tojson(self):
        d=dict(tipo=__class__.__name__,atributos=dict(tipo=__class__.__name__,modelo=self._calefactor__modelo,paisfabric=self._calefactor__paisfabri,precio=self._calefactor__pre_lista,formpago=self._calefactor__form_pago,cantcout=self._calefactor__cant_cuot,promo=self._calefactor__prom,matricu=self.__matri,calorias=self.__calori))
        return d
    def __str__(self):
        return f'{self.__matri}{self.__calori}'