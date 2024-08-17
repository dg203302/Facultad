class nodo:
    __datos:object
    __siguiente:object
    def __init__(self,datos=None,siguiente=None):
        self.__datos=datos
        self.__siguiente=siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
    def get_datos(self):
        return self.__datos
    def get_siguiente(self):
        return self.__siguiente
    def __str__(self):
        return f'{self.__datos}'
class pila_enlazada:
    __tope:nodo
    __cantidad_nodos:int
    __dimension:int
    def __init__(self,dimension=0):
        self.__tope=None
        self.__cantidad_nodos=0
        self.__dimension=dimension
    def verificar_pila(self):
        return self.__tope==None
    def insertar(self,dato):
        if self.__cantidad_nodos<self.__dimension:
            nodo_nuevo=nodo(dato)
            nodo_nuevo.set_siguiente(self.__tope)
            self.__tope=nodo_nuevo
            self.__cantidad_nodos+=1
        else:
            raise IndexError
    def suprimir(self):
        if not(self.verificar_pila()):
            i=0
            while self.__tope.get_siguiente()!=None and i<self.__cantidad_nodos:
                nodo_eliminar=self.__tope
                self.__tope=self.__tope.get_siguiente()
                i+=1
                del nodo_eliminar
    def mostrar(self):
        if not(self.verificar_pila()):
            i=0
            while i<self.__cantidad_nodos:
                print(self.__tope)
                self.__tope=self.__tope.get_siguiente()
                i+=1
pila_ejemplo=pila_enlazada(5)
pila_ejemplo.insertar(1)
pila_ejemplo.insertar(2)
pila_ejemplo.insertar(3)
pila_ejemplo.insertar(4)
pila_ejemplo.insertar(5)
try:
    pila_ejemplo.insertar(6)
except IndexError:
    print('pila llena!')
pila_ejemplo.mostrar()
pila_ejemplo.suprimir()
pila_ejemplo.mostrar()