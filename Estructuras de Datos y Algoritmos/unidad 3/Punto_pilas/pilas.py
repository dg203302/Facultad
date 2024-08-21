class pila_secuencial:
    __dimension:int
    __cantidad_elementos:int
    __items:list
    __tope:int
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__items=[0]*self.__dimension
        self.__cantidad_elementos=0
        self.__tope=-1
    def get_tope(self):
        return self.__items[self.__tope]
    def verificar_pila(self):
        return (self.__tope==-1)
    def insertar(self,elemento):
        if self.__cantidad_elementos<self.__dimension:
            self.__tope+=1
            self.__items[self.__tope]=elemento
            self.__cantidad_elementos+=1
        else:
            raise IndexError
    def mostrar(self):
        if not(self.verificar_pila()):
            for i in range(self.__tope,-1,-1):
                print(self.__items[i])
        else:
            print('pila no cargada')
    def suprimir(self):
        if self.__cantidad_elementos<=self.__cantidad_elementos:
            for i in range(self.__tope,-1,-1):
                self.__items[i]=0
    def suprimir_tope(self):
        self.__items[self.__tope]=0
        self.__tope-=1
############################################################################################
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
    __dimension:int
    def __init__(self):
        self.__tope=None
        self.__dimension=0
    def verificar_pila(self):
        return self.__tope==None
    def insertar(self,dato):
        nodo_nuevo=nodo(dato)
        nodo_nuevo.set_siguiente(self.__tope)
        self.__tope=nodo_nuevo
        self.__dimension+=1
    def suprimir(self):
        if not(self.verificar_pila()):
            i=0
            while self.__tope.get_siguiente()!=None and i<self.__dimension:
                nodo_eliminar=self.__tope
                self.__tope=self.__tope.get_siguiente()
                i+=1
                del nodo_eliminar
    def mostrar(self):
        if not(self.verificar_pila()):
            i=0
            while i<self.__dimension and self.__tope.get_siguiente()!=None:
                print(self.__tope)
                self.__tope=self.__tope.get_siguiente()
                i+=1