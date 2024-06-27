class moto:
    __pate: str
    __marca: str
    __nya: str
    __km: str
    def __init__(self, patent, marc, nya,kilo):
        self.__pate=patent
        self.__marca=marc
        self.__nya=nya
        self.__km=kilo
    def getnya(self):
        return self.__nya
    def getkm(self):
        return self.__km
    def getpat(self):
        return self.__pate
    def getmarc(self):
        return self.__marca
    def __str__(self):
        return f'patente: {self.__pate}, marca: {self.__marca}, nombre y apellido del conductor: {self.__nya}, kilometros: {self.__km}'