from visualizacion import *
import csv
class gestorvisua:
    __gestorvi:list
    def __init__(self):
        self.__gestorvi=[]
        a=open('Practica_operativa/Visualizaciones.csv',mode='r') #esto cambialo
        red=csv.reader(a,delimiter=';')
        for fil in red:
            visua=visualiz(fil[0],fil[1],fil[2],fil[3],fil[4])
            self.__gestorvi.append(visua)
        a.close()
    def mostrarminutos(self,idmiem):
        ac=0
        for viz in self.__gestorvi:
            if viz.getidmiem()==idmiem:
                ac+=viz.getmin()
        print(f'minutos totales del usuario {idmiem}: {ac}')
    def mostrr(self,visua,miem):
        band=False
        for vis in self.__gestorvi:
            if vis==visua:
                band=True
        if band == True:
            print(f'{miem.getapnom()}{miem.getcorreo()}')
    def mostrep(self,miem):
        i=0
        while self.__gestorvi[i].getidmiem()!=miem.getid():
            i+=1
        if self.__gestorvi[i].getidmiem()==miem.getid():
            self.mostrr(self.__gestorvi[i],miem)