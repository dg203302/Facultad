class beca:
    __idbeca:str
    __tipo:str
    __importebeca:float
    def __init__(self,idbec,tip,imp):
        self.__idbeca=idbec
        self.__tipo=tip
        self.__importebeca=imp
    def gettipo(self):
        return self.__tipo
    def getidbeca(self):
        return self.__idbeca
    def getimp(self):
        return self.__importebeca
    def __str__(self):
        return f'{self.__idbeca}{self.__tipo}{self.__importebeca}'