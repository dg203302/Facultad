import csv
from Federado import feder
class gestfed:
    __federas:list
    def __init__(self):
        self.__federas= []
    def agreg(self):
        arc=open('Practicasop_añopasado/Practica_tema1/federados.csv')
        reader=csv.reader(arc,delimiter=';')
        for fila in reader:
            ap,nom,dni,ed,clu=fila
            fed=feder(ap,nom,dni,ed,clu)
            print(fed)
            self.__federas.append(fed)
    def getnomfed(self,i):
        return self.__federas[i].getnom()
    def getapfed(self,i):
        return self.__federas[i].getap()
    def getedadfed(self,i):
        return self.__federas[i].getedad()
    def getclubfed(self, i):
        return self.__federas[i].getclub()