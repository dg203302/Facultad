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
class pila:
    __tope:nodo
    __cantidad:nodo
    def __init__(self,tope=None):
        self.__tope=tope
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,dato):
        nodo_nuevo=nodo(dato)
        nodo_nuevo.set_siguiente(self.__tope)
        self.__tope=nodo_nuevo
        self.__cantidad+=1
    def suprimir(self):
        if not self.vacia():
            dato_recuperado=self.__tope.get_dato()
            self.__tope=self.__tope.get_siguiente()
            self.__cantidad-=1
            return dato_recuperado
        else:
            print('Pila vacia')
            return None
    def recorrer(self):
        aux=self.__tope
        while aux!=None:
            print(aux.get_dato(), end=' ')
            aux=aux.get_siguiente()
        print()
if __name__=='__main__':
    mi_pila = pila()
    mi_pila.insertar(10)
    mi_pila.insertar(20)
    mi_pila.insertar(30)
    mi_pila.recorrer()
    mi_pila.suprimir()
    mi_pila.recorrer()