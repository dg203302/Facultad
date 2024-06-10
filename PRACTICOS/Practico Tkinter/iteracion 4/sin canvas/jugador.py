class jugador:
    __nombre:str
    __fecha:str
    __hora:str
    __puntaje:int
    __niveldific:str
    def __init__(self,nombre=None,fecha=None,hora=None,niveldificultad='',puntaje=0):
        self.__nombre=nombre
        self.__fecha=fecha
        self.__hora=hora
        self.__puntaje=puntaje
        self.__niveldific=niveldificultad
    def actnivel(self,niveldif):
        self.__niveldific=niveldif
    def getnivel(self):
        return self.__niveldific
    def getnombre(self):
        return self.__nombre
    def getpuntaje(self):
        return self.__puntaje
    def getfecha(self):
        return self.__fecha
    def gethora(self):
        return self.__hora
    def actpuntaje(self):
        self.__puntaje+=1
    def reiniciarpuntaje(self):
        self.__puntaje=0
    def actnomb(self,nombre):
        self.__nombre=nombre
    def registrarjugada(self,fecha,hora):
        self.__fecha=fecha
        self.__hora=hora
    def __gt__(self,otr):
        return self.__puntaje<otr.__puntaje
    def tojson(self):
        return dict(jugador=dict(nombre=self.__nombre,fecha=self.__fecha,hora=self.__hora,puntaje=self.__puntaje,niveldificultad=self.__niveldific))