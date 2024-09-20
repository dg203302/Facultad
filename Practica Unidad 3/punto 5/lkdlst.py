from nodo import *
from claseejem import *
import csv
from interfaz import *
class lkdlist(interface):
    __ini:nodo
    def __init__(self):
        self.__ini=None
    def carga(self):
        a=open('Python/practica 3/punto 5/ejem.csv',mode='r')
        red=csv.reader(a,delimiter=';')
        for fil in red:
            ej=ejem(fil[0],fil[1])
            self.agreg(ej)
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
    def insertar(self):
        i=int(input('ingrese la posicion que desee insertar: '))
        att1=input('ingrese el atributo 1: ')
        att2=input('ingrese atributo 2: ')
        ej=ejem(att1,att2)
        '''insercion en medio de la lista'''
        nueno=nodo(ej)
        nodau=self.__ini
        if i==0:
            nodau.agregsig(nodau)
            nodau=nueno
        else:
            try:
                j=0
                while nodau!=None and j<i-1:
                    nodau=nodau.getsig()
                    j+=1
                if j==i-1:
                    nueno.agregsig(nodau.getsig())
                    nodau.agregsig(nueno)
            except AttributeError:
                print(f'indice: {i} esta fuera de rango valido')
    def most(self):
        i=int(input('ingrese la posicion que desee saber: '))
        try:
            j=0
            while self.__ini!=None and j<(i-1):
                j+=1
                self.__ini=self.__ini.getsig()
            if j==(i-1):
                print(self.__ini)
        except:
            print('ingrese nuevamente el indice!')