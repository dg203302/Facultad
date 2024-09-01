#Lista secuencial
class lista_secuencial:
    __tamano:int
    __ultimo:int
    __items:list
    __cantidad:int
    def __init__(self,tamano=0):
        self.__tamano=tamano
        self.__ultimo=-1
        self.__items=[0]*self.__tamano
        self.__cantidad=0
    def vacia(self):
        return self.__ultimo==-1
    def insertar(self,elemento,posicion):
        if posicion>self.__tamano:
            raise IndexError
        elif posicion==0:
            if self.vacia():
                self.__items[posicion]=elemento
                self.__ultimo+=1
                self.__cantidad+=1
            else:
                for i in range(posicion,self.__cantidad):
                    self.__items[i+1]=self.__items[i]
                self.__items[posicion]=elemento
                self.__ultimo+=1
                self.__cantidad+=1
        elif self.__items[posicion]!=0:
            if self.__cantidad+1>self.__tamano:
                raise IndexError
            else:
                for i in range(posicion,self.__cantidad):
                    self.__items[i+1]=self.__items[i]
                self.__items[posicion]=elemento
                self.__ultimo+=1
                self.__cantidad+=1
        elif self.__items[posicion]==0:
                self.__items[posicion]=elemento
                self.__cantidad+=1
                if self.__items[posicion]>self.__ultimo:
                    self.__ultimo=posicion
    def mostrar(self):
        for i in range(0,self.__cantidad):
            print(self.__items[i])
    def recuperar(self,posicion):
        print(f'item de la posicion {posicion}: {self.__items[posicion]}')
    def suprimir(self,posicion):
        for i in range(posicion,self.__cantidad):
            self.__items[i-1]=self.__items[i]
        self.__cantidad-=1
        self.__ultimo-=1
    def buscar(self,elemento):
        i=0
        while self.__items[i]!=elemento:
            i+=1
        if self.__items[i]==elemento:
            print(f'ubicacion del elemento {elemento}: {i}')
#lista encadenada
class nodo_lista_enlazada:
    __anterior:object
    __siguiente:object
    __dato:object
    def __init__(self,dato=None,siguiente=None,anterior=None):
        self.__anterior=anterior
        self.__siguiente=siguiente
        self.__dato=dato
    def get_dato(self):
        return self.__dato
    def set_siguiente(self, siguiente):
        self.__siguiente=siguiente
    def set_anterior(self,anterior):
        self.__anterior=anterior
    def get_siguiente(self):
        return self.__siguiente
    def get_anterior(self):
        return self.__anterior
class lista_enlazada:
    __cantidad:int
    __primero:nodo_lista_enlazada
    __ultimo:nodo_lista_enlazada
    def __init__(self,primero=None,ultimo=None):
        self.__cantidad=0
        self.__primero=primero
        self.__ultimo=ultimo
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,dato):
        nuevo_nodo=nodo_lista_enlazada(dato)
        if self.vacia():
            self.__primero=nuevo_nodo
            self.__ultimo=self.__primero
            self.__cantidad+=1
        else:
            aux=self.__primero
            while aux.get_siguiente()!=None:
                aux=aux.get_siguiente()
            if aux.get_siguiente()==None:
                aux.set_siguiente(nuevo_nodo)
                nuevo_nodo.set_anterior(aux)
                self.__primero.set_anterior(nuevo_nodo)
    def primer_elemento(self):
        if not(self.vacia()):
            return self.__primero.get_dato()
    def ultimo_elemento(self, posicion):
        if not(self.vacia()):
            return self.__ultimo.get_dato()
    def recorrer_desde_el_principio(self):
        if not(self.vacia()):
            aux=self.__primero
            while aux!=None:
                print(aux.get_dato())
                aux=aux.get_siguiente()
    def recorrer_desde_el_ultimo(self):
        aux=self.__ultimo
        while aux!=self.__primero:
            print(aux.get_dato())
            aux=aux.get_anterior()
    '''def siguiente(self, posicion):
        if not(self.vacia()):
            return self._
    def anterior'''
#lista con cursores
lista_prueba=lista_enlazada()
lista_prueba.insertar(12)
lista_prueba.insertar(10)
lista_prueba.insertar(213)
lista_prueba.insertar(320)
lista_prueba.insertar(3330)
print('recorriendo desde el inicio')
lista_prueba.recorrer_desde_el_principio()
print('recorriendo desde el ultimo')
lista_prueba.recorrer_desde_el_ultimo()