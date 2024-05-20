import csv
from ladrillo import Ladrillo
from gstmat import gestor_materiales
class gestor_ladrillo:
    __ladr:list
    def __init__(self,gsmat):
        self.__ladr=[]
        a=open('practica 3/punto 2/ladrillos.csv',mode='r')
        rd=csv.reader(a,delimiter=';')
        for fil in rd:
            if fil[0]!=fil[1]:
                ladr=Ladrillo(fil[0],fil[1],fil[2],fil[3])
                gsmat.agreg(ladr)
                self.__ladr.append(ladr)
        a.close()
    def incisoa(self):
        iden=input('ingrese el identificador de ladrillo: ')
        i=0
        while self.__ladr[i].getid()!=iden:
            i+=1
        if self.__ladr[i].getid()==iden:
            self.__ladr[i].a()
    def incisob(self):
        for lad in self.__ladr:
            print(f'costo total: {lad.getcost()}')
    def incisoc(self):
        for lad in self.__ladr:
            lad.mostrar_dat()