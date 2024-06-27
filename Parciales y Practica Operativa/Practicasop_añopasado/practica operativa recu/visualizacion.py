class visualiz:
    __idmiem:str
    __idpelicula:str
    __fecha:str
    __hora:str
    __minutos:int
    def __init__(self,idmiem,idpeli,fecha,hora,minu):
        self.__idmiem=idmiem
        self.__idpelicula=idpeli
        self.__fecha=fecha
        self.__hora=hora
        self.__minutos=int(minu)
    def getidmiem(self):
        return self.__idmiem
    def getmin(self):
        return self.__minutos
    def __eq__(self,otr):
        return self.__idmiem==otr.__idmiem and self.__fecha==otr.__fecha and self.__hora==otr.__hora