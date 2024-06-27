import csv
from empleado import *
class gestemp:
    __empleados:list
    def __init__(self):
        self.__empleados=[]
        a=open('Python\practica 3\punto 3\empleados.csv',mode='r')
        rd=csv.reader(a,delimiter=';')
        for fil in rd:
            emp=empleado(fil[0],fil[1],fil[2])
            self.__empleados.append(emp)
        a.close()
    def registrar_empleados(self,gstpro,gstmat):
        a=open('Python\practica 3\punto 3\matriculas.csv',mode='r')
        rd=csv.reader(a,delimiter=';')
        for fi in rd:
            for emp in self.__empleados:
                gstpro.agregmat(gstmat,emp,fi)
        a.close()
    def incisoc(self,gstm):
        for emplead in self.__empleados:
            gstm.c(emplead)