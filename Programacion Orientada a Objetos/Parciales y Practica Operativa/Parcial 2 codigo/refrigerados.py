from productos import *
class refrigerados(productos):
    __cod_org:str
    def __init__(self, nprod, fechae, fechav, tempman, pais, numelo, cost, codorg):
        super().__init__(nprod, fechae, fechav, tempman, pais, numelo, cost)
        self.__cod_org=codorg
    def getimpvent(self):
        fechaven=self._productos__fech_venc
        dia,mes,anio=fechaven.split('/')
        nmes=int(mes)
        if (nmes-5)<=2 and anio=='2024':
            return (self._productos__costo_base-(self._productos__costo_base*(10/100)))
        else:
            return (self._productos__costo_base+(self._productos__costo_base*(1/100)))