import csv
from nodo import *
class lista_personal:
    __inicio:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self, inicio=None,actual=None,indice=0,tope=0):
        self.__inicio=inicio
        self.__actual=actual
        self.__indice=indice
        self.__tope=tope
        self.cargar_csv()
    def cargar_csv(self):
        file=open('FINAL/practica 3/personal.csv', mode='r')
        read=csv.reader(file,delimiter=';')
        for fila in read:
            personal_nuevo=personal(fila[0],fila[1],fila[2])
            self.insertar(personal_nuevo)
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__indice=0
            self.__actual=self.__inicio
            raise StopIteration
        else:
            datos=self.__actual.get_datos()
            self.__actual=self.__actual.get_siguiente()
            self.__indice+=1
            return datos
    def insertar(self, personal_nuevo):
        nodo_nuevo=nodo(personal_nuevo)
        if self.__inicio==None or self.__tope==0:
            self.__inicio=nodo_nuevo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while self.__indice<self.__tope and self.__actual.get_siguiente()!=None:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__actual.get_siguiente()==None:
                self.__actual.set_siguiente(nodo_nuevo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__inicio
    def insertar_en_posicion(self):
        nombre='jhony'
        apellido='mcjony'
        dni='449929494'
        personal_nuevo=personal(nombre,apellido,dni)
        nuevo_nodo=nodo(personal_nuevo)
        try:
            posicion=(int(input('ingrese la posicion donde desee ingresar el nodo!-'))-1)
            if posicion==0:
                nuevo_nodo.set_siguiente(self.__inicio)
                self.__inicio=nuevo_nodo
                self.__actual=nuevo_nodo
                self.__tope+=1
            else:
                while self.__indice!=self.__tope and self.__indice<posicion and self.__actual.get_siguiente()!=None:
                    self.__actual=self.__actual.get_siguiente()
                    self.__indice+=1
                if self.__indice==posicion:
                    nuevo_nodo.set_siguiente(self.__actual.get_siguiente())
                    self.__actual.set_siguiente(nuevo_nodo)
                    self.__actual=self.__inicio
                    self.__tope+=1
                    self.__indice=0
                else:
                    self.__actual=self.__inicio
                    self.__indice=0
                    raise IndexError
        except IndexError:
            print('indice erroneo!')
    def mostrar(self):
        for personal in self:
            print(personal)
    def mostrar_instancias(self):
        for personal_activo in self:
            if isinstance(personal_activo,personal):
                print('personal')