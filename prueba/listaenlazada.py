import csv
from subclase import *
class nodo:
    __datos:object
    __siguiente:object
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def actsig(self,siguiente):
        self.__siguiente=siguiente
    def getsig(self):
        return self.__siguiente
    def __str__(self):
        return f'{self.__datos}'
class linkdlist:
    __cabe:object
    def __init__(self):
        self.__cabe=None
    def agreg(self,dat):
        nodnue=nodo(dat)
        if self.__cabe == None:
            self.__cabe=nodnue
        else:
            nodaux=self.__cabe
            while nodaux.getsig()!=None:
                nodaux=nodaux.getsig()
            if nodaux.getsig()==None:
                nodaux.actsig(nodnue)
    def cargar(self):
        a=open('Python/prueba/personas.csv',mode='r')
        re=csv.reader(a,delimiter=';')
        for fil in re:
            trabj=trabajador(fil[0],fil[1],fil[2])
            self.agreg(trabj)
    def mostrarlist(self):
        while self.__cabe!=None:
            print(f'{self.__cabe}')
            self.__cabe=self.__cabe.getsig()