from nodo import *
class gestor_personal:
    __inicio:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self,inicio=None,actual=None,indice=0,tope=0):
        self.__inicio=inicio
        self.__actual=actual
        self.__indice=indice
        self.__tope=tope
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__inicio
            self.__indice=0
            raise StopIteration
        else:
            datos=self.__actual.get_datos()
            self.__actual=self.__actual.get_siguiente()
            self.__indice+=1
            return datos
    def insercion_al_final(self,personal):
        nodo_nuevo=nodo(personal)
        if self.__inicio==None or self.__tope==0:
            self.__inicio=nodo_nuevo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while self.__actual.get_siguiente()!=None and self.__indice<self.__tope:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__actual.get_siguiente()==None:
                self.__actual.set_siguiente(nodo_nuevo)
                self.__actual=self.__inicio
                self.__indice=0
                self.__tope+=1
    def insercion_en_posicion(self,personal):
        nodo_nuevo=nodo(personal)
        posicion=int(input('ingrese la posicion donde desee insertar: '))-1
        if posicion==0:
            nodo_nuevo.set_siguiente(self.__inicio)
            self.__inicio=nodo_nuevo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while self.__actual.get_siguiente()!=None and self.__indice<posicion:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__indice==posicion:
                nodo_nuevo.set_siguiente(self.__actual.get_siguiente())
                self.__actual.set_siguiente(nodo_nuevo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__inicio
    def carga_ejemplo(self):
        personal1=persona('julian','jose','44991308')
        self.insercion_al_final(personal1)
        personal2=trabajdor('marcos','jose','2342425',400323,23)
        self.insercion_al_final(personal2)
        personal3=persona('diego','jose','44991307')
        self.insercion_al_final(personal3)
    def mostrar(self):
        for personal in self:
            print(personal)
    def insertar_posicion_ejemplo(self):
        personalinsertar=trabajdor('JULIETA','ROSALES','422324242',324242,93)
        self.insercion_en_posicion(personalinsertar)
    #agregar json