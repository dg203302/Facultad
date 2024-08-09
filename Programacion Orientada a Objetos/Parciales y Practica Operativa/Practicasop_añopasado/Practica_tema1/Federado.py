class feder:
    __ap:str
    __nom:str
    __dni:str
    __edad:str
    __club:str
    def __init__(self, ap,no,dni,eda,club):
        self.__ap=ap
        self.__nom=no
        self.__dni=dni
        self.__edad=eda
        self.__club=club
    def getdni(self):
        return self.__dni
    def getedad(self):
        return self.__edad
    def getnom(self):
        return self.__nom
    def getap(self):
        return self.__ap
    def getclub(self):
        return self.__club
    def __str__(self):
        return f'{self.__nom} {self.__ap} {self.__dni} {self.__edad} {self.__club}'