import csv
from becas import beca
class manejadorbeca:
    __gestorbeca:list
    def __init__(self):
        self.__gestorbeca=[]
        a=open('Practicasop_añopasado/practica_tema3/becas.csv',mode='r')
        escri=csv.reader(a,delimiter=';')
        for fila in escri:
            id,tip,imp=fila
            beca=beca(id,tip,imp)
            self.__gestorbeca.append(beca)
        a.close()
    def a(self,gestobene):
        tipo=input('ingrese tipo: ')
        i=0
        while self.__gestorbeca[i].gettipo() != tipo:
            i+=1
        if self.__gestorbeca[i].gettpico() == tipo:
                gestobene.benefic(self.__gestorbeca[i].getidbeca(),self.__gestorbeca[i].getimp())
    def mostrar(self,id):
        i=0
        while self.__gestorbeca[i].getidbeca!=id:
             i+=1
        if self.__gestorbeca[i].getidbeca==id:
             print(self.__gestorbeca[i])
    def d(self,gestorbene):
        tip=input('ingrese el tipo de beca')
        i=0
        while self.__gestorbeca[i].gettipo() != tip:
             i+=1
        if self.__gestorbeca[i].gettipo() == tip:
             gestorbene.lista(self.__gestorbeca[i].getidbeca())