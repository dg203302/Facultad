class depart:
    __iddep:int
    __nomappropie:str
    __numepiso:int
    __numedepa:int
    __canthabita:int
    __cantbaño:int
    __supcubie:float
    def __init__(self, iddep,nomprop,numepis,numedep,canthabi,cantba,supcub):
        self.__iddep=iddep
        self.__nomappropie=nomprop
        self.__numepiso=numepis
        self.__numedepa=numedep
        self.__canthabita=canthabi
        self.__cantbaño=cantba
        self.__supcubie=supcub
    def getid(self):
        return self.__iddep
    def getnom(self):
        return self.__nomappropie
    def getnumep(self):
        return self.__numepiso
    def getnumde(self):
        return self.__numedepa
    def getcanth(self):
        return self.__canthabita
    def getcantb(self):
        return self.__cantbaño
    def getsupcu(self):
        return self.__supcubie
    def __str__(self):
        return f'{self.__iddep}{self.__nomappropie}{self.__numepiso}{self.__numedepa}{self.__canthabita}{self.__cantbaño}{self.__supcubie}'