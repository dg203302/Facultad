class persona:
    __nombre:str
    __edad:int
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    def __str__(self):
        return f'{self.__nombre} {self.__edad}'