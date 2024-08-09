import csv
from clientes import cliente
class gestcli:
    __gestorc:list
    def __init__(self):
        self.__gestorc=[]
    def carga(self):
        a=open('Practicasop_añopasado/Pratica_tema2/clientes.csv')
        lec=csv.reader(a,delimiter=';')
        for fila in lec:
            dni,nom,ape,tele,paten,vehi,est=fila
            clie=cliente(dni,nom,ape,tele,paten,vehi,est)
            self.__gestorc.append(clie)
    def a(self,gestrep):
        dni=input('ingrese el dni del cliente: ')
        i=0
        while self.__gestorc[i].getdni() != dni:
            i+=1
        if self.__gestorc[i].getdni() == dni:
            print(f'DNI: {self.__gestorc[i].getdni()} Apellido y Nombre: {self.__gestorc[i].getap()} {self.__gestorc[i].getnom()} \nPatente: {self.__gestorc[i].getpaten()} Vehiculo: {self.__gestorc[i].getvehic()}')
            gestrep.reparac(self.__gestorc[i].getpaten())
    def modificest(self,paterep,tot):
        i=0
        while self.__gestorc[i].getpaten() != paterep:
            i+=1
        if self.__gestorc[i].getpaten() == paterep:
            self.__gestorc[i].modific_est()
            print(f'Apellido y Nombre: {self.__gestorc[i].getap()} {self.__gestorc[i].getnom()} \nTelefono: {self.__gestorc[i].gettel()} Vehiculo: {self.__gestorc[i].getvehic()} Total a pagar: {tot}')
    def c(self,gestrep):
        for clie in self.__gestorc:
            if clie.get_est() == 'P':
                print(f'Apellido y Nombre: {clie.getap()} {clie.getnom()} Telefono: {clie.gettel()} \n Patente: {clie.getpaten()} Vehiculo: {clie.getvehic()}')
                gestrep.listarrep(clie.getpaten())
    def d(self):
        for i in range(0,len(self.__gestorc)):
            band=False
            clien=self.__gestorc[i]
            for clie in self.__gestorc:
                if clie == clien:
                    band=True
            if band==True:
                print(f'Apellido y Nombre: {clie.getap()} {clie.getnom()} Telefono: {clie.gettel()} \n Patente: {clie.getpaten()} Vehiculo: {clie.getvehic()}')