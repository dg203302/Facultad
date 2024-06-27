from servicio import *
class transporte(servicio):
    __precxhora:float
    __pesocarga:int
    __direcdest:str
    def __init__(self, nome, nomc, direc, fec, comi, precxhora,pesocar,direcdes,canthora):
        super().__init__(nome, nomc, direc, fec, comi)
        self.__precxhora=float(precxhora)
        self.__pesocarga=int(pesocar)
        self.__direcdest=direcdes
        self.__canthora=int(canthora)
    def getcosto(self):
        if self.__pesocarga>500:
            cost=self.__precxhora*self.__canthora
            porcent=(cost+(cost*(10/100)))
            return porcent+(porcent*(self._servicio__comision/100))
        else:
            cost=self.__precxhora*self.__canthora
            return cost+(cost*(self._servicio__comision/100))
    def __str__(self):
        return f'{self.getcosto()}'
    def __lt__(self,otr):
        return self.getcosto()>otr.getcosto()