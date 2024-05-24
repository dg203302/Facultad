from Publicaciones import *
class cd(publicac):
    __t_rep=int
    __narra=str
    def __init__(self,titu,cate,prec,tiemp,narra):
        super().__init__(titu,cate,prec)
        self.__t_rep=tiemp
        self.__narra=narra
    def __str__(self):
        return f'{self._publicac__tit}{self._publicac__cate}{self._publicac__preci_base}{self.__t_rep}{self.__narra}'