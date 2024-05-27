from electrico import *
from gas import *
from nodo import *
from encoderjson import *
from interfacep5 import *
class lkdlist(): #agregar la interfaz
    __cab:nodo
    __actual:nodo
    __indi:int
    __tope:int
    def __init__(self,encjson):
        self.__cab=None
        self.__actual=None
        self.__indi=0
        self.__tope=0
        self.carga(encjson)
#sobrecarga de iter
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
#sobrecarga de iter
#lectura correcta de json
    def agreg(self, objt):
        nueno=nodo(objt)
        nueno.actsig(self.__cab)
        self.__cab=nueno
        self.__actual=nueno
        self.__tope+=1
    def carga(self,encdjson):
        dic=encdjson.leerjson()
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
#lectura correcta de json
#guardado correcto de json
    def tojson(self,encdjson):
        d=dict(calefactores=[cale.tojson() for cale in self])
        encdjson.guardarjson(d)
#guardado correcto de json
    def mostrar(self):
        for ele in self:
            print(ele)