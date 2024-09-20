class material_refrac:
    __material:int
    __carac:str
    __cant_uti:float
    __cost_ad:float
    __ladrillos:list
    def __init__(self,material,carac,cantuti,costoad):
        self.__material=material
        self.__carac=carac
        self.__cant_uti=cantuti
        self.__cost_ad=float(costoad)
        self.__ladrillos=[]
    def addladri(self,ladri):
        self.__ladrillos.append(ladri)
    def getcost(self):
        return self.__cost_ad
    def getcaract(self):
        return self.__carac
    def getnom(self):
        return self.__material
    def getcosto(self):
        return self.__cost_ad
    def __str__(self):
        return f'|material refractario: {self.__material}|'