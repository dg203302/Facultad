from electrico import *
from gas import *
from nodo import *
from interfacep5 import *
import json
class lkdlist(): #agregar la interfaz
    __cab:nodo
    __actual:nodo
    __indi:int
    __tope:int
    def __init__(self):
        self.__cab=None
        self.__actual=None
        self.__indi=0
        self.__tope=0
        self.carga()
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indi==self.__tope:
            self.__actual=self.__cab
            self.__indi=0
            raise StopIteration
        else:
            self.__indi+=1
            dat=self.__actual.getdat()
            self.__actual=self.__actual.getsig()
            return dat
    def agreg(self, objt):
        nueno=nodo(objt)
        nueno.actsig(self.__cab)
        self.__cab=nueno
        self.__actual=nueno
        self.__tope+=1
    def leerjson(self):
        with open('Python/practica 3/punto 6/calefactores.json',mode='r') as arc:
            da=json.load(arc)
            arc.close()
            return da
    def carga(self):
        dic=self.leerjson()
        for obje in dic['calefactores']:
            try:
                if obje['tipo'] == 'electrico':
                    calele=electrico(**obje["atributos"])
                    self.agreg(calele)
                elif obje['tipo'] == 'gas':
                    calgas=gas(**obje["atributos"])
                    self.agreg(calgas)
            except KeyError:
                print('claves no existentes!',obje)
    def guardarjson(self,dge):
        with open('Python/practica 3/punto 6/calefactoresguard.json',mode='a') as guard:
            json.dump(dge,guard)
            guard.close()
    def tojson(self):
        d=dict(calefactores=[cale.tojson() for cale in self])
        self.guardarjson(d)
    def mostrar(self):
        for ele in self:
            print(ele)