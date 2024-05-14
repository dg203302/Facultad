import csv
from ladrillo import Ladrillo
from gstmat import gestor_materiales
class gestor_ladrillo:
    __ladr:list
    def __init__(self):
        self.__ladr=[]
        a=open('ladrillos.csv',mode='r')
        rd=csv.reader(a,delimiter=';')
        for fil in rd:
            ladr=Ladrillo(fil[0],fil[1],fil[2],fil[3],fil[4],fil[5],fil[6])
            
            self.__ladr.append(ladr)
        a.close()
    def agregmat(self,gstmat):
        for lad in self.__ladr:
            mate=gstmat.getmate()
            self.__ladr.addmateref(mate)