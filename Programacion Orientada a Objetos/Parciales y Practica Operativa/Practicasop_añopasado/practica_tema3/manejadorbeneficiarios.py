import csv
from becarios import becario
class manejadorbene:
    __gestorben:list
    def __init__(self):
        self.__gestorben=[]
        a=open('Practicasop_añopasado/practica_tema3/becarios.csv',mode='r')
        escri=csv.reader(a,delimiter=';')
        for fila in escri:
            dni,nom,ape,car,si,an,pro,idben=fila
            bene=becario(dni,nom,ape,car,si,an,pro,idben)
            self.__gestorben.append(bene)
        a.close()
    def benefic(self,idbe,imp):
        tot=0
        for bene in self.__gestorben:
            if idbe == bene.getid():
                tot+=imp
                print(bene)
        print(f'total para pagar beca: {tot}')
    def b(self,gestbeca):
        dni=input('ingrese el dni: ')
        c=0
        for becar in self.__gestorben:
            if becar.getdni() == dni:
                c+=1
        if c>1:
            print('el beneficiario tiene mas de una beca!')
            i=0
            while self.__gestorben[i].getdni!=dni:
                i+=1
            if self.__gestorben[i].getdni==dni:
                print(self.__gestorben[i])
                for bene in self.__gestorben:
                    if bene.getdni()==dni:
                        gestbeca.mostrar(bene.getid())
        else:
            print('el becario tiene solo una beca!')
    def c(self):
        self.__gestorben=sorted(self.__gestorben)
        print(self.__gestorben)
    def lista(self,id):
        for bene in self.__gestorben:
            if bene.getid()!=id:
                if bene.getprom()>8:
                    print(bene)