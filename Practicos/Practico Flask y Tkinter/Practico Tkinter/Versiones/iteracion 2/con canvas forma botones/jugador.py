class jugador:
    __nombre:str
    __fecha:str
    __hora:str
    __puntaje:int
    def __init__(self,nombre=None,fecha=None,hora=None,puntaje=0):
        self.__nombre=nombre
        self.__fecha=fecha
        self.__hora=hora
        self.__puntaje=puntaje
    def actpuntaje(self):
        self.__puntaje+=1
    def getpuntaje(self):
        return self.__puntaje
    def reiniciarpuntaje(self):
        self.__puntaje=0
    def getnombre(self):
        return self.__nombre
    def actnomb(self,nombre):
        self.__nombre=nombre
    def registrarjugada(self,fecha,hora):
        self.__fecha=fecha
        self.__hora=hora
    def tojson(self):
        return dict(nombre=self.__nombre,fecha=self.__fecha,hora=self.__hora,puntaje=self.__puntaje)