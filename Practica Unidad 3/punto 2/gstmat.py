import csv
from mat_ref import material_refrac
class gestor_materiales:
    __materiales_reci:list
    def __init__(self):
        self.__materiales_reci=[]
        a=open('practica 3/punto 2/ladrillos.csv',mode='r')
        rd=csv.reader(a,delimiter=';')
        for fil in rd:
            if fil[0]==fil[1]:
                mate=material_refrac(fil[2],fil[3],fil[4],fil[5])
                self.__materiales_reci.append(mate)
        a.close()
    def agreg(self,lad):
        a=open('practica 3/punto 2/ladrillos.csv',mode='r')
        red=csv.reader(a,delimiter=';')
        for fil in red:
            for mat in self.__materiales_reci:
                    if lad.getid()==fil[1] and mat.getnom()==fil[2]:
                        mat.addladri(lad)
                        lad.addmateref(mat)
        a.close()