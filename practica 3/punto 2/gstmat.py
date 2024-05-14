import csv
from mat_ref import material_refrac
class gestor_materiales:
    __materiales_reci:list
    def __init__(self):
        self.__materiales_reci=[]
        a=open('materiales.csv',mode='r')
        rd=csv.reader(a,delimiter=';')
        for fil in rd:
            mate=material_refrac(fil[0],fil[1],fil[2],fil[3])
            self.__materiales_reci.append(mate)
        a.close()
    def getmate(self):
        for mate in self.__materiales_reci:
            if mate.getcarac()=='bueno':
                return mate