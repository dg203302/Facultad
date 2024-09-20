import csv
from pedido import  pedido
class gestorped:
    __pedidos: list
    def __init__(self):
        self.__pedidos=[]
    def agreg(self):
        arch=open('C:/Users/Lolma/Documents/Codigos/Python/punto 4/pedidos.csv')
        reader=csv.reader(arch,delimiter=';')
        for fila in reader:
                patente,id,comi,tiest,precio=fila
                ped=pedido(patente,id,comi,tiest,precio)
                print(ped)
                self.__pedidos.append(ped)
        self.__pedidos.sort()
    def nuev(self,gestmot):
        idn=input('id del nuevo pedido: ')
        comn=input('comidas del nuevo pedido: ')
        test=input('tiempo estimado del nuevo pedido: ')
        marca=input('marca de la moto para asignar: ')
        npat=gestmot.valmar(marca)
        nped=pedido(npat,idn,comn,test)
        self.__pedidos.append(nped)
    def modif(self, pate, idped, treal):
        i=0
        while i < len(self.__pedidos):
            if self.__pedidos[i].getpat() == pate and self.__pedidos[i].getid() == idped:
                self.__pedidos[i].modifictr(treal)
                break
            i+=1
    def datprod(self, gestmot,pat):
        i=0
        tiem=[]
        gestmot.mdat(pat)
        while i < len(self.__pedidos):
            if self.__pedidos[i].getpat() == pat:
                tiem.append(self.__pedidos[i].gettreal)
            i+=1
        if len(tiem) != 0:
            print(sum(tiem)/len(tiem))
        else:
            print('no tiene horas registradas')
    def dat(self,pate):
        tot=0
        print('Identificador de pedido Tiempo estimado Tiempo Real Precio')
        i=0
        for pedido in self.__pedidos:
            if pedido.getpat() == pate:
                print(f'{pedido.getid()} {pedido.gettest()} {pedido.gettreal()} {pedido.getpre()}')
                tot+=pedido.getpre()
            i+=1
        print(f'total: {tot} \n comision: {(tot*20)/100}')