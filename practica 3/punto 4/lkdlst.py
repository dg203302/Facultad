from nodo import *
from cd import *
from libro_impreso import *
import csv
class lkdlist:
    __ini:nodo
    def __init__(self):
        self.__ini=None
    def agreg(self,objt):
        nuenodo=nodo(objt)
        if self.__ini==None:
            self.__ini=nuenodo
        else:
            nodau=self.__ini
            while nodau.getsig()!=None:
                nodau=nodau.getsig()
            if nodau.getsig()==None:
                nodau.agregsig(nuenodo)
    def carga(self):
        a=open('Python/practica 3/punto 4/publcaciones.csv',mode='r')
        red=csv.reader(a,delimiter=';')
        for fil in red:
            if len(fil) == 5:
                CD=cd(fil[0],fil[1],fil[2],fil[3],fil[4])
                self.agreg(CD)
            elif len(fil) == 6:
                lib=libroimp(fil[0],fil[1],fil[2],fil[3],fil[4],fil[5])
                self.agreg(lib)
    def mostrar(self):
        while self.__ini!=None:
            print(self.__ini)
            self.__ini=self.__ini.getsig()