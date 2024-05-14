class material_refrac:
    __material:int
    __carac:str
    __cant_uti:float
    __cost_ad:float
    def __init__(self,material,carac,cantuti,costoad):
        self.__material=material
        self.__carac=carac
        self.__cant_uti=cantuti
        self.__cost_ad=costoad