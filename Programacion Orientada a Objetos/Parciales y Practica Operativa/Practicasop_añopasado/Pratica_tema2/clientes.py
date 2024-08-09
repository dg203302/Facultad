class cliente:
    __dni:str
    __nom:str
    __ap:str
    __tel:str
    __pate:str
    __vehic:str
    __est:str
    def __init__(self,dni,nom,ape,tel,pate,vehi,est):
        self.__dni=dni
        self.__nom=nom
        self.__ap=ape
        self.__tel=tel
        self.__pate=pate
        self.__vehic=vehi
        self.__est=est
    def getdni(self):
        return self.__dni
    def getap(self):
        return self.__ap
    def getnom(self):
        return self.__nom
    def getpaten(self):
        return self.__pate
    def getvehic(self):
        return self.__vehic
    def modific_est(self):
        self.__est='T'
    def gettel(self):
        return self.__tel
    def getest(self):
        return self.__est
    def __eq__(self,otrocli):
        return self.__dni==otrocli.__dni and self.__nom == otrocli.__nom and self.__ap == otrocli.__ap and self.__tel == otrocli.__tel