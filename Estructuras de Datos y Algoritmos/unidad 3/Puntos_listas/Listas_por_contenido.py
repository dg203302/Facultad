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
        self.__ultimo=-1
    def vacia(self):
        return self.__cantidad_elementos==0
    def insertar(self,dato):
        if self.__cantidad_elementos<self.__dimension:
            i=0
            while dato>self.__items[i] and i<self.__cantidad_elementos:
                i+=1
            if dato<self.__items[i]:
                for j in range(self.__cantidad_elementos,i,-1):
                    self.__items[j]=self.__items[j-1]
                self.__items[i]=dato
                self.__cantidad_elementos+=1
            else:
                self.__ultimo+=1
                self.__items[self.__ultimo]=dato
                self.__cantidad_elementos+=1
        else:
            print('lista llena!')
    def eliminar(self,dato):
        if not(self.vacia()):
            if dato==self.__items[0]:
                for i in range(0,self.__ultimo):
                    self.__items[i]=self.__items[i+1]
                self.__ultimo-=1
            elif dato==self.__items[self.__ultimo]:
                self.__items[self.__ultimo]=0
                self.__ultimo-=1
            else:
                i=0
                while dato!=self.__items[i] and i<self.__cantidad_elementos:
                    i+=1
                if dato==self.__items[i]:
                    for j in range(i,self.__ultimo):
                        self.__items[j]=self.__items[j+1]
                    self.__ultimo-=1
                else:
                    print('dato no encontrado!')
                    return
            self.__cantidad_elementos-=1
    def recorrer(self):
        for i in range(0,self.__cantidad_elementos):
            print(self.__items[i])
#lista enlazada por contenido
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
    def insertar(self,dato):
        nodo_insertar=nodo_lista_enlazada(dato)
        if self.vacia():
            self.__primero=nodo_insertar
        else:
            anterior=None
            actual=self.__primero
            while actual!=None and actual.get_dato()<dato:
                anterior=actual
                actual=actual.get_siguiente()
            if anterior==None:
                nodo_insertar.set_siguiente(self.__primero)
                self.__primero=nodo_insertar
            else:
                nodo_insertar.set_siguiente(actual)
                anterior.set_siguiente(nodo_insertar)
        self.__cantidad+=1
    def recorrer(self):
        actual=self.__primero
        while actual!=None:
            print(actual.get_dato())
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
    def get_cantidad(self):
        return self.__cantidad
#PRUEBAS
if __name__=='__main__':
    '''
    lista=lista_secuencial_contenido(5)
    lista.insertar(1)
    lista.insertar(2)
    lista.insertar(3)
    print('--------------------')
    lista.recorrer()
    #lista.insertar(0)
    print('--------------------')
    lista.recorrer()
    lista.eliminar(2)
    print('--------------------')
    lista.recorrer()
    '''
    lista=lista_enlazada()
    lista.insertar(1)
    lista.insertar(2)
    lista.insertar(3)
    lista.insertar(0)
    lista.insertar(4)
    lista.recorrer()
    