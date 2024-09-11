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
    def agreg(self,objt): #inciso 2
        nuenodo=nodo(objt)
        nuenodo.actsig(self.__cab)
        self.__cab=nuenodo
        self.__act=nuenodo
        self.__tope+=1
    def insertar(self,objt): #inciso 1
        pos=int(input('ingrese la posicion que desee insertar: '))
        if pos==0:
            self.agreg(objt)
        else:
            nueno=nodo(objt)
            nodau=self.__cab
            i=0
            while nodau!=None and i<(pos-1):
                nodau=nodau.getsig()
                i+=1
            if i==(pos-1):
                nueno.actsig(nodau.getsig())
                nodau.actsig(nueno)
                self.__tope+=1
    def a(self):
        cuil=input('ingrese el cuil del agente: ')
        ape=input('ingrese el apellido del agente: ')
        nom=input('ingrese el nombre del agente: ')
        sueld=input('ingrese el sueldo del agente: ')
        antig=input('ingrese la antiguedad del agente: ')
        tipo=input('que tipo de agente es?: ')
        if tipo=='docente':
            carre=input('ingrese la carrera: ')
            cargo=input('ingrese el cargo: ')
            cated=input('ingrese la catedra: ')
            doc=docente(cuil,ape,nom,sueld,antig,carre,cargo,cated)
            self.insertar(doc)
        elif tipo=='investigador':
            areain=input('ingrese el area de investigacion: ')
            tipinv=input('ingrese el tipo de investigacion: ')
            inve=investigador(cuil,ape,nom,sueld,antig,areain,tipinv)
            self.insertar(inve)
        elif tipo=='docente investigador':
            carre=input('ingrese la carrera: ')
            cargo=input('ingrese el cargo: ')
            cated=input('ingrese la catedra: ')
            areain=input('ingrese el area de investigacion: ')
            tipinv=input('ingrese el tipo de investigacion: ')
            catepro=input('ingrese la categoria del programa: ')
            impext=input('ingrese el importe extra: ')
            doceinv=docenteinvest(cuil,ape,nom,sueld,antig,carre,cargo,cated,areain,tipinv,catepro,impext)
            self.insertar(doceinv)
        elif tipo=='personal de apoyo':
            categor=input('ingrese la categoria: ')
            persoapo=personalapoyo(cuil,ape,nom,sueld,antig,categor)
            self.insertar(persoapo)
    def b(self):
        cuil=input('ingrese el cuil del agente: ')
        ape=input('ingrese el apellido del agente: ')
        nom=input('ingrese el nombre del agente: ')
        sueld=input('ingrese el sueldo del agente: ')
        antig=input('ingrese la antiguedad del agente: ')
        tipo=input('que tipo de agente es?: ')
        if tipo=='docente':
            carre=input('ingrese la carrera: ')
            cargo=input('ingrese el cargo: ')
            cated=input('ingrese la catedra: ')
            doc=docente(cuil,ape,nom,sueld,antig,carre,cargo,cated)
            self.agreg(doc)
        elif tipo=='investigador':
            areain=input('ingrese el area de investigacion: ')
            tipinv=input('ingrese el tipo de investigacion: ')
            inve=investigador(cuil,ape,nom,sueld,antig,areain,tipinv)
            self.agreg(inve)
        elif tipo=='docente investigador':
            carre=input('ingrese la carrera: ')
            cargo=input('ingrese el cargo: ')
            cated=input('ingrese la catedra: ')
            areain=input('ingrese el area de investigacion: ')
            tipinv=input('ingrese el tipo de investigacion: ')
            catepro=input('ingrese la categoria del programa: ')
            impext=input('ingrese el importe extra: ')
            doceinv=docenteinvest(cuil,ape,nom,sueld,antig,carre,cargo,cated,areain,tipinv,catepro,impext)
            self.agreg(doceinv)
        elif tipo=='personal de apoyo':
            categor=input('ingrese la categoria: ')
            persoapo=personalapoyo(cuil,ape,nom,sueld,antig,categor)
            self.agreg(persoapo)
    def c(self):
        pos=int(input('ingrese la posicion de la lista que desee saber: '))
        i=0
        nodau=self.__cab
        while nodau!=None and i<(pos-1):
           nodau=nodau.getsig()
           i+=1
        if i==(pos-1):
            if isinstance(nodau,docente):
                print('es un docente!')
            elif isinstance(nodau,investigador):
                print('es un investigador!')
            elif isinstance(nodau,docenteinvest):
                print('es un docente investigador!')
            elif isinstance(nodau,personalapoyo):
                print('es un personal de apoyo!')
    def d(self):
        carre=input('ingrese la carrera que desee saber: ')
        docinv=[]
        for pers in self:
            if isinstance(pers,docenteinvest):
                docinv.append(pers)
        docinv.sort()
        for doc in docinv:
            print(doc)
    def e(self):
        area=input('ingrese el area de investigacion: ')
        c1=0
        c2=0
        for pers in self:
            if isinstance(pers,docenteinvest):
                c1+=1
            elif isinstance(pers,investigador):
                c2+=1
        print(f'cantidad\ndocentes investigadores: {c1}\ninvestigadores: {c2}')
    def f(self):
        perso=[]
        for per in self:
            perso.append(per)
        perso.sort()
        for pers in perso:
            print(f'{pers.getnom()}{pers.getape()}{pers.gettip()}{pers.getsueld()}')
    def e(self):
        categor=input('ingrese la categoria: ')
        ac=0
        for pers in self:
            if isinstance(pers,docenteinvest):
                print(f'{pers.getnom()}{pers.getape()}{pers.getimpext()}')
                ac+=pers.getimpext()
        print(ac)
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