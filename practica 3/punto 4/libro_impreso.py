from Publicaciones import *
class libroimp(publicac):
    __n_aut:str
    __f_edi:str
    __cant_pag:str
    def __init__(self, titu, cate, prec, naut,fedi,canpag):
        super().__init__(titu, cate, prec)
        self.__n_aut=naut
        self.__f_edi=fedi
        self.__cant_pag=canpag
    def __str__(self):
        return f'{self._publicac__tit}{self._publicac__cate}{self._publicac__preci_base}{self.__n_aut}{self.__f_edi}{self.__cant_pag}'