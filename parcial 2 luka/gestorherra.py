from electricas import *
from pesadas import *
from nodo import *
import csv
class gestorherra:
    __cab:nodo
    __actu:nodo
    __indice:int
    __tope:int
    def __init__(self,cab=None,actu=None,indi=0,tope=0):
        self.__cab=cab
        self.__actu=actu
        self.__indice=indi
        self.__tope=tope
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actu=self.__cab
            self.__indice=0
            raise StopIteration
        else:
            dat=self.__actu.getdat()
            self.__indice+=1
            self.__actu=self.__actu.getsig()
            return dat
    def agreg(self,obje):
        nueno=nodo(obje)
        if self.__cab==None:
            self.__cab=nueno
            self.__actu=self.__cab
            self.__tope+=1
        else:
            nodau=self.__cab
            while nodau.getsig()!=None:
                nodau=nodau.getsig()
            if nodau.getsig()==None:
                nodau.actsig(nueno)
                self.__tope+=1
    def carga(self):
        a=open('parcial 2 luka/gestorherra.py',mode='r')
        re=csv.reader(a,delimiter=';')
        for fil in re:
            if fil[0]=='M':
                maqpes=pesadas(fil[1],fil[2],fil[3],fil[4],fil[5],fil[6],fil[7],fil[8],fil[9],fil[10])
                self.agreg(maqpes)
            elif fil[0]=='E':
                maqele=electricas(fil[1],fil[2],fil[3],fil[4],fil[5],fil[6],fil[7],fil[8],fil[9])
                self.agreg(maqele)
    def most(self):
        for herra in self:
            print(herra)
    def inciso1(self):
        ind=int(input('ingrese el indice: '))
        try:
            nodoac=self.__actu
            while self.__indice!=ind:
                nodoac=nodoac.getsig()
                self.__indice+=1
            if self.__indice==ind:
                if isinstance(nodoac.getdat(),pesadas):
                    print('es una herramienta pesada!')
                elif isinstance(nodoac.getdat(),electricas):
                    print('es una herramienta electrica!')
        except IndexError:
            print('indice fuera de rango!')
    def inciso3(self):
        capa=float(input('ingrese la capacidad de carga: '))
        cont=0
        for herra in self:
            if isinstance(herra,pesadas):
                if herra.getcapa()<=capa: #el get lo cambian
                    cont+=1
        print(f'las herramientas pesadas cuya capacidad supera a {capa} es {cont}')