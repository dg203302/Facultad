class programcapac:
    __nompro:str
    __codpro:str
    __duracion:int
    def __init__(self,nomp,codp,durp):
        self.__nompro=nomp
        self.__codpro=codp
        self.__duracion=int(durp)
    def getnomp(self):
        return self.__nompro
    def gethora(self):
        return self.__duracion
    def getnomp(self):
        return self.__nompro