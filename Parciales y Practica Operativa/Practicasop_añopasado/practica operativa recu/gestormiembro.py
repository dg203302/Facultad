from miembro import *
import numpy as np
import csv
class gestormiembro:
    __gestmiem:np.array
    def __init__(self):
        self.__gestmiem=[]
        a=open('Python/Practicasop_añopasado/practica operativa recu/Miembros.csv',mode='r') #esto cambialo
        red=csv.reader(a,delimiter=';')
        for fil in red:
            miem=miembro(fil[0],fil[1],fil[2])
            self.__gestmiem.append(miem)
        a.close()
    def a(self,gstvisua):
        corre=input('ingrese el correo del miembro: ')
        i=0
        while self.__gestmiem[i].getcorreo()!=corre:
            i+=1
        if self.__gestmiem[i].getcorreo()==corre:
            gstvisua.mostrarminutos(self.__gestmiem[i].getid())
    def most(self,idvisu):
        i=0
        while not(self.__gestmiem[i].getid()==idvisu):
            i+=1
        if self.__gestmiem[i].getid()==idvisu:
            print(f'{self.__gestmiem[i].getapnom()}{self.__gestmiem[i].getcorreo()}')