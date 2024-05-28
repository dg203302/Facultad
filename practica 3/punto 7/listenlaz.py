from docenteinvestigador import *
from personalapoyo import *
from nodo import *
from interfaz import * #despues la incluyo en la clase
class listenla():
    __cab:nodo
    __act:nodo
    __tope:int
    __indice:int
    def __init__(self,cabe=None,actu=None):
        self.__cab=cabe
        self.__act=actu
        self.__indice=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__act=self.__cab
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dat=self.__act.getdat()
            self.__act=self.__act.getsig()
            return dat
    def agreg(self,objt):
        nuenodo=nodo(objt)
        nuenodo.actsig(self.__cab)
        self.__cab=nuenodo
        self.__act=nuenodo
        self.__tope+=1
    def carga(self,encoder):
        dicj=encoder.leerjson()
        for obje in dicj['personal']:
            if obje['tipo']=='docente':
                doce=docente(**obje['datos'])
                self.agreg(doce)
            elif obje['tipo']=='personal_de_apoyo':
                perapyo=personalapoyo(**obje['datos'])
                self.agreg(perapyo)
            elif obje['tipo']=='investigador':
                invest=investigador(**obje['datos'])
                self.agreg(invest)
            elif obje['tipo']=='docente_investigador':
                docinvest=docenteinvest(**obje['datos'])
                self.agreg(docinvest)
    def tojson(self,encoder):
        dic=dict(personal=[pers.tojson() for pers in self])
        encoder.guardjson(dic)