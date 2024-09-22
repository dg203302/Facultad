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
class lista:
    __primero:nodo
    __cantidad:int
    def __init__(self,primero=None):
        self.__primero=primero
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def insertar_por_posicion(self,dato,posicion):
        nodo_nuevo=nodo(dato)
        if self.vacia():
            self.__primero=nodo_nuevo
        elif posicion==0:
            nodo_nuevo.set_siguiente(self.__primero)
            self.__primero=nodo_nuevo
        else:
            i=0
            anterior=self.__primero
            while i<self.__cantidad and i<posicion-1:
                anterior=anterior.get_siguiente()
                i+=1
            if i==posicion-1:
                nodo_nuevo.set_siguiente(anterior.get_siguiente())
                anterior.set_siguiente(nodo_nuevo)
            else:
                anterior.set_siguiente(nodo_nuevo)
        self.__cantidad+=1
#------------------------------------------------IMPORTANTE POR CONTENIDO-----------------------------------------------------------#
    def insertar_por_contenido(self,dato):
        nodo_nuevo=nodo(dato)
        if self.vacia():
            self.__primero=nodo_nuevo
        else:
            anterior=None
            actual=self.__primero
            while actual!=None and dato>actual.get_dato():
                anterior=actual
                actual=actual.get_siguiente()
            if anterior==None:
                nodo_nuevo.set_siguiente(self.__primero)
                self.__primero=nodo_nuevo
            else:
                anterior.set_siguiente(nodo_nuevo)
                nodo_nuevo.set_siguiente(actual)
        self.__cantidad+=1
#-----------------------------------------------------------------------------------------------------------#
    def suprimir_por_posicion(self,posicion):
        if not self.vacia():
            if posicion==0:
                dato_recuperar=self.__primero.get_dato()
                self.__primero=self.__primero.get_siguiente()
                self.__cantidad-=1
                return dato_recuperar
            else:
                i=0
                anterior=self.__primero
                while i<self.__cantidad and i<posicion-1:
                    anterior=anterior.get_siguiente()
                    i+=1
                if i==posicion-1:
                    dato_recuperar=anterior.get_siguiente().get_dato()
                    anterior.set_siguiente(anterior.get_siguiente().get_siguiente())
                    self.__cantidad-=1
                    return dato_recuperar
                else:
                    print('posicion no encontrada')
                    return None
    def suprimir_por_contenido(self,dato):
        if not self.vacia():
            if dato==self.__primero.get_dato():
                self.__primero=self.__primero.get_siguiente()
                self.__cantidad-=1
                return 0
            else:
                i=0
                anterior=None
                actual=self.__primero
                while actual!=None and dato!=actual.get_dato():
                    anterior=actual
                    actual=actual.get_siguiente()
                    i+=1
                if dato==actual.get_dato():
                    anterior.set_siguiente(actual.get_siguiente())
                    self.__cantidad-=1
                    return i
    def mostrar(self):
        aux=self.__primero
        while aux!=None:
            print(aux.get_dato(), end=' ')
            aux=aux.get_siguiente()
        print()
    def get_primero(self):
        if not self.vacia():
            aux=self.__primero
            return aux
    def get_ultimo(self):
        if not self.vacia():
            aux=self.__primero
            while aux.get_siguiente()!=None:
                aux=aux.get_siguiente()
            return aux
    def buscar_por_posicion(self,posicion):
        if not self.vacia():
            if posicion==0:
                return self.__primero.get_dato()
            else:
                i=0
                aux=self.__primero
                while i<posicion and aux!=None:
                    aux=aux.get_siguiente()
                    i+=1
                if i==posicion:
                    return aux.get_dato()
                else:
                    print('posicion no encontrada')
                    return None
    def buscar_por_contenido(self,dato):
        if not self.vacia():
            if dato==self.__primero.get_dato():
                return 0
            else:
                i=0
                aux=self.__primero
                while aux!=None and dato!=aux.get_dato():
                    aux=aux.get_siguiente()
                    i+=1
                if dato==aux.get_dato():
                    return i
                else:
                    print('dato no encontrado')
                    return None
    def get_elemento_siguiente_por_posicion(self,posicion):
        if not self.vacia():
            if posicion==0:
                return self.__primero.get_siguiente().get_dato()
            else:
                i=0
                aux=self.__primero
                while i<posicion and aux!=None:
                    aux=aux.get_siguiente()
                    i+=1
                if i==posicion:
                    return aux.get_siguiente().get_dato()
                else:
                    print('posicion no encontrada')
                    return None
    def get_elemento_siguiente_por_contenido(self,dato):
        if not self.vacia():
            if dato==self.__primero.get_dato():
                return self.__primero.geT_siguiente().get_dato()
            else:
                aux=self.__primero
                while aux!=None and dato!=aux.get_dato():
                    aux=aux.get_siguiente()
                if dato==aux.get_dato():
                    return aux.get_siguiente().get_dato()
                else:
                    print('dato no encontrado')
                    return None
    def get_elemento_anterior_por_posicion(self,posicion):
        if not self.vacia():
            if posicion==0:
                print('no hay anterior')
            else:
                i=0
                anterior=self.__primero
                while i<posicion-1 and anterior!=None:
                    anterior=anterior.get_siguiente()
                    i+=1
                if i==posicion-1:
                    return anterior.get_dato()
                else:
                    print('posicion no encontrada')
    def get_elemento_anterior_por_contenido(self,dato):
        if not self.vacia():
            if dato==self.__primero.get_dato():
                print('no hay anterior')
            else:
                anterior=None
                actual=self.__primero
                while dato!=actual.get_dato() and actual!=None:
                    anterior=actual
                    actual=actual.get_siguiente()
                if dato==actual.get_dato():
                    return anterior.get_dato()
                else:
                    print('dato no encontrado')
if __name__=='__main__':
    lista_enlazada = lista()
    '''
    lista_enlazada.insertar_por_posicion(10, 0)
    lista_enlazada.insertar_por_posicion(20, 1)
    lista_enlazada.insertar_por_posicion(30, 2)
    lista_enlazada.insertar_por_posicion(15, 1)
    
    lista_enlazada.insertar_por_contenido(10)
    lista_enlazada.insertar_por_contenido(20)
    lista_enlazada.insertar_por_contenido(30)
    lista_enlazada.insertar_por_contenido(15)
    lista_enlazada.mostrar()
    #print(lista_enlazada.suprimir_por_posicion(2))
    #print(lista_enlazada.suprimir_por_contenido(10))
    #lista_enlazada.mostrar()
    #print(lista_enlazada.get_primero().get_dato())
    #print(lista_enlazada.get_ultimo())
    #print(lista_enlazada.buscar_por_posicion(2))
    #print(lista_enlazada.buscar_por_contenido(20))
    #print(f'elemento siguiente a la posicion 2 :{lista_enlazada.get_elemento_siguiente_por_posicion(1)}')
    #print(f'elemento siguiente a 20 :{lista_enlazada.get_elemento_siguiente_por_contenido(20)}')
    #print(f'elemento anterior a la posicion 1 :{lista_enlazada.get_elemento_anterior_por_posicion(1)}')
    #print(f'elemento anterior a 20 :{lista_enlazada.get_elemento_anterior_por_contenido(20)}')
    '''