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
    def insertar(self,dato, posicion):
        nodo_insertar=nodo_lista_enlazada(dato)
        if posicion==0:
            if self.vacia():
                self.__primero=nodo_insertar
                self.__ultimo=nodo_insertar
                self.__primero.set_siguiente(self.__ultimo)
                self.__ultimo.set_anterior(self.__primero)
                self.__primero.set_anterior(self.__ultimo)
                self.__ultimo.set_siguiente(self.__primero)
            else:
                nodo_insertar.set_siguiente(self.__primero)
                nodo_insertar.set_anterior(self.__ultimo)
                self.__primero.set_anterior(nodo_insertar)
                self.__ultimo.set_siguiente(nodo_insertar)
                self.__primero=nodo_insertar
        else:
            i=0
            anterior=self.__primero
            while i<(posicion-1):
                i+=1
                anterior=anterior.get_siguiente()
            if i==(posicion-1):
                if anterior.get_siguiente()!=self.__primero:
                    nodo_insertar.set_siguiente(anterior.get_siguiente())
                    nodo_insertar.set_anterior(anterior)
                    anterior.get_siguiente().set_anterior(nodo_insertar)
                    anterior.set_siguiente(nodo_insertar)
                else:
                    nodo_insertar.set_siguiente(anterior.get_siguiente())
                    nodo_insertar.set_anterior(anterior)
                    anterior.get_siguiente().set_anterior(nodo_insertar)
                    anterior.set_siguiente(nodo_insertar)
                    self.__ultimo=nodo_insertar
        self.__cantidad+=1
    def primer_elemento(self):
        if not(self.vacia()):
            return self.__primero.get_dato()
    def ultimo_elemento(self, posicion):
        if not(self.vacia()):
            return self.__ultimo.get_dato()
    def recorrer_desde_el_principio(self):
        if not(self.vacia()):
            aux=self.__primero
            while aux!=self.__ultimo:
                print(aux.get_dato())
                aux=aux.get_siguiente()
            print(aux.get_dato()) #para mostrar el ultimo que no sale
    def recorrer_desde_el_ultimo(self):
        aux=self.__ultimo
        while aux!=self.__primero:
            print(aux.get_dato())
            aux=aux.get_anterior()
        print(aux.get_dato())
    def get_cantidad(self):
        return self.__cantidad
    def siguiente(self, posicion):
        if not(self.vacia()):
            if posicion>self.__cantidad:
                raise IndexError
            else:
                if posicion<=(self.__cantidad/2):
                    i=0
                    aux=self.__primero
                    while aux!=None and i!=posicion:
                        aux=aux.get_siguiente()
                        i+=1
                    if i==posicion:
                        siguiente=aux.get_siguiente()
                        print(f'dato ubicado en el nodo siguiente a la posicion: {i}: {siguiente.get_dato()}')
                elif posicion>(self.__cantidad/2):
                    i=self.__cantidad
                    aux=self.__ultimo
                    while aux!=None and i!=posicion:
                        aux=aux.get_anterior()
                        i-=1
                    if i==posicion:
                        siguiente=aux.get_siguiente()
                        print(f'dato ubicado en el nodo siguiente a la posicion: {i}: {siguiente.get_dato()}')
        else:
            print('lista vacia!')
    def anterior(self, posicion):
        if not(self.vacia()):
            if posicion>self.__cantidad:
                raise IndexError
            else:
                if posicion<=(self.__cantidad/2):
                    i=0
                    aux=self.__primero
                    while aux!=None and i!=posicion:
                        aux=aux.get_siguiente()
                        i+=1
                    if i==posicion:
                        anterior=aux.get_anterior()
                        print(f'dato ubicado en el nodo anterior a la posicion: {i}: {anterior.get_dato()}')
                elif posicion>(self.__cantidad/2):
                    i=self.__cantidad
                    aux=self.__ultimo
                    while aux!=None and i!=posicion:
                        aux=aux.get_anterior()
                        i-=1
                    if i==posicion:
                        anterior=aux.get_anterior()
                        print(f'dato ubicado en el nodo anterior a la posicion: {i}: {anterior.get_dato()}')
        else:
            print('lista vacia!')
    def eliminar(self,posicion):
        if not(self.vacia()):
            if posicion==0:
                nodo_eliminar=self.__primero
                self.__ultimo.set_siguiente(nodo_eliminar.get_siguiente())
                nodo_eliminar.get_siguiente().set_anterior(self.__ultimo)
                self.__primero=nodo_eliminar.get_siguiente()
                del nodo_eliminar
            else:
                i=0
                actual=self.__primero
                while i<posicion:
                    i+=1
                    actual=actual.get_siguiente()
                if i==posicion:
                    if actual.get_siguiente()!=self.__primero:
                        nodo_eliminar=actual
                        actual.get_anterior().set_siguiente(nodo_eliminar.get_siguiente())
                        actual.get_siguiente().set_anterior(nodo_eliminar.get_anterior())
                        del nodo_eliminar
                    else:
                        nodo_eliminar=actual
                        actual.get_siguiente().set_anterior(nodo_eliminar.get_anterior())
                        actual.get_anterior().set_siguiente(nodo_eliminar.get_siguiente())
                        self.__ultimo=actual.get_anterior()
                        del nodo_eliminar
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
    print('ingresando orden')
    lista.mostrar()
    lista.insertar(6,2)
    print('ingresando en un lugar ocupado')
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
    lista_prueba.insertar(21,1)
    print(f'cantidad de elementos: {lista_prueba.get_cantidad()}')
    print('recorriendo desde el inicio')
    lista_prueba.recorrer_desde_el_principio()
    lista_prueba.eliminar(2)
    lista_prueba.recorrer_desde_el_principio()