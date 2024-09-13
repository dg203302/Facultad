class nodo_cursor:
    __dato:object
    __siguiente:int
    def __init__(self,dato=None,siguiente=-1):
        self.__dato=dato
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def get_siguiente(self):
        return int(self.__siguiente)
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
class lista_cursor:
    __primer_elemento:int
    __cantidad_elementos:int
    __dimension:int
    __elementos:list
    __disponible:int
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__elementos=[None]*self.__dimension
        self.__cantidad_elementos=0
        self.__disponible=-1
        self.__primer_elemento=0
    def buscar_vacio(self):
        i=0
        while i<self.__dimension:
            if self.__elementos[i]==None:
                self.__disponible=i
                return True
            i+=1
        return False
    def insertar_en_posicion(self,dato,indice_insertar):
        if self.__cantidad_elementos<self.__dimension and self.buscar_vacio():
            nodo_a_insertar=nodo_cursor(dato)
            self.__elementos[self.__disponible]=nodo_a_insertar
            if self.__cantidad_elementos==0:
                self.__primer_elemento=self.__disponible
            elif indice_insertar==0:
                self.__elementos[self.__disponible].set_siguiente(self.__primer_elemento)
                self.__primer_elemento=self.__disponible
            else:
                i=0
                anterior=self.__primer_elemento
                while i<indice_insertar-1 and i<self.__cantidad_elementos:
                    i+=1
                    anterior=self.__elementos[anterior].get_siguiente()
                if i==indice_insertar-1:
                    nodo_a_insertar.set_siguiente(self.__elementos[anterior].get_siguiente())
                    self.__elementos[anterior].set_siguiente(self.__disponible)
                else:
                    self.__elementos[anterior].set_siguiente(self.__disponible)
            self.__cantidad_elementos+=1
        else:
            print('lista llena!')
    def insertar_por_elemento(self,dato):
        if self.__cantidad_elementos<self.__dimension and self.buscar_vacio():
            nodo_insertar=nodo_cursor(dato)
            self.__elementos[self.__disponible]=nodo_insertar
            if self.__cantidad_elementos==0:
                self.__primer_elemento=self.__disponible
            elif dato<self.__elementos[self.__primer_elemento].get_dato():
                nodo_insertar.set_siguiente(self.__primer_elemento)
                self.__primer_elemento=self.__disponible
            else:
                anterior=self.__primer_elemento
                i=0
                while i<self.__cantidad_elementos-1 and dato>self.__elementos[anterior].get_dato():
                    anterior=self.__elementos[anterior].get_siguiente()
                    i+=1
                if dato<self.__elementos[anterior].get_dato():
                    nodo_insertar.set_siguiente(self.__elementos[anterior].get_siguiente())
                    self.__elementos[anterior].set_siguiente(self.__disponible)
                else:
                    self.__elementos[anterior].set_siguiente(self.__disponible)
            self.__cantidad_elementos+=1
        else:
            print('lista llena!')
    def eliminar(self,posicion):
        if posicion==0:
            indice_eliminar=self.__primer_elemento
            self.__primer_elemento=self.__elementos[self.__primer_elemento].get_siguiente()
            self.__elementos[indice_eliminar]=None
            self.__cantidad_elementos-=1
        else:
            i=0
            anterior=self.__primer_elemento
            while i<posicion-1:
                anterior=self.__elementos[anterior].get_siguiente()
                i+=1
            if i==(posicion-1):
                nodo_eliminar=self.__elementos[anterior].get_siguiente()
                self.__elementos[anterior].set_siguiente(self.__elementos[nodo_eliminar].get_siguiente())
                self.__elementos[nodo_eliminar]=None
                self.__cantidad_elementos-=1
            else:
                self.__elementos[anterior.get_siguiente()]=None
                self.__elementos[anterior].set_siguiente(-1)
                self.__cantidad_elementos-=1
    def eliminar_dato(self,dato):
        if dato==self.__elementos[self.__primer_elemento].get_dato():
            indice_eliminar=self.__primer_elemento
            self.__primer_elemento=self.__elementos[self.__primer_elemento].get_siguiente()
            self.__elementos[indice_eliminar]=None
        else:
            i=0
            anterior=self.__primer_elemento
            while i<self.__cantidad_elementos and dato!=self.__elementos[self.__elementos[anterior].get_siguiente()].get_dato():
                anterior=self.__elementos[anterior].get_siguiente()
                i+=1
            if dato==self.__elementos[self.__elementos[anterior].get_siguiente()].get_dato():
                indice_eliminar=self.__elementos[anterior].get_siguiente()
                self.__elementos[anterior].set_siguiente(self.__elementos[indice_eliminar].get_siguiente())
                self.__elementos[indice_eliminar]=None
            elif self.__elementos[self.__elementos[anterior].get_siguiente()].get_siguiente()==-1:
                nodo_elimnar=self.__elementos[anterior].get_siguiente()
                self.__elementos[anterior].set_siguiente(-1)
                self.__elementos[nodo_elimnar]=None
            else:
                print('dato no encontrado!')
                return
        self.__cantidad_elementos-=1
    def recorrer(self):
        if self.__cantidad_elementos!=0:
            cabeza = self.__primer_elemento
            print("Lista:", end=" ")
            while cabeza!=-1:
                print(self.__elementos[cabeza].get_dato(), end=" ")
                cabeza=self.__elementos[cabeza].get_siguiente()
            print()
        else:
            print("Lista vacía.")
    def recorrer_rudimentario(self):
        i=self.__primer_elemento
        while self.__elementos[i].get_siguiente()!=-1:
            print(f'CONTENIDO: {self.__elementos[i].get_dato()}\nSIGUIENTE: {self.__elementos[i].get_siguiente()}\n')
            i=self.__elementos[i].get_siguiente()
        print(f'CONTENIDO: {self.__elementos[i].get_dato()}\nSIGUIENTE: {self.__elementos[i].get_siguiente()}\ncantidad de elementos: {self.__cantidad_elementos}') #esto para que muestre el ultimo
if __name__=='__main__':
    '''
    lista_prueba=lista_cursor(5)
    lista_prueba.insertar_por_elemento(21)
    lista_prueba.insertar_por_elemento(12)
    lista_prueba.insertar_por_elemento(31)
    lista_prueba.insertar_por_elemento(231)
    lista_prueba.recorrer()
    lista_prueba.eliminar_dato(231)
    #lista_prueba.eliminar(0)
    lista_prueba.recorrer()
    '''
    lista_prueba=lista_cursor(5)
    lista_prueba.insertar_en_posicion(21,0)
    lista_prueba.insertar_en_posicion(12,1)
    lista_prueba.insertar_en_posicion(31,0)
    lista_prueba.insertar_en_posicion(231,2)
    lista_prueba.recorrer()
    