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
                return i
            else:
                return None
            i+=1