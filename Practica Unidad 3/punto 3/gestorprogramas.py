import csv
from matricula import *
from programacapacitacion import *
class gestprog:
    __programas:list
    def __init__(self):
        self.__programas=[]
        a=open('Python\practica 3\punto 3\programas.csv',mode='r')
        rd=csv.reader(a,delimiter=';')
        for fil in rd:
            progra=programcapac(fil[0],fil[1],fil[2])
            self.__programas.append(progra)
        a.close()
    def agregmat(self,gstmat,emp,fi):
        for pro in self.__programas:
            if fi[1]==emp.getnom() and fi[2]==pro.getnomp():
                mat=matricula(fi[0],emp,pro)
                gstmat.agregmat(mat)