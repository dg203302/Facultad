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
    def cargaautocsv(self): #carga con csv
        a=open('Python/Nueva carpeta/servicios.csv',mode='r')
        re=csv.reader(a,delimiter=';')
        for fil in re:
            if fil[0]=='transporte':
                transp=transporte(fil[1],fil[2],fil[3],fil[4],fil[5],fil[6],fil[7],fil[8],fil[9])
                self.agreg(transp)
            elif fil[0]=='embalaje':
                emba=embalaje(fil[1],fil[2],fil[3],fil[4],fil[5],fil[6],fil[7],fil[8])
                self.agreg(emba)
        a.close()
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
        for serv in self:
            if isinstance(serv,embalaje) and serv.getfechacon()==fecha:
                contem+=1
            elif isinstance(serv,transporte) and serv.getfechacon()==fecha:
                conttr+=1
        if contem>conttr:
            print(f'para la fecha {fecha} fue {contem}')
        elif conttr>contem:
            print(f'para la fecha {fecha} fue {conttr}')
    def most(self):
        for serv in self:
            print(serv)
    #para unittest
    def getuldat(self):
        nodau=self.__cab
        while nodau.getsig()!=None:
            nodau=nodau.getsig()
        if nodau.getsig()==None:
            return nodau.getdat()