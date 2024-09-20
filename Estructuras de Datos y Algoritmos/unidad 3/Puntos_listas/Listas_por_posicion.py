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
        if self.__cantidad<self.__tamano:
            if posicion==0:
                if self.vacia():
                    self.__items[posicion]=elemento
                    self.__ultimo+=1
                else:
                    for i in range(self.__ultimo+1,posicion,-1):
                        self.__items[i]=self.__items[i-1]
                    self.__items[posicion]=elemento
                    self.__ultimo+=1
            elif posicion>self.__ultimo:
                self.__ultimo+=1
                self.__items[self.__ultimo]=elemento
            else:
                for j in range(self.__ultimo+1,posicion,-1):
                    self.__items[j]=self.__items[j-1]
                self.__items[posicion]=elemento
                self.__ultimo+=1
            self.__cantidad+=1
        else:
            print('lista llena!')
    def mostrar(self):
        for i in range(0,self.__cantidad):
            print(self.__items[i])
    def recuperar(self,posicion):
        print(f'item de la posicion {posicion}: {self.__items[posicion]}')
    def suprimir(self,posicion):
        if posicion>=0 and posicion<=self.__ultimo:
            for i in range(posicion,self.__ultimo):
                self.__items[i]=self.__items[i+1]
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
    __dato:object
    __siguiente:object
    def __init__(self,dato=None,siguiente=None):
        self.__dato=dato
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def set_siguiente(self, siguiente):
        self.__siguiente=siguiente
    def get_siguiente(self):
        return self.__siguiente
class lista_enlazada:
    __cantidad:int
    __primero:nodo_lista_enlazada
    def __init__(self,primero=None):
        self.__cantidad=0
        self.__primero=primero
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,dato, posicion):
        nodo_insertar=nodo_lista_enlazada(dato)
        if posicion==0:
            self.__primero=nodo_insertar
        else:
            i=0
            anterior=self.__primero
            while i<posicion-1:
                i+=1
                anterior=anterior.get_siguiente()
            if i==(posicion-1):
                if anterior.get_siguiente()!=None:
                    nodo_insertar.set_siguiente(anterior.get_siguiente())
                    anterior.set_siguiente(nodo_insertar)
                else:
                    anterior.set_siguiente(nodo_insertar)
        self.__cantidad+=1
    def recorrer(self):
        actual=self.__primero
        i=0
        while actual!=None:
            print(f'elemento en posicion: {i}\nvalor: {actual.get_dato()}')
            i+=1
            actual=actual.get_siguiente()
    def buscar(self,indice):
        if self.vacia():
            print('lista_vacia')
        else:
            if indice==0:
                return self.__primero.get_dato()
            else:
                i=0
                actual=self.__primero
                while i!=indice:
                    i+=1
                    actual=actual.get_siguiente()
                if i==indice:
                    return actual.get_dato()
    def primer_elemento(self):
        if not(self.vacia()):
            return self.__primero #o enviar el nodo
    def ultimo_elemento(self):
        if not(self.vacia()):
            actual=self.__primero
            while actual.get_siguiente() is not None:
                actual=actual.get_siguiente()
            return actual #o enviar el nodo
    def get_cantidad(self):
        return self.__cantidad
    def siguiente(self, posicion):
        if not(self.vacia()):
            if posicion>self.__cantidad:
                raise IndexError
            else:
                i=0
                actual=self.__primero
                while i<posicion:
                    i+=1
                    actual=actual.get_siguiente()
                if i==posicion:
                    print(actual.get_siguiente().get_dato())
        else:
            print('lista vacia!')
    def anterior(self, posicion):
        if not(self.vacia()):
            if posicion>self.__cantidad:
                raise IndexError
            else:
                i=0
                anterior=self.__primero
                while i<posicion-1:
                    i+=1
                    anterior=anterior.get_siguiente()
                if i==(posicion-1):
                    print(anterior.get_dato())
        else:
            print('lista vacia!')
    def eliminar(self,posicion):
        if not(self.vacia()):
            if posicion==0:
                nodo_elim=self.__primero
                self.__primero=self.__primero.get_siguiente()
                del nodo_elim
            else:
                i=0
                anterior=self.__primero
                while i<posicion-1:
                    i+=1
                    anterior=anterior.get_siguiente()
                if i==posicion-1:
                    nodo_elim=anterior.get_siguiente()
                    anterior.set_siguiente(nodo_elim.get_siguiente())
                    del nodo_elim
        self.__cantidad-=1
#PRUEBAS
if __name__=='__main__':
    '''
    print('pruebas para lista secuencial')
    lista=lista_secuencial(5)
    lista.insertar(1,0)
    lista.insertar(2,1)
    lista.insertar(3,2)
    lista.insertar(4,0)
    lista.insertar(6,2)
    lista.mostrar()
    print('-----------------')
    lista.suprimir(2)
    lista.mostrar()
    lista.recuperar(2)
    print('suprimir 1')
    lista.suprimir(0)
    lista.mostrar()
    print('suprimir 2')
    lista.suprimir(1)
    lista.mostrar()
    print('suprimir 3')
    lista.suprimir(2)
    lista.mostrar()
    lista.buscar(6)
    '''
    lista_prueba=lista_enlazada()
    lista_prueba.insertar(12,0)
    lista_prueba.insertar(10,1)
    lista_prueba.insertar(213,2)
    lista_prueba.insertar(320,3)
    lista_prueba.insertar(21,4)
    lista_prueba.recorrer()
    print(f'cantidad de elementos: {lista_prueba.get_cantidad()}')
    # The modified $SELECTION_PLACEHOLDER$ code with ``` is:
    # lista_prueba.primer_elemento()
    # lista_prueba.ultimo_elemento()
    # lista_prueba.siguiente(2)
    # lista_prueba.anterior(2)
    lista_prueba.recorrer()
    #lista_prueba.recorrer_desde_el_principio()