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
    def a(self):
        op=int(input('ingrese la publicacion que desee agregar. 1 para cd, 2 para libro\n-'))
        if op==1:
            tit=input('ingrese el titulo del cd: ')
            cate=input('ingrese la categoria del cd: ')
            pre=float(input('ingrese el precio base del cd: '))
            tiem=int(input('ingrese el tiempo del cd: '))
            narrat=input('ingrese la narrativa del cd: ')
            Cd=cd(tit,cate,pre,tiem,narrat)
            self.agreg(Cd)
        elif op==2:
            tit=input('ingrese el titulo del libro: ')
            cate=input('ingrese la categoria del libro: ')
            pre=float(input('ingrese el precio base del libro: '))
            naut=input('ingrese el nombre del autor del libro: ')
            feedi=input('ingrese la fecha de edicion del libro: ')
            cantpag=input('ingrese la cantidad de paginas del libro: ')
            lib=libroimp(tit,cate,pre,naut,feedi,cantpag)
            self.agreg(lib)
    def b(self):
        j=int(input('ingrese la posicion que desee saber: '))
        i=0
        while self.__ini!=None and i<(j-1):
            i+=1
            self.__ini=self.__ini.getsig()
        if i==(j-1):
            if isinstance(self.__ini.getdat(),cd):
                print('es un CD')
            elif isinstance(self.__ini.getdat(),libroimp):
                print('es un Libro impreso')
    def c(self):
        ca=0 #contador de cds
        cb=0 #contador de libros
        while self.__ini!=None:
            if isinstance(self.__ini.getdat(),cd):
                ca+=1
            elif isinstance(self.__ini.getdat(),libroimp):
                cb+=1
            self.__ini=self.__ini.getsig()
        print(f'cantidad de cds: {ca}\ncantidad de libros: {cb}')
    def d(self):
        while self.__ini!=None:
            print(self.__ini)
            self.__ini=self.__ini.getsig()