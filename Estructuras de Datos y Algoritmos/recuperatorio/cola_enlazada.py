class nodo:
    __dato:int
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
class cola:
    __primero:nodo
    __ultimo:nodo
    __cantidad:int
    def __init__(self,primero=None,ultimo=None):
        self.__primero=primero
        self.__ultimo=ultimo
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,dato):
        nodo_nuevo=nodo(dato)
        if self.__cantidad==0:
            self.__primero=nodo_nuevo
            self.__ultimo=self.__primero
        else:
            self.__ultimo.set_siguiente(nodo_nuevo)
            self.__ultimo=nodo_nuevo
        self.__cantidad+=1
    def suprimir(self):
        if not self.vacia():
            dato_recuperado=self.__primero.get_dato()
            self.__primero=self.__primero.get_siguiente()
            self.__cantidad-=1
            return dato_recuperado
        else:
            print("La cola está vacía")
            return None
    def mostrar(self):
        aux=self.__primero
        while aux!=self.__ultimo:
            print(aux.get_dato(), end=' ')
            aux=aux.get_siguiente()
        print(aux.get_dato(), end=' \n')
if __name__=='__main__':
    mi_cola = cola()
    mi_cola.insertar(10)
    mi_cola.insertar(20)
    mi_cola.insertar(30)
    mi_cola.mostrar()
    mi_cola.suprimir()
    mi_cola.mostrar()