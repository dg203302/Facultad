from calefactor import *
class gas(calefactor):
    __matri:str
    __calori:str
    def __init__(self,marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion,matricula,calorias):
        super().__init__(marca,modelo,pais_de_fabricacion,precio_de_lista,forma_de_pago,cant_cuotas,promocion)
        self.__matri=matricula
        self.__calori=calorias
    def tojson(self):
        d=dict(tipo=__class__.__name__,atributos=dict(modelo=self._calefactor__modelo,paisfabric=self._calefactor__paisfabri,precio=self._calefactor__pre_lista,formpago=self._calefactor__form_pago,cantcout=self._calefactor__cant_cuot,promo=self._calefactor__prom,matricu=self.__matri,calorias=self.__calori))
        return d
    def getkilocalo(self):
        return self.__calori
    def getimpo(self):
        if self.__calori>3000:
            porc1=self._calefactor__pre_lista+(self._calefactor__pre_lista*(1/100))
            if self._calefactor__cant_cuot>1:
                porc2=porc1+(porc1*(40/100))
                if self._calefactor__prom==True:
                    imp=porc2-(porc2*(15/100))
                    return imp
                else:
                    return porc2
            else:
                if self._calefactor__prom==True:
                    imp=porc1-(porc1*(15/100))
                    return imp
                else:
                    return porc1