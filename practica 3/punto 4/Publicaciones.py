from abc import ABC
class publicac(ABC):
    __tit:str
    __cate:str
    __preci_base:float
    def __init__(self,titu,cate,prec):
        self.__tit=titu
        self.__cate=cate
        self.__preci_base=float(prec)
    def gettit(self):
        return self.__tit
    def getcate(self):
        return self.__cate
    def importe(self):
        pass