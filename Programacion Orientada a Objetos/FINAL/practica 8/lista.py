from nodo import *
class lista:
    __inicio:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self,incio=None,actual=None,indice=0,tope=0):
        self.__inicio=incio
        self.__actual=actual
        self.__indice=indice
        self.__tope=tope
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__indice=0
            self.__actual=self.__inicio
            raise StopIteration
        else:
            dato=self.__actual.get_dato()
            self.__indice+=1
            self.__actual=self.__actual.get_siguiente()
            return dato
    def insertar_al_final(self,objeto_ejemplo):
        nodo_nuevo=nodo(objeto_ejemplo)
        if self.__inicio==None or self.__tope==0:
            self.__inicio=nodo_nuevo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while self.__actual.get_siguiente()!=None and self.__indice!=self.__tope:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__actual.get_siguiente()==None:
                self.__actual.set_siguiente(nodo_nuevo)
                self.__tope+=1
                self.__actual=self.__inicio
                self.__indice=0
    def insertar_al_inicio(self,objeto_ejemplo):
        nodo_nuevo=nodo(objeto_ejemplo)
        nodo_nuevo.set_siguiente(self.__inicio)
        self.__inicio=nodo_nuevo
        self.__actual=self.__inicio
        self.__tope+=1
    def insertar_en_posicion(self,objeto_ejemplo):
        nodo_nuevo=nodo(objeto_ejemplo)
        posicion=int(input('ingrese la posicion que desee: '))-1
        if posicion==0:
            nodo_nuevo.set_siguiente(self.__inicio)
            self.__inicio=nodo_nuevo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while (self.__indice!=posicion and self.__indice<self.__tope) and self.__actual.get_siguiente()!=None:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__indice==posicion:
                nodo_nuevo.set_siguiente(self.__actual.get_siguiente())
                self.__actual.set_siguiente(nodo_nuevo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__inicio
    def cargar_prueba(self):
        prueb1=ejemplo('UNO',1)
        self.insertar_al_final(prueb1)
        prueb2=ejemplo('DOS',2)
        self.insertar_al_final(prueb2)
        prueb3=ejemplo('TRES',3)
        self.insertar_al_final(prueb3)
        prueb4=ejemplo('CUATRO',4)
        self.insertar_al_final(prueb4)
        prueb5=ejemplo('AL PRINCIPIO VOY',5)
        self.insertar_al_inicio(prueb5)
        prueb6=ejemplo('INSERTADO EN POSICION',6)
        self.insertar_en_posicion(prueb6)
    def mostrar(self):
        for objeto in self:
            print(objeto)
if __name__=='__main__':
    gestor=lista()
    gestor.cargar_prueba()
    gestor.mostrar()