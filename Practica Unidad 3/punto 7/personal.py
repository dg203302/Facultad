class personal:
    __cuil:str
    __ape:str
    __nom:str
    __sueld_bas:float
    __antig:int
    def __init__(self,cuil,apellido,nombre,sueldo_basico,antiguedad,carrera='',cargo='',catedra='',categoria='',area_investigacion='',tipo_investigacion='',categoria_incentivos='',importe_extra=0):
        self.__cuil=cuil
        self.__ape=apellido
        self.__nom=nombre
        self.__sueld_bas=float(sueldo_basico)
        self.__antig=int(antiguedad)
    def __lt__(self,otr):
        return self.__ape>otr.__ape
    def getnom(self):
        return self.__nom
    def getape(self):
        return self.__ape
    def gettip(self):
        return self.__class__.__name__
    def getsuba(self):
        return self.__sueld_bas