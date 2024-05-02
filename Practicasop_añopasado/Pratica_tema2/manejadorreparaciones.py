import csv
from reparaciones import reparacion
class gestrep:
    __gestorrep:list
    def __init__(self):
        self.__gestorrep=[]
    def carga(self):
        a=open('Practicasop_añopasado/Pratica_tema2/reparaciones.csv')
        lec=csv.reader(a,delimiter=';')
        for fila in lec:
            paten,repa,rep,precio,precio2,estado=lec
            repa=reparacion(paten,repa,rep,precio,precio2,estado)
            self.__gestorrep.append(repa)
    def reparac(self,patente):
        tot=0
        print('|reparacion| |precio repuesto| |mano de obra| |subtotal|')
        for reparacion in self.__gestorrep:
            if reparacion.getpate() == patente:
                subtotal=reparacion.getpre_rep()+reparacion.getpre_manobra()
                tot+=subtotal
                print(f'|{reparacion.getrepa()}||{reparacion.getpre_rep()}||{reparacion.getpre_manobra()}||{subtotal}|')
        print(f'total a pagar: {tot}')
    def b(self,gestclien):
        tot=0
        paterep=input('ingrese la patente: ')
        for repa in self.__gestorrep:
            if repa.getpate() == paterep:
                if repa.get_est_rep() == 'P':
                    print('hay reparaciones pendientes!')
                    break
                tot+=(repa.getpre_rep()+repa.getpre_manobra())
        gestclien.modificest(paterep,tot)
    def listarrep(self,paten):
        print('Reparacion')
        for repa in self.__gestorrep:
            if repa.getpate() == paten:
                if repa.get_est_repa() == 'P':
                    print(f'{repa.getrepa()}')