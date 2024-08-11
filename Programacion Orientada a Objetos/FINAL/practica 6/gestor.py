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
    def cargar_muestras(self):
        muestra1=wachin('diego','garcia','44991307')
        self.insercion_al_final(muestra1)
        muestra2=wachin('julieta','mogolica','23242442')
        self.insercion_al_final(muestra2)
        muestra3=wachin('jose','jose','1234567890')
        self.insercion_al_final(muestra3)
        muestra4=wachin('caca','pedo','214325232')
        self.insercion_al_final(muestra4)
if __name__=='__main__':
    gestor=lista_enlazada()
    while True:
        gestor.cargar_muestras() #cambiar por carga a traves de csv y json
        gestor.probar_cargas()
        eleccion=input('0 para salir')
        if eleccion=='0':
            break