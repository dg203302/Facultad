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
                self.__cantidad_elementos+=1
            elif indice_insertar==0:
                self.__elementos[self.__disponible].set_siguiente(self.__primer_elemento)
                self.__primer_elemento=self.__disponible
                self.__cantidad_elementos+=1
            else:
                actual=self.__primer_elemento
                for j in range(indice_insertar-1):
                    actual=self.__elementos[actual].get_siguiente()
                nodo_a_insertar.set_siguiente(self.__elementos[actual].get_siguiente())
                self.__elementos[actual].set_siguiente(self.__disponible)
                self.__cantidad_elementos+=1
        else:
            print('lista llena!')
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
    
    lista_prueba=lista_cursor(5)
    lista_prueba.insertar_en_posicion(21,0)
    lista_prueba.insertar_en_posicion(12,1)
    lista_prueba.insertar_en_posicion(31,0)
    lista_prueba.insertar_en_posicion(231,2)
    lista_prueba.recorrer()
    