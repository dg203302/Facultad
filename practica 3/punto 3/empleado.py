class empleado:
    __nya:str
    __idemp:int
    __puest:str
    def __init__(self,nya,id,pues):
        self.__nya=nya
        self.__idemp=id
        self.__puest=pues
    def getid(self):
        return self.__idemp
    def getnom(self):
        return self.__nya