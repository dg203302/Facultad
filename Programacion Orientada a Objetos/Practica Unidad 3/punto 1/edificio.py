import csv
from departamento import depart
class edificio:
    __id:int
    __nom:str
    __direc:str
    __nom_empconst:str
    __cant_pisos:int
    __cant_dep:int
    __depas:list
    def __init__(self,id,nom,dire,nomem,cantp,cantdep):
        self.__id=id
        self.__nom=nom
        self.__direc=dire
        self.__nom_empconst=nomem
        self.__cant_pisos=cantp
        self.__cant_dep=cantdep
        self.__depas=[]
    def cargardep(self):
        arch=open('Python/practica 3/punto 1/EdificioNorte.csv',mode='r')
        read=csv.reader(arch,delimiter=';')
        for fila in read:
            if len(fila)==8 and fila[0] == self.__id:
                depa=depart(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
                self.__depas.append(depa)
        arch.close()
    def getnomedi(self):
        return self.__nom
    def listardep(self):
        for depar in self.__depas:
            print(f'nombre y apellido: {depar.getnom()} del departamento: {depar.getnumde()}')
    def getsupcubi(self):
        ac=0
        for depa in self.__depas:
            ac+=float(depa.getsupcu())
        print(f'superficie cubierta por el edificio {self.__nom}: {ac}')
    def getnompropie(self,nompr):
        i=0
        while self.__depas[i].getnom()!=nompr:
            i+=1
        if self.__depas[i].getnom()==nompr:
            return self.__depas[i].getnom()
    def incisoc3(self,nompro):
        i=0
        while self.__depas[i].getnom()!=nompro:
            i+=1
        if self.__depas[i].getnom()==nompro:
            suptot=0
            for depas in self.__depas:
                suptot+=float(depas.getsupcu())
            supdep=float(self.__depas[i].getsupcu())
            print(f'porcentaje de superficie que representa: {(supdep*100)/suptot}')
    def contarporpiso(self,npiso):
        c=0
        for dep in self.__depas:
            if int(dep.getnumep())==npiso:
                if int(dep.getcanth())==3 and int(dep.getcantb())>1:
                    c+=1
        return c
    def __del__(self):
        for dep in self.__depas:
            del dep
        del self