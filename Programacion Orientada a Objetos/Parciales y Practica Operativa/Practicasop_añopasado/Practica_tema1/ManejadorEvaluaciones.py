import csv
from Puntaje import punta
class gestpun:
    __puntajes:list
    def __init__(self):
        self.__puntajes= []
    def agreg(self):
        arc=open('Practicasop_añopasado/Practica_tema1/evaluacion.csv')
        reader=csv.reader(arc,delimiter=';')
        for fila in reader:
            dni,est,p1,p2,p3=fila
            punts=punta(dni,est,p1,p2,p3)
            print(punts)
            self.__puntajes.append(punts)
    def a(self,gestfed):
        est=input('ingrese el estilo que desee saber: ')
        ed=input('ingrese la edad que desee saber: ')
        for i in range(0,len(self.__puntajes)):
            if self.__puntajes[i].getest() == est:
                gestfed.edayest(i,ed)
    def b(self,gestfed):
        jugm=max(self.__puntajes)
        gestfed.maxim(jugm.getdni(),jugm.getest())
    def c(self,gestfed):
        for i in range(0,len(self.__puntajes)):
            if self.__puntajes[i].getest() == 'E':
                gestfed.most(i)
            elif self.__puntajes[i].getest() == 'L':
                gestfed.most(i)
    def d(self):
        dni=input('ingrese el dni del inscripto: ')
        est=input('ingrese el estilo: ')
        i=0
        while dni != self.__puntajes[i].getdni() and est != self.__puntajes[i].getest():
            i+=1
        if dni == self.__puntajes[i].getdni() and est == self.__puntajes[i].getest():
            print(f'puntajes: {self.__puntajes[i].getp1()} {self.__puntajes[i].getp2()} {self.__puntajes[i].getp3()}')