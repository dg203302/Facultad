from servicio import *
class embalaje(servicio):
    __precxuniemba:float
    __pesounidad:float
    __cantuniemb:int
    def __init__(self, nome, nomc, direc, fec, comi, precuni, peso, canti):
        super().__init__(nome, nomc, direc, fec, comi)
        self.__precxuniemba=float(precuni)
        self.__pesounidad=float(peso)
        self.__cantuniemb=int(canti)
    def getpesoxuni(self):
        return self.__pesounidad
    def __str__(self):
        return f'{self.getcosto()}'
    def getcosto(self):
        if self.__pesounidad>50:
            cost=self.__precxuniemba*self.__cantuniemb
            porcent=(cost+(cost*(10/100)))
            return porcent+(porcent*(self._servicio__comision/100))
        else:
            cost=self.__precxuniemba*self.__cantuniemb
            return cost+(cost*(self._servicio__comision/100))