import csv
from encoder import *
from nodo import *
class lista_enlazada:
    __inicio:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self,incio=None,actual=None,indice=0,tope=0):
        self.__inicio=incio
        self.__actual=actual
        self.__indice=indice
        self.__tope=tope
        self.cargar_muestras()
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__indice=0
            self.__actual=self.__inicio
            raise StopIteration
        else:
            dato=self.__actual.get_dato()
            self.__actual=self.__actual.get_siguiente()
            self.__indice+=1
            return dato
    def carga_csv(self):
        try:
            archivo=open('FINAL/ejemplos relaciones/muestras.csv', mode='r')
            reader=csv.reader(archivo,delimiter=';')
            for fila in reader:
                muestra=wachin(fila[0],fila[1],fila[2])
                self.insercion_al_final(muestra)
            archivo.close()
        except FileNotFoundError:
            print('archivo no encontrado')
            return
    def cargar_muestras(self):
       op=input('1 csv, 2 json')
       while True:
           if op==0:
               break
           elif op==1:
               self.carga_csv()
           elif op==2:
               encoder_json.abrir_json(self)
    def insercion_al_principio(self,objeto_dato):
        nuevo_nodo=nodo(objeto_dato)
        nuevo_nodo.set_siguiente(self.__inicio)
        self.__inicio=nuevo_nodo
        self.__actual=self.__inicio
        self.__tope+=1
    def insercion_al_final(self,objeto_dato):
        nuevo_nodo=nodo(objeto_dato)
        if self.__inicio==None or self.__tope==0:
            self.__inicio=nuevo_nodo
            self.__actual=nuevo_nodo
            self.__tope+=1
        else:
            while self.__actual.get_siguiente()!=None and self.__indice<self.__tope:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__actual.get_siguiente()==None:
                self.__actual.set_siguiente(nuevo_nodo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__inicio
    def insercion_en_posicion(self,objeto_dato):
        nuevo_nodo=nodo(objeto_dato)
        posicion=int(input('ingrese la posicion que desee\n-'))
        if (posicion-1)==0:
            nuevo_nodo.set_siguiente(self.__inicio)
            self.__inicio=nuevo_nodo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while self.__actual.get_siguiente()!=None and (posicion-1)!=self.__indice and self.__indice<self.__tope:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if (posicion-1)==self.__indice:
                nuevo_nodo.set_siguiente(self.__actual.get_siguiente())
                self.__actual.set_siguiente(nuevo_nodo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__inicio
    def solicitar_datos(self):
        nombre=input('ingrese nombre: ')
        apellido=input('ingrese apellido: ')
        dni=input('ingrese dni: ')
        objeto=wachin(nombre,apellido,dni)
        return objeto
    def mostrar(self):
        for wachin in self:
            print(wachin)
    def probar_cargas(self):
        eleccion=input('1 para probar metodo pila, 2 para probar metodo cola, 3 para insertar en una posicion determinada')
        if eleccion=='1':
            objeto_dato=self.solicitar_datos()
            self.insercion_al_principio(objeto_dato)
            self.mostrar()
        elif eleccion=='2':
            objeto_dato=self.solicitar_datos()
            self.insercion_al_final(objeto_dato)
            self.mostrar()
        elif eleccion=='3':
            objeto_dato=self.solicitar_datos()
            self.insercion_en_posicion(objeto_dato)
            self.mostrar()
if __name__=='__main__':
    gestor=lista_enlazada()
    while True:
        gestor.probar_cargas()
        eleccion=input('0 para salir')
        if eleccion=='0':
            break