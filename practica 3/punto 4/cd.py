from Publicaciones import *
class cd(publicac):
    __t_rep=int
    __narra=str
    def __init__(self,titu,cate,prec,tiemp,narra):
        super().__init__(titu,cate,prec)
        self.__t_rep=int(tiemp)
        self.__narra=narra
    def importe(self):
        return ( (self._publicac__preci_base+(self._publicac__preci_base*(10/100))) /self._publicac__preci_base)