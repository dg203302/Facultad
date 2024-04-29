import csv
from GESTOREQU import gest_equi
from FECHAS import fecha
class gest_fech:
    __fechas:list
    def __init__(self):
        self__fechas=[]
    def cargafecha(self):
        arc=open('punto 5/fechasfutbol.csv')
        reader=csv.reader(arc,delimiter=';')
        for fila in reader:
            fech,idloc,idvisit,cantgoll,cantgolv=fila
            fec=fecha(fech,idloc,idvisit,cantgoll,cantgolv)
            self.__fechas.append(fec)
    def listado(self,gestore):
        acgolafav=0
        acgolencon=0
        acdifgole=0
        acpun=0
        nom=input('ingrese el nombre del equipo: ')
        i=gestore.busc(nom)
        if i != None:
            print(f'EQUIPO: {gestore[i].getnom()}')
            print('|fecha| |goles a favor| |goles en contra| |diferencia de goles| |puntos|')
            for fecha in range(self.__fechas):
                if gestore[i].getid() == self.__fechas[fecha].getidloc() or gestore[i].getid() == self.__fechas[fecha].getidvisi():
                    acgolafav+=gestore[i].getgolesaf()
                    acgolencon+=gestore[i].getgolesec()
                    acdifgole+=gestore[i].getdifgol()
                    acpun+=gestore[i].getpunt()
                    print(f'{gestore[i].getgolesaf()} {gestore[i].getgolesec()} {gestore[i].getdifgol()} {gestore[i].getpunt()}')
            print(f'totales: {acgolafav} {acgolencon} {acdifgole} {acpun}')
#faltan incisos d e f