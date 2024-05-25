from visualizacion import *
import csv
class gestorvisua:
    __gestorvi:list
    def __init__(self):
        self.__gestorvi=[]
        a=open('Python/Practicasop_añopasado/practica operativa recu/Visualizaciones.csv',mode='r') #esto cambialo
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
    def b(self,gstmi):
        for i in range(0,len(self.__gestorvi)):
            band=False
            j=i+1
            while j<(len(self.__gestorvi)):
                if self.__gestorvi[i]==self.__gestorvi[j] and i!=j:
                    band=True
                j+=1
            if band==True:
                gstmi.most(self.__gestorvi[i].getidmiem())