class jugador:
    __nombre:str
    __fecha:str
    __hora:str
    __puntaje:int
    def __init__(self,nombre=None,fecha=None,hora=None,puntaje=None):
        self.__nombre=nombre
        self.__fecha=fecha
        self.__hora=hora
        self.__puntaje=puntaje
    def getnombre(self):
        return self.__nombre
    def actnomb(self,nombre):
        self.__nombre=nombre
    def actpuntj(self,fecha,hora,puntaje):
        self.__fecha=fecha
        self.__hora=hora
        self.__puntaje=puntaje
    def tojson(self):
        return dict(nombre=self.__nombre,fecha=self.__fecha,hora=self.__hora,puntaje=self.__puntaje)