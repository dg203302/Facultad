from refrigerados import *
from congelados import *
import csv
class gestorproductos:
    __gest=list
    def __init__(self):
        self.__gest=[]
        self.cargacsv()
    def cargacsv(self):
        a=open('Parcial 2 codigo/productos.csv',mode='r')
        re=csv.reader(a,delimiter=';')
        for fila in re:
            if fila[0]=='C':
                prdcon=congelado(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12],)
                self.__gest.append(prdcon)
            elif fila[0]=='R':
                prdref=refrigerados(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
                self.__gest.append(prdref)
        a.close()
    def agreg(self):  #incisoa
        Nombreprod=input('ingrese el nombre del producto: ')
        fechaenvasado=input('ingrese la fecha de envasado: ')
        fechavencimiento=input('ingrese la fecha de vencimiento: ')
        temperaturamantrec=input('ingrese la temperatura de mantenimiento: ')
        paisorigen=input('ingrese el pais de origen: ')
        numlote=input('ingrese el numero de lote: ')
        costobase=input('ingrese el costo base: ')
        tipo=input('que tipo es?\n -')
        if tipo=='refrigerado':
            codigoorg=input('ingrese el código del organismo de supervisión alimentaria: ')
            alimref=refrigerados(Nombreprod,fechaenvasado,fechavencimiento,temperaturamantrec,paisorigen,numlote,costobase,codigoorg)
            self.__gest.append(alimref)
        elif tipo=='congelado':
            nitro=input('ingrese el porcentaje de nitrogeno: ')
            oxig=input('ingrese el porcentaje de oxigeno: ')
            dioxi=input('ingrese el porcentaje de dioxido de carbono: ')
            vapor=input('ingres el procentaje de vapor de agua: ')
            metodo=input('ingrese el metodo con el que fue congelado: ')
            alimcong=congelado(Nombreprod,fechaenvasado,fechavencimiento,temperaturamantrec,paisorigen,numlote,costobase,nitro,oxig,dioxi,vapor,metodo)
            self.__gest.append(alimcong)
    def b(self):
        pos=int(input('ingrese la posicion que desee saber: '))
        try:
            if isinstance(self.__gest[pos-1],refrigerados):
                print(f'el producto almacenado en la posicion {pos} es un producto refrigerado!')
            elif isinstance(self.__gest[pos-1],congelado):
                print(f'el producto almacenado en la posicion {pos} es un producto congelado!')
        except IndexError:
            print(f'indice {pos} incorrecto!')
    def c(self):
        ccong=0
        cref=0
        for prod in self.__gest:
            if isinstance(prod,congelado):
                ccong+=1
            elif isinstance(prod,refrigerados):
                cref+=1
        print(f'la cantidad de productos congelados almacenados es {ccong}\nla cantidad de productos refrigerados es: {cref}')
    def d(self):
        for prod in self.__gest:
            print(prod)