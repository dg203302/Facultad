from calefactor import *
class electrico(calefactor):
    __maxpot:str
    def __init__(self,marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion,potencia_max):
        super().__init__(marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion)
        self.__maxpot=potencia_max
    def getpote(self):
        return self.__maxpot
    def tojson(self):
        d=dict(tipo=__class__.__name__,atributos=dict(marca=self._calefactor__marca,modelo=self._calefactor__modelo,paisfabric=self._calefactor__paisfabri,precio=self._calefactor__pre_lista,formpago=self._calefactor__form_pago,cantcout=self._calefactor__cant_cuot,promo=self._calefactor__prom,maxpote=self.__maxpot,))
        return d
    def getimpo(self):
        if self.__maxpot>1000:
            porc1=self._calefactor__pre_lista+(self._calefactor__pre_lista*(1/100))
            if self._calefactor__cant_cuot>1:
                porc2=porc1+(porc1*(30/100))
                if self._calefactor__prom==True:
                    imp=porc2-(porc2*(15/100))
                    return imp
                else:
                    return porc2
            else:
                if self._calefactor__prom==True:
                    imp=porc1+(porc1*(15/100))
                    return imp
                else:
                    return porc1