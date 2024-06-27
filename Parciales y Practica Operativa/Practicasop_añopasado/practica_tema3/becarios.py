class becario:
    __dni:str
    __nombre:str
    __apellido:str
    __carrera:str
    __sigla:str
    __ano_cursa:str
    __prom:float
    __idbeca_ben:str
    def __init__(self,dni,nom,ape,car,si,an,pro,idben):
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=ape
        self.__carrera=car
        self.__sigla=si
        self.__ano_cursa=an
        self.__prom=pro
        self.__idbeca_ben=idben
    def getid(self):
        return self.__idbeca_ben
    def getdni(self):
        return self.__dni
    def getprom(self):
        return self.__prom
    def __gt__(self,otroself):
        return self.__prom>otroself.__prom and self.__ano_cursa>otroself.__ano_cursa
    def __str__(self):
        return f'{self.__nombre}{self.__apellido}{self.__carrera}{self.__dni}{self.__prom}{self.__ano_cursa}{self.__idbeca_ben}{self.__sigla}'