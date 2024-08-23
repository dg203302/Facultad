#------------------cola secuencial----------------------#
class cola_secuencial:
    __primero:int
    __ultimo:int
    __items:list
    __dimension:int
    __cantidad_elementos:int
    def __init__(self, dimension=0):
        self.__primero=0
        self.__dimension=dimension
        self.__ultimo=0
        self.__cantidad_elementos=0
        self.__items=[0]*self.__dimension
    def verificar_cola(self):
        if self.__cantidad_elementos==0:
            return
    def insertar(self,dato):
        if self.__cantidad_elementos<self.__dimension:
            self.__items[self.__ultimo]=dato
            self.__ultimo+=1
            self.__cantidad_elementos+=1
        else:
            raise IndexError
    def suprimir_todo(self):
        for i in range(self.__primero,self.__cantidad_elementos):
            self.__items[i]=0
            self.__cantidad_elementos-=1
            self.__ultimo-=0
    def recorrer(self):
        if self.__cantidad_elementos==0:
            print('cola vacia')
        else:
            for i in range(self.__primero,self.__cantidad_elementos):
                print(self.__items[i])
#------------------nodo de cola enlazada----------------------#
class nodo:
    __dato:object
    __siguiente:object
    def __init__(self,dato=None,siguiente=None):
        self.__dato=dato
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def get_siguiente(self):
        return self.__siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
#------------------cola enlazada----------------------#
class cola_enlazada:
    __primero:nodo
    __ultimo:nodo
    __cantidad_elementos:int
    def __init__(self,primero=None,ultimo=None):
        self.__primero=primero
        self.__ultimo=ultimo
        self.__cantidad_elementos=0
    def insertar(self,dato):
        nuevo_nodo=nodo(dato)
        if self.__primero==None:
            self.__primero=nuevo_nodo
            self.__ultimo=self.__primero
            self.__cantidad_elementos+=1
        else:
            self.__ultimo.set_siguiente(nuevo_nodo)
            self.__ultimo=nuevo_nodo
            self.__cantidad_elementos+=1
    def recorrer(self):
        if self.__primero==None:
            print('cola vacia')
        else:
            nodo_aux=self.__primero
            while nodo_aux!=None:
                print(nodo_aux.get_dato())
                nodo_aux=nodo_aux.get_siguiente()
    def suprimir(self):
        if self.__primero==None:
            print('cola vacia')
        else:
            nodo_eliminar=self.__primero
            self.__primero=self.__primero.get_siguiente()
            self.__cantidad_elementos-=1
            del nodo_eliminar
    def get_dato(self):
        return self.__primero.get_dato()