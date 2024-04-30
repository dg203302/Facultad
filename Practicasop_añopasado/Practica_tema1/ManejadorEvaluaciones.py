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
        i=0
        while i < len(self.__puntajes):
            if gestfed.getedadfed(i) == ed and self.__puntajes[i].getest() == est:
                print(f'datos del patinador {i}: {gestfed.getnomfed(i)} {gestfed.getapfed(i)} {self.__puntajes[i].getdni()}')
            else:
                print('incorrecto!') 
            i+=1
    def b(self,gestfed):
        i=0
        maxp=max(self.__puntajes)
        while i < len(self.__puntajes):
            if self.__puntajes[i].getpunt() == maxp:
                print(f'datos del maximo patinador: {gestfed.getnomfed(i)} {gestfed.getapfed(i)} {gestfed.getclubfed(i)}')
            else:
                print('incorrecto!') 
            i+=1
    def c(self,gestfed):
        i=0
        while i < len(self.__puntajes):
            if self.__puntajes[i].getest() == 'E':
                print(f'datos: {gestfed.getnomfed(i)} {gestfed.getapfed(i)} {gestfed.getedadfed(i)} {self.__puntajes[i].getdni()}')
            elif self.__puntajes[i].getest() == 'L':
                print(f'datos: {gestfed.getnomfed(i)} {gestfed.getapfed(i)} {gestfed.getedadfed(i)} {self.__puntajes[i].getdni()}')
            i+=1
    def d(self):
        i=0
        dni=input('ingrese el dni del inscripto: ')
        est=input('ingrese el estilo: ')
        while i < len(self.__puntajes):
            if dni == self.__puntajes[i].getdni and est == self.__puntajes[i].getest():
                print(f'valoraciones: {self.__puntajes[i].getp1()} {self.__puntajes[i].getp2()} {self.__puntajes[i].getp3()}')
            i+=1