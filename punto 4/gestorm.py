import csv
from moto import  moto
class gestormoto:
    __motos: list
    def __init__(self):
        self.__motos=[]
    def agreg(self):
        arch=open('C:/Users/Lolma/Documents/Codigos/Python/punto 4/motos.csv')
        reader=csv.reader(arch,delimiter=';')
        for fila in reader:
            if len(fila) == 4:
                patente,marca,nya,km=fila
                mot=moto(patente,marca,nya,km)
                self.__motos.append(mot)
    def valmar(self, marca):
        i=0
        while i < len(self.__motos):
            if self.__motos[i].getmarc()== marca:
                print('moto encontrada')
                return self.__motos[i].getpat()
                break
            i+=1
    def mdat(self, pate):
        i=0
        while i < len(self.__motos):
            if self.__motos[i].getpat() == pate:
                print(self.__motos[i])
            i+=1