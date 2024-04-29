import csv
from EQUIPO import equipo
class gest_equi:
    __equip:list
    def __init__(self):
        self__equip=[]
    def cargaequi(self):
        arc=open('punto 5/equipos2024.csv')
        reader=csv.reader(arc,delimiter=';')
        for fila in reader:
            id,nom,golf,golc,difgol,pun=fila
            eq=equipo(id,nom,golf,golc,difgol,pun)
            self.__equip.append(eq)
    #en el main busca el indice del equipo, despues en el gestor de fechas busco el id de fechas y comparo con el del equipo
    def busc(self,nom):
        i=0
        while i < len(self.__equip):
            if self.__equip[i].getnom():
                break
            i+=1
        if self.__equip[i].getnom == nom:
            return i
        else:
            return None
    def actu(self,idl,idv,cgloc,cgvisi):
        for i in self.__equip:
            if self.__equip[i].getid() == idl:
                if cgloc == cgvisi:
                    self.__equip[i].modificpun(1)
                elif cgloc > cgvisi:
                    self.__equip[i].modificpun(3)
                    self.__equip[i].modificg(cgloc)
                elif cgvisi > cgloc:
                    self.__equip[i].modificgcon(cgvisi)
            elif self.__equip[i].getid() == idv:
                if cgvisi == cgloc:
                    self.__equip[i].modificpun(1)
                elif cgvisi > cgloc:
                    self.__equip[i].modificpun(3)
                    self.__equip[i].modificg(cgvisi)
    def ordenyalmacen(self):
        self.__equip.sort()
        arc=open('punto 5\equipos2024.csv')
        writer=csv.writer(arc,delimiter=';')
        writer.writerows(self.__equip)
    def __del__(self):
        for elem in self.__equip:
            del elem
        print('gestor de equipos destruido!')