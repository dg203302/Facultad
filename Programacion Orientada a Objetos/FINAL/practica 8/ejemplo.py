class ejemplo:
    __nombre:str
    __numero:int
    def __init__(self,nombre,numero):
        self.__nombre=nombre
        self.__numero=numero
    def __str__(self):
        return f'{self.__nombre} {self.__numero}'