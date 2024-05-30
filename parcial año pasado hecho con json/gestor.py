from transporte import *
from embalaje import *
from nodo import *
import csv
class gestorservicios:
    __cab:nodo
    __actu:nodo
    __indi=int
    __tope=int
    def __init__(self):
        self.__cab=None
        self.__actu=None
        self.__indi=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indi==self.__tope:
            self.__actu=self.__cab
            self.__indi=0
            raise StopIteration
        else:
            self.__indi+=1
            dat=self.__actu.getdat()
            self.__actu=self.__actu.getsig()
            return dat
    def agreg(self,obj): ##IMPORTANTE PARA MAÑANA!!!!!
        nueno=nodo(obj)
        if self.__cab==None:
            self.__cab=nueno
            self.__actu=nueno
            self.__tope+=1
        else:
            nodau=self.__cab
            while nodau.getsig()!=None:
                nodau=nodau.getsig()
            if nodau.getsig()==None:
                nodau.actsig(nueno)
                self.__actu=self.__cab
                self.__tope+=1
    def cargaautojson(self,encoder): #carga con json
        dic=encoder.load()
        for obje in dic['servicios']:
            if obje['tipo']=='transporte':
                transp=transporte(**obje['atributos'])
                self.agreg(transp)
            elif obje['tipo']=='embalaje':
                emba=embalaje(**obje['atributos'])
                self.agreg(emba)
    def cargamanual(self): #carga manual
        nomemp=input('ingrese el nombre de la empresa: ')
        nomcont=input('ingrese el nombre del contratante: ')
        direcon=input('ingrese la direccion del contratante: ')
        fecha=input('ingrese la fecha: ')
        comision=input('ingrese la comision: ')
        tipo=input('que tipo de servicio es?')
        if tipo == 'transporte':
            prechora=input('ingrese el precio por hora: ')
            psocar=input('ingrese el peso de la carga: ')
            diredest=input('ingrese la direccion de destino: ')
            canthora=input('ingrese la cantidad de horas:')
            transp=transporte(nomemp,nomcont,direcon,fecha,comision,prechora,psocar,diredest,canthora)
            self.agreg(transp)
        elif tipo == 'embalaje':
            precuni=input('ingrese el precio por unidad: ')
            peso=input('ingrese el peso por unidad: ')
            cant=input('ingrese la cantidad de unidades: ')
            emba=embalaje(nomemp,nomcont,direcon,fecha,comision,precuni,peso,cant)
            self.agreg(emba)
    def b(self):
        ac=0
        tra=[]
        for serv in self:
            if isinstance(serv,transporte):
                tra.append(serv)
        tra.sort()
        print('servicios de transporte realizados:\ncontratante Costo total')
        for transp in tra:
            print(f'{transp.getcontra()}{transp.getcosto()}')
            ac+=transp.getcosto()
        print(f'total recaudado {ac}')
    def c(self):
        c=0
        for serv in self:
            if isinstance(serv,embalaje) and serv.getpesoxuni()>50:
                c+=1
        print(f'la cantidad de servicios fue: {c}')
    def d(self):
        conttr=0
        contem=0
        fecha=input('ingrese la fecha del servicio: ')
        try:
            for serv in self:
                if isinstance(serv,embalaje) and serv.getfechacon()==fecha:
                    contem+=1
                elif isinstance(serv,transporte) and serv.getfechacon()==fecha:
                    conttr+=1
            if contem>conttr:
                print(f'para la fecha {fecha} fue {contem}')
            elif conttr>contem:
                print(f'para la fecha {fecha} fue {conttr}')
        except AttributeError:
            print('fecha mal ingresada!!!')
    def insertar(self,obj):
        nuen=nodo(obj)
        pos=int(input('ingrese la posicion que desee insertar: '))
        if pos==0:
            nuen.actsig(self.__cab)
            self.__actu=nuen
            self.__tope+=1
        else:
            nodau=self.__cab
            while nodau!=None and self.__indi<(pos-1):
                nodau=nodau.getsig()
                self.__indi+=1
            if self.__indi==(pos-1):
                nuen.actsig(nodau.getsig())
                nodau.actsig(nuen)
                self.__actu=self.__cab
                self.__indi=0
                self.__tope+=1
    def eliminar(self):   #eliminar importante para mañana!!!!!!!!!!!
        pos=int(input('ingrese la posicion que desee eliminar: '))
        if pos==0:
            nodelimin=self.__cab
            self.__cab=self.__cab.getsig()
            self.__tope-=1
            del nodelimin
        else:
            nodaux=self.__cab
            while nodaux!=None and self.__indi<(pos-1):
                nodoant=nodaux
                nodaux=nodaux.getsig()
                self.__indi+=1
            if self.__indi==(pos-1):
                nodelimin=nodaux
                nodoant.actsig(nodaux.getsig())
                self.__actu=self.__cab
                self.__tope-=1
                self.__indi=0
                del nodelimin
    def insertarmanual(self):
        nomemp=input('ingrese el nombre de la empresa: ')
        nomcont=input('ingrese el nombre del contratante: ')
        direcon=input('ingrese la direccion del contratante: ')
        fecha=input('ingrese la fecha: ')
        comision=input('ingrese la comision: ')
        tipo=input('que tipo de servicio es?')
        if tipo == 'transporte':
            prechora=input('ingrese el precio por hora: ')
            psocar=input('ingrese el peso de la carga: ')
            diredest=input('ingrese la direccion de destino: ')
            canthora=input('ingrese la cantidad de horas:')
            transp=transporte(nomemp,nomcont,direcon,fecha,comision,prechora,psocar,diredest,canthora)
            self.insertar(transp)
        elif tipo == 'embalaje':
            precuni=input('ingrese el precio por unidad: ')
            peso=input('ingrese el peso por unidad: ')
            cant=input('ingrese la cantidad de unidades: ')
            emba=embalaje(nomemp,nomcont,direcon,fecha,comision,precuni,peso,cant)
            self.insertar(emba)
    def tojson(self,encoder):
        dic=dict(tipo=__class__.__name__,servicios=[serv.tojson() for serv in self])
        encoder.save(dic)
    #para unittest
    def getuldat(self):
        nodau=self.__cab
        while nodau.getsig()!=None:
            nodau=nodau.getsig()
        if nodau.getsig()==None:
            return nodau.getdat()