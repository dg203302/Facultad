class ejem:
    __att1:str
    __att2:str
    def __init__(self,att1,att2):
        self.__att1=att1
        self.__att2=att2
    def __str__(self):
        return f'{self.__att1} {self.__att2}'