#lista secuencial por contenido
#lista enlazada por contenido
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
                self.__ultimo=nuevo_nodo
                self.__cantidad+=1