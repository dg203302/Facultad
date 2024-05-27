from electrico import *
from gas import *
from nodo import *
from encoderjson import *
from interfacep5 import *
class lkdlist(interface):
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
    def insertar(self,objt):
        nueno=nodo(objt)
        pos=int(input('ingrese el indice donde quiera almacenar: '))
        try:
            if pos==0:
                nueno.actsig(self.__cab)
                self.__cab=nueno
            else:
                i=0
                nodaux=self.__cab
                while nodaux != None and i<(pos-1):
                    nodaux=nodaux.getsig()
                    i+=1
                if i==(pos-1):
                    nueno.actsig(nodaux)
                    nodoaux=nueno
                    self.__actual=nueno
                    self.__tope+=1
        except IndexError:
            print('indice fuera de rango!')
        except AttributeError:
            print('error de atributo!')
    def ayb(self): #inciso a y b combinados por conveniencia
        calef=input('que tipo de calefactor quiere agregar: ')
        if calef == 'electrico':
            marc=input('ingrese la marca: ')
            mod=input('ingrese el modelo: ')
            pais=input('ingrese el pais: ')
            precio=float(input('ingres el precio: '))
            formpag=input('ingrese la forma de pago')
            cantcu=int(input('ingrese la cantidad de cuotas: '))
            prom=input('tiene promocion??')
            if prom == 'si':
                pr=True
            else:
                pr=False
            pot=input('ingrese la potencia: ')
            calefele=electrico(marc,mod,pais,precio,formpag,cantcu,pr,pot)
            self.insertar(calefele)
        elif calef == 'gas':
            marc=input('ingrese la marca: ')
            mod=input('ingrese el modelo: ')
            pais=input('ingrese el pais: ')
            precio=float(input('ingres el precio: '))
            formpag=input('ingrese la forma de pago')
            cantcu=int(input('ingrese la cantidad de cuotas: '))
            prom=input('tiene promocion??')
            if prom == 'si':
                pr=True
            else:
                pr=False
            matr=input('ingrese la matricula: ')
            calo=input('ingrese la calorias: ')
            calefgas=gas(marc,mod,pais,precio,formpag,cantcu,pr,matr,calo)
            self.insertar(calefgas)
    def most(self): #inciso c
        try:
            pos=int(input('ingrese el indice que desee saber: '))
            i=0
            while self.__cab!=None and i<(pos-1):
                self.__cab=self.__cab.getsig()
                i+=1
            if i==(pos-1):
                if isinstance(self.__cab.getdat(),electrico):
                    print('es un calefactor electrico!')
                elif isinstance(self.__cab.getdat(),gas):
                    print('es un calefactor a gas!')
        except IndexError:
            print('indice supera el limite de la lista!')
        except ValueError:
            print('indice erroneo!')
    def d(self):
        calesgas=[]
        for cale in self:
            if isinstance(cale,gas):
                calesgas.append(cale)
        mini=min(calesgas)
        for cale in self:
            if isinstance(cale,gas) and cale==mini:
                print(f'{cale.getmarc()} {cale.getmode()} {cale.getkilocalo()}')
    def e(self):
        marca=input('ingrese la marca del calefactor: ')
        for cale in self:
            if isinstance(cale,electrico) and cale.getmarc()==marca:
                print(f'{cale.getmode()} {cale.getpote()} {cale.getprec()}')
    def f(self):
        for cale in self:
            if cale.getprom()==True:
                print(f'{cale.getmode()} {cale.getpais()} {cale.getimpo()}')
#guardado correcto de json
    def tojson(self,encdjson):
        d=dict(calefactores=[cale.tojson() for cale in self])
        encdjson.guardarjson(d)
#guardado correcto de json