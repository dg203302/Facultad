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
    def maxim(self,dni,est):
        i=0
        while self.__federas[i].getdni() != dni:
            i+=1
        if self.__federas[i].getdni() == dni:
            print(f'datos del federado que obtuvo el mayor puntaje: {self.__federas[i].getnom()} {self.__federas[i].getap()} {self.__federas[i].getclub()} {est}')
    def edayest(self,i,ed):
        if self.__federas[i].getedad() == ed:
            print(f'datos del patinador {i}: {self.__federas[i].getnom()} {self.__federas[i].getap()} {self.__federas[i].getdni()}')
    def most(self,i):
        print(f'datos Patinador Escuela: {self.__federas[i].getnom()} {self.__federas[i].getap()} {self.__federas[i].getedad()} {self.__federas[i].getdni()}')