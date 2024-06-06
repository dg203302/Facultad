from Herramientas import *
class electricas(herramientas):
    __tipo_elec:str
    def __init__(self, marc, mode, an, tipo, pot, capa, tari, canti, tipoele):
        super().__init__(marc, mode, an, tipo, pot, capa, tari, canti)
        self.__tipo_elec=tipoele
    def __str__(self):
        return 'soy un herramienta electrica!'