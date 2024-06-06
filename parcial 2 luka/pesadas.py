from Herramientas import *
class pesadas(herramientas):
    __tip_maqui:str
    __peso:int
    def __init__(self, marc, mode, an, tipo, pot, capa, tari, canti, tipomaqui, peso):
        super().__init__(marc, mode, an, tipo, pot, capa, tari, canti)
        self.__tip_maqui=tipomaqui
        self.__peso=int(peso)
    def __str__(self):
        return 'soy un herramienta pesada!'