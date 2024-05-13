import csv
from edificio import edificio
class gestedi:
    __edificios:list
    def __init__(self):
        self.__edificios=[]
        ar=open('Python/practica 3/punto 1/EdificioNorte.csv',mode='r')
        reader=csv.reader(ar,delimiter=';')
        for fila in reader:
            if len(fila) == 7:
                edi=edificio(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                edi.cargardep()
                self.__edificios.append(edi)
        ar.close()
    def c1(self):
        nom=input('ingrese le nomrbe del edificio: ')
        i=0
        while self.__edificios[i].getnomedi()!= nom:
            i+=1
        if self.__edificios[i].getnomedi()==nom:
            self.__edificios[i].listardep()
    def c2(self):
        edi=input('ingrese el edificio por teclado: ')
        i=0
        while self.__edificios[i].getnomedi()!=edi:
            i+=1
        if self.__edificios[i].getnomedi()==edi:
            self.__edificios[i].getsupcubi()
    def c3(self):
        nompro=input('ingrese el nombre del propietario: ')
        i=0
        while self.__edificios[i].getnompropie(nompro)!=nompro:
            i+=1
        if self.__edificios[i].getnompropie(nompro)==nompro:
            self.__edificios[i].incisoc3(nompro)
    def c4(self):
        npiso=int(input('ingrese el numero de piso: '))
        ac=0
        for edif in self.__edificios:
            ac+=edif.contarporpiso(npiso)
        print(f'cantidad de hab: {ac}')