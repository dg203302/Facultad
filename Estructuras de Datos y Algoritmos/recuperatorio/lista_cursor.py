class nodo:
    __dato:object
    __siguiente:int
    def __init__(self,dato=None,siguiente=-1):
        self.__dato=dato
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def get_siguiente(self):
        return self.__siguiente
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
class lista:
    __dimension:int
    __primero:int
    __disponible:int
    __cantidad:int
    __elementos:list
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__primero=0
        self.__disponible=0
        self.__cantidad=0
        self.__elementos=[None]*self.__dimension
    def vacia(self):
        return self.__cantidad==0
    def get_disponible(self):
        if self.vacia():
            self.__disponible=0
            return True
        else:
            i=0
            while i<self.__dimension and self.__elementos[i]!=None:
                i+=1
            if self.__elementos[i]==None:
                self.__disponible=i
                return True
            else:
                return False
    def insertar_por_posicion(self,dato,posicion):
        if self.__cantidad<self.__dimension and self.get_disponible():
            nodo_nuevo=nodo(dato)
            self.__elementos[self.__disponible]=nodo_nuevo
            if posicion==0:
                if self.vacia():
                    self.__primero=self.__disponible
                else:
                    nodo_nuevo.set_siguiente(self.__primero)
                    self.__primero=self.__disponible
            else:
                i=0
                anterior=self.__primero
                while i<self.__cantidad and i<posicion-1:
                    anterior=self.__elementos[anterior].get_siguiente()
                    i+=1
                if i==posicion-1:
                    nodo_nuevo.set_siguiente(self.__elementos[anterior].get_siguiente())
                    self.__elementos[anterior].set_siguiente(self.__disponible)
                else:
                    self.__elementos[anterior].set_siguiente(self.__disponible)
            self.__cantidad+=1
    def insertar_por_contenido(self,dato):
        if self.__cantidad<self.__dimension and self.get_disponible():
            nodo_nuevo=nodo(dato)
            self.__elementos[self.__disponible]=nodo_nuevo
            if self.vacia():
                self.__primero=self.__disponible
            elif dato<self.__elementos[self.__primero].get_dato():
                nodo_nuevo.set_siguiente(self.__primero)
                self.__primero=self.__disponible
            else:
                anterior=None
                actual=self.__primero
                while actual != -1 and self.__elementos[actual].get_dato()<dato:
                    anterior=actual
                    actual=self.__elementos[actual].get_siguiente()
                if actual == -1 or self.__elementos[actual].get_dato()>dato:
                    nodo_nuevo.set_siguiente(actual)
                    self.__elementos[anterior].set_siguiente(self.__disponible)
            self.__cantidad+=1
    def recorrer(self):
        if not self.vacia():
            i=self.__primero
            while i!=-1:
                print(self.__elementos[i].get_dato(), end=' ')
                i=self.__elementos[i].get_siguiente()
            print()
    def suprimir_por_posicion(self,posicion):
        if not self.vacia():
            if posicion==0:
                dato_recuperar=self.__elementos[self.__primero].get_dato()
                self.__primero=self.__elementos[self.__primero].get_siguiente()
                self.__cantidad-=1
                return dato_recuperar
            else:
                i=0
                anterior=None
                actual=self.__primero
                while i<posicion:
                    anterior=actual
                    actual=self.__elementos[actual].get_siguiente()
                    i+=1
                if i==posicion:
                    dato_recuperar=self.__elementos[actual].get_dato()
                    self.__elementos[anterior].set_siguiente(self.__elementos[actual].get_siguiente())
                    self.__cantidad-=1
                    return dato_recuperar
                else:
                    print('posicion no encontrada')
    def suprimir_por_contenido(self,dato):
        if not self.vacia():
            if dato==self.__elementos[self.__primero].get_dato():
                dato_recuperar=self.__elementos[self.__primero].get_dato()
                self.__primero=self.__elementos[self.__primero].get_siguiente()
                self.__cantidad-=1
                return dato_recuperar
            else:
                anterior=None
                actual=self.__primero
                while dato!=self.__elementos[actual].get_dato() and actual!=-1:
                    anterior=actual
                    actual=self.__elementos[actual].get_siguiente()
                if dato==self.__elementos[actual].get_dato():
                    dato_recuperar=self.__elementos[actual].get_dato()
                    self.__elementos[anterior].set_siguiente(self.__elementos[actual].get_siguiente())
                    self.__cantidad-=1
                    return dato_recuperar
                else:
                    print('elemento no encontrado')
    def buscar_por_posicion(self,posicion):
        if not self.vacia():
            if posicion==0:
                return self.__elementos[self.__primero].get_dato()
            else:
                actual=self.__primero
                i=0
                while i!=posicion:
                    actual=self.__elementos[actual].get_siguiente()
                    i+=1
                if i==posicion:
                    return self.__elementos[actual].get_dato()
                else:
                    print('posicion no encontrada')
    def buscar_por_contenido(self,dato):
        if not self.vacia():
            if dato==self.__elementos[self.__primero].get_dato():
                return 0
            else:
                actual=self.__primero
                i=0
                while dato!=self.__elementos[actual].get_dato() and actual!=-1:
                    actual=self.__elementos[actual].get_siguiente()
                    i+=1
                if dato==self.__elementos[actual].get_dato():
                    return i
                else:
                    print('elemento no encontrado')


if __name__=='__main__':
    lista_obj = lista(dimension=10)
    '''
    # Insert elements by position
    lista_obj.insertar_por_posicion(10, 0)
    lista_obj.insertar_por_posicion(20, 1)
    lista_obj.insertar_por_posicion(15, 1)
    '''
    # Insert elements by content
    lista_obj.insertar_por_contenido(5)
    lista_obj.insertar_por_contenido(25)
    lista_obj.insertar_por_contenido(17)
    lista_obj.recorrer()
    '''
    print(f'elemento de la posicion 1: {lista_obj.suprimir_por_posicion(1)}')
    print(f'posicion del elemento 17: {lista_obj.suprimir_por_contenido(25)}')
    lista_obj.recorrer()
    '''
    '''
    print(f'elemento de la posicion 1: {lista_obj.buscar_por_posicion(1)}')
    print(f'posicion del elemento 17: {lista_obj.buscar_por_contenido(17)}')
    '''