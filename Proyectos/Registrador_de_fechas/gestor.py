from encoder import *
from nodo import *
class gestor_fechas:
    __inicio:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self,inicio=None,actual=None,indice=0,tope=0):
        self.__inicio=inicio
        self.__actual=actual
        self.__indice=indice
        self.__tope=tope
        enconder_json.cargar_fechas(self)
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__inicio
            self.__indice=0
            raise StopIteration
        else:
            dato=self.__actual.get_dato()
            self.__actual=self.__actual.get_siguiente()
            self.__indice+=1
            return dato
    def insertar(self,datos_del_dia):
        nuevo_nodo=nodo(datos_del_dia)
        if self.__inicio==None:
            self.__inicio=nuevo_nodo
            self.__actual=nuevo_nodo
            self.__tope+=1
        else:
            while self.__actual.get_siguiente()!=None and self.__indice<self.__tope:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__actual.get_siguiente()==None:
                self.__actual.set_siguiente(nuevo_nodo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__inicio
    def get_fechas(self):
        lista_de_fechas=[]
        for fecha in self:
            lista_de_fechas.append(fecha)
        lista_de_fechas.sort()
        return lista_de_fechas
    def verificar(self):
        if self.__inicio==None:
            return False
        else:
            return True
    def limpiar(self):
        for fecha in self:
            del fecha
        enconder_json.guardar_json()
    def to_json(self):
        if self.__inicio==None:
            return
        else:
            diccionario_a_guardar=dict(gestor_fechas=[fecha.to_json() for fecha in self])
            enconder_json.guardar_json(diccionario_a_guardar)