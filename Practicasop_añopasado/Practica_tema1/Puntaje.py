class punta:
    __dnipat:str
    __estp:str
    __pun1:float
    __pun2:float
    __pun3:float
    def __init__(self, dni, est, p1, p2, p3):
        self.__dnipat=dni
        self.__estp=est
        self.__pun1=p1
        self.__pun2=p2
        self.__pun3=p3
    def getest(self):
        return self.__estp
    def getdni(self):
        return self.__dnipat
    def getpunt(self):
        return (self.__pun1+self.__pun2+self.__pun3)/3
    def __gt__(self,otrpunt):
        return (self.__pun1+self.__pun2+self.__pun3)/3 > (otrpunt.__pun1+otrpunt.__pun2+otrpunt.__pun3)/3
    def getp1(self):
        return self.__pun1
    def getp2(self):
        return self.__pun2
    def getp3(self):
        return self.__pun3
    def __str__(self):
        return f'{self.__dnipat}{self.__estp}{self.__pun1}{self.__pun2}{self.__pun3}'