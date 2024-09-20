class equipo:
    __id_eq: str
    __nom_eq: str
    __gol_favor: int
    __gol_cont: int 
    __dif_gol: int
    __punto: float
    def __init__(self, id,nom,golf,golc,difgol,pun):
        self.__id_eq=id
        self.__nom_eq=nom
        self.__gol_favor=golf
        self.__gol_cont=golc
        self.__dif_gol=difgol
        self.__punto=pun
    def getnom(self):
        return self.__nom_eq
    def getid(self):
        return self.__id_eq
    def getgolesaf(self):
        return self.__gol_favor
    def getgolesec(self):
        return self.__gol_cont
    def getdifgol(self):
        return self.__dif_gol
    def getpunt(self):
        return self.__punto
    def modificpun(self,puntaje):
        self.__punto+=puntaje
    def modificg(self, cg):
        self.__gol_favor+=cg
        self.__dif_gol=self.__gol_favor-self.__gol_cont
    def modificgcon(self,cgvi):
        self.__gol_cont+=cgvi
        self.__dif_gol=self.__gol_favor-self.__gol_cont
    def __gt__(self,otequi):
        if self.__punto == otequi.__punto:
            if self.__dif_gol == otequi.__dif_gol:
                if self.__gol_favor>otequi.__gol_favor:
                    return self>otequi
                else:
                    return self<otequi
            elif self.__dif_gol > otequi.__dif_gol:
                return self>otequi
            else:
                return self<otequi
        elif self.__punto>otequi.__punto:
            return self>otequi
        else:
            return self<otequi
    def __del__(self):
        print('equipo borrado!')