class miembro:
    __id:str
    __nombreape:str
    __correo:str
    def __init__(self,id,nom,cor):
        self.__id=id
        self.__nombreape=nom
        self.__correo=cor
    def getid(self):
        return self.__id
    def getcorreo(self):
        return self.__correo
    def getapnom(self):
        return self.__nombreape