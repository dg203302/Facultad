#lista secuencial por contenido
class lista_secuencial_contenido:
    __dimension:int
    __cantidad_elementos:int
    __items:list
    __ultimo:int
    def __init__(self,dimension=0):
        self.__cantidad_elementos=0
        self.__dimension=dimension
        self.__items=[0]*dimension
        self.__ultimo=0
    def insertar(self,dato):
        if self.__cantidad_elementos<self.__dimension:
            if self.__cantidad_elementos==0:
                self.__items[self.__ultimo]=dato
                self.__cantidad_elementos+=1
            elif dato>self.__items[self.__ultimo]:
                self.__ultimo+=1
                self.__items[self.__ultimo]=dato
                self.__cantidad_elementos+=1
            elif dato<self.__items[self.__ultimo]:
                i=0
                while dato>self.__items[i]:
                    i+=1
                if dato<self.__items[i]:
                    for j in range(self.__cantidad_elementos, i, -1):      #importante //asi se desplaza si el elemento sobreescribe el de la primera posicion, tanto para lista por posicion como por elemento
                        self.__items[j] = self.__items[j-1]
                    self.__items[i]=dato
                    self.__ultimo+=1
                    self.__cantidad_elementos+=1
        else:
            print('lista llena!')
    def recorrer(self):
        for i in range(0,self.__cantidad_elementos):
            print(self.__items[i])
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
#PRUEBAS
if __name__=='__main__':
    lista=lista_secuencial_contenido(5)
    lista.insertar(1)
    lista.insertar(2)
    lista.insertar(3)
    lista.recorrer()
    lista.insertar(0)
    lista.recorrer()